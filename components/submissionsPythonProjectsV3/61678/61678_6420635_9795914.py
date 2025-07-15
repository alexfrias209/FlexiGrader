from skimage import io  #imports input/output operation from skimage library
import matplotlib.pyplot as plt  #assigns plt from imported matsplotlib library

plt.rcParams["figure.figsize"] = [
    7.50, 3.50
]  #assigns two values to figsize (width, height)
plt.rcParams["figure.autolayout"] = True  #automatic layout adjusts
link = 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-card-40-iphone15prohero-202309_FMT_WHH?wid=508&hei=472&fmt=p-jpg&qlt=95&.v=1693086369818'
a = io.imread(
    link
)  #uses io submodule and imread function to read image from link, assigns to a

plt.imshow(a)  #uses plt and imshow function to display image stored in a
plt.axis('off')
plt.draw()  #redraws image
plt.pause(2)  #pauses display for 2 seconds


def userguessbrand(brand_guess, total_tries):
  #creates function with guess and attempts as parameters
  user_score = 0
  for tries in range(
      1, total_tries +
      1):  #for loop uses variable tries to iterate range of user attempts
    animal = input("Please enter the brand name (Attempt {} of {}): ".format(
        tries, total_tries
    ))  #prompts user, uses .format inserts into string placeholder
    if animal == brand_guess:  #conditional loop, checks input matches brand_guess parameter
      user_score += total_tries - tries + 1
      print("Congrats! You guessed the correct brand.")
      break
    elif tries < total_tries:  #check is variable tries is less than parameter total_tries
      print("Incorrect! Try again.")
    else:
      print("Out of attempts. The correct brand was:", brand_guess)
  return user_score  #returns user_score back to main function


def save_score(user_score):  #function to save users score to file
  with open("user_score.txt", "w") as file:
    file.write(str(user_score))  #coverts user score varaible to string


def read_score():  #function that reads user score from file
  try:  #try/accept block
    with open("user_score.txt", "r") as file:  #opens file and reads value
      user_score = int(float(file.read().strip()
                             or 0))  #strips whitespace coverts result to float
  except FileNotFoundError:  #exception handler
    user_score = 0
  return user_score  #shows score


def start():  #Starting point for code
  brand_guess = "Apple"  # assigns variable to string
  total_tries = 5  #defines number of attempts
  user_score = read_score()

  print(
      "Welcome to the Brand Guessing Game!"
  )
  print("Please enter brand name with first letter capatilized.")
  while True:
    user_score = userguessbrand(
        brand_guess, total_tries)  #call back to function, exectues function
    print(f"Your current score for this image is: {user_score}/5")
    save_score(user_score)

    play_again = input("Would you like to play this section again? (yes/no): ") #give player option to improve score by repeating the same section
    if play_again.lower(
    ) != "yes":  #if player chooses no, code breaks and moves on, otherwise repeats again
      break


if __name__ == "__main__":  #conditional statement that sets special variable "name" is equal to main if python interpreter runs source file as main program
  start()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
link = 'https://s.yimg.com/uu/api/res/1.2/0IwPHdHcjeYqfJ5qL0K44g--~B/aD0xMzMzO3c9MjAwMDthcHBpZD15dGFjaHlvbg--/https://media-mbst-pub-ue1.s3.amazonaws.com/creatr-uploaded-images/2021-01/0fee2530-5b87-11eb-b7da-de096e0632a2.cf.jpg'
a = io.imread(link)

plt.imshow(a)
plt.axis('off')
plt.draw()
plt.pause(2)


def userguessbrand(brand_guess, total_tries):

  user_score = 0
  for tries in range(1, total_tries + 1):
    animal = input("Please enter the brand name (Attempt {} of {}): ".format(
        tries, total_tries))
    if animal == brand_guess:
      user_score += total_tries - tries + 1
      print("Congrats! You guessed the correct brand.")
      break
    elif tries < total_tries:
      print("Incorrect! Try again.")
    else:
      print("Out of attempts. The correct brand was:", brand_guess)
  return user_score


