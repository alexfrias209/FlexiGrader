import requests
import datetime
import csv
from pprint import pprint

# ======================
# UTILITY FUNCTIONS
# ======================


def pst_to_unix(pst_time):
    # Adjust back to UTC
    utc_time = pst_time + datetime.timedelta(hours=8)

    #   Calculate the Unix timestamp: number of seconds between the UTC datetime and the Unix epoch
    epoch = datetime.datetime(1970, 1, 1)
    unix_timestamp = (utc_time - epoch).total_seconds()

    return int(unix_timestamp)


def unix_to_pst(unix_time):
    # Convert the unix time to a naive datetime object in UTC
    utc_naive = datetime.datetime.utcfromtimestamp(unix_time)

    # Manual adjustment for PST (PST is UTC-8)
    pst_naive = utc_naive - datetime.timedelta(hours=8)

    return pst_naive


def kelvin_to_fahrenheit(kelvin_temp):
    # Convert temperature from Kelvin to Fahrenheit
    return (kelvin_temp - 273.15) * 9 / 5 + 32


def previous_5_days(pst_str):
    # Convert the string to a datetime object
    date_str = pst_str.strftime("%Y-%m-%d %H:%M:%S.%f")
    pst_datetime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

    # Generate a list of the previous 7 days
    days = [pst_datetime - datetime.timedelta(days=i) for i in range(5)]

    return days


# ======================
# API FUNCTIONS
# ======================


def request_weather_api(time):
    API_KEY = "a62286d9e01b3228b34b333ed85d4c84"
    MERCED = [37.1666, -120.7516]
    URL = f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={MERCED[0]}&lon={MERCED[1]}1&date={time}&appid={API_KEY}"
    r = requests.get(URL)
    results = r.json()

    return results


def was_rain_expected(date):
    API_KEY = "a62286d9e01b3228b34b333ed85d4c84"
    MERCED = [37.1666, -120.7516]
    # Convert the date to UNIX timestamp
    dt = datetime.datetime.strptime(date, "%Y-%m-%d")
    timestamp = int(dt.timestamp())

    # Endpoint for historical data
    endpoint = f"http://api.openweathermap.org/data/2.5/onecall/timemachine"

    # Parameters for the request
    params = {"lat": MERCED[0], "lon": MERCED[1], "dt": timestamp, "appid": API_KEY}

    response = requests.get(endpoint, params=params)
    data = response.json()

    return True if "rain" in data["current"] else False


# ======================
# DATA STORAGE FUNCTIONS
# ======================


def update_weather_csv(json_objects, csv_filename):
    with open(csv_filename, "w", newline="") as csvfile:
        fieldnames = ["date", "max_temp", "min_temp", "mean_temp", "expected_rain", "rain"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for obj in json_objects:
            # Extract data from JSON
            date = obj["date"]
            expected_rain = obj["expected_rain"]
            rain = bool(obj["precipitation"]["total"])
            max_temp_k = obj["temperature"]["max"]
            min_temp_k = obj["temperature"]["min"]
            mean_temp_k = (max_temp_k + min_temp_k) / 2

            # Convert temperatures from Kelvin to Fahrenheit
            max_temp_f = round(kelvin_to_fahrenheit(max_temp_k), 2)
            min_temp_f = round(kelvin_to_fahrenheit(min_temp_k), 2)
            mean_temp_f = round(kelvin_to_fahrenheit(mean_temp_k), 2)

            # Write the data to the CSV file
            writer.writerow(
                {
                    "date": date,
                    "max_temp": max_temp_f,
                    "min_temp": min_temp_f,
                    "mean_temp": mean_temp_f,
                    "expected_rain": expected_rain,
                    "rain": rain,
                }
            )


def retrieve_weekly_weather_data():
    # Getting the current UTC time
    current_utc = datetime.datetime.now(datetime.UTC)

    # Manual adjustment for PST (PST is UTC-8)
    current_pst = current_utc - datetime.timedelta(hours=8)

    previous_7_day_weather_data = []
    for day in previous_5_days(current_pst)[::-1]:
        date_str_ymd = day.strftime("%Y-%m-%d")
        data = request_weather_api(date_str_ymd)
        data["expected_rain"] = was_rain_expected(date_str_ymd)
        previous_7_day_weather_data.append(data)

    return previous_7_day_weather_data


data = retrieve_weekly_weather_data()
update_weather_csv(data, "merced_weather.csv")
