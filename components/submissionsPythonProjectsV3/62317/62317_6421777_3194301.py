import matplotlib.pyplot as plt
import csv

# File path
file_path = "merced_weather.csv"

dates = []
max_temps = []
min_temps = []
mean_temps = []
expected_rain = []
rain = []

# Open and read the CSV file
with open(file_path, "r") as file:
    csv_reader = csv.reader(file)

    # Skip the header
    next(csv_reader)

    # Read each row of data
    for row in csv_reader:
        dates.append(row[0])
        max_temps.append(float(row[1]))
        min_temps.append(float(row[2]))
        mean_temps.append(float(row[3]))
        expected_rain.append((row[4]) == "True")
        rain.append((row[5]) == "True")


# Plotting the data
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot temperature data
ax1.set_xlabel("Date")
ax1.set_ylabel("Temperature (°F)", color="black")
ax1.plot(dates, max_temps, marker="o", label="Max Temp", color="red")
ax1.plot(dates, min_temps, marker="o", label="Min Temp", color="blue")
ax1.plot(dates, mean_temps, marker="o", label="Mean Temp", color="green")
ax1.tick_params(axis="y", labelcolor="black")
ax1.set_title("Weather Data with Rain Forecast and Actual Rain")
ax1.legend(loc="upper left")

# Create a second y-axis to plot the rain data
ax2 = ax1.twinx()
ax2.set_ylabel("Rain", color="black")
ax2.bar(dates, expected_rain, alpha=0.6, label="Expected Rain", color="cyan")
ax2.bar(dates, rain, alpha=0.4, label="Actual Rain", color="blue")
ax2.tick_params(axis="y", labelcolor="black")
ax2.legend(loc="upper right")

# Display the plot
fig.tight_layout()
plt.show()
