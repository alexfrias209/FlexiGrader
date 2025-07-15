# Welcome the user to the project and explain
print("Welcome!")
print("The purpose of this is to help you find your next read by answering a few couple of questions.")
read = input("Do you enjoy reading books on a budget?")
print("A Yes",
      "B No")

read = input()
if read == "A":
    print("Please continue to answer this form.")
    print()
else:
    print("Thank you for participating in this. Feel free to purchase any or all options below.")
    print()
# Make them choose their favorite book genre
print("What is your favorite book genre from the list?")
genre = ["Thriller", "Romance", "Fantasy/Science Fiction", "Crime"]
print("1", genre [0])
print("2", genre [1])
print("3", genre [2])
print("4", genre [3])
print()
genre = input("Enter your choice here (1/2/3/4):")
print()
# allow them to choose the amount of pages they want to read
print("Select the average amount of pages you want your book to contain.")
pages = ["0-250", "300-450", "500-1000"]
print("A", pages [0])
print("B", pages [1])
print("C", pages [2])
print()
#proide the user with options on what to read
pages = input("Enter your choice here (A/B/C):")
print()
while True:
    if genre == "1" and "A":
        print("'Animal Farm' by George Orwell (144 pages)")
        print("'The Family Across The Street' by Nicole Trope (240 pages)")
        print("'They All Had A Reason' by Michele Lesthers (211 pages)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in thsi project, I hope you enjoy your next read!')
        break
    
    elif genre == "1" and "B":
        print("'They Both Die At The End' by Adam Silvera (416 pages)")
        print("'I am Always Watching you' by teresa Driscoll (300 pages)")
        print("'We Were Never Here' by Andrea Bartz (350 pages)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in thsi project, I hope you enjoy your next read!')
        break
   # include the bar graph to show the population percent of people picking a certain genre 
    elif genre == "1" and "C":
        print("'All The Light We Cannot See' by Anothony Doerr (544 pages)")
        print("'The Institute' by Stephen King (576 pages)")
        print("'Crime and Punishment' by Fyodor Dostoevsky (720 pages)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in thsi project, I hope you enjoy your next read!')
        break
    # Make sure to provide options for each category
    if genre == "2" and "A":
        print("'Flipped' by Wendeline Van Draanen (256 pages)")
        print("'A Walk To remember' by Nicholas Sparks (240 pages)")
        print("'The Lost Daughter' by Elena Ferrante (144 pages)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in thsi project, I hope you enjoy your next read!')
        break
    # Make sure to provide options for each category
    elif genre == "2" and "B":
        print("'The Girl Who Lied' by Sue Fortin (384 pages)")
        print("'Begin Again' by Emma Lord (352 pages)")
        print("'The Fault In Our Stars' by John Green (313 pages)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in thsi project, I hope you enjoy your next read!')
        break
    # Make sure to provide options for each category
    elif genre == "2" and "C":
        print("'Gone With The Wind' by margaret mitchell (1037 pages)")
        print("'A shadow In The Ember' by Jennifer L. Armentrout (647 pages)")
        print("' Daughter Of No Worlds (The War Of Lost Hearts)' by Carissa Broadbent (518 pages)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in this project, I hope you enjoy your next read!')
        break
    # Make sure to provide options for each category
    if genre == "3" and "A":
        print("'City And The Stars' by Arthur C. Clarke (256 pages)")
        print("'The Time Machine' by H. G. Wells (114 pages)")
        print("'A Wrinkle In Time' by Madeleine L'Engle (256 pages)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in this project, I hope you enjoy your next read!')
        break
    # Make sure to provide options for each category
    elif genre == "3" and "B":
        print("'A Natural History Of Dragons' by Marie Brennan (352 pages)")
        print("'Space Opera' by Catherynne M. Valente (304 pages)")
        print("'The Broken Sword' by Poul Anderson (288 paes)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in this project, I hope you enjoy your next read!')
        break
    # Make sure to provide options for each category
    elif genre == "3" and "C":
        print("'The Red Mars' by Kim Stanley Robinson (640 pages)")
        print("'The Stand' by Stephen King (1,152 pages)")
        print("'pandemic' by A. G. Riddle (722 pages)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in this project, I hope you enjoy your next read!')
        break
    # Make sure to provide options for each category
    if genre == "4" and "A":
        print("'American Fire' by Monica Hesse (272 pages)")
        print("'Before He kills' by Mackenzie White (166 pags)")
        print("'The Red Parts' by Maggie Nelson (224 pages)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in thsi project, I hope you enjoy your next read!')
        break
    # Make sure to provide options for each category
    elif genre == "4" and "B":
        print("'The Fact Of A Body' by Alexandria Marzano-Lesnevich (336 pages)")
        print("'Furious Hours' by Casey Cep (352 pages)")
        print("'Bad Blood' by John Carreyrou (400 pages)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in this project, I hope you enjoy your next read!')
        break
    
    elif genre == "4" and "C":
        print("'We Keep The Dead Close' by Becky Cooper (512 pages)")
        print("'The Mammoth Book of True Huntings' by Peter Haining (544 pages)")
        print("'The Poppy War' by Rebbecca F. Kuang (544 pages)")
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Thriller', 'Romance', 'Fantasy/Science Fiction', 'Crime']
        y_axis = ['0', '13.33', '43.33', '26.67', '16.67']
        plt.bar(x_axis, y_axis)
        plt.title('favorite Genre Data')
        plt.xlabel('Genre')
        plt.ylabel("percentage")
        plt.show()
        print()
        print('Thank you for participating in this project, I hope you enjoy your next read!')
        # thank the user for completing this form
        break

