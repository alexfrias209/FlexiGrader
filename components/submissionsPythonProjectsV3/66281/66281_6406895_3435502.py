print("Welcome to my python project! I'm very proud to introduce you to my project today. ")
print("Now, before I continue, I want to make sure that you are following with me every step of the way.")
print("You will now be requested to input yes or no(remember to keep it lowercase!)")
user_compliance=str(input("Please enter yes to continue! \n"))
new_uc=user_compliance
if new_uc =="yes" :
      print("Glad to be on the same page!")
elif new_uc=="no":
    print('\n\nWell, read from the beginning buddy! Please stop the program in the console above, and try again.')
    if new_uc =="yes" :
      print("Glad to be on the same page!")
elif user_compliance != "yes" or "no":
      print("\n\nOopsie! You've made a typo for your input! Please reset the program and try again!")
print("\nUsing data gathered from my phone, into the file Screentime.txt, I was able to find the average time spent in a given week, for three weeks!")
print("If you would like to see the data within this program, please enter yes ( In lower case once again!!!!!)")
user_compliance2=input("Please enter yes if you would like to see my data! \n")
new_uc2=user_compliance2
if new_uc2== "yes":
    with open('66281_6406896_6693092.txt', 'r',encoding="cp1252") as my_file:
        for line in my_file:
            split_contents=line.split('\t')
            Data_broken_down=split_contents
            print(split_contents)
else:
    print('I see, I will be moving forward now!')
print('\nMy data is organized into 6 seperate desginations, which are Screentime, App#1, App#2, App#3, Day, and Week!')
print("App's 1,2, and 3 are the most popular apps given the specific day.")
print("Now, I will begin to demonstrate my findings, but more specified.")
print("The following is calculations based on the averages per week!")
week_choice = input('Please enter a week you are looking for (e.g., "1", "2",  "3"): \n')
week_found = False
with open('66281_6406896_6693092.txt', 'r', encoding="cp1252") as my_file:
    for line in my_file:
        split_contents = line.split('\t')
        if len(split_contents)> 5:
            Week = split_contents[5].strip()
            #strip is necessary to isolate Week value, and remove any empty space!
        else:
            print("Error: The data format in the file is not as expected.")
        if week_choice == Week:
            #my if statement is before the entire deconstructing, to prevent 
            Screentime = split_contents[0]
            App_1 = split_contents[1]
            App_2 = split_contents[2]
            App_3 = split_contents[3]
            Day = split_contents[4]
            #The next four lines of code will help extract the num of hours and minutes!
            index_hr = Screentime.find('hr')
            num_hours = Screentime[:index_hr]
            index_min = Screentime.find('min', index_hr)
            num_minutes = Screentime[index_hr + 2:index_min]
            print(f"Week {week_choice} consists of {num_hours} hours and {num_minutes} minutes, the most popular apps were {App_1}, {App_2}, {App_3} for {Day} in Week {Week}")
            week_found = True
if not week_found:
    print(f"Week {week_choice} was not found in the file. Please check for a typo.")
print(f"For the selected week of {week_choice}, I will now calculate the average!")
total_screen_time=0
with open('66281_6406896_6693092.txt', 'r', encoding="cp1252") as my_file:
    for line in my_file:
        split_contents = line.split('\t')
        Week = split_contents[5].strip()
        if week_choice == Week:
            Screentime = split_contents[0]
            Screentime=Screentime.replace(',', '').replace(' ', '')
            #I need to replace the comma and spaces in Screentime to make a proper integer for total_screen_time!
            index_hr = Screentime.find('hr')
            num_hours = int(Screentime[:index_hr])
            index_min = Screentime.find('min', index_hr)
            num_minutes = int(Screentime[index_hr + 2:index_min])
            #Now I'll gather a way to transfer hours to minutes, and find the sum!
            total_screen_time += (num_hours * 60 + num_minutes)
