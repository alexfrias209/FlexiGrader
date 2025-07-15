import logging
import time
logging.basicConfig(filename='log.txt', filemode= 'a',level=logging.INFO) # Basically creaeting a log file. Just helps to see if the code is working properly or not, especially since that some math is involved.


def clear_log_file():
    with open('log.txt', 'w') as f:
        f.write(f'--- Cleared log file. ---\n')

def enter_to_fns(): # Function to create a Fibonacci Sequence just by pressing ENTER until told to end by user input.
    time_initial = time.monotonic() # Get the time the program has been open at t-initial
    fn_sequence = [0, 1] # The first two numbers in the sequence, F0 = 0 and F1 = 1 
    n = 1 # n = 1 because as it enters the loop it will become n = 2 and so on.
    print('Press [ENTER] to keep generating numbers. Input "end" to end the sequence\n')
    print('F0 = 0\n')
    print('F1 = 1')

    while True: # Loops until user inputs 'end'
        user_input = input().lower().strip()
        if user_input == 'end':
            time_final = time.monotonic() # Get the time the program has been open at t-final
            delta_t = time_final - time_initial # Get total time passed for function to run from start to end
            print(f'\nYou have pressed [ENTER] n = {n} times...')
            print(f'Based on the equation:[ Fn = Fn-2 + Fn-1 for n >= 1 ], you have created a Fibonacci Sequence up to F{n}!\n')
            print(f'Fibonacci Sequence up to F{n}:\n{fn_sequence}')
            print(f'\n---Time To Generate: {delta_t:.4f} Seconds---')

            logging.info(f'User ended enter_to_fns() while True loop => user_input = {user_input}')
            break  
        else:
            Fn = fn_sequence[-2] + fn_sequence[-1] # Fn = Fn-2 + Fn-1 for n >= 1.
            n += 1
            print(f'F{n} = {Fn}')
            fn_sequence.append(Fn) # Add generated number  to list

            # The logging is to see if the math checks out. If it does not check out then theres something wrong with how the variables are set or how the code is ordered.
            logging.info(f' |  n = {n}  |  Fn = {Fn}  |  Fn-2 = F{n-2} = {fn_sequence[-3]}  |  Fn-1 = F{n-1} = {fn_sequence[-2]}  |  FBS up to F{n}: {fn_sequence}')
            


def n_to_fns(): # Generate "n" amount of Fibonacci numbers
    while True: # Loops until user inputs an integer
        try: # accounds for when user accidentaly inputs anything other than an integer
            fn_input = int(input('Enter a number "n" to generate a sequence up to "Fn".\n > n = ').replace(',','').replace(' ',''))

            logging.info(f'\tUser input int: {fn_input}')

            fn_sequence = [0,1] # The first two numbers in the sequence, F0 = 0 and F1 = 1
            n = 1 # n = 1 because as it enters the loop it will become n = 2 and so on.
            print('\nF0 = 0')
            print('F1 = 1')

            time_initial = time.monotonic()
            try:
                while n != fn_input: # Loop will continue until n is equal to fn_input
                    Fn = fn_sequence[-2] + fn_sequence[-1]
                    n += 1 
                    print(f'F{n} = {Fn}')
                    fn_sequence.append(Fn) # Add generated numberto list

                    # The logging is to see if the math checks out. If it does not check out then theres something wrong with how the variables are set or how the code is ordered.
                    logging.info(f' |  n = {n}  |  Fn = {Fn}  |  Fn-2 = F{n-2} = {fn_sequence[-3]}  |  Fn-1 = F{n-1} = {fn_sequence[-2]}  |  FBS up to F{n}: {fn_sequence}') 
                    
                time_final = time.monotonic()
                delta_t = time_final - time_initial
                print(f'\nAccording to the equation:[ Fn = Fn-2 + Fn-1 for n >= 1 ], you have created a Fibonacci Sequence up to F{n}!\n')
                print(f'Fibonacci Sequence up to F{n}:\n{fn_sequence}')
                print(f'\n---Time To Generate: {delta_t:.4f} Seconds---')
                break
            except OverflowError:
                with open('log.txt', 'w') as f:
                    f.write(f'--- OverflowError: User attempted to generate {fn_input} Fibonacci Numbers. Cleared log file. ---\n')
                print(f'\n--- You attempted to generate {fn_input} Fibonacci Numbers. Thats way too many numbers for the program to handle. ---\n')

        except ValueError: 
            print('\nINVALID! Be sure to input an integer!')
            logging.error(f'\tUser entered an invalid literal for int() with base 10.')




