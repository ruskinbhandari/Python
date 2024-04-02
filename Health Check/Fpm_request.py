import requests
import datetime
import time

def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to fetch data from the URL:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

def save_to_log(data, log_file):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, 'a') as f:
            f.write(f"[{timestamp}] {data}\n")  # Write timestamp and data
            f.write('\n')                        # Append an empty line
            print("Data saved to log successfully")
    except Exception as e:
        print("Error saving data to log:", e)

if __name__ == "__main__":
    url = "https://int-mobileapp.wlink.com.np/health.php"
    log_file = "Fpm_data_log.txt"

    while True:
        data = get_data(url)
        if data:
            save_to_log(data, log_file)

        # Wait for 30 minutes
        time.sleep(30 * 60)
