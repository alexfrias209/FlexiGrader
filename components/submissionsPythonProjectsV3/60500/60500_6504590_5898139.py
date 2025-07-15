
import random


# The sturucture of this game is largely functions leading to other functions
# I made a lot of different areas that the player may well visit many times
# each one is it's own function.
# The actual start of the game is at the bottom, after all of the functions
# have been created

# establishing global variables
global has_light 
has_light = False
global health
health = 10.0
global maxhealth 
maxhealth = 10.0
global goldenBird 
goldenBird = 8.0
global attackBase 
attackBase = 2
global token_power
token_power = False
global token_wisdom
token_wisdom = False
global token_strength
token_strength = False
global tokens
tokens = 0

# Welcome's the player to my game
print("Hello welcome to adventure game")
print("While playing remember to answer in simple lowercase words, such as:")
print("left or right, up or down, yes or no")
name = input('Please enter your name')
print()


def cave1():
  print("You walk further into the woods")
  print("as you walk, you come across the cave")
  choice = input("Will you explore the cave?")
  print()
  
  if choice == 'yes':
    print("You walk into the cave, but it gets really dark")
    if has_light == True:
      c6 = input("Will you pull out your lamp?")
      if c6 == 'yes':
        print("You pull out your lamp")
        print()
        cave2()        
    else:
      print('You do not have a light, you must turn back')
      print()
      spawnPoint()
  else:
      clearing2()

def cave2():
    print("As you walk deeper into the cave you come upon a large room")
    print("'Is that rock moving?'")
    print("'Oh no! It is a rock gnome and it's attacking!'")  
    print() 
    choice = input("Will you 'fight' or 'run'?")
    if choice == 'fight':
        healthy = health + (tokens * 3)
        attack = attackBase + (tokens * 2)
        gnome = 8
        while healthy > 0 and gnome > 0:
            gnomeAttack = random.randint(0,5)
            healthy -= gnomeAttack
            gnome -= attack
            print("The gnome did", gnomeAttack, "damage, your health is now", healthy)
            print("You did", attack, "damage, the gnome health is now", gnome)
        if gnome <= 0 and healthy > 0:
            print('The gnome is knocked out, you can now continue')
            print("Your health has been restored it is now", (health + (tokens * 3)))
            print()
            cave3()
        else:
            choice = input("Would you like to try again?")
            if choice == 'yes':
                cave2()
            else:
                spawnPoint()
    else:
        spawnPoint()

def cave3():
    global token_wisdom
    global tokens
    if (token_wisdom == False):
        print("As you continue walking, it begins to feel like it is closing in on you")
        print("Then you reach a deadend and right there is a stone toad")
        print('"You have done much to get here and should be proud. However before I can grant')
        print('the token of light you must prove your knowledge.')
        choice = input('Would you like to play my game?"')
        print()
        if choice == 'yes':
            print("I will be picking a word, and you must guess it within 10 tries")
            win = hangman()
            if win != False:
                print('"Wonderful job!, You have truly proven your knowledge"')
                print('"I now present you', name, 'with the token of knowledge"')
                print()
                tokens += 1
                token_wisdom = True
                spawnPoint()
            else:
                print('"You tried hard and should be proud of yourself, please come back when you are ready"')
                spawnPoint()
        else:
            print("When you are ready please come back")
            spawnPoint()
    else:
        print("There is nothing more for you here, go adventure more")
        print()
        spawnPoint()
      
def clearing2():
    global token_power
    global tokens
    print("You come upon a large open clearing with a large magical tree")
    print("As you walk towards the tree, you see what looks like a sword stuck ")
    print("in a stone, interesting")
    choice = input("Will you try to pull the sword from the stone?")
    if choice == "yes":
        if token_strength != False:
            print("You pull the sword, and it comes out of the stone shockingly easily")
            print("You look at the sword and it is beautiful, the blade is glowing as if by magic.")
            print('Suddenly the tree starts talking to you')
            print('"You have done well to get here young one, and you have proven your worth')
            print('you are now ready to defeat the tyrant king, to help you on your way I will grant')
            print('you the token of power, good luck adventurer"')
            token_power = True
            tokens += 1
            spawnPoint()
        else:
            print("Come back when you are a little stronger")
            spawnPoint()
    else:
        print("You choose to turn back, might come back later")
        spawnPoint()
    
