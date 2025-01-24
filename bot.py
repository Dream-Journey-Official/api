# noinspection PyInterpreter
import time
import requests

url = "https://dashboard.layeredge.io/api/node-points"

payload = {
    "walletAddress": "0x9742471b4B40a3Ac09D5f247Ed8Da659b28dBD6A",
    "lastStartTime": 1737719292154
}
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
    "content-type": "application/json",
    "origin": "https://dashboard.layeredge.io",
    "user-agent": "Mozilla/5.0"
}

def fetch_data():
    while True:
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                print(f"Success: {response.json()}")
                continue
            else:
                print(f"Server Error: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")

        print("Sleeping for 10 minutes due to error...")
        time.sleep(10 * 60)

if __name__ == "__main__":
    fetch_data()
