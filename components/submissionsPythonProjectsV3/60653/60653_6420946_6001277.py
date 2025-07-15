import os
import time
import csv
import matplotlib.pyplot as plt
import numpy as np

def intro_prompt(name_of_user):
    print(f"Welcome to the project {name_of_user}!\n\nMy name is {coder} and my project for ME 021 is to create a 'Product Analyzer'.\n")
    print(f"This project will require me to create a csv file that has a product names, number of sales for the products, and the year when those sales were made.")
    print(f"This will allow you, the user, to see the history of purchases of the product to see if sales are declining or rising.\n\nPretty cool right?\n")
    print(f"Well {name_of_user}, I only have 2 csv files for this project, and I figured out how to make graphs so this project should be interesting.")
    print(f"\n\nEnjoy!\n\n")
    #I just converted my initial intro_Prompt to this so I could meet the modularity requirement
    return 0

def file_opener(filename):
    information = []
    if filename == "Coca Cola":
        #https://www.statista.com/statistics/264423/revenue-and-financial-results-of-coca-cola/
        #Source above ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        file = open('60653_6420948_2687251.csv', 'r')
        for line in file:
            information += line.split(',')
        file.close()
        return information
    elif filename == "iPhone":
        #https://www.globaldata.com/data-insights/technology--media-and-telecom/annual-sales-of-apples-iphone/
        #Source above ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        file = open('60653_6420947_1900059.csv', 'r')
        for line in file:
            information += line.split(',')
        file.close()
        return information
    #this section isn't finished yet but the first two are for a proof of concept


def line_graph_maker(x_axis, y_axis, product):
    #This is to convert my list of strings into a list of integers
    x = [eval(i) for i in x_axis]
    y = [eval(i) for i in y_axis]
    #This prepares the line graph to be made using the x and y lists
    fig, ax = plt.subplots()

    plt.xlabel('Year')

    plt.ylabel('Sales in Millions $')

    plt.title(f'Sales over the Years for {product}')

    ax.plot(x, y, color = 'green', linewidth = 5 , marker = 'o', markerfacecolor = 'black', markersize = 12)
    return plt.show()

def bar_graph_maker(x_axis, y_axis, product):
    #This converts my list of strings to lists of integers so that matplot lib can properly function
    x = [eval(i) for i in x_axis]
    y = [eval(i) for i in y_axis]

    fig, ax = plt.subplots()

    plt.xlabel('Year')

    plt.ylabel('Sales in Millions $')

    plt.title(f'Sales over the Years for {product}')
    plt.bar(x,y, color = 'red')

    return plt.show()

#Now that I'm done defining stuff, the code can actually start
os.system('cls')


#Welcome the user to the project
coder = "blah"

name_of_user = input('Please enter your username to access[At least 1 character]: ')
os.system('cls')

#This if statement is just to check if they entered something for the username, if not, then the code will kill itself and you have to start it again
if len(name_of_user) > 0:
    intro_prompt(name_of_user)
else:
    print(f"Please run the code again and enter a VALID input(Anything but leaving the prompt blank)")
    print("\n\nExiting in 3 seconds.....")
    time.sleep(3)
    exit()


#Start to simulate how the Menus will look like in the terminal
ready = input('Type 1 to start|Type Anything Else to exit: ')

if ready == '1':
    raw_data = []
    while ready == '1':
        os.system('cls')
        products = ['iPhone', 'Coca Cola']
        print(f"Great choice {name_of_user}! Let's get started.....\n\n")

        product_choice = input('Please type in the name of one of the products shown in this list.....[iPhone, Coca Cola]\n\nYour choice here(Case Sensitive): ')
        
        ready_again = 0
        if product_choice in products:
            ready_again = 1
            while ready_again == 1:
                os.system('cls')

                raw_data = file_opener(product_choice)
                years = []
                sales = []
                sales_value = []
                true_sales = []


                line = 0
                for line in range(len(raw_data)):
                    if '\n' in raw_data[line]:
                        sales += raw_data[line].split(',')
                    else:
                        years += raw_data[line].split(',')
            
                for line in range(len(sales)):
                    sales_value += sales[line].split('\n')
            
                for line in range(len(sales_value)):
                    if sales_value[line] != '':
                        true_sales += sales_value[line].split(',')


                print(f"Thanks {name_of_user}!\n\nYou have selected: {product_choice}\n\nPlease enter the type of graph which you wish to see the sales for of {product_choice}\n\nI only have sales data from {years[0]} to {years[-1]}\n\nYou can select from [Bar Graph, Line Graph]")
            
                graph_selected = input('Enter the visualization format here(Case Sensitive): ')

                if graph_selected == "Line Graph":
                    line_graph_maker(years, true_sales, product_choice)
                elif graph_selected == "Bar Graph":
                    bar_graph_maker(years, true_sales, product_choice)
                else:
                    print(f"\nPlease select a valid choice from the list provided(Wait 5 seconds for reset).")
                    time.sleep(5)
                    continue

                print(f"\nI hope you enjoyed my project {name_of_user}!!!\n\n")
                finished = input('Type 1 to try another product, Type anything else to leave: ')
                if finished == '1':
                    print(f"\n\nGoing back to the beginning in 5 seconds....")
                    time.sleep(5)
                    break
                else:
                    print(f"Goodbye {name_of_user}.\nExiting in 5 seconds.....")
                    time.sleep(5)
                    os.system('cls')
                    exit()
            if finished == '1':
                continue

        else:
            print(f"\nPlease select a valid choice from the list provided(Wait 5 seconds for reset).")
            time.sleep(5)
            continue
    

else:
    os.system('cls')
    print(f"Goodbye {name_of_user}.....")
    time.sleep(5)
    os.system('cls')