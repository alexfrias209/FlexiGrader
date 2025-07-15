import math
import statistics
from statistics import quantiles
import csv 
from csv import reader



#welcome message 
welmess = print('Welcome to the statistics calculator! ')
print('______________________________________________________________________')
print('please follow the instructions below!')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')   




#Data collection
user_input = []
n = input('How many data points are you inputing: ')
digit = n.isdigit()

    
while digit == False or int(n) < 2:
    print('Invalid quantity. Please input at LEAST 2 numerical data points.')
    print('______________________________________________________________________')
    n = input('How many data points are you inputing: ') 
    digit = n.isdigit()
    

n = int(n)
    
for i in range(0,n):
    num = input()
    
    numcheck = num.isdigit()
    while numcheck == False: 
        num = input('INVALID INPUT. Please input a numerical Value:  ')   
        numcheck = num.isdigit()
    if numcheck == True:
       num = float(num) 
       user_input.append(num) 
    else:
        print('Try Again.')
    
    




#setting condition for while loop + while loop
ans = 'y'
while ans.lower() == 'y' :
    
    #prints out sorted list
    user_input.sort()
    print('______________________________________________________________________')
    print('here is your data: ', user_input)
    print('______________________________________________________________________ \n')

    #calculator/ calculations
    calc_type = input('choose calculation type: \n1.mean \n2.median \n3.mode \n4.Standard Deviation \n5.set sample data as values \n6.Choose new Data \n \nInput selection number: ', )
    ctc = calc_type.isdigit()
  
   
    while ctc == False:
        print('Invalid input, please select "y" and pick a number from 1-6... ')
        ctc == calc_type.isdigit()
        if ctc == True:
            calc_type = int(calc_type)
        else:
            print('')
        break
    
        
    
    mean = float(sum(user_input)/n)
    meanform = "{:.2f}".format(mean)
    
    med_even = float(((n/2)+((n+1)/2)))
    evenform = "{:.2f}".format(med_even)
    
    med_odd = float((n+1)/2)
    oddform = "{:.2f}".format(med_odd)
    
    med = float(statistics.median(user_input))
    medform = "{:.2f}".format(med)
    
    mode = float(statistics.mode(user_input))
    
    std = float(statistics.stdev(user_input))
    stdform = "{:.2f}".format(std)
    
    
    
    #calculation options
    if calc_type == int(1):  #mean 
        print('The mean of the data is ', meanform)
    elif calc_type == int(2): #median
        print('The median of the data is ', medform)
    elif calc_type == int(3): #mode
        print('the mode of the data is ', mode)
    elif calc_type == int(4): #standard deviation
        print('The Standard Deviation of the data is ', stdform)
    elif calc_type == int(5): #load external data as list value
        user_input.clear()
        with open('C:\\Users\\itsyo\\Documents\\pyvalues.csv') as file:
            lines = file.read().split('\n')
            for item in lines[1:]:
                if item != '':
                    user_input.append(float(item))    
        print('Sample data loaded. Values have been updated... ')
    elif calc_type == int(6): #set new user defined values
        print('______________________________________________________________________')
        user_input.clear()
        n = input('How many data points are you inputing: ')
        digit = n.isdigit()

        while digit == False or int(n) < 2:
            print('Invalid quantity. Please input at LEAST 2 numerical data points.')
            print('______________________________________________________________________')
            n = input('How many data points are you inputing: ') 
            digit = n.isdigit()
        n = int(n)
        
        for i in range(0,n):
            num = input()
            numcheck = num.isdigit()
            while numcheck == False: 
                num = input('INVALID INPUT. Please input a numerical Value:  ')   
                numcheck = num.isdigit()
            if numcheck == True:
                num = float(num) 
                user_input.append(num) 
                user_input.sort()    
            else:
                print('') 
                      
        
            
        print('______________________________________________________________________')
        print('Selected Values have been updated!')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')      
     
    
     
    #Calculation final option (reloop/break)       
    ans = input('do a different calculation? \n(y/n): ')
    while ans != 'y' and ans != 'n':
        ans = input("invalid input select (y/n): ")
         
    if ans == 'y':
        print()
    elif ans == 'n':
        print('Program Aborted...')
        break
    
        