def thrownRoom():
    global token_strength
    global tokens
    if token_strength != False:
        print("There is nothing left to do here")
        spawnPoint()
    print("You enter a large room with a massive fancy chair in the middle")  
    print("then to your horror you see that there is a small person trapped underneath it")
    print('"Hello there traveler, I am so glad you are here, I have somehow managed to ')
    print('get myself stuck under this stone thrown, will you please help me? I will reward you."')
    pick = input("Will you help this man?")
    if (pick == "no"):
        print("Please comeback when you can help me.")
        spawnPoint()
    else:
        if (token_wisdom != True):
            print("Unfortunitly, you are not strong enough, try agin ounce you hace increases your strength")
        else:
            print('"Wow, you are so strong, Thank you for saving me"')
            print('"To reward you, I will now grant you', name, 'with the token of Strength, Congradulations!"')
            token_strength = True
            tokens += 1
            spawnPoint()

def gargoil():
    print("As you walk you come upon a room guarded by a stone gargoil")
    print('"What buisness do you have here human?" the gargoil asks')
    print('"Ah, I see, you are trying to save the kingdom from the tyrant king"')
    print('"Well in that case I shall allow you to pass, however, beware')
    print('noone has been down this hallway in years, you never know what')
    print('or who you might find in here"')
    print()
    if has_light == True:
        print("You take out your light as it is dark and walk into the hallway")
        print("As you walk along, you come acrost a little green goblin")
        print("You try to hide, but it is too late, your light has alrady ")
        print("angered him. Next thing you know he comes flying at you.")
        choice = input("Will you 'fight' or 'run'")
        print()
        print()
        if choice == 'fight':
            healthy = health + (tokens * 3)
            attack = attackBase + (tokens * 2)
            goblin = 11
            while healthy > 0 and goblin > 0:
                goblinAttack = random.randint(0,5)
                healthy -= goblinAttack
                goblin -= attack
                print("The goblin did", goblinAttack, "damage, your health is now", healthy)
                print("You did", attack, "damage, the goblin's health is now", goblin)
            if goblin <= 0 and healthy > 0:
                print('The goblin is knocked out, you can now continue')
                print("Your health has been restored it is now", (health + (tokens * 3)))
                print()
                thrownRoom()
            else:
                choice = input("Would you like to try again?")
                if choice == 'yes':
                    gargoil()
                else:
                    spawnPoint()
        else:
            spawnPoint()
    else:
        print("It is too dark, consider coming back when you have a lamp")
        spawnPoint()
    
def armory():
    print("You walk into a room ")
    
def spawnPoint():
    print()
    if (tokens == 3):
        finale()
    else:
        print()
        print("strength", token_strength, "power", token_power, "Wisdom", token_wisdom, "total", tokens)
        print("You find yourself back where you woke up, wich path would you like to take now?")      
        choice = input("left or right?")
        if choice == "left":
            clearing()
        else:
            cave1()
        
def finale():
    print("You find yourself in what looks like an arena")
    print("But then the tyrant king comes walking around the corner")
    print('"You think you can defeat me, ha, pathetic"')
    print("then, he draws his sword and steps towards you")  
    print() 
    healthy = health + (tokens * 3) + 5
    attack = attackBase + (tokens * 2) + 10
    king = 40
    while healthy > 0 and king > 0:
        kingAttack = random.randint(0,6)
        healthy -= kingAttack
        king -= attack
        print("The king did", kingAttack, "damage, your health is now", healthy)
        print("You did", attack, "damage, the king's health is now", king)
    if king <= 0 and healthy > 0:
        print("The king's is dead, you did it!")
        print("Your health has been restored it is now", (health + (tokens * 3)))
        print()
        credits()
    else:
        print("you must try again")
        finale()

def credits():
    print("Thanks for playing my game!")
    print("This game was created for ME 021 ")
    print("In 2023")
    print("Programming: Frances Cardinale")
    print("Story: Frances Cardinale")
   
