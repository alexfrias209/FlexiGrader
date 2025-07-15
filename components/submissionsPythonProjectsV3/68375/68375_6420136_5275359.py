import matplotlib.pyplot as plt
print("Welcome to the UCM Club Finder Project. This project will help students find clubs and organizations that match their interests.")

print("Please choose one of the following traits/feelings that correlates to you:")
# Creating List for choices
choices = ["Anger","Creative","Sadness","Talkative"]
#list, all choices/subchoices
sub_choices_1 = ["physical aggression", "frustration", "rage"]
sub_choices_2 = ["Visual Artistry","Musical Creativity","Innovative"]
sub_choices_3 = ["Loss and Greif", "Withdrawal","Loneliness"]
sub_choices_4 = ["Public Speaking", "Persuasion","Narrative Skills"]
emotion = ""
sub_emotion = ""
#defining variable as empty string

def getsubchoices (s):
  for i in range (len (s)):
    print(i+1,s[i])
  user_input_subchoice = input()
  if int(user_input_subchoice)-1 > len(s) or int(user_input_subchoice)-1 < 0:
    print("Invalid choice. Please try again.")
    exit()
  return (int(user_input_subchoice)-1)
#creating a function to get user sub choice index

def getclub (choice, subchoice):
  file1 = open("68375_6420138_582823.txt", "r")
  lines = file1.readlines()
  linesplit = lines[choice].split(",")
  #split function splits by commas
  return linesplit[subchoice]
#creating a function to get club output from ClubNames.txt file

def getresults (fileName):
  emotion1 = {}
  emotion2 = {}
  clubName = {}
  file1 = open(fileName, "r")
  lines = file1.readlines()
  for line in lines:
#creating a function to print results from ClubNames.txt file
    linesplit = line.split("...")
    if(len(linesplit) != 3):
      continue
    linesplit[0] = linesplit[0].strip()
    linesplit[1] = linesplit[1].strip()
    linesplit[2] = linesplit[2].strip()
    if linesplit[0] in emotion1:
      emotion1[linesplit[0]] += 1
    else:
      emotion1[linesplit[0]] = 1
    if linesplit[1] in emotion2:
      emotion2[linesplit[1]] += 1
    else:
      emotion2[linesplit[1]] = 1
    if linesplit[2] in clubName:
      clubName[linesplit[2]] += 1
    else:
      clubName[linesplit[2]] = 1
  return (emotion1, emotion2, clubName)
  #split function splits by commas

def createBarGraph(data): 
  names = list(data.keys())
  values = list(data.values())
  plt.bar(range(len(data)), values, align='center', tick_label=names)
  plt.xticks(rotation=45, ha="right")
  plt.rcParams["figure.figsize"] = (10, 5)
  plt.show()


for i in range (len (choices)):
  print(i+1,choices[i])
user_input_choice = input()
#printing out the choices and getting user input
#print(user_input_choice)
match user_input_choice:
#goes to one of the cases based on the number chosen for choices (similar to if statement)
  case "1":
    user_input_subchoice = getsubchoices (sub_choices_1)
    #when line 31 executes goes to line 15
    print(choices[int(user_input_choice)-1])
    sub_emotion = sub_choices_1[int(user_input_subchoice)]
    print(sub_emotion)
    a = getclub (int(user_input_choice)-1, int(user_input_subchoice))
    print("The club that matches your traits is:", a)
    #Gives sub choices based on the choice the user picked, then prints out the club that matches the choice/subchoice
  case "2":
    user_input_subchoice = getsubchoices (sub_choices_2)
    print(choices[int(user_input_choice)-1])
    sub_emotion = sub_choices_2[int(user_input_subchoice)]
    print(sub_emotion)
    a = getclub (int(user_input_choice)-1, int(user_input_subchoice))
    print("The club that matches your traits is:", a)
  case "3":
    user_input_subchoice = getsubchoices (sub_choices_3)
    print(choices[int(user_input_choice)-1])
    sub_emotion = sub_choices_3[int(user_input_subchoice)]
    print(sub_emotion)
    a = getclub (int(user_input_choice)-1, int(user_input_subchoice))
    print("The club that matches your traits is:", a)
  case "4":
    user_input_subchoice = getsubchoices (sub_choices_4)
    print(choices[int(user_input_choice)-1])
    sub_emotion = sub_choices_4[int(user_input_subchoice)]
    print(sub_emotion)
    a = getclub (int(user_input_choice)-1, int(user_input_subchoice))
    print("The club that matches your traits is:", a)
  case _:
    print("Please enter a valid choice.")
    exit()
#prints out subchoices based on the choice chosen by user, if correct choice not chose, will go to line 110 (prints out "Please enter a valid choice")


emotion = choices[int(user_input_choice)-1]
f = open("68375_6420138_582823.txt", "a")
f.write(f"{emotion}...{sub_emotion}...{a}\n")
f.close()
e1, e2, cn = getresults("68375_6420138_582823.txt")
#opens file and writes the choice and subchoice and club into the file
createBarGraph(e1)
createBarGraph(e2)
createBarGraph(cn)
#creates bar graphs for emotions and clubs




