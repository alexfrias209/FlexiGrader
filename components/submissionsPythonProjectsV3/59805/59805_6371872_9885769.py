# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:11:20 2023

"""

# Lists to store information about hiking trails, lakes, and camping spots in Merced County
hiking_trails = [
    {"name": "Yosemite Falls Trail", "distance": 7.2, "difficulty": "Moderate"},
    {"name": "Mist Trail", "distance": 5.4, "difficulty": "Strenuous"},
    {"name": "Vernal Fall Footbridge Trail", "distance": 1.6, "difficulty": "Easy"},
]

lakes = [
    {"name": "Tenaya Lake", "size": "150 acres", "activities": "Swimming, picnicking"},
    {"name": "Mirror Lake", "size": "20 acres", "activities": "Hiking, photography"},
    {"name": "Yosemite Lake", "size": "500 acres", "activities": "Swimming, picnicking,Boating"},
]

camping_spots = [
    {"name": "Upper Pines Campground", "capacity": 238, "facilities": "Restrooms, showers"},
    {"name": "Bridalveil Creek Campground", "capacity": 110, "facilities": "Vault toilets"},
    {"name": "McConnell State Recreation Area", "capacity": 350, "facilities": "Restrooms, Camper Parking"},
]

# Function to display options and compile Itinerary
def plan_trip():
    print("Welcome to the Merced, CA Trip Planner!")
    while True:
        print("\nAvailable options:")
        print("1. Explore Hiking Trails")
        print("2. Discover Lakes")
        print("3. Find Camping Spots")
        print("4. Create Trip Itinerary")
        print("5. Save Trip Itinerary to a File")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("\nHiking Trails:")
            for trail in hiking_trails:
                print(f"{trail['name']} - Distance: {trail['distance']} miles, Difficulty: {trail['difficulty']}")
        
        elif choice == "2":
            print("\nLakes:")
            for lake in lakes:
                print(f"{lake['name']} - Size: {lake['size']}, Activities: {lake['activities']}")
        
        elif choice == "3":
            print("\nCamping Spots:")
            for spot in camping_spots:
                print(f"{spot['name']} - Capacity: {spot['capacity']}, Facilities: {spot['facilities']}")
        
        elif choice == "4":
            itinerary = []
            while True:
                place_type = input("Enter the type of place (Trail/Lake/Camping) you want to add to your itinerary (or 'done' to finish): ").lower()
                if place_type == "done":
                    break
                elif place_type == "trail":
                    trail_name = input("Enter the name of the hiking trail: ")
                    trail = next((t for t in hiking_trails if t["name"].lower() == trail_name.lower()), None)
                    if trail:
                        itinerary.append(f"Hiking Trail: {trail['name']} - Distance: {trail['distance']} miles, Difficulty: {trail['difficulty']}")
                    else:
                        print("Hiking trail not found.")
                elif place_type == "lake":
                    lake_name = input("Enter the name of the lake: ")
                    lake = next((l for l in lakes if l["name"].lower() == lake_name.lower()), None)
                    if lake:
                        itinerary.append(f"Lake: {lake['name']} - Size: {lake['size']}, Activities: {lake['activities']}")
                    else:
                        print("Lake not found.")
                elif place_type == "camping":
                    camping_name = input("Enter the name of the camping spot: ")
                    camping_spot = next((c for c in camping_spots if c["name"].lower() == camping_name.lower()), None)
                    if camping_spot:
                        itinerary.append(f"Camping Spot: {camping_spot['name']} - Capacity: {camping_spot['capacity']}, Facilities: {camping_spot['facilities']}")
                    else:
                        print("Camping spot not found.")
                else:
                    print("Invalid choice. Please enter 'Trail', 'Lake', or 'Camping'.")
            
            print("\nYour Trip Itinerary:")
            for item in itinerary:
                print(item)

        elif choice == "5":
            filename = input("Enter a filename to save your trip itinerary (e.g., my_trip.txt): ")
            with open(filename, "w") as file:
                for item in itinerary:
                    file.write(item + "\n")
            print(f"Trip itinerary saved to {filename}")

        elif choice == "6":
            print("Thank you for using the Merced, CA Trip Planner!")
        
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    plan_trip()

