import requests
import time
from datetime import datetime

class CanadaPostTracker:
    def __init__(self, tracking_id, webhook_url):
        self.tracking_id = tracking_id
        self.shipping_url = f"https://www.canadapost-postescanada.ca/track-reperage/rs/track/json/package?pins={tracking_id}"
        self.webhook_url = webhook_url
        self.last_status = None

    def send_to_discord(self, embed):
        data = {
            "embeds": [embed]
        }
        response = requests.post(self.webhook_url, json=data)
        if response.status_code != 204:
            print(f"Failed to send message to Discord: {response.status_code}, {response.text}")

    def check_shipping(self):
        try:
            response = requests.get(url=self.shipping_url)
            if response.status_code == 200:
                data = response.json()
                addtnl_orig_info = data[0].get('addtnlOrigInfo', 'N/A')
                addtnl_dest_info = data[0].get('addtnlDestInfo', 'N/A')
                status = data[0].get('status', 'N/A')
                perrmstat = data[0].get('status', 'N/A')
                expected_delivery = data[0].get('expectedDlvryDateTime', {}).get('dlvryDate', 'N/A')
                if expected_delivery != 'N/A':
                    expected_delivery_date = datetime.strptime(expected_delivery, '%Y-%m-%d')
                    formatted_delivery_date = expected_delivery_date.strftime('%A, %B %d, %Y')
                else:
                    formatted_delivery_date = 'N/A'

                if status == "FullAccepted":
                    status = "ITEM PICKED UP BY CARRIER"
                else:
                    status = status    

                if status != self.last_status:
                    self.last_status = status
                    embed = {
                        "title": "Shipping Information",
                        "fields": [
                            {"name": "Sent From", "value": addtnl_orig_info, "inline": False},
                            {"name": "Shipping To", "value": addtnl_dest_info, "inline": False},
                            {"name": "Status", "value": status, "inline": False},
                            {"name": "Expected Delivery Date", "value": formatted_delivery_date , "inline": False},
                            {"name": "TNumber", "value": self.tracking_id , "inline": False},
                            {"name": "stat", "value": perrmstat , "inline": False}
                        ],
                        "timestamp": datetime.utcnow().isoformat()
                    }
                    self.send_to_discord(embed)
            else:
                print("Check the shipping number and try again")    
        except Exception as e:
            print(f'Error: {e}')

    def start_tracking(self, interval=300):
        while True:
            self.check_shipping()
            time.sleep(interval)