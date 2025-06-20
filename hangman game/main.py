import random

# 1. Predefined word list
words = ["apple", "banana", "grape", "orange", "peach"]

# 2. Choose a random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# 3. Create display for the word
display_word = ["_" for _ in word]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# 4. Game loop
while wrong_guesses < max_wrong and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
        for idx, letter in enumerate(word):
            if letter == guess:
                display_word[idx] = guess
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

# 5. End of game
if "_" not in display_word:
    print(f"\n🎉 Congratulations! You guessed the word: {word}")
else:
    print(f"\n💀 Game Over! The word was: {word}")
