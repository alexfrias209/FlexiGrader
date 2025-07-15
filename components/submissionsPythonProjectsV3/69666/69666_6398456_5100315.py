while True:
#allows for infinite loops provided that there are no breaks
    print("\nWelcome to the Palindrome Checker!")
    print("Verify if your word(s) are Palindromes")
    
    print("\nPlease select from the options below:")
    print("1. What is a palindrome?")
    print("2. Palindrome checker")
    print("3. Exit")
#options 
    choice = input("Your selection (1/2/3): ")
    
    if choice == "1":
        print("\nA Palindrome is a word, phrase, or sequence that reads the same backward as forward.")
        print("For example, the word 'MOM' is a palindrome because it remains the same when read backward.")
        
        question = input("Would you like more examples? (Yes/No): ")
        if question.lower() == "yes":
#accounts for minor errors/ease of use; turns user input to lowercase
            print("Other palindromes include 'DAD,' '202,' 'MADAM,' and '177771.'\n")
        elif question.lower() == "no":
#accounts for minor errors/ease of use; turns user input to lowercase
            print("\n")
    
    elif choice == "2":
        print("\nPlease select the function of the palindrome checker:")
        print("1. Verify palindromes within a CSV file")
        print("2. Exit")
#sub_options        
        sub_choice = input("Enter your choice (1/2): ")
#sub-category of questions within the loop
        if sub_choice == "1":
            import csv
            def palindrome_checker(word): 
                word = word.lower()
                return word == word[::-1]
#Palindrome_checker becomes a function that reads values backwards as the "-1" suggests

            csv_file_path = "69666_6398457_3728313.csv"
#Uploaded csv file in use for this; the r lets python interpret it location or read the file 

            palindromes = []                                        #the empty palindrome container
            with open(csv_file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    for word in row:
                        if palindrome_checker(word):
                            palindromes.append(word)
#Each for statement breaks the given file down until it reaches a singular value... the word
#Then will be plugged into the function to where values deemed as palindromes will be added to the empty palindrome container 

            if palindromes:
                print("\nPalindromes found in the CSV file:")
                for word in palindromes:
                    print(word)
#Values deemed palindromes will then go into the palindrome container where the print statement will show
            else:
                print("\nNo palindromes found in the CSV file.")
#will show if the file doesn't contain any palindromes                
        elif sub_choice == "2":
            break
        else:
            print("Invalid input. Please enter 1 or 2.")
#accounts for errors by directing the user with correct instructions
    elif choice == "3":
#exits the main script
        print("\nThank you for using the palindrome checker. Goodbye!")
        break
#here to end any further iterations, or stop any continuation
    else:
        print("Invalid input. Please select 1, 2, or 3.")
#accounts for any mistakes in the first stage


#contains a palindrome function "palindrome_checker"
#contains a loop using "while true:"
#contains sufficient branch statements with the use of "if/elif/else"
#uses sub-sections with the previously mentioned brach statements
#contains a csv file
#contains comments for the purpose of clarity and explanation


