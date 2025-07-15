name_for_order = input("Thank you for choosing starbucks I am XXXX, \nmay I have the name for the order? \n")
hotorcold = input("\n Hello "+ name_for_order + ","" Would you like a hot \ndrink, or a cold drink? \n")
while hotorcold != "hot drink" and hotorcold != "cold drink":
  print("Sorry, I didn't understand that. Please try again.")
  hotorcold = input("Would you like a hot drink, or a cold drink? \n")
  print ("Thank you for your cooperation")
if hotorcold == "hot drink":
      Hsweetorunsweet = input ("Would you like a sweet or an unsweet drink? \n")
elif hotorcold == "cold drink":
  Csweetorunsweet = input ("Would you like a sweet or a unsweet drink? \n")
else:
  print ("Sorry, I didn't understand that. Please try again.")
Hsweetorunsweet = ""
while Hsweetorunsweet != "sweet drink" and Hsweetorunsweet != "unsweet drink":
  print("Sorry, lets try again.")
  Hsweetorunsweet = input ("Would you like a sweet or a unsweet drink? \n") 
  print ("Thank you for your cooperation that will be an excelent choice!")
                           
if Hsweetorunsweet == "sweet drink":
  sweet_drink = input("We currently have: \nCaramel apple spice, \nBlonde smoked butterscotch latte, \nChai latte, \nWhite chocolate mocha Frappuccino. \nWhich one would you like? \n")

elif Hsweetorunsweet == "unsweet drink":
  unsweet_drinks= input("We currently have: \nIced Black Tea Lemonade, \nIced Chai Latte, \nMatcha Crème Frappuccino, \nDragon Drink, \nIced Brown Sugar Oatmilk Shaken Espresso.")

else: 
  print("Sorry, we do not have that at this moment.")
  
while Csweetorunsweet != "sweet drink" and Csweetorunsweet != "unsweet drink":
  print("Sorry, lets try again.")
  Csweetorunsweet = input ("Would you like a sweet or a unsweet drink? \n") 
  print ("Thank you for your cooperation that will be an excelent choice!")
 
#drinks = {"Caramel apple spice": 5.45, 
          #"Blonde smoked butterscotch latte": 5.75, 
          #"Chai latte": 5.45, 
          #"White chocolate mocha Frappuccino": 5.35}

#print(drinks.get("Chai latte"))   
#else: hotorcold != "hot" or "cold"':'
#print("Please try again.")
#while True:
        #print("Please try again.")
      
#hotorcold = input("Would you like a hot drink, or a cold drink?")

  #hot_drinks = input("That is a great choice. We currently have \n Americano, \n Flat white, \n Pumpkin spice latte, \n Caffe Mocha, \n Caramel apple spice.")
    
      #if hot_drinks == Americano


#f = open("Hotdrinks.txt", "r")
#file_content = f.read()
#f.close()
#print(Hotdrinks)
#for line in f:
  #print(line)
