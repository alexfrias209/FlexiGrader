import requests

NEWS_API_KEY = '37a768b30f9c418fbb1db6145781ecf3'

top_headlines = []

# Function to fetch top headlines from the News API with English language
def fetch_top_headlines():
    url = f'https://newsapi.org/v2/top-headlines?apiKey={NEWS_API_KEY}&language=en'
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'ok':
        top_headlines = [{'title': article['title'], 'score': 0} for article in data['articles']]
        return top_headlines
    else:
        return None

# Function to fetch category-specific news from the News API with English language
def fetch_category_news(category):
    url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={NEWS_API_KEY}&language=en'
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'ok':
        category_news = [{'title': article['title'], 'score': 0} for article in data['articles']]
        return category_news
    else:
        return None

# Function to search for news based on various search options with English language
def search_news():
    while True:
        print("\nSearch Options:")
        print("1. Search by keyword")
        print("2. Search by source")
        print("3. Search by language")
        print("4. Back to Main Menu")

        search_option = input("Enter your search option (1/2/3/4): ")

        if search_option == '1':
            keyword = input("Enter a keyword to search for news: ")
            print(f"Searching for news related to '{keyword}'...")
            # Add code to search and display news based on the keyword.
            # Potentially add a loop here to display multiple search results.

        elif search_option == '2':
            source = input("Enter a news source to search for news: ")
            print(f"Searching for news from '{source}'...")
            # Add code to search and display news based on the source.
            # Potentially add a loop here to display multiple search results.

        elif search_option == '3':
            print("Searching for news in English...")
            # Add code to search and display news based on the language ('en').
            # Potentially add a loop here to display multiple search results.

        elif search_option == '4':
            return  # Return to the main menu

        else:
            print("Invalid choice. Please try again.")

# Function to get the user's name and favorite news topic
def get_user_info():
    user_name = input("Please enter your name: ")
    favorite_topic = input("Please enter your favorite news topic: ")
    return user_name, favorite_topic

# Function to load the user's name and favorite news topic
def load_user_info():
    try:
        with open("61240_6402323_9026783.txt", "r") as file:
            user_info = file.read().strip()
            if user_info:
                user_name, favorite_topic = user_info.split('\n')
                return user_name, favorite_topic
    except FileNotFoundError:
        return None, None

# Function to save the user's name and favorite news topic
def save_user_info(user_name, favorite_topic):
    with open("61240_6402323_9026783.txt", "w") as file:
        file.write(f"{user_name}\n{favorite_topic}")

# Function to rate news articles
def rate_news(news_list):
    while True:
        print("\nRate News Articles:")
        for index, article in enumerate(news_list, start=1):
            print(f"{index}. {article['title']} (Score: {article['score']})")

        article_choice = input("Enter the number to rate an article (0 to go back to the main menu): ")
        if article_choice != '0' and article_choice.isnumeric():
            article_index = int(article_choice) - 1
            if 0 <= article_index < len(news_list):
                rating = input("Rate this article (1-5, 5 being the best): ")
                if rating.isnumeric() and 1 <= int(rating) <= 5:
                    news_list[article_index]['score'] = int(rating)
                else:
                    print("Invalid rating. Please enter a number between 1 and 5.")
            else:
                print("Invalid article number. Please try again.")
        elif article_choice == '0':
            break

# Main program starts here
print("Welcome to My News Aggregator Project!")

