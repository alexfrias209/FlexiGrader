from geopy.geocoders import Nominatim

# Nominatim is a geocoding service provided by OpenStreetMap

from geopy.distance import geodesic

# geodesic is a distance calculation function

import random


# Define a function to get coordinates of a location
def get_coordinates(location_name):
  geolocator = Nominatim(user_agent="geo_distance_guesser")
  # user_agent is a parameter used to identify the application or service          making the request to Nominatim

  location = geolocator.geocode(location_name, timeout=5)
  return (location.latitude, location.longitude)


# Define a function to calculate distance
def calculate_distance(location1, location2):
  return geodesic(location1, location2).miles
  #calculate_distance is a distance calculation function from geopy.distance module of geodesic


# Function to load locations from a text file
def load_locations_from_file(file_path):
  #sets file path as the parameter for load_locations_from_file
  with open(file_path, 'r') as file:
    return file.read().splitlines()


# Game mode function
def game_mode(locations):
  location1, location2 = random.sample(locations, 2)
  coordinates1 = get_coordinates(location1)
  coordinates2 = get_coordinates(location2)
  correct_distance = calculate_distance(coordinates1, coordinates2)

  user_guess = float(
      input(
          f"What is the distance between {location1} and {location2} (in miles)? "
      ))

  allowed_error = 0.2 * correct_distance

  if abs(correct_distance - user_guess) <= allowed_error:
    print("Correct!")
    print(f"The correct distance is {correct_distance:2f} miles")
  else:
    print("Incorrect!")
    print(f"Sorry, the correct distance is {correct_distance:.2f} miles.")


# Study mode function
def study_mode():
  location1 = input("Enter the first location: ")
  location2 = input("Enter the second location: ")

  coordinates1 = get_coordinates(location1)
  coordinates2 = get_coordinates(location2)

  distance = calculate_distance(coordinates1, coordinates2)
  print(
      f"The distance between {location1} and {location2} is {distance:.2f} miles."
  )


# Main program
if __name__ == "__main__":
  # Load locations from a text file
  locations_list = load_locations_from_file('60433_6371029_2959147.txt')

  while True:
    print("\nMenu:")
    print("1. Game Mode")
    print("2. Study Mode")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
      game_mode(locations_list)
    elif choice == "2":
      study_mode()
    elif choice == "3":
      print('Goodbye!')
      break
    else:
      print("Invalid choice. Please enter a valid option.")
