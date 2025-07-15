import os
os.path.abspath("List.txt")
print('Hello, I am a Fish lure guide for your collection of fish lures')
print('You are able to go as you wish in this system.')
print('But if you ever want to opt out and close the program, press q whenever presented.')
print('To go through our options of what is possible, press 1 to see our list of fishing bait,')
print("press 2 to see and adjust your favorite's list if wanted, (Press q to exit program) ")
#print("And press 3 to  ")not sure for this one yet, but i want at least 3 options
op = str(input())
favorites_list = []
def add(index):
    pass
    f = open('List.txt', 'r')
    content = f.readlines()
    x = favorites_list.append(content.)
    return x
def remove(Bait):
    pass
    #instead of going through a filem we just use the specific name of the bait, and locate it
    #then remove it from favorites_list

if op == '1':
    F_L_L = open('List.txt', 'r')  
    #Still trying to figure out how to grab the file from my computer, but the rest should work so far
    content = F_L_L.read()
    print(content)
if op =='2':
    print("You can either add, remove or view your favorite's list")
    print('press 1 to add, 2 to remove, and 3 to view(Press q to exit program)')
    opi = str(input())
    if opi == '1':
        print('Please enter the Bait # of what bait you want to add')


    if opi =='2':
        print('not dun yet') 

    if opi =='3':
        print('also not dun yet')
    #if len(favorites_list)<0:
     #   print('There is nothing in your list so far')
    #if len(favorites_list)>0:
     #   print('Here is whats in your list.')
    if opi =='q':
        print('Thank you for using the Fish lure guide :D')
        exit()
        
if op =='q':
    print('thank you for using the Fish lure guide :D')
    exit()

#not entirely done, but a lot of work added that was needed
#will finish the ncessary portion of this project before the 20th
#then will continue with the project as so.
#also while i can't attach the txt file that is required to be used with this code
#i will send an email with it to whoever needs it to test out the functionality of the code
#when the code is ready 




