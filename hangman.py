import random

# Predefined list of words
words = ["apple", "bread", "chair", "grape", "house"]

# Randomly select a word from the list
word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Display the word with underscores for unguessed letters
def display_word(word, guesses):
    return " ".join([letter if letter in guesses else "_" for letter in word])

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Main game loop
while incorrect_guesses < max_incorrect:
    print("\n" + display_word(word_to_guess, guessed_letters))
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabetical character.")
        continue

    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! You have {max_incorrect - incorrect_guesses} guesses left.")

    # Check for win condition
    if all(letter in guessed_letters for letter in word_to_guess):
        print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
        break
else:
    print("\n💀 You've run out of guesses. The word was:", word_to_guess)
