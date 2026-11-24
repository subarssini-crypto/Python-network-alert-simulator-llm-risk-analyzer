# 🚨 Python Network Alert Simulator + LLM Risk Analyzer

An AI-powered network security monitoring project that simulates network events, detects suspicious activities, and uses a Large Language Model (LLM) to analyze potential cybersecurity threats and recommend mitigation actions.

## 📌 Project Overview

This project combines Python-based network event simulation, rule-based alert detection, and LLM-powered risk analysis to demonstrate an intelligent Security Operations Center (SOC) monitoring workflow.

The system generates simulated network events, identifies suspicious activities based on predefined security thresholds, and uses the Phi-3 Mini language model to classify threats and provide security recommendations.

An interactive Streamlit dashboard displays network events, risk levels, detected alerts, and recommended actions.

## ✨ Key Features

- **Network Event Simulation:** Generates simulated network events with IP addresses, packet rates, failed login attempts, and port scanning indicators.
- **Rule-Based Alert Detection:** Identifies high packet rates, multiple failed login attempts, and port scanning activities.
- **LLM-Based Risk Analysis:** Uses the Phi-3 Mini model to analyze network events and classify security risks.
- **Threat Classification:** Categorizes events into LOW, MEDIUM, and HIGH risk levels.
- **Intelligent Recommendations:** Generates explanations and recommended mitigation actions.
- **Interactive Dashboard:** Visualizes network events and security analysis using Streamlit.
- **IP Reputation Tracking:** Maintains alert counts associated with IP addresses.
- **CSV Logging:** Records timestamps, IP addresses, alerts, risk levels, attack types, reasons, and recommended solutions.
- **Risk Trend Visualization:** Displays event risk levels through a line chart.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive dashboard |
| Ollama | Local LLM execution |
| Phi-3 Mini | AI-based risk analysis |
| Pandas | Data handling and visualization |
| Requests | Communication with the LLM API |
| CSV | Network event logging |

## 📂 Project Structure

```text
Python-network-alert-simulator/
│
├── alert_detector.py
├── dashboard.py
├── main.py
├── network_simulator.py
├── risk_analyzer.py
├── network_event_logs.csv
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/subarssini-crypto/Python-network-alert-simulator-llm-risk-analyzer.git
```

### 2. Navigate to the project directory

```bash
cd Python-network-alert-simulator-llm-risk-analyzer
```

### 3. Install dependencies

```bash
pip install streamlit pandas requests
```

### 4. Set up Ollama

Install Ollama and download the Phi-3 Mini model:

```bash
ollama pull phi3:mini
```

Ensure the Ollama API is accessible at:

```text
http://localhost:11435/api/generate
```

The API endpoint must match the URL configured in `risk_analyzer.py`.

### 5. Run the project

**To run the Python-based simulation:**

```bash
python main.py
```

**To launch the interactive dashboard:**

```bash
streamlit run dashboard.py
```

## 🔍 System Workflow

1. Network Simulator generates random network events.
2. Alert Detector checks events against predefined security thresholds.
3. Risk Analyzer sends event details to the local LLM.
4. The LLM identifies the risk level, attack type, reason, and recommended solution.
5. The dashboard displays the analysis and detected alerts.
6. Network event details and analysis results are stored in a CSV file.
7. A risk trend chart visualizes the analyzed events.

## 📊 Risk Classification

| Risk Level | Description |
|---|---|
| LOW | No significant suspicious activity detected |
| MEDIUM | Potentially suspicious network activity |
| HIGH | High-risk network activity requiring attention |

## 🎯 Project Objective

The primary objective is to demonstrate how traditional rule-based network monitoring can be integrated with Large Language Models to provide contextual security analysis, threat classification, and actionable mitigation recommendations.

## 🚀 Future Enhancements

- Integration with real-time network traffic monitoring.
- Advanced intrusion detection mechanisms.
- Threat intelligence and IP reputation integration.
- Automated incident response.
- Enhanced dashboard analytics and reporting.

## ⚠️ Disclaimer

This project is designed for educational and demonstration purposes. Network events are simulated and do not represent actual live network traffic. Risk classifications and recommendations are generated using predefined rules and an LLM.

---

**Developed using Python, Streamlit, and Local LLM Technology.**
