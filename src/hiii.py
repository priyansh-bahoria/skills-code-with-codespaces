
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")
print("I have selected a number between 1 and 100.")
print("Can you guess it?")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            attempts -= 1
        elif guess < secret_number:
            print("Too low! Try a bigger number.")
        elif guess > secret_number:
            print("Too high! Try a smaller number.")
        else:
            print(f"\nCorrect! You guessed the number!")
            print(f"The number was {secret_number}.")
            print(f"You took {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")
