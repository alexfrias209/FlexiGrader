#to begin our Bobcat Shuttle Tracker we are going to define a functionto read the shuttle schedules
def file_schedules(filename):
    schedules = {}
    try:
#open file for reading
        with open(filename, 'r') as file:
#split departure and time
            for line in file:
#store data in dictionary
                stop, departure_time = [item.strip() for item in line.split(',')]
                schedules[stop] = departure_time
        return schedules
    except FileNotFoundError:
        print(f'File {filename} not found.')
        return{}
#present the main function of the shuttle schedule
def pres_shuttle_schedule(shuttle_info, shuttle_name, schedules, default_times):
    if shuttle_name in shuttle_info:
#look to get shuttle information
        info = shuttle_info[shuttle_name]
        route = info['route']
        departure_times = info['departure_times']
        #display name of shuttle
        print(f'Shuttle Name: {shuttle_name}')
#cycle through each stop and departure time
        for stop, time in zip(route, departure_times):
#We will use N/A as a placeholder if departure time from schedule isnt found
            departure_time = schedules.get(stop, default_times.get(stop, 'N/A'))
#show the stop and departure time
            print(f'Stop: {stop}, Departure Time: {departure_time}')
#add a separation
        print('------------------')
    else:
        print('That did not work. Please try again.')
#Define filename of DefaultTimes
default_times_file = '660151_6422430_8981145.txt'
#Read DefaultTimes frmom file
default_times = file_schedules(default_times_file)
output_file = 'shuttle_tracker_output.txt'
#Add shuttle info dict.
bobcat_shuttle_info = {
    'Bobcat_Express': {
        'route': [
            'Merced Station',
            'Merced College',
            'Target',
            'Walmart',
            'Amtrak',
            'Downtown Merced',
            'In n Out',
            'UC Merced'
        ],
        'departure_times': [
            '9:00 AM',
            '10:00 AM',
            '11:30 AM',
            '1:00 PM',
            '2:00 PM',
            '2:45 PM',
            '3:30 PM',
            '5:00 PM'
        ]
    },
    'Fast_Cat': {
        'route': [
            'Merced College',
            'Amtrak',
            'UC Merced',
            'Walmart',
            'Merced Station',
            'Downtown Merced',
            'In n Out',
            'Target',
        ],
        'departure_times': [
            '9:15 AM',
            '10:30 AM',
            '11:00 AM',
            '1:00 PM',
            '2:15 PM',
            '3:00 PM',
            '4:30 PM',
            '5:30 PM'
        ]
    },
    'G_Line': {
        'route': [
            'In n Out',
            'Downtown Merced',
            'Merced College',
            'Merced Station',
            'Amtrak',
            'UC Merced',
            'Walmart',
            'Target',
        ],
        'departure_times': [
            '8:30 AM',
            '9:45 AM',
            '10:45 AM',
            '12:15 PM',
            '1:30 PM',
            '2:30 PM',
            '3:30 PM',
            '4:45 PM'
        ]
    },
    'Yosemite_Express': {
        'route': [
            'Walmart',
            'Target',
            'Merced College',
            'Merced Station',
            'In n Out',
            'Downtown Merced',
            'Amtrak',
            'UC Merced',
        ],
        'departure_times': [
            '9:30 AM',
            '10:00 AM',
            '11:15 AM',
            '1:00 PM',
            '2:15 PM',
            '3:30 PM',
            '4:30 PM',
            '5:45 PM'
        ]
    },
    'Merced_Express': {
        'route': [
            'UC Merced',
            'Amtrak',
            'In n Out',
            'Merced Station',
            'Merced College',
            'Downtown Merced',
            'Walmart',
            'Target',
        ],
        'departure_times': [
            '8:45 AM',
            '9:15 AM',
            '10:30 AM',
            '11:45 AM',
            '12:45 PM',
            '1:15 PM',
            '2:30 PM',
            '3:15 PM'
        ]
    }
}
for shuttle_name, info in bobcat_shuttle_info.items():
    for stop, departure_time in zip(info['route'], info['departure_times']):
        default_times[stop] = departure_time
#begin infinite loop for user
while True:
    #Welcome + Options + Selection

    print('What would you like to do today?\n')
    print('1. Track a Shuttle')
    print('2. See Shuttle Schedule')
    print('3. Exit')
    selection = input('Please select an option (1,2,3): ')
    if selection == '1':
        print('You have chosen to track a shutle')
    #user has choice to track the shuttle they want
        specific_shuttle_selection = input('Enter name of shuttle you would like to track Bobcat_Express, Fast_Cat, G_Line, Yosemite_Express, or Merced_Express): ')
        if specific_shuttle_selection in bobcat_shuttle_info:
            print("Debug - Calling pres_shuttle_schedule with specific_shuttle_selection and default_times:", specific_shuttle_selection, default_times)
            #display the schedule
            pres_shuttle_schedule(bobcat_shuttle_info, specific_shuttle_selection, default_times, default_times)
            with open(output_file, 'a') as output:
                output.write(f'Shuttle information for {specific_shuttle_selection}:\n')
                for stop in bobcat_shuttle_info[specific_shuttle_selection]['route']:
                    departure_time = default_times.get(stop, 'N/A')
                    output.write(f'Stop: {stop}, Departure Time: {departure_time}\n')
                output.write('------------------\n')
            print(f'Shuttle information has been saved to {output_file}.')
        else:
            print('That did not work. Please try again.')
    elif selection == '2':
        print('You have chosen to view the shuttle schedule')
        #pres_shuttle_schedule shows shedule for all shuttles
        for shuttle_name in bobcat_shuttle_info:
            print("Debug - Calling pres_shuttle_schedule with shuttle_name and default_times:", shuttle_name, default_times)   
            pres_shuttle_schedule(bobcat_shuttle_info, shuttle_name, default_times, default_times)
    elif selection == '3':
        #simple user exit
        print('You have chosen to exit the Bobcat Shuttle Service. See you Soon!')
        break
    else:
        print('That did not work. Please select (1, 2, 3)')
        
