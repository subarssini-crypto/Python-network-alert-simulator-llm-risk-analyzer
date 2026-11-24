class AlertDetector:
    def __init__(self):
        self.packet_threshold = 350
        self.login_threshold = 4

    def check_alerts(self, event):
        alerts = []

        if event["packet_rate"] > self.packet_threshold:
            alerts.append("High packet rate")

        if event["failed_logins"] > self.login_threshold:
            alerts.append("Multiple failed logins")

        if event["port_scan"]:
            alerts.append("Port scanning detected")

        return alerts