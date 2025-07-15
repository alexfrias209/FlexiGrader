
print('Welcome to "Gas Amount" \n')

print('These program would give the user the amount of gasoline based on:\n 1)The users car\n 2)The amount of miles required to get to the desired destination\n')

while True:
    amiles =input('what is the amount of miles required to get to your destination?\n:')

    try:
        amiles = int(amiles)
        break

    except ValueError:
        print('invalid answer\n try again')




 
if amiles >= 1 :
    didanswer=True
    print('Please enter the car with the type of transmicion, engine size, and the cylinders.\n or \nJust the car and transmicion.')   
    cars= input('\nWhat type of car you have? \n \n-----examples-----\n LAMBORGHINI Aventador Coupe AM-S7 6.5L 12cyl \n or \n LAMBORGHINI Aventador Coupe AM-S7 \n \n PORSCHE 911 GT3 AM-S7 3.8L 6cyl \n or \n PORSCHE 911 GT3 AM-S7 \n------------------- \n:')

    if amiles and cars:
        with open("68079_6420780_2054302.txt", "r", encoding="cp1252") as file:
            foundcar= False
            
    
            for line in file:
                parts= line.strip().split(',')

                carname=parts[0]               
                mpg= parts[1]

                if carname.lower()== cars.lower():
                    foundcar= True
                    print(f'you have selected the car {carname}.\n')
            
                    print(f'the gas needed for {carname} to travel {amiles} miles is {amiles/int(mpg)} gallons \n')
                
        
            if not foundcar:
                    print("Car not found!")
    else:
        print('you did not answer all the questions, sorry :( ')
else:
    print('no reasonable number of miles :( \n')


print('have a good day :)')
