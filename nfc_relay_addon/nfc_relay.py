import requests
import time

# Replace with your Home Assistant base URL and API key
HA_BASE_URL = "http://localhost:8123"
API_KEY = "your_api_key"

def relay_nfc_information(nfc_data):
    # Replace with your logic to relay NFC information
    print("NFC Data:", nfc_data)

def main():
    while True:
        # Replace with your ESPHome NFC sensor endpoint
        nfc_sensor_data = requests.get("http://esphome-nfc-sensor:port/api/nfc").json()
        
        if nfc_sensor_data:
            relay_nfc_information(nfc_sensor_data)

        time.sleep(5)  # Adjust as needed

if __name__ == "__main__":
    main()
