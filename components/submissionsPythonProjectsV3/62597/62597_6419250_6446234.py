list1 = []

list2 = [
    'Puerto Rico',
    'Virgin Islands',
    'Massachusetts',
    'Connecticut',
    'New Hampshire',
    'Vermont',
    'New Jersey',
    'New York',
    'South Carolina',
    'Tennessee',
    'Rhode Island',
    'Virginia',
    'Wyoming',
    'Maine',
    'Georgia',
    'Pennsylvania',
    'West Virginia',
    'Delaware',
         ]
state_counts = {}

name = input('What is your name? \n')

print('Hello',name,'This project will ask you for a state and provide the lowest, highest, and the average price of houses in your state.\n it will also provide you a histogram at the end showing you the amaount of for sale houses in each state.\n')

print(
    'Puerto Rico\n'
    'Virgin Islands\n'
    'Massachusetts\n'
    'Connecticut\n'
    'New Hampshire\n'
    'Vermont\n'
    'New Jersey\n'
    'New York\n'
    'South Carolina\n'
    'Tennessee\n'
    'Rhode Island\n'
    'Virginia\n'
    'Wyoming\n'
    'Maine\n'
    'Georgia\n'
    'Pennsylvania\n'
    'West Virginia\n'
    'Delaware\n'
    '\nThese are the available states\n'
      )
      
    
state = input('Enter what state your looking for? \n')#gets state from user
# while statement for error. try again
while state not in list2:
    if state not in list2:
        print('Invalid state! Try picking one of the states lised below.')
        print(
    '\nPuerto Rico\n'
    'Virgin Islands\n'
    'Massachusetts\n'
    'Connecticut\n'
    'New Hampshire\n'
    'Vermont\n'
    'New Jersey\n'
    'New York\n'
    'South Carolina\n'
    'Tennessee\n'
    'Rhode Island\n'
    'Virginia\n'
    'Wyoming\n'
    'Maine\n'
    'Georgia\n'
    'Pennsylvania\n'
    'West Virgina\n'
    'Delaware\n'
    '\nThese are the available states\n'
      )
        state = input('Enter what state your looking for? \n')
        
with open('62597_6419251_90502.csv', mode = 'r') as csvfile: #open and reads file
    
    lines = csvfile.readlines()
        
    for line in lines: #checks line by line

        row = line.strip()
        
        clean = line.split(',') #splits it into commas
        
        state_x = clean[5]  #all the states
        
        #price = float(clean[-1])
        
        if state_x == state:  # checks if correct
            
            price = float(clean[-1])
            
            city = clean[4]
            
            list1.append(price)

#sets up my price
        if state_x not in state_counts:
            
            state_counts[state_x] = 1
        else:
            state_counts[state_x] += 1
            
#checks if state is in dict, if not then add it
        if 'state' in state_counts:
            
            del state_counts['state']

         


# all 'math' is done here   
xx = list1.sort()

x = list1[-1]

y = list1[0]

z = sum(list1)

zz = len(list1)

avg = z / zz

#gets all states and the amounnt of houses in each state split into list
states = list(state_counts.keys())

house_counts = list(state_counts.values())

#print statements
print('The lowest price in',state,'is %.2f' %y)

print('The the highest price in',state,' is %.2f'%x)

print('The average price in',state,'is %.2f' %avg)

print('The highest price in all of the states is in New York, with 875,000,000')

import matplotlib.pyplot as plt
# graph is done here
plt.bar(states, house_counts, width = .8)

plt.xlabel('States')

plt.ylabel('Number of Houses')

plt.title('Number of for sale houses in each state')

plt.xticks(fontsize = 8, rotation = 'vertical')

plt.show()
