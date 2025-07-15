stock = {
    "Apple Iphone 15": {"price": 829, "rating": 4.5},
    "Apple AirPods (Gen 1)": {"price": 119, "rating": 4.8},
    "Apple AirPods (Gen 2)": {"price": 129, "rating": 4.5},
    "Samsung Galaxy S23": {"price": 800, "rating": 4.5},
    "Galaxy Buds": {"price": 90, "rating": 4.4},
    "Galaxy Buds2": {"price": 110, "rating": 4.4}
}

print("Welcome to the online shop\n" "Developed\n")

print("Our current stock:")
for item, details in stock.items():
    print(f"{item} - Price: {details['price']} USD - Rating: {details['rating']}")

total = 0 # total value of order
items = [] # list of item names

while True: # input prompts
    if len(items) == 0:
        selected_item = input("Enter the name of the item you'd like to select (case-sensitive):")
    else:
        selected_item = input("Pick another item (type 'done' to place your order): ")
    
    if selected_item.lower() == 'done':
        break   

    if selected_item in stock: # searches for items in stock and adds item's value to total and keeps list of item names
        item_data = stock[selected_item]
        item_price = item_data["price"]
        total += item_price
        items.append(selected_item)
        print(f"{selected_item} is in your cart and costs {item_price} USD.")
    else:
        print(f"{selected_item} is not available at this time. Please pick a different item.")

print("Your cart: ")
for item in items:
    print(item)

print(f"The total cost of your order is {total} USD. Thank you for shopping at Brian's online shop!")