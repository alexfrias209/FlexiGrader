print('Welcome to workout generator!')
print()
print('Developed')
print('This program is a guide to beginners who need help understanding which workouts to use in order to get the results they desire')
print()
workouts = ['Here is your workout:']
while True:
    group = input('What muscle group would you like to excersice today?\n 0. Start Workout! \n 1. Upper Body \n 2. Lower Body \n 3. Abdominal \n')
    if group == '1':
        print('Working Upper Body')
        choice = input('Please choose a section of Upper Body \n 1. Biceps \n 2. Forearms \n 3. Triceps \n 4. Chest \n 5. Back \n 6. Traps \n 7. Go back \n')
        if choice == '1':
            print('Working Biceps')
            workouts.append('Hammer curls: 3 sets 12 reps')
            workouts.append('Barbell curls: 3 sets 10 reps')
        elif choice == '2':
            print('Working Forearms')
            workouts.append('Wrist curl: 3 sets 12 reps')
            workouts.append('Reverse curl: 3 sets 10 reps')
        elif choice == '3':
            print('Working Triceps')
            workouts.append('Tricep extensions: 3 sets 15 reps')
            workouts.append('Skull crushers: 3 sets 10 reps')
        elif choice == '4':
            print('Working Chest')
            workouts.append('Bench press: 3 sets 10 reps')
            workouts.append('Dumbell bench press: 3 sets 10 reps')
            workouts.append('Incline bench press: 3 sets 10 reps')
            workouts.append('Cable flies: 3 sets 10 reps')
        elif choice == '5':
            print('Working Back')
            workouts.append('Bent over row: 3 sets 15 reps')
            workouts.append('Back extensions: 3 sets 10 reps')
            workouts.append('Lat pull downs: 3 sets 12 reps')
            workouts.append('Cable seated row: 3 sets 15 reps')
        elif choice == '6':
            print('Working Traps')
            workouts.append('Shoulder shrugs: 3 sets 15 reps')
            workouts.append('Upright row: 3 sets 10 reps')
            workouts.append('Dumbell lateral raise: 3 sets 15 reps')
        elif choice == '7':
            print('Go back')
            
    elif group == '2':
        print('Working Lower Body')
        choice = input('Please choose a section of Lower Body \n 1. Quadriceps \n 2. Hamstrings \n 3. Calfs \n 4. Go back \n')
        if choice == '1':
            print('Working Quadriceps')
            workouts.append('Barbell squat: 3 sets 10 reps')
            workouts.append('Leg extensions: 3 sets 15 reps')
            workouts.append('Leg press: 3 sets 10 reps')
            workouts.append('Split squats: 2 sets 20 reps')
        elif choice == '2':
            print('Working Hamstrings')
            workouts.append('Glute bridge: 3 sets 15 reps')
            workouts.append('Ball leg curl: 3 sets 10 reps')
            workouts.append('Leg curl: 3 sets 15 reps')
        elif choice == '3':
            print('Working Calfs')
            workouts.append('Calf raises: 3 sets 20 reps')
        elif choice == '4':
            print('Go back')
            
    elif group == '3':
        print('Working Abdominal')
        choice = input('Please choose a section of Abdominals \n 1. Obliques \n 2. Upper Abs \n 3. Lower Abs \n 4. Go back \n')
        if choice == '1':
            print('Working Obliques')
            workouts.append('Russian Twist: 3 sets of 30 reps')
            workouts.append('Side Plank: hold for 60 seconds on each side')
            workouts.append('Bicycle Crunch: 2 sets of 30 reps')
            workouts.append('Mountain Climbers: 3 sets 30 reps')
        elif choice == '2':
            print('Upper Abs')
            workouts.append('Crunch: 2 sets of 30 reps')
            workouts.append('Sit Ups: 3 sets of 30 reps')
            workouts.append('Plank: hold for 60 seconds')
            workouts.append('Cable crunches: 3 sets of 15 reps')
        elif choice == '3':
            print('Lower Abs')
            workouts.append('Leg Lowers: 2 sets of 20 reps')
            workouts.append('Toe Touches: 2 sets of 20 reps')
            workouts.append('Flutter Kicks: Do this for thirty seconds at a steady pace')
            workouts.append('Scissor Kicks: Do this for thirty seconds at a steady pace')
        elif choice == '4':
            print('Go back')

    elif group == '0':
        break
print('\n'.join(workouts))
input()






