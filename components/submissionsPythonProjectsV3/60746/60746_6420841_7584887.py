import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.geometry('600x600')

questions = [" What UC are you In? "," What is the name of the UCM mascot?"," what year was UCM Founded?","What rank is the University at between the UC's?","Where is the University located?","What is the acceptance rate?","Would you like to play the game again?"]
options = [['UC Merced','UC Riverside','UC Davis','UC LA','UC Merced'],['Doggo','Rufus','Hunter','Bean','Rufus'],['2000','2003','2004','2005','2005'],
['8th','4th','5th','6th','5th'],['The Bay','The central valley','The LA county','The south','The central valley'],['90.9%','83.7%','50.7%','86.6%','86.6%'], ['Yes','No','Later','Some other time', 'Yes']]


frame = tk.Frame(root, padx=15, pady=10,bg='red')
question_label = tk.Label(frame,height=7, width=28,bg='black',fg="white", 
                          font=('Verdana', 30),wraplength=500)

#stucutre of questions and formates
v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

index = 0
correct = 0

#adding radiobuttons and formating 
option1 = tk.Radiobutton(frame, bg="Black", variable=v1, font=('Verdana', 20),
                         command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="Black", variable=v2, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="Black", variable=v3, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="Black", variable=v4, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option4))

button_next = tk.Button(frame, text='Next',bg='white', font=('Verdana', 20), 
                        command = lambda : displayNextQuestion())

frame.pack(fill="y", expand="true")
question_label.grid(row=0, column=0)

#Postion of the answers given 
option1.grid(sticky= 'n', row=1, column=0)

option2.grid(sticky= 'n', row=2, column=0)

option3.grid(sticky= 'n', row=3, column=0)

option4.grid(sticky= 'n', row=4, column=0)

button_next.grid(row=6, column=0)

#what question you start off in and how many points you start with as well
#index = 0 
#correct = 0
# function to disable radiobuttons 
def disableButtons(state):
    option1['state'] = state
    
    option2['state'] = state
    
    option3['state'] = state
    
    option4['state'] = state

# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    
   #if radio == option1:
    #    clear_selection_v1()
    #elif radio == option2:
     #   clear_selection_v2()
    #elif radio == option3:
     #   clear_selection_v3()
    #elif radio == option4:
     #   clear_selection_v4()
    # the 4th item is the correct answer
    # we will check the user selected answer with the 4th item
    if radio['text'] == options[index][4]:
        correct += 1

    #index = 0
    #correct = 4
    index +=1
    disableButtons('disable')

#def clear_selection_v1():
 #   v2.set(None)
  #  v3.set(None)
   # v4.set(None)

#def clear_selection_v2():
 #   v1.set(None)
  #  v3.set(None)
   # v4.set(None)
    
#def clear_selection_v3():
 #   v2.set(None)
  #  v1.set(None)
   # v4.set(None)
    
#def clear_selection_v4():
   # v2.set(None)
    #v3.set(None)
    #v1.set(None)



# create a function to display the next question
def displayNextQuestion():
    global index, correct
    
    #checkAnswer = ('true')

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'black'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/2:
           question_label['bg'] = 'green'
       else:
            question_label['bg'] = 'red'





    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check the Results'


       # index += 1


displayNextQuestion()

root.mainloop()