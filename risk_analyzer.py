import requests

class RiskAnalyzer:
    def __init__(self, model_name="phi3:mini"):
        self.model_name = model_name
        self.url = "http://localhost:11435/api/generate"

    def analyze(self, event):

        prompt = f"""
You are an expert SOC cybersecurity analyst.

Analyze the network event and provide structured output.

STRICT FORMAT ONLY:

Risk Level: <LOW/MEDIUM/HIGH>
Alert: <YES/NO>
Attack Type: <Brute-force / DDoS / Port Scan / Suspicious Traffic / Normal>
Reason: <2-3 sentences explaining the threat clearly>
Solution: <2-3 actionable mitigation steps>

Rules:
- HIGH if packet_rate > 350 OR failed_logins > 6 OR port_scan = True
- MEDIUM if packet_rate > 200 OR failed_logins > 3
- LOW otherwise

Network Event:
IP Address: {event['ip_address']}
Packet Rate: {event['packet_rate']}
Failed Logins: {event['failed_logins']}
Port Scan: {event['port_scan']}
"""

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.0,
                "num_predict": 250
            }
        }

        response = requests.post(self.url, json=payload, timeout=120)
        return response.json()["response"]