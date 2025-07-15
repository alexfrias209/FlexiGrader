#main module

import movie_mod      #This is my own module that imports the main movie code 1-4.
import time                   #Delays the intended function by 1 second. I was a fun idea I wanted to try.

def print_welcome_statement():#This defined function helps to keep the welcome statement in a neater format. The function is then called at the end.
    print("\nWelcome to the Movie Watchlist!\n")
    name = input("Please enter your name: ").capitalize()#The user is prompted for their name so that the program can display the welome statements.
    print(f"\nHello {name}!, my name is blah and I am the 'Movie Watchlist' developer!")
    print(f'The purpose of my project is to allow you, {name}, to create a list of movies you want to watch.')
    print(f'You can also mark movies as watched, and rate or review them.')
print_welcome_statement()                                                #This is where the defined function is called/ displayed when the porgram is ran. 

def main_menu():                                                         #This defined function will display the main menu for the user.
    print("\n**********Main Menu***********")
    print("\nPlease progress through steps 1-4 for one movie at a time.")#This is advised so that the user has the full experience of this movie program.
    print("\n1. Add a movie to watchlist ")
    print("2. Mark a movie as watched ")
    print("3. Rate a movie ")
    print("4. Review a movie ")
    print("5. Display your review ")
    print("6. Exit menu\n ")                                             #The user has two options to exit the game. This is the first option. The second option is at the end of the while loop.

def movie_watchlist():                           #This function is the main program. At the end there is an if statement that helps make this entire part of the code work.
    with open("43716_6419438_8500827.txt", "a") as movie_file:  #This line defines the variable, "movie_file". The program won't work without this function.I tried getting rid of it on both .py modules at a time but on the "movie_mod.py" module, the user's input was not showing on the 'movies.txt' file. I kepts getting errors after I tired to modify it but ultimately, this current way worked successfully.
                                                 #Opens and closes "movies.txt" file on this main program to add the user's input to the required dictionary/list.
        titles = []                              #Main empty list of movies that will store the user's input in 'movies.txt' file.
        rated_movs = {}                          #Dictionary that stores the rated movies after the user has rated their chosen input.
        movie_reviews = {}                       #Dictionary that stores the user's reviews (in movie_reviews.txt file).
        watched_movies = []                      #List that stores the user's watched movies (in watched_movies.txt file).
    while True:                                  #This loop will cause the main movie program to keep looping until the user either enters option 6 or "n".
        main_menu()                              #Calls the defined "main_menu" and displays the movie program's menu.
        prompt = input("\nPlease enter a menu option (1-6): ")
        if prompt == "1":
            movie_mod.add_mov(titles, movie_file)#add_mov = the defined function in 'movie_mod.py' that allows the user to input/ add movies to the 'titles' dictionary. The variable 'movie_file' is the file object that allows the "movies.txt"file to be opened and appended.
        elif prompt == "2":
            movie_mod.mark_watched(titles, movie_file, watched_movies)# mark_watched = defined function that promps the user to mark a movie as watched. The program checks if user's movie is "titles" list and adds it to the "watched_movies" dictionary and stored in 'wacthed_movies.txt'file.  
        elif prompt == "3":                      #watched_movies = records the movie as watched and is stored in the watched_movies.txt file.
            movie_mod.rate_movie(titles)         #rate_movie = defined function that prompts the user in "movie_mod" to rate a movie.
        elif prompt == "4":
            movie_mod.write_rev(titles, movie_reviews)#write_rev = defined function that prompts the user to write a review for their input. if the user's input is in the "titles" list, the user can write the review and the review will be added to the 'movie_reviews.txt' file.
        elif prompt == "5":#This option allows the user to see their review by checking if the user's input is in the dictionary, "movie_reviews". If it is, the review will display, if not,an error message will show.
            review = input("\nwhich movie's review would you like to see? ").capitalize() 
            if review in movie_reviews:
                print('\n....Review.....')
                time.sleep(1)
                print('     ...       ')
                time.sleep(1)
                print('....loading....')
                time.sleep(1)
                print(f"\nYour review for {review}:\n")
                show_rev = print(movie_reviews[review]) #displays the user's review for the movie they want to see. This is also stored in the movies_review.txt file.
            else:
                print(f"\nError! {review} does not exist! Please write a review before seeing it\n")
                    
        elif prompt == "6": #Exit option
                 print("\nMovie list program closing...")      #Fun feature I wanted to add to simulate the movie program closing.
                 time.sleep(1)
                 print('      .......')
                 time.sleep(1)
                 print('        ...')
                 time.sleep(1)
                 print('         . \n')
                 time.sleep(1)
                 print("Thank you for participating! Goodbye!")
                 break                                         #Breaks the program if this option is chosen
        else:
            print("\nError! Please choose number in range: ")
            continue                                           #If the user inputs something out of range, the system allows the user to reloop and display the menu again.
        

        
        cont_inue = input("\nDo you wish to continue? (y/n): ")#Asks if the user wants to continue. This is the other option of exiting the program and will continue to loop until tje user either enter option 6 or 'n'.
        if cont_inue.lower() == 'y':
            continue                                           #when the user chooses 'y', the program will display the main menu.
   
        elif cont_inue != "n" and cont_inue != "y":
            print("\nError! Please choose a new menu option: ")
            continue                                          #If user inputs something else, the program will display the main menu and promt the user to choose a new option.
        else:
            cont_inue.lower() == 'n'
            print("\nGoodbye! Consider coming back!")
            break



                
if __name__ == "__main__":             #Makes sure the main movie program works as intended. Seen similar formats from code guides
    movie_watchlist()                  #source: https://realpython.com/if-name-main-python/
                                       #source: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
