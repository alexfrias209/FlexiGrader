import random

INSULATION_QUALITIES = {
    "poor": 1.2,
    "average": 1.0,
    "good": 0.8
}

def get_user_inputs():
    try:
        building_area = float(input("Enter the building area (in square meters): "))
        insulation_quality = input("Enter the insulation quality (poor/average/good): ").lower()
        desired_temperature = float(input("Enter the desired indoor temperature (in Celsius): "))
        days = int(input("Enter the number of days to simulate: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for building area, desired temperature, and days.")
        exit(1)
    return building_area, insulation_quality, desired_temperature, days

def simulate_energy_consumption(building_area, insulation_quality, desired_temperature, days):
    insulation_factor = INSULATION_QUALITIES.get(insulation_quality, 1.0)
    daily_energy_consumption = []

    for day in range(1, days + 1):
        external_temperature = random.uniform(-10, 30)
        hvac_settings = random.uniform(15, 25)

        energy_consumption = (building_area / insulation_factor) * (desired_temperature - external_temperature)
        daily_energy_consumption.append(energy_consumption)

    return daily_energy_consumption

def display_energy_consumption_chart(daily_energy_consumption):
    print("\nDaily Energy Consumption Chart:")
    for day, consumption in enumerate(daily_energy_consumption, start=1):
        print(f"Day {day}: {consumption:.2f} kWh")

def main():
    building_area, insulation_quality, desired_temperature, days = get_user_inputs()
    daily_energy_consumption = simulate_energy_consumption(building_area, insulation_quality, desired_temperature, days)
    display_energy_consumption_chart(daily_energy_consumption)
    total_energy_consumption = sum(daily_energy_consumption)
    print(f"\nTotal Energy Consumption for {days} days: {total_energy_consumption:.2f} kWh")

if __name__ == "__main__":
    main()
