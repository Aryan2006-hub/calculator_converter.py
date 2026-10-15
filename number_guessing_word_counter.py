
import random
from collections import Counter
import string
import os


def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("\nGuess the number between 1 and 100!")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess == number:
                score = (max_attempts - attempts + 1) * 10
                print("Correct! You won!")
                print("Attempts:", attempts)
                print("Score:", score)
                return
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")

            print("Attempts left:", max_attempts - attempts)

        except ValueError:
            print("Invalid input! Enter a whole number.")

    print("Game over! The number was", number)
    print("Score: 0")


def word_counter():
    filename = input("Enter text file name: ")

    if not os.path.isfile(filename):
        print("File not found! Create the text file first.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()

        words = [
            word.strip(string.punctuation)
            for word in text.split()
        ]
        words = [word for word in words if word]

        frequency = Counter(words)

        print("Total words:", len(words))
        print("Word frequency:")

        for word, count in frequency.most_common():
            print(word, ":", count)

    except OSError:
        print("Unable to read the file.")


while True:
    print("\n--- Python Utility Tool ---")
    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        number_guessing_game()
    elif choice == "2":
        word_counter()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
