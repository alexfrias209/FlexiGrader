print("Hello, My name is XXXXX XXXXXX and my project is about visualizing Pokemon, this project is a dynamic and engaging visual quiz application designed to challenge users' perception and attention to detail. The core idea behind this project is to present users with a series of image-based quizzes, where they must identify the correct Pokemon.")
name = input("What is your name? \n")
age = input("What is your age? \n")
frequency = input("How often do you use visual quiz apps or games on a scale of 1 to 5? \n")
familiar = int(input("On a scale of 1 to 5 how familiar are you with 'Pokemon' Characters? \n"))
print(name, "is",age," years old and has a Pokemon knowledge of",familiar)
if familiar== 1:
    print("which means he or she is not familiar with Pokemon")
elif familiar== 2:
    familiar = print("which means he or she does not know much about Pokemon")
elif familiar== 3:
    familiar =print("which means his or her knowledge is neutral on Pokemon")
elif familiar==4:
    familiar= print("wich means he or she is familiar with Pokemon")
elif familiar==5:
    familiar= print("which means he or she is very familiar with Pokemon")
else:
    print("Please enter a valid number")#Part of the milestone
#Allows you tu utilize your web browser
import webbrowser
#Indicates that this code will use random variables or numbers
import random

#Reads data from txt file
def load_pdata(filename):
    with open(filename, "r") as file:
        data=[] 
        for line in file:
            parts= line.strip().split(',')#Splits name and Url of pokemon into lines
            if len(parts)==2:
                name, image_url = parts
                data.append({"name": name, "image_url": image_url})
        return data
#Displays image on user's default browser
def display_image(image_url):
    webbrowser.open(image_url)
#Main game
def main():
    pdata = load_pdata("55989_6421744_3129037.txt")

    score=0
    random.shuffle(pdata)#Shuffles data from the text file

    for pokemon in pdata: 
        display_image(pokemon["image_url"]) #Displays the shuffled data
        userguess = input("What Pokemon is this? ").strip()

        if userguess.lower() == pokemon["name"].lower():
            print("Correct!\n")
            score += 1#If the user answers correctly they get 1 point, if they answer incorrectly they get no points
        else:
            print(f"Incorrect Answer! It's {pokemon['name']}.\n")

    print(f"Game Over!Your total score is {score} out of {len(pdata)}. Thank you for playing!")

if __name__ == "__main__":
    main()
    