while True:
    # Ask for the user's name and favorite news topic every time they use the code
    user_name, favorite_topic = load_user_info()
    if user_name is None:
        user_name, favorite_topic = get_user_info()
        save_user_info(user_name, favorite_topic)

    print(f"Hello, {user_name}! Your favorite news topic is '{favorite_topic}'. Stay updated with the latest news effortlessly.\n")

    # Main Menu
    print("Please choose an option below:\n")
    print("1. Top Headlines")
    print("2. Categories")
    print("3. Search")
    print("4. Rate News Articles")
    print("5. Set User Favorite News Topic")
    print("6. Exit")

    user_choice = input("\nEnter your choice (1/2/3/4/5/6): ")

    if user_choice == '1':
        # Top Headlines Section
        print("\nFetching top headlines...")
        top_headlines = fetch_top_headlines()
        if top_headlines:
            for index, headline in enumerate(top_headlines, start=1):
                print(f"{index}. {headline['title']} (Score: {headline['score']})")

        # Option to view a specific headline
        headline_choice = input("Enter the number to view a headline (0 to go back to the main menu): ")
        if headline_choice != '0' and headline_choice.isnumeric():
            headline_index = int(headline_choice) - 1
            if 0 <= headline_index < len(top_headlines):
                print("\nHeadline:")
                print(top_headlines[headline_index]['title'])
                # You can fetch the full article from the News API using the article URL.

    elif user_choice == '2':
        while True:
            # Categories Menu
            print("\nExplore news by category:\n")
            print("1. Technology")
            print("2. Sports")
            print("3. Entertainment")
            print("4. Back to Main Menu")

            category_choice = input("\nEnter your category choice (1/2/3/4): ")

            if category_choice == '1':
                # Technology News Section
                print("Fetching technology news...")
                technology_news = fetch_category_news('technology')
                if technology_news:
                    for index, article in enumerate(technology_news, start=1):
                        print(f"{index}. {article['title']} (Score: {article['score']})")

                # Option to view a specific article in the category
                article_choice = input("Enter the number to view an article (0 to go back to the category menu): ")
                if article_choice != '0' and article_choice.isnumeric():
                    article_index = int(article_choice) - 1
                    if 0 <= article_index < len(technology_news):
                        print("\nArticle:")
                        print(technology_news[article_index]['title'])
                        # You can fetch the full article from the News API using the article URL.

            elif category_choice == '2':
                # Sports News Section
                print("Fetching sports news...")
                sports_news = fetch_category_news('sports')
                if sports_news:
                    for index, article in enumerate(sports_news, start=1):
                        print(f"{index}. {article['title']} (Score: {article['score']})")

                # Option to view a specific article in the category
                article_choice = input("Enter the number to view an article (0 to go back to the category menu): ")
                if article_choice != '0' and article_choice.isnumeric():
                    article_index = int(article_choice) - 1
                    if 0 <= article_index < len(sports_news):
                        print("\nArticle:")
                        print(sports_news[article_index]['title'])
                        # You can fetch the full article from the News API using the article URL.

            elif category_choice == '3':
                # Entertainment News Section
                print("Fetching entertainment news...")
                entertainment_news = fetch_category_news('entertainment')
                if entertainment_news:
                    for index, article in enumerate(entertainment_news, start=1):
                        print(f"{index}. {article['title']} (Score: {article['score']})")

                # Option to view a specific article in the category
                article_choice = input("Enter the number to view an article (0 to go back to the category menu): ")
                if article_choice != '0' and article_choice.isnumeric():
                    article_index = int(article_choice) - 1
                    if 0 <= article_index < len(entertainment_news):
                        print("\nArticle:")
                        print(entertainment_news[article_index]['title'])
                        # You can fetch the full article from the News API using the article URL.

            elif category_choice == '4':
                break  # Return to the main menu

    elif user_choice == '3':
        search_news()  # Call the search_news function to handle search options

    elif user_choice == '4':
        rate_news(top_headlines)
        rate_news(technology_news)
        # rate_news(sports_news)  # Remove this line
        # rate_news(entertainment_news)  # Remove this line

    elif user_choice == '5':
        user_name, favorite_topic = get_user_info()
        save_user_info(user_name, favorite_topic)

    elif user_choice == '6':
        # Exit
        print("Thank you for using My News Aggregator. Goodbye!")
        break

    else:
        # Invalid Choice
        print("Invalid choice. Please try again.")