def save_score(user_score):
  with open("samsunguserscore.txt", "w") as file:
    file.write(str(user_score))


def read_score():
  try:
    with open("samsunguserscore.txt", "r") as file:
      user_score = int(float(file.read() or 0))
  except FileNotFoundError:
    user_score = 0
  return user_score


def start():
  brand_guess = "Samsung"
  total_tries = 5
  user_score = read_score()

  print("Please enter brand name with first letter capatilized.")
  while True:
    user_score = userguessbrand(brand_guess, total_tries)
    print(f"Your current score for this image is: {user_score}/5")
    save_score(user_score)

    play_again = input("Would you like to play this section again? (yes/no): ")
    if play_again.lower() != "yes":
      break


if __name__ == "__main__":
  start()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
link = 'https://static.nike.com/a/videos/t_PDP_1280_v1/f_auto,q_auto:eco,so_0/916fb268-149e-41f7-8143-f43c1bfb79e8/sb-chron-2-skate-shoe-VdBzLw.jpg'
a = io.imread(link)

plt.imshow(a)
plt.axis('off')
plt.draw()
plt.pause(2)


def userguessbrand(brand_guess, total_tries):

  user_score = 0
  for tries in range(1, total_tries + 1):
    animal = input("Please enter the brand name (Attempt {} of {}): ".format(
        tries, total_tries))
    if animal == brand_guess:
      user_score += total_tries - tries + 1
      print("Congrats! You guessed the correct brand.")
      break
    elif tries < total_tries:
      print("Incorrect! Try again.")
    else:
      print("Out of attempts. The correct brand was:", brand_guess)
  return user_score


def save_score(user_score):
  with open("nikeuserscore.txt", "w") as file:
    file.write(str(user_score))


def read_score():
  try:
    with open("nikeuserscore.txt", "r") as file:
      user_score = int(float(file.read() or 0))
  except FileNotFoundError:
    user_score = 0
  return user_score


def start():
  brand_guess = "Nike"
  total_tries = 5
  user_score = read_score()

  print("Please enter brand name with first letter capatilized.")
  while True:
    user_score = userguessbrand(brand_guess, total_tries)
    print(f"Your current score for this image is: {user_score}/5")
    save_score(user_score)

    play_again = input("Would you like to play this section again? (yes/no): ")
    if play_again.lower() != "yes":
      break


if __name__ == "__main__":
  start()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
link = 'https://i.insider.com/618da1f73d74d00019f4099e?width=1000&format=jpeg&auto=webp'
a = io.imread(link)

plt.imshow(a)
plt.axis('off')
plt.draw()
plt.pause(2)


def userguessbrand(brand_guess, total_tries):

  user_score = 0
  for tries in range(1, total_tries + 1):
    animal = input("Please enter the brand name (Attempt {} of {}): ".format(
        tries, total_tries))
    if animal == brand_guess:
      user_score += total_tries - tries + 1
      print("Congrats! You guessed the correct brand.")
      break
    elif tries < total_tries:
      print("Incorrect! Try again.")
    else:
      print("Out of attempts. The correct brand was:", brand_guess)
  return user_score


def save_score(user_score):
  with open("kirklanduserscore.txt", "w") as file:
    file.write(str(user_score))


def read_score():
  try:
    with open("kirklanduserscore.txt", "r") as file:
      user_score = int(float(file.read() or 0))
  except FileNotFoundError:
    user_score = 0
  return user_score


def start():
  brand_guess = "Kirkland"
  total_tries = 5
  user_score = read_score()

  print("Please enter brand name with first letter capatilized.")
  while True:
    user_score = userguessbrand(brand_guess, total_tries)
    print(f"Your current score for this image is: {user_score}/5")
    save_score(user_score)

    play_again = input("Would you like to play this section again? (yes/no): ")
    if play_again.lower() != "yes":
      break


if __name__ == "__main__":
  start()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
link = 'https://d3s8goeblmpptu.cloudfront.net/mrp/toyota/2023/corolla/2023-toyota-corolla_landing-2.jpg'
a = io.imread(link)