def mult_phi_to_fns(): # Multiply phi to create FBS
    phi = 1.618033988749895 # Golden Ratio
    while True: # Loops until user inputs an integer
        try: # accounds for when user accidentaly inputs anything other than an integer
            while True:
                print('Enter a number "n" to indicate how many Fibonnaci Numbers you to multiply PHI by.\n[Make sure that n >= 2]')
                fn_input = int(input(' > n = ').replace(',','').replace(' ',''))
                if fn_input < 2:
                    print('\nMake sure that n >= 2')
                    logging.info('\tUser attempted to input a number less than 2')
                else:
                    break

            time_initial = time.monotonic()
            logging.info(f'\tUser input int: {fn_input}')
            print(' ')
            print('!!Take note that "=>" means we reounded to the nearest whole number!!')
            print('PHI = 1.618033988749895...')
            print('F0  =  0')
            print('F1  =  1')
            print('F2  =  1')

            fn_sequence = [0,1,1] # In this case we need to start off with F2 due to n >= 2
            n = 1 # n = 1 because as it enters the loop it will become n = 2 and so on.
            try:
                while n != fn_input: # limit as n -> infinity of [Fn * PHI] = Fn+1 , for n >= 2
                    Fn = phi * fn_sequence[-1] # Multiply phi by the last number in the index
                    n += 1
                    print(f'F{n+1}  =  PHI * F{n}  =  PHI * {fn_sequence[-1]}  =  {Fn:.4f}...  =>  {round(Fn)}') # Fn * PHI = Fn+1
                    fn_sequence.append(round(Fn))  # Add generated number (that is rounded to nearest whole) to list

                    # The logging is to see if the math checks out. If it does not check out then theres something wrong with how the variables are set or how the code is ordered.
                    logging.info(f' |  n = {n+1}  |  Fn = {Fn}  |  PHI * Fn  =  PHI * {Fn}  |  FBS up to F{n+1}: {fn_sequence}')

                time_final = time.monotonic()
                delta_t = time_final - time_initial     
                print(f'\nAccording to the equation: [ Fn * PHI = Fn+1 , for n >= 2 ], you have created a Fibonacci Sequence up to F{n+1}!\n')
                print(f'Fibonacci Sequence up to F{n+1}:\n{fn_sequence}')
                print(f'\n---Time To Generate: {delta_t:.4f} Seconds---')
                break
            except OverflowError:
                with open('log.txt', 'w') as f:
                    f.write(f'--- OverflowError: User attempted to generate {fn_input} Fibonacci Numbers. Cleared log file. ---\n')
                print(f'\n--- You attempted to generate {fn_input} Fibonacci Numbers. Thats way too many numbers for the program to handle. ---\n')

        except ValueError:
            print('\nINVALID! Be sure to input an integer!')
            logging.error(f'\tUser entered an invalid literal for int() with base 10.')



def div_fns_to_phi(): # Divide numbers in FSB to create PHI
    while True: # Loops until user inputs an integer
        try: # accounds for when user accidentaly inputs anything other than an integer

            while True: # Checks if user puts in 0. If this isnt here then math will break.
                print('Enter a number "n" to indicate what how many Fibonnaci Numbers you to divide consecutively.\n[Make sure that n >= 1]')
                fn_input = int(input(' > n = ').replace(',','').replace(' ',''))
                if fn_input == 0: 
                    print('\nDivideByZeroError: Are you trying to create a black hole?')
                    logging.info('\tMy bro is attempting to make a black hole...')
                else:
                    break

            time_initial = time.monotonic()
            logging.info(f'\tUser input int: {fn_input}')
            print(' ') # Space :)

            fn_sequence = [0,1] # The first two numbers in the sequence, F0 = 0 and F1 = 1
            n = 0 # n is 0 because as it enters the loop it will become n = 1 and so on...
            try:
                while n != fn_input: # limit as n -> infinity of [(Fn+1)/(Fn)] = PHI , for n >= 1
                    Fn = fn_sequence[-2] + fn_sequence[-1] 
                    n += 1 
                    fn_sequence.append(Fn) # THIS SINGLE LINE HERE HAS TO BE IN THIS SPECIFIC POSITION. OTHERWISE EVERYTHING BREAKS. (Div by zero error)
                    phi = fn_sequence[-1] / fn_sequence[-2] # Divides the last index by the second to last index to create phi as the sequence is being created.
                    print(f'F{n+1} / F{n}  =  {fn_sequence[-1]} / {fn_sequence[-2]}  =  {phi}...') # [(Fn+1)/(Fn)] = PHI
                    
                    # The logging is to see if the math checks out. If it does not check out then theres something wrong with how the variables are set or how the code is ordered.
                    logging.info(f'  |  n = {n}  |  Fn+1 = F{n+1} = {fn_sequence[-1]}  |  Fn = F{n} = {fn_sequence[-2]}  |  F{n+1} / F{n} = {fn_sequence[-1]} / {fn_sequence[-2]} = {phi}  |  FBS up to F{n+1}: {fn_sequence}')  

                time_final = time.monotonic()
                delta_t = time_final - time_initial
                print(f'\n---Time To Generate: {delta_t:.4f} Seconds---')   
                print(f'\nAccording to the equation: [ (Fn+1)/(Fn)  = PHI , for n >= 1 ], you have divided {n} Fibonacci numbers consecutively!')
                print('Notice how as you move up the Fibonnaci Sequence and take the ratio of consecutive Fibonacci numbers, you get closer to what PHI is.')
                print('Of course, since PHI is an irrational number, the terms will go on forever.')
                break
            except OverflowError:
                with open('log.txt', 'w') as f:
                    f.write(f'--- OverflowError: User attempted to generate {fn_input} Fibonacci Numbers. Cleared log file. ---\n')
                print(f'\n--- You attempted to generate {fn_input} Fibonacci Numbers. Thats way too many numbers for the program to handle. ---\n')

        except ValueError:
            print('\nINVALID! Be sure to input an integer!')
            logging.error(f'\tUser entered an invalid literal for int() with base 10.')
   


if __name__ == '__main__': 
    """
    This is where I can test the induvidual functions seperately from the main code
    The if __name__ == '__main__' is to prevent the main code file from executing anything under this block.
    So if I run THIS SPECIFIC FILE FILE (myfunct.py) the __name__ will output as __main__
    If run this file as a module on a different file, the __name__ for this file will have a different output that is not called __main__
    """
    
    #enter_to_fns()
    n_to_fns()
    #mult_phi_to_fns()
    #div_fns_to_phi()
    #clear_log_file()