# Function to load reviews from a text file
def load_reviews():
    professor_reviews = {}
    course_reviews = {}
    try:
        with open("55531_6422306_8442488.txt", "r") as file:
            lines = file.readlines()
            current_category = None
            for line in lines:
                line = line.strip()
                if line == "Professor Reviews:":
                    current_category = professor_reviews
                elif line == "Course Reviews:":
                    current_category = course_reviews
                elif line:
                    name, rating_comment = line.split(": ")
                    rating, comment = rating_comment.split(" - ")
                    current_category[name] = {"Rating": float(rating), "Comment": comment}
    except FileNotFoundError:
        print("No saved reviews found.")
    return professor_reviews, course_reviews

# Function to add a review for any professor
def add_professor_review(professor_reviews):
    professor_name = input("Enter the professor's name: ")
    rating = None
    while rating is None:
        try:
            rating = float(input("Enter the rating (1 to 5): "))
            if rating < 1 or rating > 5:
                raise ValueError
        except ValueError:
            print("Invalid input. Rating must be a number between 1 and 5.")
            rating = None
    comment = input("Enter your comment: ")
    professor_reviews[professor_name] = {"Rating": rating, "Comment": comment}

# Function to add a review for any course
def add_course_review(course_reviews):
    course_name = input("Enter the course name: ")
    rating = None
    while rating is None:
        try:
            rating = float(input("Enter the rating (1 to 5): "))
            if rating < 1 or rating > 5:
                raise ValueError
        except ValueError:
            print("Invalid input. Rating must be a number between 1 and 5.")
            rating = None
    comment = input("Enter your comment: ")
    course_reviews[course_name] = {"Rating": rating, "Comment": comment}

# Function to calculate average rating and display top-rated items
def display_top_rated(reviews, category):
    if reviews:
        average_rating = sum(review["Rating"] for review in reviews.values()) / len(reviews)
        print(f"Average Rating for {category}: {average_rating:.2f}")
        print(f"Top-Rated {category}:")
        for item, review in reviews.items():
            if review["Rating"] >= average_rating:
                print(f"{item}: {review['Rating']} - {review['Comment']}")
    else:
        print(f"No {category.lower()} reviews available.")

# Function to save reviews to a text file
def save_reviews(professor_reviews, course_reviews):
    with open("55531_6422306_8442488.txt", "w") as file:
        file.write("Professor Reviews:\n")
        for professor, review in professor_reviews.items():
            file.write(f"{professor}: {review['Rating']} - {review['Comment']}\n")
        file.write("\nCourse Reviews:\n")
        for course, review in course_reviews.items():
            file.write(f"{course}: {review['Rating']} - {review['Comment']}\n")
    print("Reviews saved to 55531_6422306_8442488.txt. Exiting...")

# Main function
def main():
    print("Welcome to my ME 021 Python Project!")
    print("Developer: Hernandez, Hector")
    print("My project goal is to develop a review system for professors and courses. It will have inputs of student reviews, professors and course data, with the output of the project being the average ratings, top-rated professors and courses offered at UC Merced!")

    # Load reviews from the saved file
    professor_reviews, course_reviews = load_reviews()

    while True:
        print("\nProfRateUCM - Review System")
        print("1. Add Professor Review")
        print("2. Add Course Review")
        print("3. View Top-Rated Professors")
        print("4. View Top-Rated Courses")
        print("5. Save Reviews and Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_professor_review(professor_reviews)
        elif choice == "2":
            add_course_review(course_reviews)
        elif choice == "3":
            display_top_rated(professor_reviews, "Professors")
        elif choice == "4":
            display_top_rated(course_reviews, "Courses")
        elif choice == "5":
            save_reviews(professor_reviews, course_reviews)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Entry point of the program
if __name__ == "__main__":
    main()
