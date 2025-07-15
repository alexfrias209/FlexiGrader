print("Welcome to my project, my name is Ibrahim Sayeed and this project will output the efficency of solar panels in varying conditions\n")
t = int(input("How many total hours of sunlight do the panels recieve a day?"))
p = int(input("What is the maximum output of your panel per hour? (W)"))
a = int(input("What is the total area? (M^2)"))
#d = input("What is the name of your data file? (end with .txt)")
##inputs theoretical data and real data
import json 

with open("59724_6489479_8478184.txt") as f: 
    data = f.read() 
data = json.loads(data)
## reads data file and turns it into a dict
powerSUM = 0
hoursSUM = 0
tally = 0
for key, value in data.items():
    hoursSUM = hoursSUM + int(key)
    powerSUM = powerSUM + value
    tally = tally + 1
## reads the dict created from data file and tallys the totals of power and sunlight hours in order to average multiple days of data

## sums values from data file and turns them into an int variable
def calculate(Pmax,Area):
    x = Pmax / Area
    return x
## calculates power per area
def KWH(sunlight, power):
    x = power * sunlight
    return x 
## calculates power per day by multiplying power by hour of sunlight
def efficency(t,d):
    return (t / d)
def avg():
    return ((powerSUM / tally) * (hoursSUM / tally))
## averages data from input data
print("Your data shows a power per day of " + str(avg()) + "KW")
choice = input("Enter true if you would like to calculate efficency")
if(choice == "true"):
    print("Your data shows an efficency of " + str((efficency(KWH(t,p),avg()) * 100)) + " percent compared to theoretical data")
choice = input("Enter true if you would like to calculate power per area from your data")
if(choice == "true"):
    print(calculate(powerSUM,a))
choice = input("Enter true if you would like to calculate theoretical power per day")
if(choice == "true"):
    print(KWH(t,p))
choice = input("Enter true if you would like to calculate theoretical power per area")
if(choice == "true"):
    print(KWH(p,a))
## several inputs to determine what data user would like to recieve, if statements check if the input is true to calculate and display the data using above functions




  


    


