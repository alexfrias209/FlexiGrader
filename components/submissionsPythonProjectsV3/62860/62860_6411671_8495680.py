print('This project is meant to calculate a monthly loan payment of the user.')

while True:
    user_choice = input('Do you want to calculate a monthly loan payment? (yes/no): ')

    if user_choice == 'yes':
        print('Lets gather some basic information about your loan.')
        break
    if user_choice == 'no':
        print('Then why are you here?')
        import sys
        sys.exit()
#simple yes/no line, if user desnt want to use the program then the program ends

import math
# math involved with this program

print('Please only enter values in numerical form; for example, two thousand should be 2000; or thirty four should be 34.')
print('Only include the number value; dont put "months" or % at the end of each value.')


while True:
    try:
        Annual_percentage_rate = input('Please enter an Annual Percentage rate. (interest rate)')
        APR_percent = float(Annual_percentage_rate)
        APR_decimal = APR_percent / 100
        # float commands make the variable into a number that can be manipulated, and was divided by 100 to turn a value into decimal form.
        print('Your APR is', Annual_percentage_rate, 'percent; or,', APR_decimal, 'in decimal form.')
        break
    except ValueError:
        print('Please enter a number value only; as the instructions read. Three should be 3.')
        # value error makes sure the program doesnt end because of an error; but prompts a retry from the user. 
        
    
while True:
    try:
        principal = input('Please enter the principal of your loan; or the base price before interest.')
        principal = float(principal)
        print('Your principal is', principal, ' dollars.')
        break
    except ValueError:
        print('These values should be numerical values, not words. If you get a message like this last time then you need to read instrutions.')

while True:
    try:
        loan_length = input('How many years will your loan last?')
        loan_length = float(loan_length)
        print('Your loan payments will last', loan_length, 'year(s).')
        break
    except ValueError:
        print('Number Values please. If youre getting this message for the second or third time then read the instructions.')

print('Since we are calculating a monthly loan payment, you will be making 12 payments per year.')

def calculate_loan(principal, APR_decimal, loan_length):
    Monthly_payment = (principal * (APR_decimal / 12)) / (1-(1+APR_decimal/12) ** -(12*loan_length))
    Monthly_payment = float(Monthly_payment)
    Monthly_payment = round(Monthly_payment, 2)
    return Monthly_payment
    # turned a simple equation into a funtion that can be called upon
    
result = calculate_loan(principal, APR_decimal, loan_length)
    # function is used to pull all of the user generated values and puts them accordingly into the funtion or equation. 
print(f'Your monthly loan payment is estimated to be about {result} dollars per month for the next', loan_length,'years.')
 # the line of code displayed the amount paid per month, or the output of the funtion, as well as how long you have to pay that sum. This is the payment scheduel. 

while True:
    satisfactory = input('Are you happy with your outcome?')
    
    if satisfactory == 'yes':
        break
    else:
        print('nuh uh. You are satisfied with the outcome. say yes.')
    
    # just used this as a way for the program to NOT end and close abruptly when running this on my computer. 
        





