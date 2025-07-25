import matplotlib.pyplot as plt

def calculate_turbo_horsepower(turbo_size_mm, turbo_brand, num_turbos):
    if turbo_size_mm > 88:
        if turbo_brand == "Garrett":
            additional_horsepower_per_turbo = 8
        elif turbo_brand == "Holset":
            additional_horsepower_per_turbo = 6
        elif turbo_brand == "BorgWarner":
            additional_horsepower_per_turbo = 12
        else:
            additional_horsepower_per_turbo = 0

        total_additional_horsepower = num_turbos * additional_horsepower_per_turbo
    else:
        total_additional_horsepower = 0

    return total_additional_horsepower

def calculate_score(horsepower, fuel_efficiency, has_turbo, turbo_size_mm, turbo_brand, num_turbos):
    turbo_horsepower = 0
    if has_turbo:
        turbo_horsepower = calculate_turbo_horsepower(turbo_size_mm, turbo_brand, num_turbos)
    score = horsepower / 10 + turbo_horsepower
    score -= fuel_efficiency
    return score

scores_car1 = []
scores_car2 = []

while True:
    print("Car Comparison Tool. This Comparison tool takes little to no knowledge about a car, and anything not known can be found with a simple google search.")
    print("Choose an option:")
    print("1. Compare cars")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        car1_horsepower = float(input("Enter the horsepower of the first car: "))
        car1_fuel_efficiency = float(input("Enter the fuel efficiency of the first car (miles per gallon): "))
        car1_has_turbo = input("Does the first car have a turbo (yes/no)? ").lower() == 'yes'
        car1_turbo_size_mm = 0
        car1_turbo_brand = ""
        car1_num_turbos = 0

        if car1_has_turbo:
            car1_turbo_size_mm = float(input("Enter the turbo size of the first car (in millimeters): "))
            car1_turbo_brand = input("Enter the turbo brand of the first car (Garrett/Holset/BorgWarner): ")
            car1_num_turbos = int(input("Enter the number of turbos: "))

        car2_horsepower = float(input("Enter the horsepower of the second car: "))
        car2_fuel_efficiency = float(input("Enter the fuel efficiency of the second car (miles per gallon): "))
        car2_has_turbo = input("Does the second car have a turbo (yes/no)? ").lower() == 'yes'
        car2_turbo_size_mm = 0
        car2_turbo_brand = ""
        car2_num_turbos = 0

        if car2_has_turbo:
            car2_turbo_size_mm = float(input("Enter the turbo size of the second car (in millimeters): "))
            car2_turbo_brand = input("Enter the turbo brand of the second car (Garrett/Holset/BorgWarner): ")
            car2_num_turbos = int(input("Enter the number of turbos: "))

        car1_score = calculate_score(car1_horsepower, car1_fuel_efficiency, car1_has_turbo, car1_turbo_size_mm, car1_turbo_brand, car1_num_turbos)
        car2_score = calculate_score(car2_horsepower, car2_fuel_efficiency, car2_has_turbo, car2_turbo_size_mm, car2_turbo_brand, car2_num_turbos)
        scores_car1.append(car1_score)
        scores_car2.append(car2_score)
        print("\nComparison Results:")
        print(f"Car 1 Score: {car1_score}")
        print(f"Car 2 Score: {car2_score}")

        if car1_score > car2_score:
            print("Car 1 is better.")
        elif car2_score > car1_score:
            print("Car 2 is better.")
        else:
            print("Both cars are equally good.")

    elif choice == '2':
        print("Thank you for using the Car Comparison Tool")

        total_score_car1 = sum(scores_car1)
        total_score_car2 = sum(scores_car2)


        plt.figure(figsize=(6, 4))
        plt.bar(['Car 1', 'Car 2'], [total_score_car1, total_score_car2])
        plt.xlabel('Cars')
        plt.ylabel('Total Score')
        plt.title('Total Score Comparison')
        plt.show()


    else:
        print("Invalid choice. Please enter 1 or 2.")
