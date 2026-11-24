from network_simulator import NetworkSimulator
from alert_detector import AlertDetector
from risk_analyzer import RiskAnalyzer

simulator = NetworkSimulator()
detector = AlertDetector()
analyzer = RiskAnalyzer(model_name="phi3:mini")

for i in range(5):
    print(f"\n{'='*50}")
    print(f"Event {i+1}")

    event = simulator.generate_event()
    print("Network Event:", event)

    # ✅ FIXED: Only one return value
    alerts = detector.check_alerts(event)

    # LLM Analysis
    llm_result = analyzer.analyze(event)
    lines = [line.strip() for line in llm_result.split("\n") if line.strip()]

    # -------- PARSE LLM OUTPUT -------- #
    risk_level = "LOW"
    final_alert = "NO"
    attack_type = "Normal"
    reason = ""
    solution = ""

    for line in lines:
        line_upper = line.upper()

        if "RISK LEVEL" in line_upper:
            risk_level = line.split(":")[-1].strip()

        elif "ALERT" in line_upper:
            final_alert = line.split(":")[-1].strip().upper()

        elif "ATTACK TYPE" in line_upper:
            attack_type = line.split(":")[-1].strip()

        elif "REASON" in line_upper:
            reason = line.split(":", 1)[-1].strip()

        elif "SOLUTION" in line_upper:
            solution = line.split(":", 1)[-1].strip()

    # -------- COMBINE OUTPUT -------- #
    combined_reason = ", ".join(alerts) if alerts else "No alerts"

    if reason:
        combined_reason += f" | LLM Analysis: {reason}"

    # -------- PRINT OUTPUT -------- #
    print("Alerts:", alerts if alerts else "No alerts")
    print("Final Risk Level:", risk_level)
    print("Final Alert:", final_alert)
    print("Attack Type:", attack_type)

    print("\n Analysis:")
    print(reason if reason else "No analysis available")

    print("\n Recommended Action:")
    print(solution if solution else "No action available")

    print("="*50)