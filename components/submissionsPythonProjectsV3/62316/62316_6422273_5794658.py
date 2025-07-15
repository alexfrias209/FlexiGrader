print()
print("Welcome to DeskFinder!")
print("Developed")
print("Please use this program to find a desk to use.")

#CODE WILL LOOP ALLOWING USER TO CONTINUE USING UNTIL THEY DECIDE THEY DON'T WANT TO.

while True:
    
    #THIS FIRST PART ALLOWS USERS TO CHOOSE THE DESK THEY WANT.
    
    print()
    print("[Desk 1]     [Desk 2]     [Desk 3]     [Desk 4]")
    print()
    print("[Desk 5]     [Desk 6]     [Desk 7]     [Desk 8]")
    print()
    user_choice = input("Which desk would you like to choose? (Please type desk number.)\n(Type 'Exit' to exit.)\n")
    if "1" in user_choice:
        print("You have selected Desk 1.")
        x = 1
    elif "2" in user_choice:
        print("You have selected Desk 2.")
        x = 2
    elif "3" in user_choice:
        print("You have selected Desk 3.")
        x = 3
    elif "4" in user_choice:
        print("You have selected Desk 4.")
        x = 4
    elif "5" in user_choice:
        print("You have selected Desk 5.")
        x = 5
    elif "6" in user_choice:
        print("You have selected Desk 6.")
        x = 6
    elif "7" in user_choice:
        print("You have selected Desk 7.")
        x = 7
    elif "8" in user_choice:
        print("You have selected Desk 8.")
        x = 8
    elif user_choice.upper() == "EXIT":
        print("Exiting...")
        break
    else:
        print()
        user_choice = input("Please choose a desk from the screen or Exit.\n")
        if "1" in user_choice:
            print("You have selected Desk 1.")
            x = 1
        elif "2" in user_choice:
            print("You have selected Desk 2.")
            x = 2
        elif "3" in user_choice:
            print("You have selected Desk 3.")
            x = 3
        elif "4" in user_choice:
            print("You have selected Desk 4.")
            x = 4
        elif "5" in user_choice:
            print("You have selected Desk 5.")
            x = 5
        elif "6" in user_choice:
            print("You have selected Desk 6.")
            x = 6
        elif "7" in user_choice:
            print("You have selected Desk 7.")
            x = 7
        elif "8" in user_choice:
            print("You have selected Desk 8.")
            x = 8
        elif user_choice.upper() == "EXIT":
            print("Exiting...")
            break
    print()
    next_choice = input("What would you like to do? (Type corresponding number)\n1. Use desk now. (180 minute maximum time use)\n2. Check desk reservations.\n3. Exit.\n")
    print()
    if "1" in next_choice:
        
        #IF USERS WANT TO USE THE DESK NOW, THE PROGRAM SENDS THEM REMINDERS BEFORE THEY USE THE DESIRED DESK.
        
        print("Please make sure to...\n")
        print("1. Check the desk is not currently in use.\n2. Remember to give up the desk to those who have reservations.\n3. Be mindful of the 180 minute time limit to use the desk.\n")
        print("Thank you.\n")
        print("Exiting...")
        break
    elif "2" in next_choice:
        
        #THIS PART OF THE CODE ALSO LOOPS UNTIL THE USER DECIDES TO EXIT. THE CODE WILL ALLOW THE USER TO INSEPCT RESERVATIONS OF THE DESK THEY CHOSE.
        #THEY WILL BE ABLE TO SEE THE AVAILABLE TIMES FOR WHATEVER DATES THEY CHOOSE AND ALSO BE ABLE TO RESERVE FOR ANY AVAILABLE TIMES.
        
        while True:
            if x == 1:
                print()
                print("1. January   2. February 3. March     4. April")
                print("5. May       6. June     7. July      8. August")
                print("9. September 10. October 11. November 12. December\n")
                month_res = int(input("Which month would you like to check the desk reservation? (Please type the corresponding number.)\n"))
                month_dict = {
                        "1" : "JANUARY",
                        "2" : "FEBRUARY",
                        "3" : "MARCH",
                        "4" : "APRIL",
                        "5" : "MAY",
                        "6" : "JUNE",
                        "7" : "JULY",
                        "8" : "AUGUST",
                        "9" : "SEPTEMBER",
                        "10" : "OCTOBER",
                        "11" : "NOVEMBER",
                        "12" : "DECEMBER",
                    }
                day31list = [1, 3, 5, 7, 10, 12]
                day30list = [4, 6, 8, 9, 11]
                if month_res in day31list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n| 31                            |\n")
                elif month_res in day30list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n")
                elif month_res == 2:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28       |\n")
                day_res = input("Which day would you like to check the desk reservation? (Please type corresponding day.)\n")
                year_res = input("What year would you like to check? (ex: 2023, 2024, etc.)\n")
                month_res = str(month_res)
                timebox = []
                checkres = []
                checkres.append(month_dict[month_res])
                checkres.append(day_res)
                checkres.append(year_res)
                with open("desk1.txt", 'r') as f:
                    for resline in f:
                        resline = str(resline)
                        reslinecheck = resline.split()
                        comp = []
                        comp.append(reslinecheck[0])
                        comp.append(reslinecheck[1])
                        comp.append(reslinecheck[2])
                        if checkres == comp:
                            timebox.append(reslinecheck[3])
                print("The available times for this date are...\n")
                timeslots = ["8AM", "11AM", "2PM", "5PM"]
                for timing in timeslots[:]:
                    if timing in timebox:
                        timeslots.remove(timing)
                for availtime in timeslots:
                    print(availtime)
                print()
                print("Would you like to reserve for any of these times?\n(Type the corresponding number.)\n")
                res_next = input("1. Yes\n2. No\n3. Back to main menu.\n")
                if res_next == "1":
                    print()
                    resertime = input("Please enter the time you would like to reserve as it is written on screen.\n")
                    resertime = resertime.upper()
                    checkres.append(resertime)
                    updateres = checkres[0] + ' ' + checkres[1] + ' ' + checkres[2] + ' ' + checkres[3]
                    with open("desk1.txt", 'a') as f:
                        f.write(updateres + "\r")
                    print()
                    print("You have successfully reserved Desk 1 for", checkres[3], "on", checkres[0], checkres[1], checkres[2])
                    print()
                elif res_next == "2":
                    continue
                elif res_next == "3":
                    print("Heading back to main menu...")
                    break   
            elif x == 2:
                print()
                print("1. January   2. February 3. March     4. April")
                print("5. May       6. June     7. July      8. August")
                print("9. September 10. October 11. November 12. December\n")
                month_res = int(input("Which month would you like to check the desk reservation? (Please type the corresponding number.)\n"))
                month_dict = {
                        "1" : "JANUARY",
                        "2" : "FEBRUARY",
                        "3" : "MARCH",
                        "4" : "APRIL",
                        "5" : "MAY",
                        "6" : "JUNE",
                        "7" : "JULY",
                        "8" : "AUGUST",
                        "9" : "SEPTEMBER",
                        "10" : "OCTOBER",
                        "11" : "NOVEMBER",
                        "12" : "DECEMBER",
                    }
                day31list = [1, 3, 5, 7, 10, 12]
                day30list = [4, 6, 8, 9, 11]
                if month_res in day31list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n| 31                            |\n")
                elif month_res in day30list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n")
                elif month_res == 2:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28       |\n")
                day_res = input("Which day would you like to check the desk reservation? (Please type corresponding day.)\n")
                year_res = input("What year would you like to check? (ex: 2023, 2024, etc.)\n")
                month_res = str(month_res)
                timebox = []
                checkres = []
                checkres.append(month_dict[month_res])
                checkres.append(day_res)
                checkres.append(year_res)
                with open("desk2.txt", 'r') as f:
                    for resline in f:
                        resline = str(resline)
                        reslinecheck = resline.split()
                        comp = []
                        comp.append(reslinecheck[0])
                        comp.append(reslinecheck[1])
                        comp.append(reslinecheck[2])
                        if checkres == comp:
                            timebox.append(reslinecheck[3])
                print("The available times for this date are...\n")
                timeslots = ["8AM", "11AM", "2PM", "5PM"]
                for timing in timeslots[:]:
                    if timing in timebox:
                        timeslots.remove(timing)
                for availtime in timeslots:
                    print(availtime)
                print()
                print("Would you like to reserve for any of these times?\n(Type the corresponding number.)\n")
                res_next = input("1. Yes\n2. No\n3. Back to main menu.\n")
                if res_next == "1":
                    print()
                    resertime = input("Please enter the time you would like to reserve as it is written on screen.\n")
                    resertime = resertime.upper()
                    checkres.append(resertime)
                    updateres = checkres[0] + ' ' + checkres[1] + ' ' + checkres[2] + ' ' + checkres[3]
                    with open("desk2.txt", 'a') as f:
                        f.write(updateres + "\r")
                    print()
                    print("You have successfully reserved Desk 2 for", checkres[3], "on", checkres[0], checkres[1], checkres[2])
                    print()
                elif res_next == "2":
                    continue
                elif res_next == "3":
                    print("Heading back to main menu...")
                    break
            elif x == 3:
                print()
                print("1. January   2. February 3. March     4. April")
                print("5. May       6. June     7. July      8. August")
                print("9. September 10. October 11. November 12. December\n")
                month_res = int(input("Which month would you like to check the desk reservation? (Please type the corresponding number.)\n"))
                month_dict = {
                        "1" : "JANUARY",
                        "2" : "FEBRUARY",
                        "3" : "MARCH",
                        "4" : "APRIL",
                        "5" : "MAY",
                        "6" : "JUNE",
                        "7" : "JULY",
                        "8" : "AUGUST",
                        "9" : "SEPTEMBER",
                        "10" : "OCTOBER",
                        "11" : "NOVEMBER",
                        "12" : "DECEMBER",
                    }
                day31list = [1, 3, 5, 7, 10, 12]
                day30list = [4, 6, 8, 9, 11]
                if month_res in day31list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n| 31                            |\n")
                elif month_res in day30list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n")
                elif month_res == 2:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28       |\n")
                day_res = input("Which day would you like to check the desk reservation? (Please type corresponding day.)\n")
                year_res = input("What year would you like to check? (ex: 2023, 2024, etc.)\n")
                month_res = str(month_res)
                timebox = []
                checkres = []
                checkres.append(month_dict[month_res])
                checkres.append(day_res)
                checkres.append(year_res)
                with open("desk3.txt", 'r') as f:
                    for resline in f:
                        resline = str(resline)
                        reslinecheck = resline.split()
                        comp = []
                        comp.append(reslinecheck[0])
                        comp.append(reslinecheck[1])
                        comp.append(reslinecheck[2])
                        if checkres == comp:
                            timebox.append(reslinecheck[3])
                print("The available times for this date are...\n")
                timeslots = ["8AM", "11AM", "2PM", "5PM"]
                for timing in timeslots[:]:
                    if timing in timebox:
                        timeslots.remove(timing)
                for availtime in timeslots:
                    print(availtime)
                print()
                print("Would you like to reserve for any of these times?\n(Type the corresponding number.)\n")
                res_next = input("1. Yes\n2. No\n3. Back to main menu.\n")
                if res_next == "1":
                    print()
                    resertime = input("Please enter the time you would like to reserve as it is written on screen.\n")
                    resertime = resertime.upper()
                    checkres.append(resertime)
                    updateres = checkres[0] + ' ' + checkres[1] + ' ' + checkres[2] + ' ' + checkres[3]
                    with open("desk3.txt", 'a') as f:
                        f.write(updateres + "\r")
                    print()
                    print("You have successfully reserved Desk 3 for", checkres[3], "on", checkres[0], checkres[1], checkres[2])
                    print()
                elif res_next == "2":
                    continue
                elif res_next == "3":
                    print("Heading back to main menu...")
                    break
            elif x == 4:
                print()
                print("1. January   2. February 3. March     4. April")
                print("5. May       6. June     7. July      8. August")
                print("9. September 10. October 11. November 12. December\n")
                month_res = int(input("Which month would you like to check the desk reservation? (Please type the corresponding number.)\n"))
                month_dict = {
                        "1" : "JANUARY",
                        "2" : "FEBRUARY",
                        "3" : "MARCH",
                        "4" : "APRIL",
                        "5" : "MAY",
                        "6" : "JUNE",
                        "7" : "JULY",
                        "8" : "AUGUST",
                        "9" : "SEPTEMBER",
                        "10" : "OCTOBER",
                        "11" : "NOVEMBER",
                        "12" : "DECEMBER",
                    }
                day31list = [1, 3, 5, 7, 10, 12]
                day30list = [4, 6, 8, 9, 11]
                if month_res in day31list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n| 31                            |\n")
                elif month_res in day30list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n")
                elif month_res == 2:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28       |\n")
                day_res = input("Which day would you like to check the desk reservation? (Please type corresponding day.)\n")
                year_res = input("What year would you like to check? (ex: 2023, 2024, etc.)\n")
                month_res = str(month_res)
                timebox = []
                checkres = []
                checkres.append(month_dict[month_res])
                checkres.append(day_res)
                checkres.append(year_res)
                with open("desk4.txt", 'r') as f:
                    for resline in f:
                        resline = str(resline)
                        reslinecheck = resline.split()
                        comp = []
                        comp.append(reslinecheck[0])
                        comp.append(reslinecheck[1])
                        comp.append(reslinecheck[2])
                        if checkres == comp:
                            timebox.append(reslinecheck[3])
                print("The available times for this date are...\n")
                timeslots = ["8AM", "11AM", "2PM", "5PM"]
                for timing in timeslots[:]:
                    if timing in timebox:
                        timeslots.remove(timing)
                for availtime in timeslots:
                    print(availtime)
                print()
                print("Would you like to reserve for any of these times?\n(Type the corresponding number.)\n")
                res_next = input("1. Yes\n2. No\n3. Back to main menu.\n")
                if res_next == "1":
                    print()
                    resertime = input("Please enter the time you would like to reserve as it is written on screen.\n")
                    resertime = resertime.upper()
                    checkres.append(resertime)
                    updateres = checkres[0] + ' ' + checkres[1] + ' ' + checkres[2] + ' ' + checkres[3]
                    with open("desk4.txt", 'a') as f:
                        f.write(updateres + "\r")
                    print()
                    print("You have successfully reserved Desk 2 for", checkres[3], "on", checkres[0], checkres[1], checkres[2])
                    print()
                elif res_next == "2":
                    continue
                elif res_next == "3":
                    print("Heading back to main menu...")
                    break
            elif x == 5:
                print()
                print("1. January   2. February 3. March     4. April")
                print("5. May       6. June     7. July      8. August")
                print("9. September 10. October 11. November 12. December\n")
                month_res = int(input("Which month would you like to check the desk reservation? (Please type the corresponding number.)\n"))
                month_dict = {
                        "1" : "JANUARY",
                        "2" : "FEBRUARY",
                        "3" : "MARCH",
                        "4" : "APRIL",
                        "5" : "MAY",
                        "6" : "JUNE",
                        "7" : "JULY",
                        "8" : "AUGUST",
                        "9" : "SEPTEMBER",
                        "10" : "OCTOBER",
                        "11" : "NOVEMBER",
                        "12" : "DECEMBER",
                    }
                day31list = [1, 3, 5, 7, 10, 12]
                day30list = [4, 6, 8, 9, 11]
                if month_res in day31list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n| 31                            |\n")
                elif month_res in day30list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n")
                elif month_res == 2:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28       |\n")
                day_res = input("Which day would you like to check the desk reservation? (Please type corresponding day.)\n")
                year_res = input("What year would you like to check? (ex: 2023, 2024, etc.)\n")
                month_res = str(month_res)
                timebox = []
                checkres = []
                checkres.append(month_dict[month_res])
                checkres.append(day_res)
                checkres.append(year_res)
                with open("desk5.txt", 'r') as f:
                    for resline in f:
                        resline = str(resline)
                        reslinecheck = resline.split()
                        comp = []
                        comp.append(reslinecheck[0])
                        comp.append(reslinecheck[1])
                        comp.append(reslinecheck[2])
                        if checkres == comp:
                            timebox.append(reslinecheck[3])
                print("The available times for this date are...\n")
                timeslots = ["8AM", "11AM", "2PM", "5PM"]
                for timing in timeslots[:]:
                    if timing in timebox:
                        timeslots.remove(timing)
                for availtime in timeslots:
                    print(availtime)
                print()
                print("Would you like to reserve for any of these times?\n(Type the corresponding number.)\n")
                res_next = input("1. Yes\n2. No\n3. Back to main menu.\n")
                if res_next == "1":
                    print()
                    resertime = input("Please enter the time you would like to reserve as it is written on screen.\n")
                    resertime = resertime.upper()
                    checkres.append(resertime)
                    updateres = checkres[0] + ' ' + checkres[1] + ' ' + checkres[2] + ' ' + checkres[3]
                    with open("desk5.txt", 'a') as f:
                        f.write(updateres + "\r")
                    print()
                    print("You have successfully reserved Desk 2 for", checkres[3], "on", checkres[0], checkres[1], checkres[2])
                    print()
                elif res_next == "2":
                    continue
                elif res_next == "3":
                    print("Heading back to main menu...")
                    break
            elif x == 6:
                print()
                print("1. January   2. February 3. March     4. April")
                print("5. May       6. June     7. July      8. August")
                print("9. September 10. October 11. November 12. December\n")
                month_res = int(input("Which month would you like to check the desk reservation? (Please type the corresponding number.)\n"))
                month_dict = {
                        "1" : "JANUARY",
                        "2" : "FEBRUARY",
                        "3" : "MARCH",
                        "4" : "APRIL",
                        "5" : "MAY",
                        "6" : "JUNE",
                        "7" : "JULY",
                        "8" : "AUGUST",
                        "9" : "SEPTEMBER",
                        "10" : "OCTOBER",
                        "11" : "NOVEMBER",
                        "12" : "DECEMBER",
                    }
                day31list = [1, 3, 5, 7, 10, 12]
                day30list = [4, 6, 8, 9, 11]
                if month_res in day31list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n| 31                            |\n")
                elif month_res in day30list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n")
                elif month_res == 2:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28       |\n")
                day_res = input("Which day would you like to check the desk reservation? (Please type corresponding day.)\n")
                year_res = input("What year would you like to check? (ex: 2023, 2024, etc.)\n")
                month_res = str(month_res)
                timebox = []
                checkres = []
                checkres.append(month_dict[month_res])
                checkres.append(day_res)
                checkres.append(year_res)
                with open("desk6.txt", 'r') as f:
                    for resline in f:
                        resline = str(resline)
                        reslinecheck = resline.split()
                        comp = []
                        comp.append(reslinecheck[0])
                        comp.append(reslinecheck[1])
                        comp.append(reslinecheck[2])
                        if checkres == comp:
                            timebox.append(reslinecheck[3])
                print("The available times for this date are...\n")
                timeslots = ["8AM", "11AM", "2PM", "5PM"]
                for timing in timeslots[:]:
                    if timing in timebox:
                        timeslots.remove(timing)
                for availtime in timeslots:
                    print(availtime)
                print()
                print("Would you like to reserve for any of these times?\n(Type the corresponding number.)\n")
                res_next = input("1. Yes\n2. No\n3. Back to main menu.\n")
                if res_next == "1":
                    print()
                    resertime = input("Please enter the time you would like to reserve as it is written on screen.\n")
                    resertime = resertime.upper()
                    checkres.append(resertime)
                    updateres = checkres[0] + ' ' + checkres[1] + ' ' + checkres[2] + ' ' + checkres[3]
                    with open("desk6.txt", 'a') as f:
                        f.write(updateres + "\r")
                    print()
                    print("You have successfully reserved Desk 2 for", checkres[3], "on", checkres[0], checkres[1], checkres[2])
                    print()
                elif res_next == "2":
                    continue
                elif res_next == "3":
                    print("Heading back to main menu...")
                    break
            elif x == 7:
                print()
                print("1. January   2. February 3. March     4. April")
                print("5. May       6. June     7. July      8. August")
                print("9. September 10. October 11. November 12. December\n")
                month_res = int(input("Which month would you like to check the desk reservation? (Please type the corresponding number.)\n"))
                month_dict = {
                        "1" : "JANUARY",
                        "2" : "FEBRUARY",
                        "3" : "MARCH",
                        "4" : "APRIL",
                        "5" : "MAY",
                        "6" : "JUNE",
                        "7" : "JULY",
                        "8" : "AUGUST",
                        "9" : "SEPTEMBER",
                        "10" : "OCTOBER",
                        "11" : "NOVEMBER",
                        "12" : "DECEMBER",
                    }
                day31list = [1, 3, 5, 7, 10, 12]
                day30list = [4, 6, 8, 9, 11]
                if month_res in day31list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n| 31                            |\n")
                elif month_res in day30list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n")
                elif month_res == 2:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28       |\n")
                day_res = input("Which day would you like to check the desk reservation? (Please type corresponding day.)\n")
                year_res = input("What year would you like to check? (ex: 2023, 2024, etc.)\n")
                month_res = str(month_res)
                timebox = []
                checkres = []
                checkres.append(month_dict[month_res])
                checkres.append(day_res)
                checkres.append(year_res)
                with open("desk7.txt", 'r') as f:
                    for resline in f:
                        resline = str(resline)
                        reslinecheck = resline.split()
                        comp = []
                        comp.append(reslinecheck[0])
                        comp.append(reslinecheck[1])
                        comp.append(reslinecheck[2])
                        if checkres == comp:
                            timebox.append(reslinecheck[3])
                print("The available times for this date are...\n")
                timeslots = ["8AM", "11AM", "2PM", "5PM"]
                for timing in timeslots[:]:
                    if timing in timebox:
                        timeslots.remove(timing)
                for availtime in timeslots:
                    print(availtime)
                print()
                print("Would you like to reserve for any of these times?\n(Type the corresponding number.)\n")
                res_next = input("1. Yes\n2. No\n3. Back to main menu.\n")
                if res_next == "1":
                    print()
                    resertime = input("Please enter the time you would like to reserve as it is written on screen.\n")
                    resertime = resertime.upper()
                    checkres.append(resertime)
                    updateres = checkres[0] + ' ' + checkres[1] + ' ' + checkres[2] + ' ' + checkres[3]
                    with open("desk7.txt", 'a') as f:
                        f.write(updateres + "\r")
                    print()
                    print("You have successfully reserved Desk 2 for", checkres[3], "on", checkres[0], checkres[1], checkres[2])
                    print()
                elif res_next == "2":
                    continue
                elif res_next == "3":
                    print("Heading back to main menu...")
                    break
            elif x == 8:
                print()
                print("1. January   2. February 3. March     4. April")
                print("5. May       6. June     7. July      8. August")
                print("9. September 10. October 11. November 12. December\n")
                month_res = int(input("Which month would you like to check the desk reservation? (Please type the corresponding number.)\n"))
                month_dict = {
                        "1" : "JANUARY",
                        "2" : "FEBRUARY",
                        "3" : "MARCH",
                        "4" : "APRIL",
                        "5" : "MAY",
                        "6" : "JUNE",
                        "7" : "JULY",
                        "8" : "AUGUST",
                        "9" : "SEPTEMBER",
                        "10" : "OCTOBER",
                        "11" : "NOVEMBER",
                        "12" : "DECEMBER",
                    }
                day31list = [1, 3, 5, 7, 10, 12]
                day30list = [4, 6, 8, 9, 11]
                if month_res in day31list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n| 31                            |\n")
                elif month_res in day30list:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28 29 30 |\n")
                elif month_res == 2:
                    print()
                    print("| 1  2  3  4  5  6  7  8  9  10 |\n| 11 12 13 14 15 16 17 18 19 20 |\n| 21 22 23 24 25 26 27 28       |\n")
                day_res = input("Which day would you like to check the desk reservation? (Please type corresponding day.)\n")
                year_res = input("What year would you like to check? (ex: 2023, 2024, etc.)\n")
                month_res = str(month_res)
                timebox = []
                checkres = []
                checkres.append(month_dict[month_res])
                checkres.append(day_res)
                checkres.append(year_res)
                with open("desk8.txt", 'r') as f:
                    for resline in f:
                        resline = str(resline)
                        reslinecheck = resline.split()
                        comp = []
                        comp.append(reslinecheck[0])
                        comp.append(reslinecheck[1])
                        comp.append(reslinecheck[2])
                        if checkres == comp:
                            timebox.append(reslinecheck[3])
                print("The available times for this date are...\n")
                timeslots = ["8AM", "11AM", "2PM", "5PM"]
                for timing in timeslots[:]:
                    if timing in timebox:
                        timeslots.remove(timing)
                for availtime in timeslots:
                    print(availtime)
                print()
                print("Would you like to reserve for any of these times?\n(Type the corresponding number.)\n")
                res_next = input("1. Yes\n2. No\n3. Back to main menu.\n")
                if res_next == "1":
                    print()
                    resertime = input("Please enter the time you would like to reserve as it is written on screen.\n")
                    resertime = resertime.upper()
                    checkres.append(resertime)
                    updateres = checkres[0] + ' ' + checkres[1] + ' ' + checkres[2] + ' ' + checkres[3]
                    with open("desk8.txt", 'a') as f:
                        f.write(updateres + "\r")
                    print()
                    print("You have successfully reserved Desk 2 for", checkres[3], "on", checkres[0], checkres[1], checkres[2])
                    print()
                elif res_next == "2":
                    continue
                elif res_next == "3":
                    print("Heading back to main menu...")
                    break
    elif "3" in next_choice:
        
        #IF A USER DECIDES THEY WANT TO STOP USING THE PROGRAM, THIS CODE WILL ALLOW THEM TO EXIT.
        
        print("Exiting...")
        break
print()
print("Thank you for using DeskFinder.")
    
