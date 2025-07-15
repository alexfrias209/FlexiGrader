import pandas as pd
def intro(User): 
    print(f"Welcome to My ME021 project {User}!\nMy name is {my_name}, and my project is cologne or perfume recomender.")
    print(f"My project required me to make a csv file that includes the cataloge of colognes and perfumes.")
    print(f"For the you {User} the survey will have you answer each problem then it will tell you if have imputed one of the options stated.")
    print(f"{User} Thank you for participating in my project")

my_name = 'XXXXXXXXX'
User = input('Enter your name here(Must include at least one character):')
if len(User) >=1:
    intro(User)

start_button = input("Please press enter anyhing to find your cologne!\n: ")

print("What type of cologne are you looking for?")
print("Please choose one of the following options")
print("1.Masculine/Colonge")
print("2.Feminine/Perfume")
print("3.Neutral ")

file = open('62066_6421006_5713391.csv','r')

valid_answers = [1, 2, 3]

while True:     
    Gender = int(input("Enter number option here (1/2/3):"))
    if Gender  in valid_answers:
        print("Your response is valid:", Gender)
        break
    else:
        print("Invalid response. Please try again.")

if Gender == 1:
    print("You chose the Masculine/Cologne option")
elif Gender == 2:
    print("You chose the Feminine/Perfume option")
elif Gender == 3:
    print("You chose the Neutral option")

print("What type of Scense are you looking for?")
print("Please choose one of the following options")
print("1.Floral (Lilac, Rose)")
print("2.Citrus (Lemon, Yuzu)")
print("3.Sweet (Honey, Vanilla)")
print("4.Spicy (Allspice, Ginger)")

valid_answers = [1,2,3,4]
while True:
    cologne_scent = int(input("Enter number option here (1/2/3/4):"))
    if cologne_scent in valid_answers:
        print("Your response is valid:", cologne_scent)
        break
    else:
        print("Invalid response. Please try again.")

if cologne_scent == 1:
    print("You chose the Floral (Lilac, Rose) option")
elif cologne_scent == 2:
    print("You chose the Citrus (Lemon, Yuzu) option")
elif cologne_scent == 3:
    print("You chose the Sweet (Honey, Vanilla) option")
elif cologne_scent == 4:
    print("You chose the Spicy (Allspice, Ginger option")


print("What is the price range you are looking for?")
print("Please choose one of the following options")
print("1. Under 100$")
print("2. 100$ to 250$")
print("3. 250$ to 500$")
print("4. 500$ & above")

valid_answers = [1,2,3,4]
while True:
    cologne_price_range = int(input("Enter number option here (1/2/3/4):"))
    if cologne_price_range in valid_answers:
        print("Your response is valid:", cologne_price_range)
        break
    else:
        print("Invalid response. Please try again.")

if cologne_price_range == 1:
    print("You chose the Under 100$ price range")
elif cologne_price_range == 2:
    print("You chose the 100$ to 250$ price range")
elif cologne_price_range == 3:
    print("You chose the 250$ to 500$ price range")
elif cologne_price_range == 4:
    print("You chose the 500$ & above price range")


def filter_perfumes(filename, Gender, cologne_scent, cologne_price_range):
    df = pd.read_csv(filename)

    filtered_df = df.query(f'Gender == {Gender} and Scent == {cologne_scent} and `Price Range` == {cologne_price_range}')

    if not filtered_df.empty:
        matching_names = filtered_df['Name'].tolist()
        return matching_names
    else:
        return []

matching_colognes = filter_perfumes('62066_6421006_5713391.csv', Gender, cologne_scent, cologne_price_range)

if matching_colognes:
    print("Matching colognes/perfumes:")
    for name in matching_colognes:
        print(f'Thank you {User} for participating in my Project for ME 021')
        print('With the imputs you provided your recomended cologne or perfume is:')
        print(name)
else:
    print("No matching colognes/perfumes found.")
