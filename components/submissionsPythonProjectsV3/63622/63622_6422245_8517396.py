import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Function to calculate monthly payment with a given interest rate
def calculate_monthly_payment(principal, interest_rate, years):
    monthly_rate = interest_rate / 12 / 100
    months = years * 12
    return principal * (monthly_rate / (1 - (1 + monthly_rate) ** -months))

# Function to collect user information
def get_user_info():
    print("Welcome! Let's collect some information.")
    user_name = input("Please enter your name: ")
    principal = float(input("Enter the mortgage principal amount: $"))
    years = int(input("Enter the number of years for the mortgage: "))
    pg_and_e_payment = float(input("Enter your monthly PG&E bill payment amount: $"))
    water_payment = float(input("Enter your monthly water bill payment amount: $"))
    garbage_payment = float(input("Enter your monthly garbage bill payment amount: $"))
    sewage_payment = float(input("Enter your monthly sewage bill payment amount: $"))
    
    return user_name, principal, years, pg_and_e_payment, water_payment, garbage_payment, sewage_payment

# Function to simulate mortgage payments with varying interest rates
def simulate_mortgage(user_name, principal, years, pg_and_e_payment, water_payment, garbage_payment, sewage_payment):
    years_list, monthly_payment_list, total_expenses_list = [], [], []
    current_interest_rate = 5
    
    for year in range(1, 31):
        monthly_payment = calculate_monthly_payment(principal, current_interest_rate, years)
        total_expenses = monthly_payment + pg_and_e_payment + water_payment + garbage_payment + sewage_payment

        years_list.append(year)
        monthly_payment_list.append(monthly_payment)
        total_expenses_list.append(total_expenses)

        if current_interest_rate < 20:
            current_interest_rate += 1

    return years_list, monthly_payment_list, total_expenses_list

# Function to save data to a file
def save_data(user_name, years_list, monthly_payment_list, total_expenses_list):
    with open(f'{user_name}_mortgage_simulation_results.txt', 'w') as file:
        file.write(f"User Name: {user_name}\n")
        file.write("Year\tInterest Rate (%)\tMonthly Payment ($)\tTotal Monthly Expenses ($)\n")
        for year, interest_rate, monthly_payment, total_expenses in zip(years_list, range(5, 21), monthly_payment_list, total_expenses_list):
            file.write(f"{year}\t{interest_rate:.2f}\t{monthly_payment:.2f}\t{total_expenses:.2f}\n")

# Function to plot the results
def plot_results(years_list, total_expenses_list):
    plt.figure(figsize=(10, 6))
    plt.plot(years_list, total_expenses_list, marker='o', linestyle='-', color='b')
    plt.title('Total Monthly Expenses Over 30 Years')
    plt.xlabel('Year')
    plt.ylabel('Total Monthly Expenses ($)')
    plt.grid(True)
    plt.show()

# Function to read mortgage rate data from a CSV file
def read_mortgage_rates(MORTGAGE30US):
    df = pd.read_csv(MORTGAGE30US)
    return df['Year'], df['Mortgage Rate (%)']

# Main program
def main():
    user_name, principal, years, pg_and_e_payment, water_payment, garbage_payment, sewage_payment = get_user_info()
    
    years_list, monthly_payment_list, total_expenses_list = simulate_mortgage(
        user_name, principal, years, pg_and_e_payment, water_payment, garbage_payment, sewage_payment)
    
    save_data(user_name, years_list, monthly_payment_list, total_expenses_list)
    plot_results(years_list, total_expenses_list)
    
# Display the expected monthly expenses at the end
    final_year = years_list[-1]
    final_total_expenses = total_expenses_list[-1]
    print(f"After {final_year} years, you can expect to spend ${final_total_expenses:.2f} per month.")

if __name__ == "__main__":
    main()
