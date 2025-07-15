Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import random

def guess_the_number():
...     secret_number = random.randint(1, 100)
...     attempts = 0
...     max_attempts = 10
... 
...     print("Welcome to the Guess the Number Game!")
...     print("I'm thinking of a number between 1 and 100. Can you guess it? You have 10 attempts.")
... 
...     while attempts < max_attempts:
...         try:
...             guess = int(input("Enter your guess: "))
...             attempts += 1
... 
...             if guess < secret_number:
...                 print("Try higher.")
...             elif guess > secret_number:
...                 print("Try lower.")
...             else:
...                 print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
...                 break
...         except ValueError:
...             print("Invalid input. Please enter a valid number.")
... 
...     if attempts >= max_attempts:
...         print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
... 
... if __name__ == "__main__":
...     while True:
...         guess_the_number()
...         while True:
...             play_again = input("Do you want to play again? (yes/no): ").lower()
...             if play_again == "yes":
...                 break
...             elif play_again == "no":
...                 exit()
...             else:
...                 print("Please enter 'yes' or 'no'.")
