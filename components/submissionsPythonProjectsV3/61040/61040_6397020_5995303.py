import csv
sex = []
height = []
size = []
#opens file and puts everything into lists.
with open('61040_6397022_5718946.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        sex.append(row[1])
        height.append(row[2])
        size.append(row[3])

#this gets rid of titles
mainlist = []
sex = sex[1:]
height = height[1:]
size = size[1:]
#appends everything to one big list.
for index in range(len(sex)):
    mainlist.append([sex[index],height[index],size[index]])



# function to find averages by sex
def sexcolavg(column, list, sex):
    count = 0
    total = 0
    for item in list:
        if (item[0] == sex):
            total += float(item[column])
            count += 1
    return total /count
   #user selection Menu     
print('''Hello, my name is aiden jemelian and my projecct is about reading shoe
sizes from a CSV file and compairing them. It shows the average height and shoe size
between men and woman, in EU sizes.''')

print("""\nwhat would you like to find out about:
         A: Average men's size and height
         B: Average Woman's size and height
         C: Add your height and shoe size to the list
         I: US to EU size chart
         X: Exit Program""")
select = input('\n Make your selection ')
#operates selections
while select != 'X':
    if select == 'A':
        print("you have selected men's size and height")
        print('The average Male shoe size is', round(sexcolavg(2, mainlist, "man"), 2))
        print('The average Male height is', round(sexcolavg(1, mainlist, "man"), 2))

    elif select == 'B':
        print("you have selected woman's size and height")
        print('The average female shoe size is', round(sexcolavg(2, mainlist, "woman"), 2))
        print('The average female height is', round(sexcolavg(1, mainlist, "woman"), 2))
    elif select == 'C':
        print("you have selected to add your shoe size and height to the list")
        sizeinput = input('''\nWhat is your sex (man, woman), what is your height(in cm), and what is
              your shoe size(in EU size) please seperate each value by space ''')
        datainput = sizeinput.split(' ')
        datainput.insert(0,'na')   #puts a na on the column we are not using

        with open ("61040_6397022_5718946.csv", 'a', newline = '') as csvfile:           # Writes the user data to the CSV file
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(datainput)
        #size conversion chart       
    elif select == 'I':
        print(''' US mens size/ US womans size          EU size
                    3.5/5                               35
                    4/5.5                               35.5
                    4.5/6                               36
                    5/6.5                               37
                    5.5/7                               37.5
                    6/7.5                               38
                    6.5/8                               38.5
                    7/8.5                               39
                    7.5/9                               40
                    8/9.5                               41
                    8.5/10                              42
                    9/10.5                              43
                    10.5/12                             44
                    11.5/13                             45
                    12.5/14                             46.5
                    14/15.5                             48.5''')

    else:
        print('INVALID INPUT!!!')
    select = input('\n Make your selection ')
      
print('You have exited the program')
