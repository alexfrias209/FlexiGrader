print('\nHi! Welcome to the Game Theory Python Project!!')
print("This project will focus on the Prisoner's Dilemma Scenario")
print()

#reference: https://www.investopedia.com/terms/p/prisoners-dilemma.asp#:~:text=The%20prisoner's%20dilemma%20presents%20a,parties%20choose%20to%20co%2Doperate.
import random                                                   #imports the random module 

#defining global variables
num_betray = int()                                              #variable for number of betrayals
num_cooperate = int()                                           #variable for the number of cooperations
num_prison = int()                                              #variable for the number of time sent to prison
prison_alone = int()                                            #variable for the number of times Ayush was sent to prison alone
revenge = int()                                                 #variable for the number of times Ayush chooses revenge during his sentence 
escape = int()                                                  #variable for the number of times Ayush chooses to escape during his sentence
num_revenge = int()                                             #variable for the number of times Ayush commits to revenge
num_escape = int()                                              #variable for the number of times Ayush has escaped from prison
num_peace = int()                                               #creates a variable for number of times user wants peace

#asks the user how many times they would like the game to loop
loops = int(input("How many times would you like to play this game? (Please choose a whole number) "))
if loops <= 0:
    print("Please enter a valid number")
    exit()

def percentage(value):                                          #functions that calculates the percentages of user's choices / times sent to prison          
    value_percent = round(float((value / loops) * 100), 2)
    return value_percent

def alone_percentage(alone_choice):                             #functions that calculate the percentage of the choices when sent to prison alone
    if prison_alone > 0:                                        #percentages can't be calculated if denominator = 0
        alone_percent = round(float((alone_choice / prison_alone) * 100), 2)
        return alone_percent
    else:
        alone_percent == 0
        return alone_percent

#explains the general scenario for Prisoner's Dilemma
print('\nThere are 2 robbers, Ayush and Pandey, who have been arrested for robbing a bank.')
print("There were no witnesses to the robbery, so the police can only rely on the robbers' confessions")
print('As such, the robbers have been sepearated from each other, so neither will know what the other will say (or confess).')

for x in range(0, loops):                                       #game will loop as many times as the user would like
    #defining local variables for amount of years sent to prison (resets with each loop)
    ayush_sentence = int()
    pandey_sentence = int()

    #user will choose an action for Ayush
    print('\nYou are playing as Ayush. Choose an action: ')
    print('A - Betray Pandey - Say that Pandey robbed the bank')
    print("B - Cooperate - confess Ayush's crime")
    user_choice1 = input()

    pandey_choice = ['A', 'B']                                  
    pandey_choice = random.choice(pandey_choice)                #randomly chooses an action for Pandey
    
    if user_choice1.upper() =='A':                              #if user chooses to betray Pandey
        print("Ayush has betrayed Pandey!")
        num_betray += 1
        if pandey_choice == 'A':                                #if Pandey betrays Ayush
            print("Pandey has chosen to betray Ayush!")
            ayush_sentence += 3                                 #Ayush is sentenced to 3 years of prison
            pandey_sentence += 3                                #Pandey is sentenced to 3 years of prison
            num_prison += 1
        
        elif pandey_choice == 'B':                              #if Pandey cooperates
            print("Pandey confessed and said that he robbed the bank!")
            pandey_sentence += 5                                #Pandey is sentenced to 5 years of prison
    
    elif user_choice1.upper() == 'B':                           #user chose to cooperate with the authorities
        print("Ayush has confessed to his crime!")
        num_cooperate += 1
        num_prison += 1
        
        if pandey_choice == 'A':                                #if Pandey betrays Ayush
            print("Pandey has chosen to betray you!")
            prison_alone += 1
            ayush_sentence += 5                                 #Ayush is senteneced to 5 years of prison
        
        elif pandey_choice == 'B':                              #if Pandey cooperates
            print("Pandey confessed and said that he robbed the bank!")
            ayush_sentence += 1                                 #Ayush is sentenced to 1 year of prison
            pandey_sentence += 1                                #Pandey is sentenced to 1 year of prison
    
    else:                                                       #if user enters an invalid input
        print()
        print("What you chose isn't an available option, please play again")
        break
    
    if ayush_sentence == 0 and pandey_sentence != 0:            #printed if only Pandey was sent to prison
        print("Pandey was sent to prison!")
        print(f'Pandey was sentenced to {pandey_sentence} years in prison.')
    
    elif ayush_sentence != 0:                                   #printed if Ayush is sentenced to prison
        if pandey_sentence != 0:                                #printed if Pandey is sent to prison too
            print('Ayush and Pandey are both brought to prison for their crimes.')
            print(f'Ayush is sentenced to {ayush_sentence} years in prison.')
            print(f'Pandey is sentenced to {pandey_sentence} years in prison.')
        
        elif pandey_sentence == 0:                              #game will continue only if Ayush wsa sent to prison alone
            print('Pandey is set free.')
            print('Ayush has been sent to prison!')
            print(f'Ayush is sentenced to {ayush_sentence} years in prison.')
            print("Ayush, in prison, notices that Pandey wasn't sentenced as well")
            print("Knowing that he was betrayed, Ayush could only wait until his sentence was up... or would he?\n")
            
            for i in range(0, ayush_sentence):                  #user will choose the an action for each year of Ayush's sentence  
                print(f"Choose an action for year {i} of the sentence: ")
                print("(To escape or to seek revenge, it must be chosen twice. So choose carefully)")
                print("A - Plan for revenge")
                print("B - Plan to escape")
                print('C - Peacefully wait for sentence to end')
                sentence_choice = input()

                if sentence_choice.upper() == 'A':              #plan for revenge
                    revenge += 1
                    if revenge % 2 == 0:                        #if revenge is chosen 2 times, Ayush will seek revenge on Pandey
                        print("Ayush decided to seek out Pandey for revenge after his sentence!")
                        num_revenge += 1  
                        break
                
                elif sentence_choice.upper() == 'B':            #plan for escape
                    escape += 1
                    if escape % 2 == 0:                         #if escape is chosen 2 times, Ayush will break out of prison
                        print("Ayush broke out of prison!")
                        num_escape += 1
                        break
                
                elif sentence_choice.upper() == 'C':            #if user choose the 'peaceful' ending
                    print("Ayush decided that he no longer wanted to be a criminal and turned over a new leaf!")
                    num_peace += 1
                    break

print("\nUser statistics:")                                     #gives the user the statistics / percentages of their choices
print(f"Betrayed Pandey: {percentage(num_betray)}%")
print(f"Cooperated with the police: {percentage(num_cooperate)}%")
print(f"Sent to prison: {percentage(num_prison)}%")
if prison_alone > 0:
    print("\nStatistics if only Ayush was sent to prison:")
    print(f"Escaped prison: {alone_percentage(num_escape)}%")
    print(f"Planned for revenge: {alone_percentage(num_revenge)}%")
    print(f"Choose the peaceful ending: {alone_percentage(num_peace)}%")
print("\nThanks for playing!!\n")
