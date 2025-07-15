print("welcome to Cave Quest by Luis Santiago")

items = ["Lantern", "Stick", "Boomerang"]

Backpack = items

print("You found a dark cave that you soon enter.")


while True:
    while True:
        print("Backpack: ", Backpack) #Good way to give correct input
        choice = input("The cave is dark from what you can see and there a cavern you see some vines what do you do: ")
        if choice == "Boomerang":
            print("The Boomerang snag the vine to you, You use the vine to swing acroos it snap of one you in the other side. You see a way further, you enter another cavern")
            items.append("Vine")
            break
        elif choice == "Stick":
            print("You try to grab the vine with the stick and can't reach. You thought of throwing it but it a nice stick.")
        elif choice == "Lantern":
            print("You put the lantern in front of you, the vine look far to reach maybe something can help reach it")
        else: # Doesn't need to be complicate
            print("Nothing happen")
    while True:
        #have no idea if putting it above would affect it
        print("Backpack: ", Backpack)
        choice = input("You enter further in the cave their seem to be a way further up a ledge what do you do: ")
        if choice == "Boomerang":
            print("You threw the Boomerang and it hit the ledge falling back in front of you. You pick it up from the floor.")
        elif choice == "Stick":
            print("You use the stick to get leverage to climb up the ledge you venture further")
            break
        elif choice == "Lantern":
            print("You put the lantern in front of you, the wall below the ledge is made of a smooth stone it would be hard to climb as is.")
        else:
            print("Nothing happen") 
    while True:
        print("Backpack: ", Backpack)
        choice = input("The you enter a crystal room with reflective glass piller. You see a way out but it block by the piller: ")
        if choice == "Boomerang":
            print("The Boomerang hit the glass and it chip it a little. The amount of time it would take to break make this not worth energy.")
        elif choice == "Stick":
            print("The Stick hit the glass and it chip it a little. The amount of time it would take to break make this not worth the time.")
        elif choice == "Lantern":
            while True: #Puzzel chain where an item need to be use to move forward in a room
                print("Backpack: ", Backpack)
                choice = input("You put the lantern in front of you, the glass reflect the light show a loss boulder up a ledge what do you do: ")
                if choice == "Boomerang":
                    print("You threw the Boomerang and it hit the ledge falling back in front of you. You pick it up from the floor.")
                elif choice == "Stick":
                    print("You use the stick to try and get leverage to climb up the ledge but the cliff is to tall and thier no leverage.")
                elif choice == "Lantern":
                    print("You put the lantern in front of the cliff. You notice no climable surfice but a rock, something can snag on.")
                elif choice == "Vine":
                    while True:
                        print("Backpack: ", Backpack)
                        choice = input("You threw the vine to try and snag something. You use the vine as a rope up. The boulder is in front of you: ")
                        if choice == "Boomerang":
                            print("You threw the Boomerang and it hit the boulder falling back in front of you. You pick it up from the floor.")
                        elif choice == "Stick":
                            print("You use the stick to try and get leverage to push the boulder. It work, the glass break. You pick up a piece of glass and it sharp and reflect. You move forward.")
                            items.append("Glass")
                            break
                        elif choice == "Lantern":
                            print("You put the lantern in front of the boulder. You notice a small hole not block by the boulder.")
                        elif choice == "Vine":
                            print("You whip the boulder. It did nothing.")
                        else:
                            print("Nothing happen")
                    break        
                else:
                    print("Nothing happen")
                break # To exit loop
        else:
            print("Nothing happen")
        break
    while True:
        print("Backpack: ", Backpack)
        choice = input("You find yourself in a room filled with foliage. You think you see a way forward bit it block by foliage: ")
        if choice == "Boomerang":
            print("You threw the Boomerang at the foliage. It get stuck in it. You pick it back up.")
        elif choice == "Stick":
            print("You use the stick to push the plant. Thier to much foliage to push back")
        elif choice == "Lantern":
            print("You put the lantern in front of you, You see that the foliage are like roses full of thorns.")
        elif choice == "Glass":
            print("You use the Glass to cut the foliage the path forward is now passable.")
            break
        else:
            print("Nothing happen") 
    while True:
        print("Backpack: ", Backpack)
        choice = input("You enter further in the cave their seem to be a dead end you can't see a way to move forward: ")
        if choice == "Boomerang":
            print("You threw the Boomerang at the wall. It bounced back and hit you in the head. -1HP")
        elif choice == "Stick":
            print("You where about to use the stick but you stop because of the possibility it would break.")
        elif choice == "Lantern":
            print("You put the lantern in front of you, you notice a different color rock you press it and a way further apearts. You enther further in.")
            break
        else:
            print("Nothing happen") 
    while True:
        choice = input("The cavern is empty but you see a light up ahead it the other side of the caves. 'Leave': ")
        if choice == "Leave":
            print("You left the cave.")
            break
        else:
            print("Nothing happen")
    break
        
print("Thanks for playing")# end program

