#Will implement the code to retrive file in lab since I can't get it to work
print()
print('In this project I will be creating a food recomender,')
print('it will take the qualities you want and will print out all the food that have the qualities')

states_countries = ['California', 'Texas', 'New Jersy']
print()
print()
print(f'These are places you can choose from {states_countries}')
#inputs
food_area = input('What state(USA)/Country do you want to eat in: ')
choice = input('Do you want your food healthy or unhealthy(type exit anytime to stop): ')
if food_area in states_countries:
    while choice != 'exit':

#CALIFORNIA
        if food_area == 'California':
            if choice == "healthy":
                healthy_c = input('Do you want a salad, sandwhich, fruit ')
#ill add more options in finalized project this is the base
#healthy California
                while healthy_c != 'exit':
                    if healthy_c == 'exit':
                        exit()
                    if healthy_c == 'salad':
                        print('You should try: Greek Salad with Lettuce, Italian Pasta Salad, Caesar Salad, Tomato Cucumber Avocado Salad.')
                        exit()
                    elif healthy_c == 'sandwhich':
                        print('You should try: Grilled cheese, Grilled chicken, Turkey, Roast beef, Ham.')
                        exit()
                    elif healthy_c == 'fruit':
                        print('You should try: Blueberries, Oranges, Prunes, Raspberries.')
                        exit()
                    healthy_c = input('Incorrect choice: Do you want a salad, sandwhich, fruit ')
#unhealthy California
            if choice == "unhealthy":
                unhealthy_c = input('Do you want a burger, candy, or food recomendations ')
                if unhealthy_c == 'exit':
                    exit()
                while unhealthy_c != 'exit':
                    if unhealthy_c == 'burger':
                        print('You should try a cheeseburger, turkey burger, bacon burger, or a mushroom burger')
                        exit()
                    if unhealthy_c == 'candy':
                        print('You should try a snickers bar, Sourpatch kids, Air heads, or Hersheys')
                        exit()
                    if unhealthy_c == 'food recomendations':
                        print("You should go to Wingstop, McDonalds, Arby's, or Panda Express")
                        exit()
                    unhealthy_c = input('Incorrect choice: Do you want a burger, candy, or food recomendations ')
#Texas
        if food_area == 'Texas':
            if choice == "healthy":
                healthy_c = input('Do you want a salad, sandwhich, fruit ')
#ill add more options in finalized project this is the base
#healthy Texas
                while healthy_c != 'exit':
                    if healthy_c == 'exit':
                        exit()
                    if healthy_c == 'salad':
                        print('You should try: Texas bibb Salad, Texas Caviar chopped salad, or Texas style bean salad')
                        exit()
                    elif healthy_c == 'sandwhich':
                        print('You should try: Smoked brisket, Avacodo grilled cheese, Classic Monte Cristo')
                        exit()
                    elif healthy_c == 'fruit':
                        print('You should try: Red Grapefruit, Melons, Prunes, Raspberries.')
                        exit()
                    healthy_c = input('Incorrect choice: Do you want a salad, sandwhich, fruit ')
#unhealthy Texas
            if choice == "unhealthy":
                unhealthy_c = input('Do you want a burger, candy, or food recomendations ')
                if unhealthy_c == 'exit':
                    exit()
                while unhealthy_c != 'exit':
                    if unhealthy_c == 'burger':
                        print('You should try a cheeseburger, turkey burger, sloppy joe, or a bbq beef')
                        exit()
                    if unhealthy_c == 'candy':
                        print('You should try a snickers bar, Sourpatch kids, Air heads, or Hersheys')
                        exit()
                    if unhealthy_c == 'food recomendations':
                        print("You should go to Wingstop, McDonalds, Arby's, or Whataburger")
                        exit()
                    unhealthy_c = input('Incorrect choice: Do you want a burger, candy, or food recomendations ')
        else:
            print('Please enter one of the options for places to eat (your desired meal is most likely in one of them)')
#New Jersy
        if food_area == 'New Jersy':
            if choice == "healthy":
                healthy_c = input('Do you want a salad, sandwhich, fruit ')
#Healthy Jersy
                while healthy_c != 'exit':
                    if healthy_c == 'exit':
                        exit()
                    if healthy_c == 'salad':
                        print('You should try: Greek Salad with Lettuce, Italian Pasta Salad, Caesar Salad, Tomato Cucumber Avocado Salad.')
                        exit()
                    elif healthy_c == 'sandwhich':
                        print('You should try: Submarine sandwhich, Jersy sub, Jersy bagel breakfast sandwhich')
                        exit()
                    elif healthy_c == 'fruit':
                        print('You should try: Goose berry, Apples, Peaches, Squash.')
                        exit()
                    healthy_c = input('Incorrect choice: Do you want a salad, sandwhich, fruit ')
#Unhealthy Jersy
            if choice == "unhealthy":
                unhealthy_c = input('Do you want a burger, candy, or food recomendations ')
                if unhealthy_c == 'exit':
                    exit()
                while unhealthy_c != 'exit':
                    if unhealthy_c == 'burger':
                        print('You should try a stuffed grassfed burger, White Manna slidders, or White Star bar burgers')
                        exit()
                    if unhealthy_c == 'candy':
                        print('You should try a snickers bar, Sourpatch kids, Air heads, or Hersheys')
                        exit()
                    if unhealthy_c == 'food recomendations':
                        print("You should go to The Frog and the Peach, H&W Drive in, Johnny Rockets, or Resturant Serenade")
                        exit()
                    unhealthy_c = input('Incorrect choice: Do you want a burger, candy, or food recomendations ')
        else:
            print('Please enter one of the options for places to eat (your desired meal is most likely in one of them)')