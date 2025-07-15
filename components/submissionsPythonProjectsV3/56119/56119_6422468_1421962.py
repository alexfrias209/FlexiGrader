print("Welcome to the Electric Vehicle Charging Calculator!")

print("This tool will help you calculate the cost for charging your vehicle.")
charging_history = []
# Function to add a record to charging history
def add_to_history(date, car_name, miles_driven, charging_rate, electricity_rate, charging_cost):
    record = {
        "Date": date,
        "Car Name": car_name,
        "Miles Driven": miles_driven,
        "Charging Rate (kWh/mile)": charging_rate,
        "Electricity Rate (cost per kWh)": electricity_rate,
        "Charging Cost": charging_cost,
    }
    charging_history.append(record)

# Function to view charging history
def view_charging_history():
    print("Charging History:")
    if not charging_history:
        print("No records found.")
    else:
        for i, record in enumerate(charging_history, 1):
            print(f"Record {i}:")
            for key, value in record.items():
                print(f"{key}: {value}")
            print()
#Function to export charging history to a text file 
def export_information(filename):
    with open(filename,"w") as file: 
        for record in charging_history:
            file.write('Record:\n')
            for key, value in record.items():
                file.write(f'{key}:{value}\n')
            file.write("\n")
#List of cars the user can choose 
cars_available = {
    'Lucid Air': 516,
    'Tesla Model S': 405,
    'Hyundai Ioniq 6': 361,
    'Tesla Model 3': 358 ,
    'Tesla Model X': 348 ,
     'Mercedes-EQ EQS450 Sedan': 340,
    'Tesla Model Y': 330,
    'Rivian R1T': 328 ,
    'BMW iX': 324,
    'Rivian R1S': 321,
    'Ford F-150 Lightning': 320,
    'BMW i7': 318,
    'Cadillac Lyriq': 312,
    'Ford Mustang Mach-E': 312,
    'Kia EV6': 310,
    'Mercedes-EQ EQS450 SUV': 305,
    'Nissan Ariya': 304,
    'BMW i4 Gran Coupe': 301 
}
#Function to get miles per charge for a car 
def get_milage(car_name):
    return cars_available.get(car_name, 0)
while True:
    print("Main Menu:")
    print("1. Calculate the charging cost for your vehicle")
    print("2. View Charging History")
    print("3. Export Charging History to Text File")
    print("4. Exit")

    user_choice = input()

    if user_choice == "1":  
        print("You have chosen to calculate charging cost")
        car_name = input("Enter your car name: ")
        miles_per_charge = get_milage(car_name)

        if miles_per_charge == 0:
            miles_per_charge = float(input("Enter miles per charge for your vehicle: "))
        
        while True:  #Checks that the number is not non-negative
            miles_driven = float(input("Enter the miles that you plan to drive: "))
            if miles_driven >=0:
                break
            else:
                print("Invalid response. Please enter a non-negative value.")

        while True:   #Verifies the input is not a negative value 
            charging_rate = float(input("Enter charging rate for the station (kWh/mile):"))
            if charging_rate >= 0:
                break
            else:
                print("Invalid price. Please enter a non-negative value.")
        while True:   #Verifies that input is not a negative value 
            electricity_rate = float(input("Enter the rate of Electricity (Price per kW/h): "))
            if electricity_rate >= 0:
                break
            else:
                print("Invalid price. Please enter a non-negative value.")
        charge_cost = (miles_driven / miles_per_charge) * charging_rate * electricity_rate  #Cost Caulation 
        add_to_history("Current Date", car_name, miles_driven, charging_rate, electricity_rate, charge_cost) #Dictionary being updated 
        print(f"The cost for {miles_driven} miles in a {car_name} is ${charge_cost:.2f}")

    elif user_choice == "2":
        view_charging_history()

    elif user_choice == "3":
        export_information("charging_history.txt")
        print("Charging history exported to 'charging_history.txt")

    elif user_choice == "4":
        print("Exiting the program. Have a good day.")
        break

    else:
        print("Invalid Choice. Please choose option 1/2/3/4")