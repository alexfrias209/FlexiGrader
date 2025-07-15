def color_calculator():
    print("Welcome to the Color Calculator!")
    print("Choose two primary colors from Red, Yellow, and Blue to see what they make.")
    print("Any of the codes you see can be put into https://www.color-hex.com")
    print("https://www.color-hex.com")
    
    # Define the primary colors and their hex codes
    primary_colors = {
        "Red": "#FF0000",
        "Yellow": "#FFFF00",
        "Blue": "#0000FF"
    }
    
    while True:
        # Get user input for the first color
        #capitalize make things upper casde and same for lower (makes it cleaner in my opinion)
        while True:
            color1 = input("Enter the first color (Red, Yellow, or Blue): ").capitalize()
            if color1 in primary_colors:
                break
            else:
                print("Invalid input. Please choose from Red, Yellow, or Blue.")
        
        # Get user input for the second color
        while True:
            color2 = input("Enter the second color (Red, Yellow, or Blue): ").capitalize()
            if color2 in primary_colors:
                break
            else:
                print("Invalid input. Please choose from Red, Yellow, or Blue.")
        
        # Calculate the secondary color
        if (color1 == "Red" and color2 == "Yellow") or (color1 == "Yellow" and color2 == "Red"):
            result = "Orange"
            hex_code = "#FFA500"
        elif (color1 == "Red" and color2 == "Blue") or (color1 == "Blue" and color2 == "Red"):
            result = "Purple"
            hex_code = "#800080"
        elif (color1 == "Yellow" and color2 == "Blue") or (color1 == "Blue" and color2 == "Yellow"):
            result = "Green"
            hex_code = "#008000"
        elif (color1 == "Yellow" and color2 == "Yellow"):
            result = "My recommended shades of yellow: #e5e500, #cccc00, #b2b200"
            hex_code = "#FFFF00"
            while True:
                see_more = input("Would you like to see more shades of Yellow? (yes/no): ").lower()
                if see_more == "yes":
                    print("#999900, #808000, #666600, #4c4c00")
                    break
                elif see_more == "no":
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        elif (color1 == "Blue" and color2 == "Blue"):
            result = "My recommended shades of blue: #0000e5, #0000cc, #0000b2, #000099, #00007f, #000066, #00004c"
            hex_code = "#0000FF"
            while True:
                see_more = input("Would you like to see more shades of Blue? (yes/no): ").lower()
                if see_more == "yes":
                    print("#000033, #000019, #000000")
                    break
                elif see_more == "no":
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        elif (color1 == "Red" and color2 == "Red"):
            result = "My recommended shades of red: #e50000, #cc0000, #b20000, #990000"
            hex_code = "#FF0000"
            while True:
                see_more = input("Would you like to see more shades of Red? (yes/no): ").lower()
                if see_more == "yes":
                    print("#800000, #660000, #4c0000")
                    break
                elif see_more == "no":
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            result = "Invalid combination"
            hex_code = None
        
        print(f"{color1} ({primary_colors[color1]}) + {color2} ({primary_colors[color2]}) = {result} ({hex_code})")
        
        # Ask if the user wants to calculate another combination
        #loop area 
        another_calculation = input("Do you want to calculate another color combination? (yes/no): ").lower()
        if another_calculation != "yes":
            break
    
    print("I hope you enjoyed using my app!")
    print("Please use anytime!!")

# Run the color calculator
color_calculator()
