# Welcome, Today im creating a number guessing game using Python
# In this game the program generates a random number using Python random module (a build-in module)
# The user has to guess the number, and the program will tell the user if the number is high or low, 
# if the guess is correct, it congratulate the player

# To enhance the better experence I'll add guess limits, Allow Replay(ask the user if they want to play again after finishing)
# Track and Display the scores.... an we can add hint system also

# oh one thing more, here instead of integers, you can use floats by using (random.random()) method
#  you can choice from a list or string (e.g. choice a color from list) > lets do this too later

# Lets begin coding...

# Importing the random module
import random

print("Welcome to the Number Guessing Game!")
print("I have picked a random number between 1 to 100. \nYour task is to guess the number.")
print("After each guess, I will tell you if your guess is high or low.")
print("If you guess the number correctly, I will congratulate you and display your score.")
print("You have 10 chances to guess the number. If you lose and couldn't guess the number you can start over, and can play again when game is over.")
print("Let's start the game, Good Luck!!")


while True:

    # Step 1: Generate a random number by program
    random_number = random.randint(1, 100) 
    # here 1 indicates the start value and 100 is the end value, player has to guess between these integers.

    # Step 3: Initialize scores and set the limits and attempts
    total_score = 0
    total_games = 0
    max_attempts = 7
    attempts = 0
    round_score = max_attempts  #Start with maximum score

    # Step 4: Start the game loop
    while attempts < max_attempts:
        try:
            # Step 5: Ask the user for their guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter Your Guess: "))
            # {attempts + 1} : Calculates the current attempt number,
            # (e.g, if attempts is 2, it displays 3 because indexing usually starts from 0, human bases count starts with 1).
            attempts += 1

            if guess < random_number:
                print("Too Low!")
            elif guess > random_number:
                print("Too High!")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
                total_games += 1
                total_score += round_score
                break # Exit the guessing loop

            # Reduce the score with each incorrect attempt
            round_score -= 1

            # Provide a hint after 3 wrong guesses
            if attempts == 3:
                hint = "even" if random_number % 2 == 0 else "odd"
                print(f"Hint: The number is {hint}.")
        
        except ValueError:
            print("Invalid input! Please enter a number.")

    else:
        # If user runs out of attempts
        print(f"Game Over! You have used all {max_attempts} attempts. The number was {random_number}.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print(f"Thanks for playing! Your total score is {total_score} in {total_games} game")
    else:
        print("Lets play again!")

