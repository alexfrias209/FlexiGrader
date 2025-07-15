from PIL import Image

filename = "69587_6421973_3696433.PNG"
img = Image.open(filename)
img.show()

name = "empty"
bread_choice = "empty"
filling_flavor = "empty"
decoration_theme = "empty"

print("***Welcome to The Silly Goose Ordering Site!***")
print("Here, we will take your desired cake and turn it into with a few questions.")

orders = {}  # Initialize an empty dictionary to store orders

while True:
    order_cake = input(
        "\nWould you like to order a cake? (Press 1 for yes, 2 for no, 3 to check order): "
    )

    if order_cake == "2":
        print("Thank you for visiting The Silly Goose Co. Have a nice day!")
        break
    elif order_cake == "3":
        customer_name = input("Enter your name to retrieve your order: ")
        if customer_name in orders:
            order = orders[customer_name]
            print(f"Order details for {customer_name}:\n{order}")
            edit_order = input("Would you like to edit your order? (yes/no): ")
            if edit_order.lower() == "yes":
                edit_field = input(
                    "Which field would you like to edit (name, phone, email, size, bread, filling, theme/decoration, or additional comments)? Enter 'done' to continue: "
                )

                if edit_field == "name":
                    new_name = input("Please enter the new name: ")
                    orders[new_name] = orders.pop(customer_name)
                    customer_name = new_name
                elif edit_field == "phone":
                    new_phone = input("Please enter the new phone: ")
                    orders[customer_name]["phone_number"] = new_phone
                elif edit_field == "email":
                    new_email = input("Please enter the new email address: ")
                    orders[customer_name]["email"] = new_email
                elif edit_field == "size":
                    area = float(input("What size would you like the cake? (inches): "))
                    total_price = 2 * area
                    orders[customer_name]["area"] = area
                    orders[customer_name]["total_price"] = total_price
                elif edit_field == "bread":
                    new_bread_choice = input(
                        "What type of bread would you like? (Chocolate, Vanilla, Strawberry, custom): "
                    )
                    orders[customer_name]["bread_choice"] = new_bread_choice
                elif edit_field == "filling":
                    new_filling_flavor = input(
                        "What type of filling would you like in your cake? (Strawberry, Blueberry, Raspberry, Chocolate, custom): "
                    )
                    orders[customer_name]["filling_flavor"] = new_filling_flavor
                elif edit_field == "theme/decoration":
                    new_decoration_theme = input(
                        "What type of decoration would you like on your cake? Please enter your theme/decorations: "
                    )
                    orders[customer_name]["decoration_theme"] = new_decoration_theme
                elif edit_field == "additional comments":
                    additional_comments = input("Any additional comments? (yes/no): ")
                    if additional_comments.lower() == "yes":
                        new_user_comments = input("Please type your new comments: ")
                orders[customer_name]["additional_comments"] = new_user_comments

            print("You have updated your order.")
        else:
            print(f"Order for {customer_name} not found.")
    elif order_cake == "1":
        name = input("Please enter your name: ")
        phone_number = input("Please enter your phone number: ")
        email = ""

        while True:
            contact_method = input(
                "How would you like to be contacted (call, text, email)? "
            ).lower()

            if contact_method == "email":
                email = input("Please enter your email address: ")
                print(f"Thank you, {name}! We will contact you via email at {email}.")
                break
            elif contact_method == "call":
                print(f"Thank you, {name}! We will contact you by phone at {phone_number}.")
                break
            elif contact_method == "text":
                print(f"Thank you, {name}! We will send you a text message at {phone_number}.")
                break
            else:
                print("Invalid contact method. Please choose from call, text, or email.")

        area = float(input("\nWhat size would you like the cake? (inches): "))
        total_price = 2 * area
        print(f"Total is: ${total_price}")

        bread_choice = input(
            "\nWhat type of bread would you like? (Chocolate, Vanilla, Strawberry, custom): "
        )
        filling_flavor = input(
            "What type of filling would you like in your cake? (Strawberry, Blueberry, Raspberry, Chocolate, custom): "
        )
        decoration_theme = input(
            "What type of decoration would you like on your cake? Please enter your theme/decorations: "
        )
        additional_comments = input("Any additional comments? (yes/no): ")
        user_comments = ""
        if additional_comments.lower() == "yes":
            user_comments = input("Please type your comments: ")

        # Store the order details in the dictionary
        order_details = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "area": area,
            "total_price": total_price,
            "bread_choice": bread_choice,
            "filling_flavor": filling_flavor,
            "decoration_theme": decoration_theme,
            "additional_comments": user_comments,
        }
        orders[name] = order_details  # Use the customer's name as the key
        print(
            "Thank you {name} for your order!\nYou've chosen {bread_choice} bread\nwith {filling_flavor} filling\nand the theme '{decoration_theme}'.\nWe will send you a message when it's ready for pick up!\nThank You for ordering at The Silly Goose Co.\n?(??????)?"
        )

print(
    f"Thank you {name} for your order!\nYou've chosen {bread_choice} bread\nwith {filling_flavor} filling\nand the theme '{decoration_theme}'.\nWe will send you a message when it's ready for pick up!\nThank You for ordering at The Silly Goose Co.\n?(??????)?"
)
