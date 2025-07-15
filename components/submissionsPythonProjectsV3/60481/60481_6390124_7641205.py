import random
counter = int(input('How many times would you like to play (1-4)? '))
print('We will have a number of points based on your number of times played, starting at zero. If you live then you get a point, if you die then you get no points. Max points is 1.0, lowest is 0')
score = 0
heheha = counter
while counter > 0:
    thing = open('chambers.txt', 'r')
    #opens the file to be read
    k = thing.readlines()
    for line in k:
        empty_chambers = line.split(' ')
    #creates a list for the numbers in the chamber
    thing.close()
    #closes file
    user_choice = int(input('Enter an amount of bullets (1-6)'))

    # ask the user for the range of numbers changed
    for i in range(0, user_choice):
        empty_chambers[i] = "-"
        #replaces the first few index numbers with -
    def chance(user_choice):
        c = (user_choice / 6) * 100
        return c
    #Creates a function that gives the user the lose percent
    print(f'You currently have a {chance(user_choice):.2f}% of getting shot here.')
    print(empty_chambers)
    user = input(f'Would you like to fire the gun? yes or no ')
    #Gives the choice of continuing the game
    if user == 'yes':
        o = random.randint(0, 5)
        #chooses a random number for the user and uses this number to display death or not
        if empty_chambers[o] == '-':
            print(empty_chambers[o])
            print('You have been shot :(')
        else:
            print(empty_chambers[o])
            print('You lived!')
            score += 1
    if user == 'no':
        print('Good Choice')
    
    counter -= 1
score = score / heheha
print(f'Your final average score is {score}')
if heheha == 1:
    #does this for every number but add a highscore to the file
    with open('high_1.txt', 'a') as file:
        file.write(f'{score} \n')
        #adds score
    with open('high_1.txt', 'r') as file:
        numbers = [float(line.strip()) for line in file]
    numbers = sorted(numbers, reverse=True)
    #reads the file to then sort the file by highest to lowest

    with open('high_1.txt', 'w') as file:
        for number in numbers:
            file.write(f'{number} \n')
    #adds score and sorts it
    print(f'The highest score is {numbers[0]}')
    
if heheha == 2:
    with open('high_2.txt', 'a') as file:
        file.write(f'{score} \n')
    with open('high_2.txt', 'r') as file:
        numbers = [float(line.strip()) for line in file]
    numbers = sorted(numbers, reverse=True)

    with open('high_2.txt', 'w') as file:
        for number in numbers:
            file.write(f'{number} \n')

    print(f'The highest score is {numbers[0]}')
        
    
if heheha == 3:
    with open('high_3.txt', 'a') as file:
        file.write(f'{score} \n')
    with open('high_3.txt', 'r') as file:
        numbers = [float(line.strip()) for line in file]
    numbers = sorted(numbers, reverse=True)

    with open('high_3.txt', 'w') as file:
        for number in numbers:
            file.write(f'{number} \n')
    print(f'The highest score is {numbers[0]}')
    
if heheha == 4:
    with open('high_4.txt', 'a') as file:
        file.write(f'{score} \n')
    with open('high_4.txt', 'r') as file:
        numbers = [float(line.strip()) for line in file]
    numbers = sorted(numbers, reverse=True)

    with open('high_4.txt', 'w') as file:
        for number in numbers:
            file.write(f'{number} \n')
    print(f'The highest score is {numbers[0]}')
