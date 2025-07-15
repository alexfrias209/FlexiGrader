#define functions to read the contents of files with the calendar info
#as well as write that info into a saved file with a desired file name input by the user
def show_events_sports(sports_gender):
    file_name = 'gs.txt' if sports_gender =='girls' else 'bs.txt'
    with open(file_name, 'r') as file:
        sports_contents = file.read()
    with open(desired_file_name,'w') as file_name:
        file_name.write(sports_contents)
def show_events_academic(academic_type):
    file_name = 'stem.ac.txt' if academic_type == 'STEM' else 'writing.ac.txt'
    with open(file_name, 'r') as file:
        academic_contents = file.read()
    with open(desired_file_name, 'w') as file_name:
        file_name.write(academic_contents)
def show_events_social(event_type):
    file_name = 'net.ev.txt' if event_type == 'networking' else 'soc.ev.txt'
    with open(file_name, 'r') as file:
        events_contents = file.read()
    with open(desired_file_name, 'w') as file_name:
        file_name.write(events_contents)
#welcome user
print('Welcome to the UCM Event Calendar!')
print('Get info on several categories of activities held here at UCM!')
print('\nPlease choose one of the following event categories youre interested in looking at:')
print('1. Sports \n2. Academics \n3. Social')
choice = input('')
print('You have chosen the event category', choice)
if choice == '1':
#choice one is associated with the choice sports
#has two subchoices of girls or boys sports
    print('Would you like to see girls or boys sports?')
    sports_gender = input()
    print('You have chosen to see', sports_gender,'sports')
    print('Enter a name you would like the file to be saved as ')
    desired_file_name = input()
    show_events_sports(sports_gender)
elif choice == '2':
#choice two is associated with the choice academic events
#has two subchoices of STEM or writing academic activities
    print('Would you like to see STEM or writing academic events?')
    academic_type = input()
    print('You have chose to see', academic_type , 'academic events!')
    print('Enter a name you would like the file to be saved under ')
    desired_file_name = input()
    show_events_academic(academic_type)
elif choice == '3':
#choice three is associated with the choice social events
#has two subchoices of networking or casual social events
    print('Would you like to see networking events or social events?')
    event_type = input()
    print('You have chosen to see', event_type ,'events!')
    print('Enter a name you would like the file to be saved as ')
    desired_file_name = input()
    show_events_social(event_type)
else:
    print('Your choice was not an option!')
    