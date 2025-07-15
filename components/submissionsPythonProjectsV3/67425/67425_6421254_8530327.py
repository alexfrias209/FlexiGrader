import pandas

def recommend(min_budget, max_budget, in_type, mpg, df):
    recommended = df[(df["cost"] <= max_budget) & (df["cost"] >= min_budget) & (df["type"].str.lower() == in_type.lower()) & (df["mpg"] >= mpg)]
    return recommended

def add_vehicle(df, make, model, vehicle_type, cost, mpg):
    new_vehicle = {"Make": make, "model": model, "type": vehicle_type, "cost": cost, "mpg": mpg}
    df = df._append(new_vehicle, ignore_index=True)
    df.to_csv ("67425_6421255_9908153.csv", index=False)

def main():
    print("\nWelcome to the new vehicle finder!\nThis program is meant to help you find a car that is within your budget and meets your needs.")
    df = pandas.read_csv("67425_6421255_9908153.csv")
    
    ask_add = input("Do you want to add a new car? ('yes' or 'no'): ")
    if ask_add.lower() == "yes":
        Make = input("Enter the brand of the new vehicle: ")
        model = input("Enter the model of the new vehicle: ")
        vehicle_type = input("Enter the type of the new vehicle (Coupe, Sedan, SUV, Truck): ")
        cost = int(input("Enter the cost of the new vehicle: "))
        mpg = int(input("Enter the fuel efficiency in MPG: "))
        add_vehicle(df, Make, model, vehicle_type, cost, mpg)
        print("The new vehicle has been added successfully, thanks!")

    else:
        print("Okay lets look for a new car!")
        min_budget = int(input("Enter your minimum budget: "))
        max_budget = int(input("Enter your maximum budget: "))
        in_type = input("Enter your desired vehicle type (Coupe, Sedan, SUV, Truck): ")
        mpg = int(input("Enter your minimum desired fuel efficiency in MPG: "))
        out_recommended = recommend(min_budget, max_budget, in_type, mpg, df)

        if out_recommended.empty:
            print("\nNo vehicles meet your needs, try again. Maybe with a bigger budget!")
        else:
            print("\n The cars that meet your needs are:")
            print(out_recommended.to_string(index=False))

main()
