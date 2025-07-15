# Fast Food Restaurant Ordering Simulator

# Dictionary to store the menu for each restaurant
menu = {
    "McDonald's": {
        "Big Mac": 5.99,
        "Fries": 2.49,
        "Chicken McNuggets": 4.99
    },
    "Burger King": {
        "Whopper": 6.49,
        "Onion Rings": 2.99,
        "Chicken Sandwich": 5.99
    },
    "KFC": {
        "Original Recipe Chicken": 7.99,
        "Mashed Potatoes": 2.49,
        "Cole Slaw": 1.99
    },
    "Pizza Hut": {
        "Pepperoni Pizza": 8.99,
        "Garlic Knots": 3.49,
        "Hawaiian Pizza": 9.99
    }
}

# Function to display the menu for a restaurant
def display_menu(restaurant):
    print(f"\nMenu for {restaurant}:")
    for item, price in menu[restaurant].items():
        print(f"{item}: ${price:.2f}")

# Function to take an order and calculate the total
def take_order(restaurant):
    order = {}
    total = 0

    while True:
        print("\nEnter the number of the item you want to order (0 to finish ordering):")
        for i, item in enumerate(menu[restaurant], start=1):
            print(f"{i}. {item}")
        
        item_choice = int(input())
        
        if item_choice == 0:
            break
        
        if 1 <= item_choice <= len(menu[restaurant]):
            selected_item = list(menu[restaurant].keys())[item_choice - 1]
            item_price = menu[restaurant][selected_item]
            order[selected_item] = item_price
            total += item_price
            print(f"{selected_item} added to your order.")

    return order, total

# Function to calculate change
def calculate_change(total, amount_paid):
    return amount_paid - total

# Main function to run the program
def main():
    print("Welcome to the Fast Food Ordering Simulator!")

    while True:
        print("\nPlease choose a fast food restaurant:")
        for i, restaurant in enumerate(menu.keys(), start=1):
            print(f"{i}. {restaurant}")
        print("0. Quit")

        try:
            restaurant_choice = int(input("Enter the number of your chosen restaurant: "))
            
            if restaurant_choice == 0:
                break
            
            if 1 <= restaurant_choice <= len(menu):
                chosen_restaurant = list(menu.keys())[restaurant_choice - 1]
                print(f"You have chosen {chosen_restaurant}.")
                display_menu(chosen_restaurant)
                order, total = take_order(chosen_restaurant)

                print("\nYour order:")
                for item, price in order.items():
                    print(f"{item}: ${price:.2f}")
                print(f"Total: ${total:.2f}")

                # Prompt the user for the amount paid and calculate change
                amount_paid = float(input("Enter the amount paid: $"))
                change = calculate_change(total, amount_paid)
                print(f"Change: ${change:.2f}")
            
            else:
                print("Invalid choice. Please select a valid restaurant number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Thank you for using the Fast Food Ordering Simulator!")

if __name__ == "__main__":
    main()
