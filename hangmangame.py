import random

def hangman():
    # List of words to choose from
    words = ["python", "hangman", "challenge", "programming", "developer", "algorithm"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    guessed_letters = set()
    attempts = 6  # Number of attempts to guess the word

    print("Welcome to Hangman!")
    print("Try to guess the word before you run out of attempts.")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            attempts -= 1
            print(f"'{guess}' is not in the word. You have {attempts} attempts left.")

        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()
