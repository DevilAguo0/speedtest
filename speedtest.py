# speedtest.py

import requests
import time

def test_speed():
    url = "https://speed.cloudflare.com/"
    start_time = time.time()
    
    try:
        response = requests.get(url)
        end_time = time.time()
        
        if response.status_code == 200:
            download_time = end_time - start_time
            print(f"Download Time: {download_time:.2f} seconds")
        else:
            print(f"Failed to reach the server, status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_speed()
