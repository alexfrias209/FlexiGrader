#ME 021 Python Project
print('          Welcome to my Simple Encryption Algorithm')
print()
print('The objective of this program is to encrypt and decrypt text using simple encryption algorithms like Caesar or Vigenère ciphers')
print()
print()
print('To quit the program write "q" or "quit"')
print()

number= 0
while number >= 0:
    number= input('\nPlease enter the shift number (The number must be between 1 and 25): ')
    if (number == 'q') or (number== 'quit'):   #Check if the user wants to quit the program
        break                                  #Break the program by skiping the rest of the code inside the while loop
    number= int(number)                        #Converts the user string input to an integer used as shift number
    while (25 < number) or (number < 1):       #Check if the user number input is between the range, it is a loop until the given value is valid (between the range)
        print('\nThe given number is not valid, please enter a valid number.')  #If the value is not between the range then it prints and statement asking for a valid number
        number=input('\nPlease enter the shift number (The number must be between 1 and 25):') #Gives the user opportunity to enter a new number between the range
        number= int(number)                    #Converts the given string into a integer

    func= input('\nDo you want to encrypt or dencrypt? (enc or den) ')         #Ask user if wants to encrypt or dencrypt. It is used to determine which function will be used.
    while (func != 'enc') and (func != 'den'):                               #Checks if the user given input is valid, it is a loop until the given input is valid (enc or den)
        print('\nThe given option is not valid, please enter a valid option.')  #Let the user know that the given input value is not valid and ask for a valid input
        func= input('\nDo you want to encrypt or dencrypt? (enc or den) ')     #Gives the user opportunity to enter a new valid input
    
    original= input('\nEnter the text you want to encrypt or dencrypt: ')       #Ask the user for the text to encrypt or dencrypt
    option= input('\nWant to see the original text after encrypt or dencrypt? (yes or no) ') #Ask the user if wants to see the original text input

    firstLetter= ord('A')   #Is the number for the first alphabet capital letter in ASCII
    lastLetter= ord('Z')    #Is the number for the last alphabet capital letter in the ASCII
    letterRange= 26         #Number of letters in alphabet


    def encrypt_message(original, number):   #Function for encrypt
        encrypt= ''                          #Placeholder for message
        if 0 < number < 26: 
            for letter in original.upper():  #Reading letter by letter the text given by the user
                if letter.isalpha():         #Only change the code number of letters, no special characters
                    letter_num= ord(letter)      #Analize the code number of each letter using ASCII code
                    new_num= letter_num + number #Creates the new code number for each letter adding the given shift number

                    if new_num >lastLetter:     #If the new code number is out of the letters section then it start again giving us a code number inside the alphabet
                        new_num -=letterRange   

                    if new_num < firstLetter:
                        new_num += letterRange

                    new_letter= chr(new_num)     #Convert from code number to letter 
                    encrypt+= new_letter         #Stores the new letters in the encrypt placeholder

                else:
                    encrypt+= letter             #Add especial characters to the encrypt message as spaces and symbols
        return encrypt

    def decrypt_message(original, number):   #Function for decrypt 
        decrypt= ''                          #Placeholder for message
        if 0 < number < 26:
            for letter in original.upper():  #Reading letter by letter the text given by the user
                if letter.isalpha():         #Only change the code number of letters, no special characters
                    letter_num= ord(letter)      #Analize the code number of each letter using ASCII code
                    new_num= letter_num - number #Creates the new code number for each letter substracting the given shift number

                    if new_num > lastLetter:     #if the new number is out of the letters section then it start again giving us a code number inside the alphabet
                        new_num -= letterRange   

                    if new_num < firstLetter:
                        new_num += letterRange

                    
                    new_letter= chr(new_num)     #Convert from code number to letter 
                    decrypt+= new_letter         #Stores the new letters in the dencrypt placeholder
                else:
                    decrypt+= letter             #Add the special characters to the decrypt place holder
        return decrypt

    if func == 'enc' or func == 'encrypt':      #If statement to use and print the encrypt function
        print('\nEncryption number:', number)   #Print the shift number
        enc = encrypt_message(original, number) #Call the encrypt function
        print('Encrypted message:', enc)        #Print the encrypt message

    elif func == 'den' or func == 'decrypt':    #If statement to use and print the decrypt function
        print('\nDecryption number:', number)   #Print the shift number
        dec = decrypt_message(original, number) #Call the decrypt function
        print('Decrypted message:', dec)        #Print the decrypt message

    if option == 'yes' or option =='y':         #Check if user wants to see original message
        print('Original message:', original)    #If true prints original message

print('\nThank you for trying my program!')       #Prints a sentence that thanks the user after enter q or quit value to end the loop


    
