import random

class NetworkSimulator:
    def generate_event(self):
        return {
            "ip_address": f"192.168.1.{random.randint(1,255)}",
            "packet_rate": random.randint(50, 600),
            "failed_logins": random.randint(0, 10),
            "port_scan": random.choice([True, False])
        }