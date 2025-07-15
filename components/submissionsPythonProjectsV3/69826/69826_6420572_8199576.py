
#-----------------------------------User Input for City of Choice--------------------------
Choice_1 = input('Please choose one from the from the list of Cities: \nNew York \nLos Angeles \nHouston \nSeattle \nSan Francisco \nDallas \nPhiladelphia \nMiami \nAtlanta \nMerced \nChicago \n')
Verify_1 = ['new york', 'los angeles', 'houston', 'seattle', 'san francisco', 'dallas', 'chicago', 'miami', 'philadelphia', 'merced', 'atlanta', 'dev']
Choice_1_lower = Choice_1.lower() #Forcing input to be in lower case so there isn't a problem in registering it, Although it does make the grammar incorrect in the print lines. 
if Choice_1_lower in Verify_1: #Makes sure that the input is in the list 
    print('You have chosen:', Choice_1)
else:
    print('City not found in provided list, please try again')
    end1 = input('Press enter to exit code\n')
    quit()

#-----------------------------User Input of Fruit tree of Choice--------------------------------------------
Choice_2 = input('Now, from the following list please select the fruit tree you want to plant in your city: \n(Please type your answer as "Fruit tree" where Fruit is your choice) \nPeach tree \nAvocado tree \nApple tree \nCherry tree \nMango tree \nPear tree \nSoursop tree \n')
Verify_2 = ['peach tree', 'avocado tree',  'apple tree', 'cherry tree', 'mango tree', 'pear tree', 'soursop tree', 'dev']
Choice_2_lower = Choice_2.lower() #Forces the user input to be in all lower case 
if Choice_2_lower in Verify_2: #Makes sure that the input is in the list
    print('You have chosen:', Choice_2)
else:
    print('Tree not found in provided list, please try again')
    end2 = input('Press enter to exit code\n')
    quit()

#------------------------Getting the City's Information------------------------
City_file = open('69826_6420573_5414951.txt', 'r', encoding="cp1252") #Open cities.txt file 


City_lines = []
New_line = ['city', 'zone', 'temp', 'rain'] 
city = ['city']
City_choice = []
Zone = ['Zone']
temp = ['temp']
# Here I created a bunch of new list to use in future code 


City_lines = City_file.readlines()

City_val = 0
for line in City_lines:
    City_line = line.split()
    City = City_line[0:1]
    City = [city.replace("-", " ") for city in City]
    City_str = ''.join(City)
    City_lower = City_str.lower()
    if Choice_1_lower in City_lower:
        City_choice = City[0:1]
        City_Zone = City_line[1:2]
        City_rain = City_line[2:3]
        City_val = 1

if City_val == 0:
    print('system error occurred, please try again') #Just in case for some reason the previous for and if loop dont work 
    end3 = input('Press enter to exit code\n')
    quit()
    
City_file.close()#Close City_file since its not needed anymore 
City_str = ''.join(City_choice)
Zone_str = ''.join(City_Zone) # Converts Zone from list into string 
rain_str = ''.join(City_rain) # Converts rain from list into string


print(f"{City_str}'s hardiness zone is {Zone_str}, with an average rainfall of {rain_str}")

#------------------------------Getting the Fruit tree's information---------------------------------
Tree_line = []


Tree_file = open('69826_6420574_9583031.txt', 'r', encoding="cp1252") #Open tree.txt file

tree = [' tree']
tree = ''.join(tree)
Tree_lines = Tree_file.readlines()
Tree_val = 0
for line in Tree_lines:
    Tree_line = line.split()
    fruit = Tree_line[0]
    fruit = ''.join(fruit)
    fruit = fruit + tree # Adding 'tree' to make the string 'fruit tree' because when I put in peach tree instead of Peach tree, the code would find that 'tree' in the text file satisfied my code making the valid line ['tree', 'zone', 'rain'] which Tree val wouldn't catch  but Min = int(Fruit_zone[0]) would give me an error since 'zone' isn't an integer
    fruit_lower = fruit.lower()
    if fruit_lower in Choice_2_lower:
        Tree_val = 1
        Fruit_tree = fruit
        Fruit_zone = Tree_line[1]
        Fruit_rain = Tree_line[2]

if Tree_val == 0:
    print('system error occurred, please try again') #Just in case for some reason the previous for and if loop dont work 
    end4 = input('Press enter to exit code\n')
    quit()
    
    
Tree_file.close()#Closing Tree_file 


print(f"The {Fruit_tree} tree has a zone range of {Fruit_zone} and an average rainfall of {Fruit_rain} inches")


City_zone = ''.join((x for x in Zone_str if x.isdigit()))#Strips the City's zone of letters, so 8b becomes 8 inorder to calculate range
City_zone = int(City_zone)

#----------------Hardiness Zone Range Calculator-----------------------------
Fruit_zone = ''.join(Fruit_zone)#Convert Fruit_zone from list into string 
Fruit_zone = Fruit_zone.split('-')#Converts Fruit_zone from string to list seperating my lower and upperbound
Min = int(Fruit_zone[0])
Max = int(Fruit_zone[1])
Fruit_range = range(Min, Max)


if City_zone in Fruit_range:
    print(f"{City_str}'s Hardiness Zone of {Zone_str} is in the {Fruit_tree} tree's Hardiness Zone range of {Min}-{Max}")
    Zone_val = 2
else:
    print(f"{City_str}'s Hardiness Zone is not in the {Fruit_tree} tree's Hardiness Zone range")
    Zone_val = -2


#---------------------------------------- Average yearly Rainfall-------------------

if rain_str > Fruit_rain:
    print(f"The {Choice_2} would recieve more than enough rain in {City_str} to supplement itself")
    Rain_val = +1
elif rain_str < Fruit_rain:
    print(f"The {Choice_2} would not recieve enough rain in {City_str} to supplement itself")
    Rain_val = -1
elif rain_str == Fruit_rain:
    print(f"The {Choice_2} would exactly enough rain in {City_str} to supplement itself")
    Rain_val = +1
    
    
#-------------------------------Final Results--------------------------

total_val = Rain_val + Zone_val 
if Zone_val and Rain_val >= 0:
    print(f"{City_str} is a great place for the {Choice_2}, and the {Choice_2} would thrive")
elif Zone_val > 0 and Rain_val < 0:
    print(f"{City_str} is a great place for the {Choice_2}, but the {Choice_2} should be watered reguarly to help it thrive")
elif Zone_val and total_val < 0:
    print(f"The {Choice_2} is not suitable to grow in {City_str} ")
#-------------------------------Final Question--------------------
Choice_3 = input('Thank you for participating please type exit to close the program \n')
Verify_3 = ['exit']
if Choice_3 is Verify_3:
    quit()