plt.imshow(a)
plt.axis('off')
plt.draw()
plt.pause(2)


def userguessbrand(brand_guess, total_tries):

  user_score = 0
  for tries in range(1, total_tries + 1):
    animal = input("Please enter the brand name (Attempt {} of {}): ".format(
        tries, total_tries))
    if animal == brand_guess:
      user_score += total_tries - tries + 1
      print("Congrats! You guessed the correct brand.")
      break
    elif tries < total_tries:
      print("Incorrect! Try again.")
    else:
      print("Out of attempts. The correct brand was:", brand_guess)
  return user_score


def save_score(user_score):
  with open("toyotauserscore.txt", "w") as file:
    file.write(str(user_score))


def read_score():
  try:
    with open("toyotauserscore.txt", "r") as file:
      user_score = int(float(file.read() or 0))
  except FileNotFoundError:
    user_score = 0
  return user_score


def start():
  brand_guess = "Toyota"
  total_tries = 5
  user_score = read_score()

  print("Please enter brand name with first letter capatilized.")
  while True:
    user_score = userguessbrand(brand_guess, total_tries)
    print(f"Your current score for this image is: {user_score}/5")
    save_score(user_score)

    play_again = input("Would you like to play this section again? (yes/no): ")
    if play_again.lower() != "yes":
      break


if __name__ == "__main__":
  start()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
link = 'https://www.golfposer.com/media/wysiwyg/PUMA-GOLF-SHOES-WHITE-NAVY-RS-G-01.jpg'
a = io.imread(link)

plt.imshow(a)
plt.axis('off')
plt.draw()
plt.pause(2)


def userguessbrand(brand_guess, total_tries):

  user_score = 0
  for tries in range(1, total_tries + 1):
    animal = input("Please enter the brand name (Attempt {} of {}): ".format(
        tries, total_tries))
    if animal == brand_guess:
      user_score += total_tries - tries + 1
      print("Congrats! You guessed the correct brand.")
      break
    elif tries < total_tries:
      print("Incorrect! Try again.")
    else:
      print("Out of attempts. The correct brand was:", brand_guess)
  return user_score


def save_score(user_score):
  with open("pumauserscore.txt", "w") as file:
    file.write(str(user_score))


def read_score():
  try:
    with open("pumauserscore.txt", "r") as file:
      user_score = int(float(file.read() or 0))
  except FileNotFoundError:
    user_score = 0
  return user_score


def start():
  brand_guess = "Puma"
  total_tries = 5
  user_score = read_score()

  print("This is the last image, good luck!")
  print("Please enter brand name with first letter capatilized.")
  while True:
    user_score = userguessbrand(brand_guess, total_tries)
    print(f"Your current score for this image is: {user_score}/5")
    save_score(user_score)

    play_again = input("Would you like to play this section again? (yes/no): ")
    if play_again.lower() != "yes":
      break


if __name__ == "__main__":
  start()



complete_score = 0 #variable to store entire game score
files_with_scores = ["user_score.txt", "samsunguserscore.txt", "nikeuserscore.txt", "kirklanduserscore.txt", "toyotauserscore.txt", "pumauserscore.txt"] #file names in list data structure
for actual_name in files_with_scores: #iterates through all files, coverts values to integers
  try:
    with open(actual_name, 'r') as file:
      pack = file.read() #reads file
      score = int(pack) #converts contents in file to integer
      complete_score += score #adds computated score to complete_score
  except FileNotFoundError: #handles expectional case of file not found
    print("file not found, please retry.")
  




out_of_30 = min(complete_score, 30) #sets outof30 to calculate total score, max of 30, min function used to ensure total score is not greater than 30
print(f"Your total score is: {out_of_30}/30 possible points")

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
link = 'https://t4.ftcdn.net/jpg/02/11/54/33/360_F_211543376_kv7x0SwdITkWbqajGzglhcvZV25AsPsS.jpg'
a = io.imread(link)

plt.imshow(a)
plt.axis('off')
plt.draw()
plt.pause(10)