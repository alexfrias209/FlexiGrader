import csv

# Define an empty list to store distances between points from a CSV file.
point_distances = []

# Load distances between points from a CSV file into the list.
def load_point_distances():
    with open('65759_6415492_4590848.py', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            point_distances.append({
                'From City': row['From City'],
                'To City': row['To City'],
                'Distance In Miles': (row['Distance In Miles'])
            })

# Calculate the speed needed to reach a destination from a starting point in a given time.
def calculate_speed(start, destination, time):
    total_distance = 0
    for dist_info in point_distances:
        if start == dist_info['From City'] and destination == dist_info['To City']:
            total_distance = dist_info['Distance In Miles']
            break
    speed = float(total_distance) / (time / 60)  # Calculate the required speed in mph
    return speed

# Display the available points for travel.
def display_points():
    print("Available citys for travel:")
    for dist_info in point_distances:
        print(f"From City {dist_info['From City']} To City {dist_info['To City']}")

# Main program
if __name__ == "__main__":
    # Load point distances from the CSV file.
    load_point_distances()

    while True:
        print("Welcome to the Speedometer Calculator!")
        display_points()

        start = input("Please enter your Location: ")
        destination = input("Please enter you desire destination: ")
        time = float(input("Please enter the amount of time you want to spend on the road (in minutes): "))

        speed = calculate_speed(start, destination, time)
        print(f"To reach your desired destination in {time} minutes, you need to be going at {speed:.2f} mph.")

        another_calculation = input("Hello again, Do you want to plan another trip? (yes/no): ")
        if another_calculation.lower() != 'yes':
            break
        
