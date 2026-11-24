import streamlit as st
import time
import csv
from datetime import datetime
from collections import defaultdict
import pandas as pd

from network_simulator import NetworkSimulator
from alert_detector import AlertDetector
from risk_analyzer import RiskAnalyzer


# ---------------- DASHBOARD SETUP ---------------- #

st.set_page_config(
    page_title="Network Security Monitor",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Network Security Monitoring Dashboard")
st.caption("Real-time Threat Detection using LLM Risk Analysis")


simulator = NetworkSimulator()
detector = AlertDetector()
analyzer = RiskAnalyzer(model_name="phi3:mini")   # ✅ CHANGED

ip_reputation = defaultdict(int)
risk_history = []

total_events = 0
high_risk_count = 0
alert_count = 0
unique_ips = set()

LOG_FILE = "network_event_logs.csv"


# ---------------- CREATE LOG FILE ---------------- #

try:
    with open(LOG_FILE, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Timestamp",
            "IP Address",
            "Alerts",
            "Risk Level",
            "Final Alert",
            "Attack Type",
            "Reason",
            "Solution"
        ])
except FileExistsError:
    pass


# ---------------- HELPER FUNCTIONS ---------------- #

def risk_to_number(risk):
    return {"LOW": 1, "MEDIUM": 2, "HIGH": 3}.get(risk, 1)


def color_risk(risk):
    if risk == "HIGH":
        return "🔴 HIGH"
    elif risk == "MEDIUM":
        return "🟡 MEDIUM"
    else:
        return "🟢 LOW"


# ---------------- MAIN LOOP ---------------- #

event_container = st.container()

for i in range(10):

    event = simulator.generate_event()
    alerts = detector.check_alerts(event)

    total_events += 1
    unique_ips.add(event["ip_address"])

    try:
        llm_output = analyzer.analyze(event)
    except Exception as e:
        st.error(f"LLM Error: {e}")
        break


    # -------- DEFAULT VALUES -------- #

    risk_level = "LOW"
    final_alert = "NO"
    attack_type = "Normal"
    reason = ""
    solution = ""


    # -------- PARSE LLM OUTPUT (ROBUST) -------- #

    for line in llm_output.split("\n"):

        line = line.strip()

        if "Risk Level" in line:
            risk_level = line.split(":")[-1].strip().upper()

        elif "Alert" in line:
            final_alert = line.split(":")[-1].strip().upper()

        elif "Attack Type" in line:
            attack_type = line.split(":")[-1].strip()

        elif "Reason" in line:
            reason = line.split(":", 1)[-1].strip()

        elif "Solution" in line:
            solution = line.split(":", 1)[-1].strip()


    # -------- COUNTERS -------- #

    if final_alert == "YES":
        alert_count += 1
        ip_reputation[event["ip_address"]] += 1

    if risk_level == "HIGH":
        high_risk_count += 1


    reputation_score = ip_reputation[event["ip_address"]]

    risk_history.append({
        "Event": total_events,
        "Risk": risk_to_number(risk_level)
    })


    # ---------------- DISPLAY ---------------- #

    with event_container:

        with st.expander(f"Event {total_events} - {color_risk(risk_level)}"):

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Network Event")
                st.code(event, language="json")

            with col2:
                st.subheader("Analysis Summary")

                st.markdown(f"**Risk Level:** {color_risk(risk_level)}")
                st.markdown(f"**Final Alert:** {final_alert}")
                st.markdown(f"**Attack Type:** {attack_type}")
                st.markdown(f"**IP Reputation Score:** {reputation_score}")

                if risk_level == "HIGH":
                    st.error("🚨 Immediate action required!")

            st.markdown("**Detected Alerts:**")
            st.write(", ".join(alerts) if alerts else "No alerts")

            st.markdown("**🧠 Analysis:**")
            st.info(reason if reason else "No analysis available")

            st.markdown("**🛠️ Recommended Action:**")
            st.success(solution if solution else "No action available")

        st.divider()


    # ---------------- LOG ---------------- #

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            event["ip_address"],
            ", ".join(alerts) if alerts else "No alerts",
            risk_level,
            final_alert,
            attack_type,
            reason,
            solution
        ])

    time.sleep(5)


# ---------------- GRAPH ---------------- #

st.subheader("📈 Threat Risk Trend")

df = pd.DataFrame(risk_history)
st.line_chart(df.set_index("Event"))