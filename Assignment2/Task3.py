# Ask the user to guess a number (between 1 and 10). Keep asking until they guess right (use while loop)
# number = 5  # The number to guess
number = 5
# guess = 0  # Initialize guess to a value that is not equal to number
guess = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the right number.")
# The code above is a simple number guessing game. The user is prompted to guess a number between 1 and 10. 