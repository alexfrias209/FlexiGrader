"""
    This project aims to create a full on Fibonacci Sequence through a few methods.

    Check Project Changes.txt to see the changes and updates that the code went through over time. 
"""

import os
import logging # go into the mymodules folder, then go into myfunct.py, and then import every single function onto here
from second import * 
logging.basicConfig(filename='log.txt', filemode='a', level=logging.INFO) # opens log.txt in mode'a' with logging level 'info'
cwd = os.getcwd()
logging.info(' --- ')
logging.info(f'\tUser opened program in: {cwd}') # Get the path to the current working directory 


# Menu options
menue_options = {
    1: 'How the Fibonacci Sequence Works',
    2: 'The Golden Ratio and its Relationship to the Fibonnaci Sequence',
    3: 'Generation Methods',
    4: 'CLEAR LOG FILE',
    5: 'See Project Changes'
}
menue_options_2 = {
    1: 'Generate sequence by pressing ENTER',
    2: 'Generate sequecnce by input up to "Fn" Fibonacci numbers.',
    3: 'Multiplying PHI to generate a Fiboacci Sequence',
    4: 'Dividing numbers in the Fibonnaci Sequence to create the Golden Ratio'
}


def how_fsb_works():  # This function simply explains how the Fibonnaci Sequence Works.
    HFSWTXT_file_path = os.path.join(cwd, 'How The Fibonacci Sequence Works.txt') # join the cwd path with the path to the .txt file
    logging.info(f'\tHFSWTXT_file_path: {HFSWTXT_file_path}')
    try:
        with open(HFSWTXT_file_path) as HFSWTXT:
            print(HFSWTXT.read())
    except FileNotFoundError:
        print('File not found: How The Fibonacci Sequence Works.txt')
        logging.error('File not found: How The Fibonacci Sequence Works.txt')

def what_is_phi():  # This one for Phi
    WTGRP_file_path = os.path.join(cwd, 'What Is The Golden Ratio Phi.txt') # join the cwd path with the path to the .txt file
    logging.info(f'\tWTGRP_file_path: {WTGRP_file_path}')
    try:
        with open(WTGRP_file_path) as WTGRP:
            print(WTGRP.read())
    except FileNotFoundError:
        print('File not found: What Is The Golden Ratio Phi.txt')
        logging.error('File not found: What Is The Golden Ratio Phi.txt')

def project_changes():
    PJC_file_path = os.path.join(cwd, 'Project Changes.txt')
    logging.info(f'\tPJC_file_path: {PJC_file_path}')
    try:
        with open(PJC_file_path) as PJC:
            print(PJC.read())
    except FileNotFoundError:
        print('File not found: Project Changes.txt')
        logging.error('File not found: What Is The Golden Ratio Phi.txt')


def present_menue_options():  # First menu option
    while True:  # Loops until user inputs an integer
        print('\nPlease Select an option...')

        for key, value in menue_options.items():
            print(f'\t{key} : {value}')  # Prints the dictionary

        try:  # accounds for when user accidentaly inputs anything other than an integer
            options_output = int(input(' > '))
            if options_output in menue_options:
                # Gets the value accosiated with key.
                choice = menue_options[options_output]
                print('\nYou have selected:', choice, '\n')

                logging.info(f'\tUser chose {options_output} => {choice}')

                return options_output
            else:
                print('\nINVALID! Be sure to input the number associated with your option!')

        except ValueError:
            print('\nINVALID! Be sure to input the number associated with your option!')
            logging.error(f'\tUser entered an invalid literal for int() with base 10.')


