# Define the service_recommendations function to read service recommendations based on car make and mileage
def service_recommendations(car_make, mileage):
    recom = {}  # Initialize a dictionary to store service recommendations
    
    # Read service recommendations from the file and populate the recommendations dictionary
    with open('39951_6421004_9132174.txt', 'r') as file:
        lines = file.readlines()  # Read all lines from the file
        header = lines[0].strip().split()  # Get the header row and split it into a list of the names of the services
        for line in lines[1:]:  # Iterate through the data lines except the header
            parts = line.strip().split()  # Split each line into a part
            make = parts[0].lower()  # Get the column of car makes and convert it to lowercase
            services = {}  # Initialize a dictionary to store service names and their recommended mileage
            for i in range(1, len(header)):  # Iterate over the available service columns excluding the column of car makes 
                if i < len(parts):  # Check if there's a mileage value for this service in the current line
                    service_name = header[i]  # Get the service name from the header
                    service_value = parts[i].replace(',', '')  # Remove commas and get the service value
                    try:
                        services[service_name] = int(service_value)  # Convert the service mileage string to an integer 
                    except ValueError:
                        services[service_name] = 0  # Handle invalid values as 0 mileage
            recom[make] = services  # Add the services to the recommendations dictionary, indexed by car make

    #Now we check if the car make is in the recommendations dictionary
    if car_make in recom:
        services = recom[car_make]  # Get the services for the specified car make
        recommended_services = []  # Initialize a list to store recommended services
        for service, interval in services.items():
            if mileage >= interval:
                recommended_services.append(service)  # Add the service to the list if the mileage is greater or equal to the recommended interval
        if recommended_services:
            recommend=', '.join(recommended_services)
    
            return f"Here is a list of recommended services: {recommend}"  # Return the list of recommended services of the vehicle the user 
        else:
            return ["No recommended service at this mileage"]  # Return a message if no services are recommended
    else:
        return ["Car make not found in recommendations"]  # Return a message if the car make is not found in the recommendations

def save_data_to_file(car_info, mileage, services):
    with open('service_recommendations.txt', 'a') as file:
        file.write("Year, Make, Model: {}\n".format(car_info))
        file.write("Mileage: {}\n".format(mileage))
        file.write("Service Recommendations: {}\n\n".format(services))

def display_saved_data():
    with open('service_recommendations.txt', 'r') as file:
        saved_data = file.read()
        print("Saved Data:\n")
        print(saved_data)

# Main program starts here

print("Developed by Angel Daniel Fuentes, Fuentes Designs TM*\n\n\n\n\n")

print("This program is used to create a service recommendation.\n\nThis is based on your vehicle's Year, Make and Mileage.")
american = ('GM', 'Ford', 'Chrysler')  # List of American car makes
european = ('Audi', 'BMW', 'Volkswagen', 'Volvo')  # List of European car makes
asian = ('Toyota', 'Honda', 'Nissan', 'Mazda')  # List of Asian car makes

# Initialize the carList variable
carList = [american, european, asian]

print("You will be asked a series of information regarding your vehicle.\nEnter accurately below to return accurate service recommendations.")
x = 1  # Initialize a loop control variable
  # Initialize a list to store car information

# Main loop for entering car information
while x > 0:
    car = []
    carYear=0
    carMake=""
    carModel=""
    carYear = input("Please enter the year of your vehicle:\n")
    if not carYear.isdigit():
        print("Input is not a correct response, please try again")
        continue
    else:
        carYear = int(carYear)
        print("\nAmerican Makes:")
        for make in american:
            print(make)
        print("\nEuropean Makes:")
        for make in european:
            print(make)
        print("\nJapanese Makes:")
        for make in asian:
            print(make)
        carMake = input("\nPlease enter the make of your vehicle from the given list:\n").title()  # Convert to title case
        if carMake not in [make.title() for line in carList for make in line]:
            print("Invalid Car make. Please input the correct info")
            continue
        carModel = input("Please enter the model of your vehicle:\n")  # Separate variable for model

        mileage = 0  # Initialize mileage
        while True:
            try:
                mileage = int(input("Please enter the mileage of your vehicle:\n"))  # Request mileage input here
                if mileage < 0:
                    print("Invalid input for mileage. Please input the correct mileage")
                else:
                    break  # Break out of the loop if mileage is valid
            except ValueError:
                print("Invalid input for mileage. Please input the correct mileage")
        carInfo=[]
        car.append(carYear)
        car.append(carMake)
        car.append(carModel)
        carInfo = " ".join(map(str, car))

        print("You have a", carInfo, " with", mileage, "miles.")
        carMakeLow=carMake.lower()
        services = service_recommendations(carMakeLow, mileage)  # Access the services for the car make
        print(services) 

        # Save the data to a file
        save_data_to_file(carInfo, mileage, services)



        choice = input("If you would like to enter another car, enter 'Y'. If you are done and would like to return your cars and services, enter 'N")
        if choice.lower() == 'y':
            carInfo=[]
            carYear=0
            carMake=""
            carModel=""
            continue
        else:
            display_saved_data()  # Display the saved data
            x = 0