def clearing():
    print("Your come upon a clearing with a large rock in the middle, the rock looks odd")
    c2 = input("Will you inspect the rock?")
    if c2 == 'yes':
        print("You lift the rock to find large tunnel underneath")
        print("You wonder if you should go through the tunnel")
        c3 = input("Will you go into the tunnel?")
        print()
        if c3 == 'yes':
            gargoil() 
        else:
            print("Come back when you are braver")
            spawnPoint()
               
    else:
        print("Solid choice, who knows what is up with that thing")
        bird1()
      
def bird2():
    print('The bird looks at you and says "I applaud your bravery,')
    print('I would like to grant you the gift of light, but first you')
    print('must prove your worth. I will refill your health, then you')
    print('must defeat me in combat."')
    choice = input("Will you accept this challange?")
    if choice == 'yes':
        # this establishes the variables for the fight
        # it also allows for health or attack to be raised when
        # the player has progressed further in the game
        # I have not set this not to allow for replay even after 
        # lamp is collected, because it can be fun to redo fights once 
        # the player has made progress
        healthy = health + (tokens * 3)
        attack = attackBase + (tokens * 2)
        birdy = goldenBird
        while healthy > 0 and birdy > 0:
            #This will randomly assign the bird an attack for each round
            birdAttack = random.randint(0,5)
            #this calculates the attack and new health for each fighter and prints it
            healthy -= birdAttack
            birdy -= attack
            print("The bird did", birdAttack, "damage, your health is now", healthy)
            print("You did", attack, "damage, the bird's health is now", birdy)
            #checks if the bird has been defeated    
        if birdy <= 0 and healthy > 0:
            print('"You have proven yourself a powerful warrior, I will now present you')
            print('with this lamp to light your future travels"')
            global has_light
            has_light = True
            print("Your health has been restored it is now", (health + (tokens * 3)))
            spawnPoint()
        else:
            choice = input("Would you like to try again?")
            if choice == 'yes':
                bird2()
            else:
                spawnPoint()
    else:
        spawnPoint()
                
def bird1():
    print("You walk around the trees looking at the birds and bugs")
    print("You find a bird that looks like it is made of gold, 'What?'")
    c4 = input("Will you look into the bird?")
    print()
    if c4 == 'yes':
        bird2()
  
def hangman():
    myfile = open('60500_6504591_5536865.txt', 'r')
    wordList = ['']
    for word in myfile:
        wordList.append(word)
    word = wordList[random.randint(0,len(wordList))]
    guessed_letters = []
    win = False
    tries = 10  # Number of allowed incorrect tries
    # print(word)
    goal = []
    for letter in word:
        goal.append(letter)
    while tries > 0:
        # Display the current status of the word with blank spaces and correctly guessed letters
        display_word = ""
        cnt = 0
        for letter in word :
            if letter in guessed_letters:
                display_word += letter
            elif letter != word[-1]:
                display_word += "_"
                cnt +=1
        #cnt counts the number of times '-' is printed, because when the word has been 
        #guessed correctly '-' should never be printed
        if (cnt == 0 ):
            print("Congratulations! You guessed the word:", word)
            win = True
            return win

        print("Current word:", display_word)
        print("Tries left:", tries)

        # Prompt the user to guess a letter
        guess = input("Guess a letter: ").lower()

        # Check if the guessed letter is valid and not already guessed
        if guess.isalpha() and len(guess) == 1 and guess not in guessed_letters:
            guessed_letters.append(guess)
        else:
            print("Invalid guess. Please enter a single letter.")
            continue

        # Check if the guessed letter is in the word
        if guess in word:
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            tries -= 1
   #if the player fails to guess correctly this gives the chance to retry
    print("Unfortunity you didn't guess correctly, the word was", word)
    choice = input("Would you like to try again?")
    print()
    if choice == 'yes':
        hangman()
    else:
        return win

# Beginning of the story        
print("You wake up in the woods and can't figure out where you are")
print("all you know is that you must find a way to defeat the tyrant king")
c1 = input("Will you go left, or right?")
print()

if c1 == "left":
    clearing()
else:
    cave1()