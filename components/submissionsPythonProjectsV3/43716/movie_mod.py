#movie_mod.py this file has the main code and will be the imported module to the main python file (#main moule)

import time #Module that allows me to use the time.slee(1) function.
#1
def add_mov(titles, movie_file):          #This defined function works by prompting the user to add a movie input
    add_mov = input("\nPlease enter the movie you want to add to your list: ").capitalize()
    titles.append(add_mov)                #adds the user's input to the "titles" list.
    with open('movies.txt', 'a') as movie_file:#opens and closes the 'movies.txt' file
        movie_file.write('\n' + add_mov)  #creates a newline everytime a movie is added. This is used to link/group the user's input string.
    print("\n...adding your movie to your list...")
    time.sleep(1)                         # time.sleep(1) delays the specified part of the program by one second so that each section takes one second to show.
    print('      .......')
    time.sleep(1)
    print('        ...')
    time.sleep(1)
    print('         . \n')
    time.sleep(1)
    print(f'Congrats! {add_mov} has been added to your list!\n')
#2
def mark_watched(titles, watched_movies, movie_file):               #This defined function prompts the user to mark a movie as watched. watched_movies = file that records the movies that were already watched.
    seen_movie = input("\nPlease enter the movie you have already watched: ").capitalize()
    with open("watched_movies.txt", "a") as movie_file:             #opens and closes a file but 'a' appends (adds the movie the user inputted).
        movie_file.write(seen_movie + "\n")                         #writes to the file, "watched_movies.txt", the user's input
    if seen_movie in titles:                                        #checks if the user input is in the "titles" list on the main movie program module.
        print(f'\nYou have marked {seen_movie} as watched.\n')      #The "if-else" conditional statement will print is the user's input is in the list, if it is not, then the "else" print statement will execute.
    else:
        print(f'\n{seen_movie} has not been added to the list or watched yet')
        print(f'\nPlease add {seen_movie} to your list.')
#3
def rate_movie(titles):                                            #This defined function prompts the user to rate a movie/ their input by checking if their input is already in the 'titles' list. 
    rate = input("\nEnter the movie you would like to rate: ").capitalize() 
    if rate in titles:                                             #If the user's input is in the list, the user will be allowed to rate their input from a scale of 1-10.
        print(f"\nYou have chosen to rate {rate}")
        user_rate = float(input("\nChoose a rating from 1-10: "))
        if 1 <= user_rate <= 3.5:
            print(f'\nOuch! thats a low rating for {rate}. Consider writing a review?')
        elif 3.6 <= user_rate <= 6.5:
            print(f'\nA {user_rate:.1f} star rating for {rate}!')
        elif 6.6 <= user_rate <= 9.5:    
            print(f'\nNot bad! A {user_rate:.1f} star for {rate}!')
        elif 9.6 <= user_rate <= 10:
            print(f'\nWOW a {user_rate:.1f} is fantastic for {rate}! You should consider writing a review.')  
    else:
        if rate not in titles:
            print(f'\nERROR!! {rate} has not yet been added to your list! Please add it before rating it!')
        
            
#4   
def write_rev(titles, movie_reviews):                              #This defined function prompts the user to review their movie/ input by first checking if their input is in the "titles" list. 
    review_inp = input("\nWhat movie would you like to review? ").capitalize()
    if review_inp in titles:                                       #If the user's input exists, the user will be prompted to write their review. The review will be stored in the "movie_reviews.txt" dictionary and file. 
        print(f"\nYou have chosen to review: {review_inp}")
        write_review = input(f"\nYour review for {review_inp} goes here:\n")
        movie_reviews[review_inp] = write_review
        with open('movie_reviews.txt' , 'w') as rev_file:
            rev_file.write(write_review)                          #writes to the file the user's review and stores it until called to be seen in option 5.
            if write_review != "N/A" and write_review != "n/a":   # if the user writes 'n/a' or 'N/A', the program will display an error message.
                print("\nThank you for the review! Please review a movie again soon!\n ")
            else:
                print(f"\n{write_review} is NOT a review! Please write a better review.\n")
    else:
        if review_inp not in titles:                             #If the user's input is not in the titles list, an error message will display.
            print(f"\n{review_inp} is not in your movie list! Please make sure to add it first!\n")


 


    
