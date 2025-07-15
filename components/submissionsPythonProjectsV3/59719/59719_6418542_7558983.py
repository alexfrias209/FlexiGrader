#username
username = input('Hello, welcome to a basic car builder. What is your name: ')

#cars
car_list = ['2000 Honda Civic','2013 Scion FRS','2006 Toyota MR2','2004 Mazda RX8']
car_price_list = ['2500', '13000', '6000', '8500']
#List to display selection of cars
print(f'1. {car_list[0]}, ${car_price_list[0]}')
print(f'2. {car_list[1]}, ${car_price_list[1]}')
print(f'3. {car_list[2]}, ${car_price_list[2]}')
print(f'4. {car_list[3]}, ${car_price_list[3]}')

#I have to use 'try' and 'except' for the list otherwise it would return an index error rather than returning to the loop
#Use a while loop so when an incorrect value is entered, it loops. Applies to all the other categories too
while True:
  try:
    car = input("Choose your car by inputting the number next to the one you want:")
    if car.isnumeric() == True:
      car_choice = (car_list[int(car)-1])
      car_price = int(car_price_list[int(car)-1])
      print(car_choice)
      break
  except IndexError:
    print('Please enter a number next to the car')

#wheels
wheel_list = ['Enkei RPF1', 'Rays TE37', 'Rays 57CR', 'Konig Dekagram', 'Konig Hypergram']
wheel_price_list = ['1252', '3268', '1915', '1016', '968']
#wheel prices are mainly based off of the diameter of the wheel, for this project it was 17"
#List to display selection of wheels
print(f'1. {wheel_list[0]}, ${wheel_price_list[0]}')
print(f'2. {wheel_list[1]}, ${wheel_price_list[1]}')
print(f'3. {wheel_list[2]}, ${wheel_price_list[2]}')
print(f'4. {wheel_list[3]}, ${wheel_price_list[3]}')
print(f'5. {wheel_list[4]}, ${wheel_price_list[4]}')
while True:
  try:
    wheels = input('Choose a set of wheels by inputting the number next to the wheels you want: ')
    if wheels.isnumeric() == True:
      wheel_choice = (wheel_list[int(wheels)-1])
      wheel_price = int(wheel_price_list[int(wheels)-1])
      print(wheel_choice)
      break
  except IndexError:
        print('Please enter a number next to the wheels')

#tires
tire_list = ['Yokohama','Bridgstone','Nitto','Kumho','Michelin']
tire_price_list = ['1032', '964', '648','824', '1056']
#tire prices are also mainly based off of performance tires and the width of the tire, for this project it was 245mm
#List to display selection of tires
print(f'1. {tire_list[0]}, ${tire_price_list[0]}')
print(f'2. {tire_list[1]}, ${tire_price_list[1]}')
print(f'3. {tire_list[2]}, ${tire_price_list[2]}')
print(f'4. {tire_list[3]}, ${tire_price_list[3]}')
print(f'5. {tire_list[4]}, ${tire_price_list[4]}')
while True:
  try:
    tires = input('Choose a set of tires by inputting the number next to the brand of tires you want: ')
    if tires.isnumeric() == True:
      tire_choice = (tire_list[int(tires)-1])
      tire_price = int(tire_price_list[int(tires)-1])
      print(tire_choice)
      break
  except IndexError:
        print('Please enter a number next to the tires')

#suspension
suspension_list = ['Fortune Auto', 'BC Racing', 'KW Coilover', 'Tein', 'Truhart']
suspension_price_list = ['900', '1245', '1599', '920', '544']
#List to display selection of suspension
print(f'1. {suspension_list[0]}, ${suspension_price_list[0]}')
print(f'2. {suspension_list[1]}, ${suspension_price_list[1]}')
print(f'3. {suspension_list[2]}, ${suspension_price_list[2]}')
print(f'4. {suspension_list[3]}, ${suspension_price_list[3]}')
print(f'5. {suspension_list[4]}, ${suspension_price_list[4]}')
while True:
  try:
    suspension = input('Choose which brand of suspension you want by inputting the number next to the one you want: ')
    if suspension.isnumeric() == True:
      suspension_choice = (suspension_list[int(suspension)-1])
      suspension_price = int(suspension_price_list[int(suspension)-1])
      print(suspension_choice)
      break
  except IndexError:
        print('Please enter a number next to the suspension')

#brakes
brake_list = ['Brake pads','Brake calipers','Brake rotors']
brake_price_list = ['80', '562', '1052']
#List to display selection of brakes
print(f'1. {brake_list[0]}, ${brake_price_list[0]}')
print(f'2. {brake_list[1]}, ${brake_price_list[1]}')
print(f'3. {brake_list[2]}, ${brake_price_list[2]}')
while True:
  try:
    brakes = input('Choose which brake upgrade you want by inputting the number next to the one you want: ')
    if brakes.isnumeric() == True:
      brake_choice = (brake_list[int(brakes)-1])
      brake_price = int(brake_price_list[int(brakes)-1])
      print(brake_choice)
      break
  except IndexError:
        print('Please enter a number next to the brakes')
#engine
engine_list = ['Hot air intake', 'Cold air intake']
engine_price_list = ['450', '400']
#List to display selection of engine parts
print(f'1. {engine_list[0]}, ${engine_price_list[0]}')
print(f'2. {engine_list[1]}, ${engine_price_list[1]}')
while True:
  try:
    engine = input('Choose which engine upgrade you want by inputting the number next to the one you want: ')
    if engine.isnumeric() == True:
      engine_choice = (engine_list[int(engine)-1])
      engine_price = int(engine_price_list[int(engine)-1])
      print(engine_choice)
      break
  except IndexError:
        print('Please enter a number next to engine')

#exhaust
exhaust_list = ['Cat-back exhaust', 'Full exhaust']
exhaust_price_list = ['1445', '2145']
#List to display selection of exhaust
print(f'1. {exhaust_list[0]}, ${exhaust_price_list[0]}')
print(f'2. {exhaust_list[1]}, ${exhaust_price_list[1]}')
while True:
  try:
    exhaust = input('Choose which exhaust upgrade you want by inputting the number next to the one you want: ')
    if exhaust.isnumeric() == True:
      exhaust_choice = (exhaust_list[int(exhaust)-1])
      exhaust_price = int(exhaust_price_list[int(exhaust)-1])
      print(exhaust_choice)
      break
  except IndexError:
        print('Please enter a number next to exhaust')

#total
total_price = (car_price + wheel_price + tire_price + suspension_price + brake_price + engine_price + exhaust_price)
print(f"So, {username}. Your total selection is a {car_choice} with {wheel_choice} wheels, {tire_choice} tires, {suspension_choice} suspension, {brake_choice}, a {engine_choice}, and a {exhaust_choice}. The total price for your build is ${total_price}.")
