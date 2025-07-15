print("Welcome to the Top 3 Major Employment Analysis")

print("Pick your desired choice and enjoy learning about the Top 3 Majors of 2022-2023!")

while True:
    print("\nPlease choose an option:")
    print("1. Top 3 Most Employed Majors of 2022-2023")
    print("2. Growth Expectancy")
    print("3. Unemployment Expectancy")
    print("4. Annual Wage")
    print("5. Exit")
    
    user_choice = input("Enter your choice (1/2/3/4/5): ")
    
    if user_choice =='1':
        while True:
            print("\nThe Top 3 Most Employed Majors of 2022-2023")
            print("1. Biomedical Engineering")
            print("2. Computer Science")
            print("3. Marine Engineering")
            print("4. Nevermind!")
            
            sub_choice = input("Please chose (1/2/3/4):")
            major_choice = None

            if sub_choice =='1':
                major_choice = "You chose the Top 1 most employed major of 2022-2023: Biomedical Engineering."
            elif sub_choice == '2':
                major_choice = "You chose the Top 2 most employed major of 2022-2023: Computer Science."
            elif sub_choice == '3':
                major_choice = "You chose the Top 3 most employed major of 2022-2023: Marine Engineering."
            elif sub_choice == '4':
                break
            else:
                print("Invalid sub_choice. Please select a valid option (1/2/3/4).")
                continue
            with open("60533_6414915_4197823.txt", 'a') as file:
                file.write(f"Most Employed Major: {major_choice}\n")
            print(major_choice) 
    

    elif user_choice =='2':
        while True:
            print("\nThe Growth Expectancy for the Top 3 majors of 2022-2023")
            print("1. Biomedical Engineering")
            print("2. Computer Science")
            print("3. Marine Engineering")
            print("4. Nevermind!")
            
            sub_choice = input("Please pick a major (1/2/3/4):")
            growth_choice = None
            
            if sub_choice =='1':
                growth_choice = "There is a projected 5 percent growth expectancy from 2022 to 2032."
            elif sub_choice == '2':
                growth_choice = "There is a projected 23 percent growth expectancy from 2022 to 2032."
            elif sub_choice == '3':
                growth_choice = "There is a projected 3 percent growth expectancy from 2022 to 2032."
            elif sub_choice == '4':
                break
            else:
                print("Invalid sub_choice. Please select a valid option (1/2/3/4).")
                continue
            with open("60533_6414915_4197823.txt", "a") as file:
                file.write(f"Growth Expectancy for Major: {growth_choice}\n")
            print(growth_choice) 

    elif user_choice =='3':
        while True:
            print("\nThe Unemployment Expectancy for the Top 3 majors of 2022-2023")
            print("1. Biomedical Engineering")
            print("2. Computer Science")
            print("3. Marine Engineering")
            print("4. Nevermind!")
            
            sub_choice = input("Please pick a major (1/2/3/4):")
            unemployment_choice = None
            
            if sub_choice =='1':
                unemployment_choice = "There is a projected 4 percent unemployment expectancy."
            elif sub_choice == '2':
                unemployment_choice = "There is a projected 5 percent unemployment expectancy."
            elif sub_choice == '3':
                unemployment_choice = "There is a projected 2 percent unemployment expectancy."
            elif sub_choice == '4':
                break
            else:
                print("Invalid sub_choice. Please select a valid option (1/2/3/4).")
                continue
            with open("60533_6414915_4197823.txt", "a") as file:
                file.write(f"Unemployment Expectancy for Major: {unemployment_choice}\n")
            print(unemployment_choice)  

    elif user_choice =='4':
        while True:
            print("\nThe annual pay for the Top 3 majors of 2022-2023")
            print("1. Biomedical Engineering")
            print("2. Computer Science")
            print("3. Marine Engineering")
            print("4. Nevermind!")
            
            sub_choice = input("Please chose a major (1/2/3/4):")
            annual_choice = None
            
            if sub_choice =='1':
                annual_choice = "Biomedical Engineering has an annual pay of $99,550."
            elif sub_choice == '2':
                annual_choice = "Computer Science has an annual pay of $136,620."
            elif sub_choice == '3':
                annual_choice = "Marine Engineering has an annual pay of $96,910."
            elif sub_choice == '4':
                break
            else:
                print("Invalid sub_choice. Please select a valid option (1/2/3/4).")
                continue
            with open("60533_6414915_4197823.txt", "a") as file:
                file.write(f"Annual Employment: {annual_choice}\n")
            print(annual_choice)  

    elif user_choice == '5':
        break

print("Thank you for using the Top 3 Major Employment Analysis. Your choices have been saved in 'user_choice.txt'.")