def present_menue_options_2():  # Function to output the menue_options_2 dictionary to user as a menue. If anything this function works exactly like present_menue_options()
    while True:  # Loops until user inputs an integer
        print("\nPlease select an option...")

        for key, value in menue_options_2.items():
            print(f'\t{key} : {value}')

        try:  # accounds for when user accidentaly inputs anything other than an integer
            options_output_2 = int(input(' > '))
            if options_output_2 in menue_options_2:
                choice = menue_options_2[options_output_2]
                print('\nYou have selected:', choice, '\n')

                logging.info(f'\tUser chose {options_output_2} => {choice}')

                return options_output_2
            else:
                print('\nINVALID! Be sure to input the number associated with your option! \n')

        except ValueError:
            print('\nINVALID! Be sure to input the number associated with your option!')
            logging.error(f'\tUser entered an invalid literal for int() with base 10.')


# User welcome
user_name = input('Hello user! What is your name?\n > ')
print(f'\nHello {user_name}!')
print('This project here is a Fibonnaci Sequence Generator. You will be presented with a few options; please select the option you desire by inputing the number associated with it.')
print('I suggest that you first chose Option 1 to understand how the Fibonacci Sequence works.')
print('If you want, you can also chose Option 2 to see how the Golden Ratio is related the sequence.')
print('!! Quick Note: Try not to generate too large of numbers !!')
logging.info(f'\tuser_name = {user_name}')


