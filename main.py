import random
from list_of_words import word_list
from diagrams import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Testing code
#print(f"Hey, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display.append('_')

guessed_letters = []  # Keep track of guessed letters

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue  # Skip the rest of the loop and start the next iteration

    guessed_letters.append(guess)

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print(stages[0])  # Display the final Hangman stage
            end_of_game = True
            print(f"You lose. The correct word is {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("Congrats! You won.")

    if not end_of_game:
        print(stages[lives])
