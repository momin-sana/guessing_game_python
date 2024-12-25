# we will do the same code, will use color list instead of integers
# also this time we will create method first and then call the method to start the game.

import random

colors = ["green", "blue", "golden", "orange", "grey", "olive", "purple", "black", "pink", "peach", "brown"]

print("Welcome to the Color Guessing Game!")
# we will create a method to start the game

def play_game():
    # we will create a list of random colors
    choosen_color = random.choice(colors)
    guesses_left = 5 # set the number of guesses the player has
    score = 0 #Initialize the score (track the number of attempts)

    print("I'm thinking of a color from the list:", ", ".join(colors))
    print(f"You have {guesses_left} guesses to get it right!")

    # Start the game loop
    while guesses_left > 0:
        # Ask the user for their guess
        user_guess = input("Enter your guess: ").lower()
        # Check if the user's guess is in the list of colors
        if user_guess in choosen_color:
            print(f"Congratulations! You've gueesed the color {choosen_color} correct! You took {score + 1} guesses")
            break
        # If the user's guess is not in the list of colors, decrement the number of guesses
        else:
            print(f"Sorry, {user_guess} is not correct guess. You have {guesses_left} guesses left.")
            guesses_left -= 1
            score += 1
        
        if score == 3:
            # Provide a hint (first letter of the correct color)
            print(f"Hint: The color starts with '{choosen_color[0].upper()}'.")
    
    
    # If the user has no guesses left, end the game and print a message
    if guesses_left == 0:
        print(f"Sorry, you've run out of guesses! The color was {choosen_color}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        print("Lets play again!")
        # Call the method to start the game
        play_game()
    else:
        print("Thanks for playing!")

# start the game by calling the function
play_game()

        
