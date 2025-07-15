import matplotlib.pyplot as plt
import csv
import datetime

#define the reader to open csv
def read_csv(filepath):
    dictionary = {}
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            movement = row[0]
            weights = [int(weight) for weight in row[1:]]
            dictionary[movement] = weights
    return dictionary

#create the ability to edit the csv
def write_csv(filepath, dictionary):
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['movement', 'pr', 'light', 'med', 'heavy'])
        for movement, weights in dictionary.items():
            writer.writerow([movement] + weights)

#function to only append, not edit csv
def append_progress_csv(filepath, data):
    with open(filepath, 'a', newline='') as file:
        writer = csv.writer(file)
        today = datetime.date.today().strftime("%Y-%m-%d")
        row = [today, data['squat'][0], data['bench'][0], data['deadlift'][0]]
        writer.writerow(row)

#creates ability to plot the progress(lbs) over time
def plot_progress(filepath):
    dates, squats, benches, deadlifts = [], [], [], []
    with open(filepath, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dates.append(row['Date'])
            squats.append(float(row['Squat']))
            benches.append(float(row['Bench']))
            deadlifts.append(float(row['Deadlift']))

    plt.figure(figsize=(10, 5))
    plt.plot(dates, squats, label='Squat', marker='o')
    plt.plot(dates, benches, label='Bench', marker='o')
    plt.plot(dates, deadlifts, label='Deadlift', marker='o')

    plt.title('Workout Progress')
    plt.xlabel('Date')
    plt.ylabel('Weight (lbs)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

filepath = '61291_6419697_9870287.csv'
filepath_progress = '61291_6419698_6808531.csv'
bar = 45 #weight of empty bar

x = input('Enter "y" to start and "n" to stop.\n') #starting/stopping code
while x.lower() == 'y':
    print('Enter the number of plates on the bar to calculate weight') #calculating weight lifted
    red = int(input('How many 55lb plates\n'))
    blue = int(input('How many 45lb plates\n'))
    yellow = int(input('How many 35lb plates\n'))
    green = int(input('How many 25lb plates\n'))
    black = int(input('How many 15lb plates\n'))
    grey = int(input('How many 10lb plates\n'))
    white = int(input('How many 5lb plates\n'))
    purple = int(input('How many 2.5lb plates\n'))

    bar += 2 * (red*55 + blue*45 + yellow*35 + green*25 + black*15 + grey*10 + white*5 + purple*2.5)
    bar_kg = round(bar * 0.45359, 2) #lbs -> kgs
    bar = int(bar)

    print('You have', bar, 'lbs/', bar_kg, 'kg on the bar') #displaying weight

    data = read_csv(filepath) #accsessing csv to view last pr
    user = input('Did you squat, bench, or deadlift: ').lower()
    print(f'You chose {user}, your last one rep max was {data[user][0]}') 

    #updating csv only if current weight is greater than last pr
    if bar > data[user][0]:
        data[user][0] = bar
        write_csv(filepath, data)
        append_progress_csv(filepath_progress, data)
        print("Great job! We've saved your progress.")

    else:
        print("Not quite a Pr, keep pushing!!!")

    new_prs = {exercise: weights[0] for exercise, weights in data.items()}
    print(f'Your updated PRs are {new_prs}')

    plot_progress(filepath_progress)
  
    #continuing or stopping program
    x = input('Would you like to continue? (y/n)\n') 

print('Have a good lift')