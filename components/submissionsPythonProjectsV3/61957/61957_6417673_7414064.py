import pandas as pd
import random

# Initialise the current score
current_score = 0
asked_questions = set()  # Tracks asked questions to prevent repetition

# Load and prepare the Jeopardy! dataset
def prepare_jeopardy_data(file_path):
    column_names = ['Show Number', 'Air Date', 'Round', 'Category', 'Value', 'Question', 'Answer']
    
    try:
        df = pd.read_csv(file_path, header=None, names=column_names, skiprows=1, on_bad_lines='skip', low_memory=False)
        if df.iloc[0]['Show Number'] == 'Show Number':
            df = df.iloc[1:].reset_index(drop=True)
        df['Air Date'] = pd.to_datetime(df['Air Date'], format='%Y-%m-%d', errors='coerce')
        df['Value'] = pd.to_numeric(df['Value'].str.replace('[^\d.]', '', regex=True), errors='coerce')
    except Exception as e:
        print(f"An error occurred while reading the CSV: {e}")
        return None

    return df

# Randomly select an episode from the large dataset
def select_random_episode(df):
    show_numbers = df['Show Number'].dropna().unique()
    if show_numbers.size == 0:
        print("No valid show numbers found in the dataset.")
        return None, None

    show_number = random.choice(show_numbers)
    episode_df = df[df['Show Number'] == show_number].reset_index(drop=True)
    return show_number, episode_df

def play_jeopardy(jeopardy_df):
    global current_score, asked_questions
    asked_questions.clear()  # Reset the set of asked questions for a new game

    selected_show, episode_df = select_random_episode(jeopardy_df)

    if episode_df is None:
        return

    # Get the air date of the episode
    air_date = episode_df['Air Date'].iloc[0].date()
    print(f"This...is...Jeopardy! (Try to imagine the iconic theme music)\n"
          f"Welcome to Episode #{selected_show}, originally aired on {air_date}\n")

    # Play the Jeopardy round
    play_round(episode_df, 'Jeopardy!')

    # Double Jeopardy
    play_round(episode_df, 'Double Jeopardy!')

    # Final Jeopardy
    play_final_jeopardy(episode_df)

    # Final score display
    if current_score > 0:
        print(f"Congratulations! You won ${current_score}!")
    else:
        print(f"Game over! You ended with ${current_score}. Better luck next time!")

# Function to play a round (Jeopardy or Double Jeopardy)
def play_round(episode_df, round_name):
    global current_score, asked_questions
    print(f"Now it's time for {round_name}!")
    current_round_df = episode_df[episode_df['Round'] == round_name]
    while len(asked_questions) < len(current_round_df):
        select_question(current_round_df)
        print(f"Your current score is: ${current_score}\n")

# Function to play Final Jeopardy
def play_final_jeopardy(episode_df):
    global current_score, asked_questions
    print("It's time for Final Jeopardy!")
    final_round_df = episode_df[episode_df['Round'] == 'Final Jeopardy!']
    display_categories(final_round_df)
    
    final_jeopardy_category = input("Select a category for Final Jeopardy: ").lower()
    final_jeopardy_wager = float(input("Please enter your wager: $"))
    
    # Filter questions by category and ensure it hasn't been asked
    matching_questions = final_round_df[
        final_round_df['Category'].str.lower() == final_jeopardy_category
    ]
    
    if not matching_questions.empty and all(idx not in asked_questions for idx in matching_questions.index):
        question = matching_questions.iloc[0]
        asked_questions.add(question.name)
        
        print(f"Here's the Final Jeopardy question from {final_jeopardy_category.title()}: {question['Question']}")
        final_answer = input("Your answer: ")
        
        if final_answer.lower() == question['Answer'].lower():
            print("Correct!")
            current_score += final_jeopardy_wager
        else:
            print(f"Sorry, the correct answer is: {question['Answer']}")
            current_score -= final_jeopardy_wager
    else:
        print("That category is not available or the question has already been asked.")

# Function to display categories and their available dollar amounts for a given round
def display_categories(current_round_df):
    categories = current_round_df['Category'].unique()
    print(f"Categories and available dollar amounts for this round:")
    print("---------------------------------------")
    for category in categories:
        # Filter out asked questions for this category
        available_questions = current_round_df[
            (current_round_df['Category'] == category) & (~current_round_df.index.isin(asked_questions))
        ]
        # Get unique values sorted in ascending order
        values = sorted(available_questions['Value'].dropna().unique())
        print(f"{category.title()}: {' '.join(['$' + str(value) for value in values])}")
    print("---------------------------------------")

# Function to select a question based on user input for a given round
def select_question(current_round_df):
    global current_score, asked_questions
    display_categories(current_round_df)
    
    selected_category = input("Select a category: ").lower()
    selected_value = float(input("Select an amount: $"))
    
    # Use lower() on category for case-insensitive comparison and ensure the question wasn't asked before
    matching_questions = current_round_df[
        (current_round_df['Category'].str.lower() == selected_category) & 
        (current_round_df['Value'] == selected_value) & 
        (~current_round_df.index.isin(asked_questions))
    ]
    
    if not matching_questions.empty:
        question = matching_questions.iloc[0]
        asked_questions.add(question.name)
        
        print(f"Question for ${selected_value}: {question['Question']}")
        user_answer = input("What's your answer? ")
        
        if user_answer.lower() == question['Answer'].lower():
            print("Correct!")
            current_score += selected_value
        else:
            print(f"Incorrect. The correct answer was: {question['Answer']}")
            current_score -= selected_value
    else:
        print("That question is not available or has already been asked. Please choose another.")

# Start the game
if __name__ == '__main__':
    file_path = "61957_6417674_1262284.csv"  # File path of Jeopardy! Questions
    jeopardy_df = prepare_jeopardy_data(file_path)
    if jeopardy_df is not None:
        play_jeopardy(jeopardy_df)
