import os
print('Welcome to the currency converter.')
print('This program is a currency converter. It will ask you to enter the origin code,') 
print('destination code, and amount to be converted. It will utilize different files depending on the origin.\n')

# This function will execute the conversion.
def convert_currencies(origin, destination, amount):
    rates = open(f'{origin}.txt', 'r')  # will open the file that coresponds with the origin

    dic1 = {} # creates an empty dictionary

    ex_amount = 0.0   # initialize the exchange amount variable

    for line in rates.readlines():  # read in the lines from the origin file
        if destination in line: # if statement for when it reaches the line with the destination code
            dest_code, rate = line.split('\t')  # splits the line that corresponds with the destination
            dic1[dest_code] = float(rate)   # adds the line to the empty dictionary, and conveting the rate to a float type
            ex_amount = amount * dic1[dest_code]    # conducts the conversion operation

    rates.close()   # closes the origin file
    return ex_amount    # returns the value of the exchange amount

start = input("Do you want to convert currencies (Y/N)? ")
print(os.getcwd())
while start == "Y":

    dic = {}    # creates an empty dictionary

    f = open('Countries.txt', 'r')  # opens a text file with the available exchange currencies

    print('CODE    Currency')

    for line in f.readlines():  # 'for' loop to read over the file one line at a time
        print(line)
        code, currency = line.split('\t')   # splits the line
        dic[code] = currency    # adds the split line to the dictionary
    print('\n')

    f.close()   # closes the file

    origin = input('Enter the code for the origin currency: ') # Code for the currency
    if origin in dic: # if loop to check if origin code is in the dictionary
        dest = input('Enter the code for the destination currency: ')
        if dest in dic: # if loop to check if destination code is in the dictionary
            amount = float(input('Enter amount to convert: '))
            dest_amount = convert_currencies(origin, dest, amount) # calls on the convert_currencies fuction
            print(f'You are converting {dic[origin][0:-1]} to {dic[dest][0:-1]}.')
            print(f'{amount} {dic[origin][0:-1]} is worth {dest_amount:.2f} {dic[dest][0:-1]}')
        else:
            print('Destination code not valid.')
    else:
        print('Origin code not valid.')
    
    start = input("Do you want to convert currencies (Y/N)? ")

if start == "N":
    print("Have a good day.")