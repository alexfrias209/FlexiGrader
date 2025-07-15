import random
from PIL import Image

States_names = {
    0: 'alabama', 1: 'alaska', 2: 'arizona', 3: 'arkansas', 4: 'california', 5: 'colorado', 6: 'connecticut', 7: 'delaware',
    8: 'florida', 9: 'georgia', 10: 'hawaii', 11: 'idaho', 12: 'illinois', 13: 'indiana', 14: 'iowa', 15: 'kansas',
    16: 'kentucky', 17: 'louisiana', 18: 'maine', 19: 'maryland', 20: 'massachusetts', 21: 'michigan', 22: 'minnesota',
    23: 'mississippi', 24: 'missouri', 25: 'montana', 26: 'nebraska', 27: 'nevada', 28: 'new hampshire', 29: 'new jersey',
    30: 'new mexico', 31: 'new york', 32: 'north carolina', 33: 'north dakota', 34: 'ohio', 35: 'oklahoma', 36: 'oregon',
    37: 'pennsylvania', 38: 'rhode island', 39: 'south carolina', 40: 'south dakota', 41: 'tennessee', 42: 'texas',
    43: 'utah', 44: 'vermont', 45: 'virginia', 46: 'washington', 47: 'west virginia', 48: 'wisconsin', 49: 'wyoming'
}

def state_image(random_pick):
    image_file = f'./pic_stash/{random_pick}.png'
    return Image.open(image_file)

def quiz_setup():
    global score
    user_progress = 0
    while user_progress <= 49:
        randomizing = random.randint(0, 49)
        order = States_names[randomizing]
        final_pic = state_image(order)
        final_pic.show()
        user_attempts = 0
        while user_attempts <= 2:
            user_answer = input().lower()
            if user_answer == order:
                print("Correct!")
                score += 1
                user_progress += 1
                break
            else:
                user_attempts += 1
                turns = 3 - user_attempts
                print(f"Sorry, but you have {turns} more tries.")
        else:
            print(f"Sorry, but the answer was {order}")
            return True

if __name__ == "__main__":
    print('This is a quiz on the 50 states that uses images to test whether you know your states.')
    all_scores = []
    while True:
        score = 0
        result = quiz_setup()
        if result:
            all_scores.append(score)
            highscore = max(all_scores)
            print(f'Your final score is {score}')
            print(f'Your highscore is {highscore}')

        play_again = input('Press enter to try again, or type "quit" to exit: ').lower()
        if play_again == 'quit':
            break