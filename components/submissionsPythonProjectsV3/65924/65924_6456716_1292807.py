import matplotlib.pyplot as plt


with open('stuff.txt', 'r') as myfile:
    f_contents = myfile.read()
    print(f_contents)
print('Welcome to the average crime rate generator.')

print('')

print('The calculator uses a formual (total crime / total population x 1000) to calculate the number of crimes per 1000 residents')

print('')

user_input = input('Do you know the total population and total crime of your area ? Please answer yes or no. ')

print('You entered no. Please refer to the file attached above to see the total population and crime statistics of your city.(right click to view file)') if user_input.lower() == 'no' else None

print('')

city_name = input('Please enter the name of your city: ')

print(f'You Entered {city_name}')

print('')

user_crime_input = float(input('Please enter the total number of crimes that have occured in your area:'))

print(f'You Entered {user_crime_input} total crimes.')

print('')

user_population_input = float(input('Please enter the total population of your area: '))

print('')

print(f'You Entered {user_population_input}.')

print('')

average_crime = (user_crime_input / user_population_input) * 1000
print('')

print(f'The average crime rate of {city_name} is: {average_crime:.2f} crimes per 1000 residents.')
print('')

print('Here is a graph of the average crime and total crime based on your inputs.')
print('Thank you for using the average crime rate generator.')
x_values = [average_crime, user_crime_input]
y_values = [1000, user_population_input]


plt.plot(x_values, y_values, marker='x', linestyle='-.', color='m')
plt.title("User-Inputted Graph")
plt.xlabel("Average Crime & Total Crime")
plt.ylabel("Total Population")

plt.show()



