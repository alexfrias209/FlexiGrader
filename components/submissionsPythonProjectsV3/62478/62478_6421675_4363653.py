file_name = 'Winstreak.txt'

Characters = ["Shrek", "Buzz Lightyear", "Spongebob", "Courage the Cowardly Dog", "Scooby-Doo"]
def options():
    print('1. Yes\n2. No\n3. Probably\n4. IDK\nPlease choose a selection(1/2/3/4)')
#so i dont have to keep on typing same thing, may add some pointers on capitalization
#added pointers in the welcome line
def nonumber():
    print('You are clearly not taking this seriously. How is that even possible with the given characters?')
    #the Probably and IDK options are just a formality with the given characters, so anything that isn't a yes or no will default to this. is vague enough to cover a response such as "who cares" with the first sentence
try:
    with open(file_name, 'r') as file:
        wincount = int(file.read())
except FileNotFoundError:
     wincount = 0
#reads to  a wincount file, but does not write. was broken trying to write, so erased that feature

print('Would you like to play Pythonator, the python based akinator?(Yes or No) ')
#make sure it can skip the function like it should
choice = input()

while choice =='Yes':
    print('Welcome to Pythonator!\nDeveloped by Zacharia Khan\nPlease choose a character from the given list!\nYou should know, any response besides what is asked will result in the game ending.\nCapitalization Matters!\n')
    #example text like how pandey had it. now with pointers.

    # printing the list using loop and can iterate over any length.
    for C in range(len(Characters)):
        print(Characters[C])
    

#note that there is no longer a win() function. This is because upon further thinking, creating a win function would have taken up two more lines of code rather
#than just putting the work the function would do after each win.
#the first of many if statements to deduce the character.

    print('\nEnter Done when you have chosen.')
    Answer = input()
    if Answer == 'Done':
        print('Great! Now, does your character speak coherent english?')
        options()
        Choose = input()
    else:
        print('please restart the program.')
        break
    if Choose =='1':
        print('I see, that narrows it down a tad')
        print('Well, does your character breathe air?')
        options()
        Choose2 = input()
        if Choose2 =='2':
            print('Must be Spongebob. Do not feel bad, I am the best both above and under the sea!')
            wincount +=1
        elif Choose2 == '1':
            print('Does your character have organs?')
            options()
            Choose3 = input()
            if Choose3 == '1':
                print('Shrek. Please, try harder and be more original.')
                wincount += 1
            elif Choose3 =='2':
                print('Buzz Lightyear! My powers also reach to infinity and beyond, clearly.')
                wincount += 1
            else:
                nonumber()
                
        else:
            nonumber()
            
    elif Choose == '2':
        print('Almost there! Well is your character oddly colored?')
        options()
        finalchoice = input()
        if finalchoice == '1':
            print('Well, I guess your character must be Courage! My genius, it can be sometimes frightening.')
            wincount += 1
        elif finalchoice =='2':
            print('It must be Scooby-Doo! This should clearly prove that I am the GREATEST detective in the world!') 
            wincount +=1
    else:
        nonumber()
        
    Question = input('Would you like to see the total wins I have?(Yes or No) ')
    if Question =='Yes' and wincount < 10:
        print('I have a total of', wincount, 'wins.')
    elif Question == 'Yes' and wincount >= 10:
        print('I am proud I have', wincount,'wins yet disappointed it is so low. You must have given up upon realizing my greatness.')
    choice = input('Would you like to go again?(Yes or No) ')
    #completes the while loop at the very top, so that the wincount can be stored
else:
    print('Well, what are you doing here?')


