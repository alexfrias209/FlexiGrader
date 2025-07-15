# Initialize an empty list to store cars
cars = []

# Create an infinite loop to dislay a menu and handle their choices
while True:
    # Displaying the menu options
    print("\nOptions:")
    print("1. Add a car")
    print("2. View cars")
    print("3. Search for a car")
    print("4. Exit")

    # Getting their choice
    user_choice = input("Enter your choice (1/2/3/4): ")

    # Option 1: add a new car to create a list
    if user_choice == "1":
        # Prompt to enter the car details
        make = input("Enter the car make: ")
        model = input("Enter the car model: ")
        year = input("Enter the car year: ")
        # Create a dictionary to represent the car
        car = {"Make": make, "Model": model, "Year": year}
        # Add the car dictionary to 'cars' list
        cars.append(car)
        # Notify them that the car was added
        print("Car added successfully!")
        continue        # continue to the menu
    
    # Option 2: View the list of cars
    elif user_choice == "2":
        if not cars:        # If 'cars' list is empty, inform them
            print("No cars in the list.")
        else:
            # Display the details of each car in the 'cars' list
            print("\nCars:")
            for idx, car in enumerate(cars, start=1):               
                print(f"{idx}. Make: {car['Make']}, Model: {car['Model']}, Year: {car['Year']}")

    # Option 3: Search for the car by make
    elif user_choice == "3":        # Prompt to enter the making of the car to search for
        search_make = input("Enter the make of the car to search for: ")
        found_cars = []
        for car in cars:
            if car["Make"].lower() == search_make.lower():
                # If the make matches, add the car to the 'found_cars' list
                found_cars.append(car)
        if found_cars:
            # If matching cars were found, inform them
            print("\nFound cars:")
            for idx, found_car in enumerate(found_cars, start=1):
                print(f"{idx}. Make: {found_car['Make']}, Model: {found_car['Model']}, Year: {found_car['Year']}")
        else:       # If no matching cars were found, inform them
            print(f"No cars with make '{search_make}' found.")
    # Option 4: Exit the program
    elif user_choice == "4":        # inform the user that the program is exiting
        print("Exiting the program.")
        break

    else:       # If they enter an invalid choice, inform them 
        print("Invalid input. Please choose a valid option (1/2/3/4).")
