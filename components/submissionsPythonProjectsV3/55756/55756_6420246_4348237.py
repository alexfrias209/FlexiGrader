import json
print('Welcome to the Organization Project, user.\n')
print('This project was made by XXXXXX for ME 021 project.\nThis project consists of helping students find clubs and organizations that match their interests.\nPlease state your interests in all lowercase after the colen, for example art,engineering,sports')


# Dictionary
clubs = {
    "ACS Association for Computing Machinery": {
        "name": "ACS Association for Computing Machinery",
        "description": "Learn and practice programming in a fun and collaborative environment.",
        "interests": ["programming", "technology", "computers"],
    },
    "Bobcat_Band_club": {
        "name": "Band Club",
        "description": "Explore your musical talents and enjoy jam sessions with fellow music enthusiasts.",
        "interests": ["music", "instruments", "singing", "band"],
    },
    "Young Artist's Movement": {
        "name": "Art Club",
        "description": "Unleash your creativity through painting, drawing, and various art forms.",
        "interests": ["art", "painting", "drawing"],
    },
    "SHPE": {
        "name": "SHPE",
        "description": "The purpose of this student chapter is to increase the number of Hispanic engineering students at the University of California Merced, promote the advancement of Hispanic engineers and scientists in employment and education, develop and participate in programs with industry and the university, which benefit students seeking technical degrees. Another goal we have is to improve the retention of Hispanic students enrolled in engineering and science. ",
        "interests": ["engineering", "hsipanic", "family"],
    },
    "AIAA, American Institute of Aeronautics and Astronautics": {
        "name": "AIAA",
        "description": "Our members are at the center of what we do at AIAA. Our club provides a diverse portfolio of strategic experiences that offer skill-development opportunities that prepare our members for the professional world. In fact, our Alumni have received offers and now work at some of the top Aerospace Companies in the world. Interested in joining one of our projects? Check out our external website!",
        "interests": ["engineering", "aerospace", "team", "projects"],
    },
    "book_club": {
        "name": "Book Club",
        "description": "Discuss and explore the world of literature with fellow book enthusiasts.",
        "interests": ["reading", "literature", "books"],
    },
    "Yosemite leadership program": {
        "name": "Outdoor Adventure Club",
        "description": "Embark on exciting outdoor adventures like hiking, camping, and rock climbing.",
        "interests": ["outdoor", "adventures", "hiking"],
    },
    "environmental_club": {
        "name": "Environmental Club",
        "description": "Work together to promote eco-friendly practices and protect the environment.",
        "interests": ["environment", "sustainability", "conservation"],
    },
    "sports_club": {
        "name": "Sports Club",
        "description": "Stay active and engage in various sports activities with other sports enthusiasts.",
        "interests": ["sports", "fitness", "athletics"],
    },
    "student filmakers club": {
        "name": "student filmakers club",
        "description": "Watch and discuss movies from various genres and eras with fellow film buffs.",
        "interests": ["movies", "cinema", "film analysis"],
    },
    "dance_club": {
        "name": "Dance Club",
        "description": "Learn different dance styles and choreograph dance routines with other enthusiasts.",
        "interests": ["dance", "choreography", "music"],
    },
    "biological_sciences_club": {
        "name": "biological_sciences_club",
        "description": "Explore and conduct experiments in various scientific disciplines with your peers.",
        "interests": ["science", "experimentation", "discovery"],
    },
    "history_club": {
        "name": "History Club",
        "description": "Delve into the past, unravel historical mysteries, and discuss world history events.",
        "interests": ["history", "historical events", "research"],
    },
    "debate_club": {
        "name": "Debate Club",
        "description": "Sharpen your public speaking and argumentation skills through debates on various topics.",
        "interests": ["debate", "public speaking", "argumentation"],
    },
}

# Function to match student interests with clubs
def find_matching_clubs(student_interests):
    matching_clubs = []

    for club_key, club_info in clubs.items():
        club_name = club_info["name"]
        club_description = club_info["description"]
        club_interests = club_info["interests"]

        # Format the output if interest match dictionary
        if any(interest in student_interests for interest in club_interests):
            matching_clubs.append({
                "name": club_name,
                "description": club_description,
            })

    return matching_clubs

# ask the studednts for tehir interests
student_interests = input("Enter your interests or hobbies, make sure they are comma separated.: ").split(",")

# Find clubs that work for the student
recommended_clubs = find_matching_clubs(student_interests)

if recommended_clubs:
    print("Recommended Clubs:")
    for club in recommended_clubs:
        print(f"{club['name']}: {club['description']}")
else:
    print("No matching clubs found.")

# Saving the clubs to a new file that will be imported to user computer
with open("recommended_clubs.txt", "w") as file:
    json.dump(recommended_clubs, file)

print("Recommended clubs/organizations were saved to your computer in files as'recommended_clubs.txt' for future reference.")
