import random
import csv
import matplotlib.pyplot as plt

def simulate_monthly_weather(location, start_date, end_date):
    # Simulate monthly weather and return the data
    weather_data = []
    current_date = start_date
    while current_date <= end_date:
        year, month = map(int, current_date.split('-'))
        temperature = random.uniform(10, 30)
        precipitation = random.uniform(0, 50)
        weather_data.append([f"{year}-{month:02d}", temperature, precipitation])

        # Move to the next month
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1

        current_date = f"{year}-{month:02d}"

    return weather_data

def save_weather_data(location, data, filename):
    # Save weather data to a CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Month", "Average Temperature (°C)", "Total Precipitation (mm)"])
        writer.writerows(data)
    print(f"Weather data for {location} has been saved to {filename}.")

def load_weather_data(filename):
    data = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header row
            for row in reader:
                month, temperature, precipitation = row
                data.append([month, float(temperature), float(precipitation)])
        return data
    except FileNotFoundError:
        print(f"File not found: {filename}. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred while importing data: {e}")
    return []

def plot_weather_data(data):
    # Plot weather data
    months = [entry[0] for entry in data]
    temperatures = [entry[1] for entry in data]
    precipitations = [entry[2] for entry in data]

    plt.figure(figsize=(10, 6))
    plt.bar(months, temperatures, label='Temperature (°C)')
    plt.bar(months, precipitations, label='Precipitation (mm)')
    plt.xlabel('Month')
    plt.xticks(rotation=45)
    plt.ylabel('Value')
    plt.title('Monthly Weather Data')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('graph.png')  # Save the plot as an image file
    plt.close()  # Close the plot to prevent freezing

def main():
    while True:
        print("Welcome to the Simple Weather Simulator!")
        print("Please choose an option:")
        print("1. Simulate Weather")
        print("2. Predict Future Weather")
        print("3. Export Weather Data")
        print("4. Import Weather Data")
        print("5. Exit")

        user_choice = input("Enter your choice (1/2/3/4/5): ")

        if user_choice == "1" or user_choice == "2":
            location = input("Enter the location (Merced/Turlock): ")
            if location not in ["Merced", "Turlock"]:
                print("Invalid location. Please choose Merced or Turlock.")
                continue

            if user_choice == "1":
                start_date = "2020-01"
                end_date = "2022-12"
                weather_data = simulate_monthly_weather(location, start_date, end_date)
                for row in weather_data:
                    print(f"{row[0]} | {row[1]:.2f}                       | {row[2]:.2f}")
                plot_weather_data(weather_data)

            elif user_choice == "2":
                future_start_date = "2023-01"
                future_end_date = "2023-12"
                weather_data = simulate_monthly_weather(location, future_start_date, future_end_date)
                for row in weather_data:
                    print(f"{row[0]} | {row[1]:.2f}                       | {row[2]:.2f}")
                plot_weather_data(weather_data)

        elif user_choice == "3":
            if not weather_data:
                print("No weather data available for export. Please simulate or import data first.")
                continue
            location = input("Enter the location (Merced/Turlock): ")
            filename = f"{location}_weather_data.csv"
            save_weather_data(location, weather_data, filename)

        elif user_choice == "4":
            while True:
                # This imports weather data from a CSV file
                filename = input("Enter the filename to import (or 'exit' to cancel): ")

                if filename.lower() == "exit":
                    print("Exiting data import. Goodbye!")
                    break

                loaded_data = load_weather_data(filename)
                if loaded_data:
                    print("Imported weather data:")
                    for row in loaded_data:
                        print(f"{row[0]} | {row[1]:.2f}                       | {row[2]:.2f}")
                    break
                else:
                    print("Failed to import data. Please check the file and try again.")

        elif user_choice == "5":
            print("Exiting the Simple Weather Simulator. Goodbye!")
            print("Project by Chi Cheng")
            print(":3")
            break

if __name__ == "__main__":
    main()
