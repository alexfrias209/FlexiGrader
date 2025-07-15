import csv
import os
def checklocation(state_choice, county_choice):
    with open("62098_6419756_5409740.csv", mode ='r') as file:
        data_file = csv.reader(file)
        location_valid = 0
        for lines in data_file:
            if set([state_choice, county_choice]).issubset(set(lines)):
                location_valid = 1
        file.close()
        return location_valid
def finddata_location(data_file, state_choice, county_choice):
    state_data = []
    county_data = []
    for lines in data_file:
        if state_choice == lines[0]:
            state_data.append(lines)
    for lines in state_data:
        if county_choice == lines[1]:
            county_data.append(lines)
    return county_data
def turndateintostring(yyyy, mm, dd):
    yyyy_str = str(yyyy)
    mm_str = str(f'{mm:02d}')
    dd_str = str(f'{dd:02d}')
    date_choice = yyyy_str + '-' + mm_str + '-' + dd_str
    return date_choice
while True:
    print('Welcome to the air quality checker! \nDeveloped by Clement Yo \nWith this project, you can view daily and annual summary air quality data for your selected location')
    print()
    state_choice = str(input('Please enter the state: '))
    county_choice = str(input('Please enter the county: '))
    print(f'You chose {county_choice} County in {state_choice}')
    location_valid = checklocation(state_choice, county_choice)
    if location_valid == 1:
        print('Your location choice is valid.')
    else:
        print('Your location choice is invalid, please check state and county spelling/capitalization.')
        end_program = str(input('Press Y to restart, N to quit '))
        if end_program == 'Y':
            continue
        elif end_program == 'N':
            exit()
    data_choice = int(input('Would you like to view: \n1. Daily air quality data \n2. Annual summary \nPlease type 1 or 2 to select'))
    print()
    state_data = []
    county_data = []
    if data_choice == 1:
        with open("62098_6419756_5409740.csv", mode ='r') as file:
            data_file = csv.reader(file)
            county_data = finddata_location(data_file, state_choice, county_choice)
            yyyy = int(input('Please enter the year: '))
            print()
            mm = int(input('Please enter the month: '))
            print()
            dd = int(input('Please enter the date: '))
            print()
            date_choice = turndateintostring(yyyy, mm, dd)
            print(date_choice)
            for i in county_data:
                if date_choice in i:
                    print(f'The air quality index on {date_choice} in {county_choice}, {state_choice} was {i[5]}, categorized as "{i[6]}".')
                    break
            else:
                print('There appears to be no data for the given date...')
                breakoutflag = False
                for j in range(15):
                    new_yyyy_neg = yyyy
                    new_mm_neg = mm
                    new_dd_neg = dd - (j + 1)
                    new_yyyy_pos = yyyy
                    new_mm_pos = mm
                    new_dd_pos = dd + (j + 1)
                    if new_dd_neg < 1:
                        new_mm_neg = mm - 1
                        if new_mm_neg < 1:
                            new_yyyy_neg = yyyy - 1
                            new_mm_neg = 12 + new_mm_neg
                        if new_mm_neg == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                            new_dd_neg = 31 + new_dd_neg
                        elif new_mm_neg == 4 or 6 or 9 or 11:
                            new_dd_neg = 30 + new_dd_neg
                        elif new_mm_neg == 2 and ((new_yyyy_neg % 4) != 0 or ((new_yyyy_neg % 400) != 0 and (new_yyyy_neg % 100) == 0)):
                            new_dd_neg = 28 + new_dd_neg
                        elif new_mm_neg == 2 and new_yyyy_neg % 4 == 0:
                            new_dd_neg = 29 + new_dd_neg
                    if new_dd_pos > 28:
                        if new_dd_pos > 28 and mm == 2 and ((yyyy % 4) != 0 or ((yyyy % 100) == 0 and (yyyy % 400) != 0)):
                            new_mm_pos = mm + 1
                            new_dd_pos = new_dd_pos - 28
                        elif new_dd_pos > 29 and mm == 2 and yyyy % 4 == 0:
                            new_mm_pos = mm + 1
                            new_dd_pos = new_dd_pos - 29
                        elif new_dd_pos > 30 and mm == 4 or 6 or 9 or 11:
                            new_mm_pos = mm + 1
                            new_dd_pos = new_dd_pos - 30
                        elif new_dd_pos > 31 and mm == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                            new_mm_pos = mm + 1
                            new_dd_pos = new_dd_pos - 31
                        if new_mm_pos > 12:
                            new_yyyy_pos = yyyy + 1
                            new_mm_pos = new_mm_pos - 12
                    date_choice_neg = turndateintostring(new_yyyy_neg, new_mm_neg, new_dd_neg)
                    date_choice_pos = turndateintostring(new_yyyy_pos, new_mm_pos, new_dd_pos)
                    for i in county_data:
                        if date_choice_pos in i:
                            print(f'However, on the closest date... \nThe air quality index on {date_choice_pos} in {county_choice}, {state_choice} was {i[5]}, categorized as "{i[6]}".')
                            breakoutflag = True
                            break
                        elif date_choice_neg in i:
                            print(f'However, on the closest date... \nThe air quality index on {date_choice_neg} in {county_choice}, {state_choice} was {i[5]}, categorized as "{i[6]}".')
                            breakoutflag = True
                            break
                    if breakoutflag:
                        break
                else:
                    print('There is no data within 15 days before or after your chosen date, please choose another date')
    if data_choice == 2:
        with open("62098_6419755_9312668.csv", mode ='r') as file:
            data_file = csv.reader(file)
            county_data = finddata_location(data_file, state_choice, county_choice)
            year_choice = str(input('Please enter the year you would like to view the summary for (supported years: 2020, 2021, 2022): '))
            print()
            for i in county_data:
                if year_choice in i:
                    print(f'In {year_choice}, of the {i[3]} days measured, {county_choice}, {state_choice} had {i[4]} good days, {i[5]} moderate days, {i[6]} unhealthy for sensitive groups days, {i[7]} unhealthy days, and {i[8]} hazardous days. The maximum measured AQI was {i[10]}, the 90th percentile AQI was {i[11]}, and the median AQI was {i[12]}.')
                    break
            else:
                print('Please enter a valid year.')
    end_of_program = str(input('Would you like to continue? \nY to continue, N to end program '))
    print()
    if end_of_program == 'Y':
        continue
    elif end_of_program == 'N':
        exit()
                


