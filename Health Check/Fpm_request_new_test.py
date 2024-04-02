import requests
import datetime
import time
import json  # Import json for parsing the response


def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Directly return JSON
        else:
            print(f"Failed to fetch data from the URL: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


def save_to_log(data, log_file):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Log Taken Time:", timestamp)
        with open(log_file, 'a') as f:
            f.write(f"[{timestamp}] {json.dumps(data)}\n")  # Save the data as a JSON string
            f.write('\n')  # Append an empty line
            print("Data saved to log successfully")
    except Exception as e:
        print(f"Error saving data to log: {e}")


if __name__ == "__main__":
    url = "https://int-mobileapp.wlink.com.np/health.php"
    log_file = "Fpm_data_log.txt"

    while True:
        data = get_data(url)
        if data:
            save_to_log(data, log_file)

            # Assuming 'data' is a dictionary with 'fpm' and 'disk' keys
            fpm_value = int(data.get('fpm', 0))
            disk = data.get('disk', {})  # 'disk' is assumed to be a dictionary
            diskfree_value = int(disk.get('diskfree', 9999))

            print("FPM Value:", fpm_value)
            print("Diskfree Value:", diskfree_value)

            if fpm_value > 180:
                sleep_time = 5 * 60  # Sleep for 5 minutes if FPM is above 180
            else:
                sleep_time = 30 * 60  # Otherwise, sleep for 30 minutes
        else:
            sleep_time = 30 * 60  # Default to 30 minutes if data fetch fails or is not in expected format

        # Wait for the calculated interval
        time.sleep(sleep_time)
