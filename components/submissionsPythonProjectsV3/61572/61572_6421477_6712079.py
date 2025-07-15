

import csv

def view():
  with open('61572_6421478_7698706.csv', mode ='r') as file:
    # reading the CSV file
    
    csvFile = csv.reader(file)
    next(csvFile)
    # displaying the contents of the CSV file
    choose = int(input("Press 1 to filter or 2 for all Movies"))
    if choose == 1:  
      letter = input("Enter a single letter")
      for lines in csvFile:
            if lines[1][0] == letter:
              print(lines[1])
    else:
      for lines in csvFile:
          print(lines[1])

def average(movie_id, ratings_data):
  total_rating = 0
  num_ratings = 0
  for row in ratings_data:
    if row[1] == movie_id:
      total_rating += float(row[2])
      num_ratings += 1
  if num_ratings == 0:
    return None
  else:
    return total_rating / num_ratings
  
def filter(x):
  with open('61572_6421478_7698706.csv', mode ='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    next(csvFile)
    # displaying the contents of the CSV file
    findingID = None
    for lines in csvFile:
          id,title,categories = lines
          if remove(title) == remove(x):
            findingID = id
  
  with open ('61572_6421479_4856774.csv', mode='r') as ratings_file:
    ratings_data = list(csv.reader(ratings_file))
    
  avg = average(findingID, ratings_data)
  
  if avg is not None:
    print(f"Average rating for {x}: {avg:.2f}")
  

def remove(string):
  return string.replace(" ", "")

def main():
  print('Welcome to movie rating!')
  print()
  print('Not sure what to watch? Choose from this list of movies to get their rating!')
  
  print('\nMOVIE LIST:')
  
  while True:
    decision = input("Choose from the following: 1. View Movies 2. View Rating 3. Exit\n")
    if decision.isnumeric():
      decision = int(decision)
      if decision >= 1 and decision<=3:
        break
    print('Invalid input. Please enter a valid integer.')
    # You can decide how you want to handle the invalid input, such as asking the user again or exiting the program
  
  if decision == 1:
    view()
  elif decision == 2:
    movieTitle = input('\nEnter movie name here: ')
    year = input('Enter movie year here: ')
    x = f"{movieTitle} ({year})"
    filter(x)
  elif decision == 3:
    print("Exiting")
    return
  else:
    print("Invalid choice. Please choose 1, 2, or 3 to exit")
  
main() 
    
# for movie in movies:
#     print(movie)

# decision = input('\nChoose any of these movies to find the average rating: ')

# # Assuming you have a dictionary with movie ratings
# movie_ratings = {
#     'The Conjuring': 3.5,
#     'Jaws': 4.0,
#     'Talk to Me': 3.0,
#     'The Sandlot': 4.5,
#     'Scott Pilgrim': 4.2,
# }

# if decision in movie_ratings:
#     rating = movie_ratings[decision]
#     print(f'You have chosen {decision}, it has an average rating of {rating}')
# else:
#     print('Invalid movie selection')