print(f"The sum of minutes is {total_screen_time}")
avg_screentime_mins = total_screen_time / 7
avg_hours= total_screen_time / 60 / 7
avg_scrtme=round(avg_screentime_mins,2)
avg_scrtme_hr=round(avg_hours,2)
#If i want to have a minutes solution that isn't greater than 60, I need to set a variable for that!(line 73)
print(f"Given the total screentime for week {week_choice}, the average screentime for the given week was {avg_scrtme} minutes, or {avg_scrtme_hr} hours! \n")
print("Now that we have my information here, I'm going to recommend some alternatives!")
if 12>= avg_scrtme_hr >= 9:
    print('My average hours for this week are looking pretty high! I recommed taking breaks of 30 minutes or greater in between assignments or other activities done throguh a screen!')
    print('Some alternative activities I personally enjoy are walking at least a mile, or building some models!')
elif avg_scrtme_hr <9:
    print('My average hours for the selected week are within a recommended range! However, I would suggest taking a fair break in between assingments or activities with a screen, from 30 minutes to an hour!')
    print('What I can subsitute is going for a drive with some music. I love doing this in my free time!')
if avg_scrtme_hr >= 13:
    print("Wow! That's a hefty amount of average hours, I do recommend immediate change to my behavior.")
    print("I need to commit myself to non-technology field for a considerable amount of time.")
    print("I am ashamed :(")


print("If you would like the average on another week, please reset the program and use an applicable week!")
print(f"Using the information profided because of every week Choice, we can gather than the largest value was for week 2, with a hefty 506.57 minutes, or 8.44 Hours!")
print("Because this week was more focused on midterm preperation, you could argue it was justified.")
print(f"\nOrganizing the information into minuntes and hours, we recieve two graphs printed as a result!")

import matplotlib.pyplot as plt  #Graph for minutes!
weeks=['Week 1', 'Week 2', 'Week3']
averages_mins=[397.71, 506.57, 467.29]
fig,ax=plt.subplots()
ax.bar(weeks,averages_mins,color='b',alpha=0.7)
ax.set_xlabel('Week')
ax.set_ylabel('Average Screen time(minutes)')
ax.set_title('Average Screen Time per Week in Minutes')
plt.show()
import matplotlib.pyplot as plt  #Graph for hours!
weeks=['Week 1', 'Week 2', 'Week 3']
averages_hrs=[6.63,8.44,7.79]
fig,ax=plt.subplots()
ax.bar(weeks,averages_hrs,color='c',alpha=0.7)
ax.set_xlabel('week')
ax.set_ylabel('Average Screen time(hours)')
ax.set_title('Average Screen Time per Week in Hours')
plt.show()
print("\n\nNow, I'd like to give you the opportunity to imput your own data!")
final_user_input=str(input("If you would like to add some information, type 'yes'!"))
fui=final_user_input
if fui == 'yes':
    def user_data_to_file(New_Screentime):
        with open(New_Screentime,"a") as file:
            Screentime=input("Enter Screentime (ex: '7hr,03min)")
            App_1=input("Enter the first most used app!")
            App_2=input("Enter the second most used app!")
            App_3=input("Enter the third most popular app!")
            Day=input("Enter a week day!(Full day name)")
            Week=input("Enter the week!(ex:'3','4','1','23' )")
            file.write(f"{Screentime}\t{App_1}\t{App_2}\t{App_3}\t{Day}\t{Week}")
        print("Your data has been uploaded!")
    user_data_to_file("66281_6406896_6693092.txt")
    print("\n Now, Let's run it again!")
    print("Using the code you provided! Let's re-run the program and start again!")
if fui != 'yes':
    print("\nWell,my services are completed! I have applied my current knowledge to allow not only myself to improve my data, but also allow the user to add thier own data.")
    print("I am always improving, but for my first project, I'm glad for my progress.")
    print("Thank you for your dedication, and have an amazing time!")
    