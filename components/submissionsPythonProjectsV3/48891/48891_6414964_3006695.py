
print("Welcome to your contact book!\n Developed by Juan Alvarado\n Lets contact someone")
def options():
    
    print("\t1. Find contact")
    print("\t2. Create a new contact")
    print("\t3. Delete a contact")
    print("\t4. Modify a contact")
    print("\t5. Exit")


    

x = "0"


print("Please choose one of the following:")

while x != "5":
    if x != "0":
        print("Would you like to do something else?")
    options()
    x = input("What would you like to do? (1, 2, 3, 4, or 5): \n")
    
    if x == "1":
        t = 0
        h = input("Who's contact are you looking for? \n")
        
        with open("48891_6414963_8848678.txt", "r") as file1:
            for line in file1:
                mini = line.split("\t")
                if mini[0] == h:
                    t += 1
                    print(line)
        
        if t == 0:
            print("Contact does not exist\n")
    elif x == "2":
        a = input("What is the name of your new contact?\n")
        b = input("What is the phone # of your new contact?\n")
        c = input("What is their affiliation?\n")

        with open("48891_6414963_8848678.txt", "a") as file2:
            newline = str(f'\n{a}\t{b}\t{c}')
            file2.write(newline)
        
        
        print("Your new contact has been added!")
        
    elif x == "3":
        
        d = input("Who would you like to Delete?\n")
        with open("48891_6414963_8848678.txt", "r") as file3:
            
            lines = file3.readlines()
 
            with open('48891_6414963_8848678.txt', 'w') as f3:
                
                for line in lines:
                    smol = line.split('\t')
                    if smol[0] != d:
                        f3.write(line)
                
        print("Your contact has been deleted!\n")

        
    elif x == "4":
        e = input("Who would you like to modify?\n")
        t = 0
        with open("48891_6414963_8848678.txt", "r") as file1:
            for line in file1:
                mini = line.split("\t")
                if mini[0] == h:
                    t += 1
        
        if t == 0:
            print("Contact does not exist\n")
        else:    
            y = input("Options:\n\t1.Name\n\t2.phone #\n\t3.affilitaion\nWhat would you like to modify?(1, 2, or 3):\n")
            if y == "1":
                f =input("Enter your contact's new name:")
                with open("48891_6414963_8848678.txt", "r") as j1:
                    for line in j1:
                        save2 = line.split("\t")
                        if save2[0] == e:
                            a2 = save2[1]
                            b2 = save2[2]
                
                with open("48891_6414963_8848678.txt", "r") as file5:
            
                    lines2 = file5.readlines()
                
                
                    with open('48891_6414963_8848678.txt', 'w') as f5:
                
                        for line in lines2:
                            smol2 = line.split('\t')
                            if smol2[0] != e:
                                f5.write(line)
                with open('48891_6414963_8848678.txt', 'a') as g2:
                    newline = str(f'\n{f}\t{a2}\t{b2}')
                    g2.write(newline)
                print("Your contact has been successfully modified!")
            
            elif y == "2" :
                g = input("Enter your contact's new phone Number:")
                with open("48891_6414963_8848678.txt", "r") as j1:
                    for line in j1:
                        save2 = line.split("\t")
                        if save2[0] == e:
                            a2 = save2[0]
                            b2 = save2[2]
                
                with open("48891_6414963_8848678.txt", "r") as file5:
            
                    lines2 = file5.readlines()
                    
                
                    with open('48891_6414963_8848678.txt', 'w') as f5:
                
                        for line in lines2:
                            smol2 = line.split('\t')
                            if smol2[0] != e:
                                f5.write(line)
                    with open('48891_6414963_8848678.txt', 'a') as g2:
                        newline = str(f'\n{a2}\t{g}\t{b2}')
                        g2.write(newline)

                print("Your contact has been successfully modified!")
           
            elif y == "3":
                h = input("Enter your contact's new affiliation:")
                with open("48891_6414963_8848678.txt", "r") as j1:
                    for line in j1:
                        save2 = line.split("\t")
                        if save2[0] == e:
                            a2 = save2[0]
                            b2 = save2[1]
                
                with open("48891_6414963_8848678.txt", "r") as file5:
            
                    lines2 = file5.readlines()
                
                
                    with open('48891_6414963_8848678.txt', 'w') as f5:
                
                        for line in lines2:
                            smol2 = line.split('\t')
                            if smol2[0] != e:
                                f5.write(line)
                with open('48891_6414963_8848678.txt', 'a') as g2:
                    newline = str(f'\n{a2}\t{b2}\t{h}')
                    g2.write(newline)
                    
                print("Your contact has been successfully modified!")
            
            else:
                print("Not a valid input\n")
        
    elif x== "5":
        break
    else:
        print("Not a valid input\n")
    
print("Have a good day!")