#
# THIS HERE IS THE MAIN CODE; THE I/O FUNCTIONALLITY
#
def main_io(): # This being an ENTIRE function will make sense when you scroll down to the last lines of code...
    options_output = present_menue_options()  # Presents menue_options dict.
    if options_output == 1:  # Choice 1: See what the heck the FB Sequence is about.
        how_fsb_works()

        while True:  # After user looks over how_fsb_works(), they are presented with two choices, either to look at what the GR is about or continue to see the Generation Methods.
            print('\nChose one...\n\t1 : The Golden Ratio and its Relationship to the Fibonnaci Sequence\n\t2 : Go to Generation Methods')

            try:  # Try block "checks" if the user_input is in fact an integer
                user_input = int(input(' > '))
                if user_input == 1:  # First Choice: See what the heck Phi is about.
                    logging.info(f'\tUser chose {user_input} => what_is_phi()')
                    what_is_phi()
                    # After user looks over what_is_phi(), they press ENTER to continue to see Generation Methods.
                    
                    # Presents user_opetions2 dict.
                    options_output_2 = present_menue_options_2()

                    while True:
                        if options_output_2 == 1:
                            enter_to_fns()
                            break
                        elif options_output_2 == 2:
                            n_to_fns()
                            break
                        elif options_output_2 == 3:
                            mult_phi_to_fns()
                            break
                        elif options_output_2 == 4:
                            div_fns_to_phi()
                            break
                        else:
                            logging.info(f'\tUser entered an invalid input.')
                            print('\nINVALID! Be sure to input the number associated with your option! \n')
                    break

                elif user_input == 2:  # Second Choice: Get presented by Generation Methods.
                    logging.info(f'\tUser chose {user_input} => present_menue_options_2()')
                    # Outputs menue_options_2 dictionary
                    options_output_2 = present_menue_options_2()
                    while True:
                        if options_output_2 == 1:
                            enter_to_fns()
                            break
                        elif options_output_2 == 2:
                            n_to_fns()
                            break
                        elif options_output_2 == 3:
                            mult_phi_to_fns()
                            break
                        elif options_output_2 == 4:
                            div_fns_to_phi()
                            break
                        else:
                            logging.info(f'\tUser entered an invalid input.')
                            print('\nINVALID! Be sure to input the number associated with your option! \n')
                    break
                else:
                    logging.info(f'\tUser entered an invalid input.')
                    print('\nINVALID! Be sure to input the number associated with your option! \n')
            # If the user inputs anything other than an integer the code goes straight to here.
            except ValueError:
                logging.error(f'\tUser entered an invalid literal for int() with base 10.')
                print('\nINVALID! Be sure to input the number associated with your option! \n')


    elif options_output == 2:  # Choice 2: See what the heck Phi is about.
        what_is_phi()

        while True:  # After user looks over what_is_phi(), they are presented with two choices, either to look at what the FB Sequence is about or continue to see the Generation Methods.
            print('\nChose one...\n\t1 : How The Fibonnaci Sequence Works\n\t2 : Go to Generation Methods')

            try:  # Try block "checks" if the user_input is in fact an integer
                user_input = int(input(' > '))
                if user_input == 1:  # First Choice: See what the heck the FB Sequence is about.
                    logging.info(f'\tUser chose {user_input} => how_fsb_works()')
                    how_fsb_works()
                    # After user looks over what_is_phi(), they press ENTER to continue to see Generation Methods.
                    
                    # Outputs menue_options_2 dict.
                    options_output_2 = present_menue_options_2()

                    while True:
                        if options_output_2 == 1:
                            enter_to_fns()
                            break
                        elif options_output_2 == 2:
                            n_to_fns()
                            break
                        elif options_output_2 == 3:
                            mult_phi_to_fns()
                            break
                        elif options_output_2 == 4:
                            div_fns_to_phi()
                            break
                        else:
                            print('\nINVALID! Be sure to input the number associated with your option! \n')
                    break

                elif user_input == 2:  # Second Choice: Get presented by Generation Methods.
                    # Outputs menue_options_2 dictionary
                    options_output_2 = present_menue_options_2()
                    while True:
                        if options_output_2 == 1:
                            enter_to_fns()
                            break
                        elif options_output_2 == 2:
                            n_to_fns()
                            break
                        elif options_output_2 == 3:
                            mult_phi_to_fns()
                            break
                        elif options_output_2 == 4:
                            div_fns_to_phi()
                            break
                        else:
                            logging.info(f'\tUser entered an invalid input.')
                            print('\nINVALID! Be sure to input the number associated with your option! \n')
                    break
                else:
                    logging.info(f'\tUser entered an invalid input.')
                    print('\nINVALID! Be sure to input the number associated with your option! \n')
            # If the user inputs anything other than an integer the code goes straight to here.
            except ValueError:
                logging.error(f'\tUser entered an invalid literal for int() with base 10.')
                print('\nINVALID! Be sure to input the number associated with your option! \n')


    elif options_output == 3:  # Go straight and present the various Generation Methods.
        # Outputs menue_options_2 dictionary
        options_output_2 = present_menue_options_2()
        while True:
            if options_output_2 == 1:
                enter_to_fns()
                break
            elif options_output_2 == 2:
                n_to_fns()
                break
            elif options_output_2 == 3:
                mult_phi_to_fns()
                break
            elif options_output_2 == 4:
                div_fns_to_phi()
                break
            else:
                logging.info(f'\tUser entered an invalid input.')
                print('\nINVALID! Be sure to input the number associated with your option!\n')
                
    elif options_output == 4:
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('\tIf you chose this option, then you were either just curious on what it does-')
        print("\tor you generated so many Fibonacci Numbers, that the size of the Log File grew to the freaking Gigabytes, and it's too big to open. ")
        print('\n\tYes this being an option also implies I did try such thing (I tried to generate 15,000 numbers and the Log File grew to 25GB)')
        print('\n\tAnyways, the file has been cleared...')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        clear_log_file()

    elif options_output == 5:
        project_changes()

# This allows the user to ether chose between ending the program or chosing another option after doing their inital one.
# (Better than having to open the program again just to chose another option.)
loop_var = 1
while loop_var == 1:
    main_io() # See it looks less of a mess when the main IO is an entire function :)
    while True:
        print('\nWould you like to try a different option?\n\t1 : Try different option\n\t2 : Exit program')
        try:
            user_input = int(input(' > '))
            if user_input == 1:
                loop_var = 1
                logging.info('\tUser is going to chose a different option...')
                break
            else:
                loop_var = 0
                logging.info(f'\tUser exited the program.')
                break
        except ValueError:
            logging.error(f'\tUser entered an invalid literal for int() with base 10.')
            print('\nINVALID! Be sure to input the number associated with your option! \n')
