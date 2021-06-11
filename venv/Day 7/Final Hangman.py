#FINAL

import random
import hangman_art as art
import hangman_words as word
import os
os.system("cls")

chosen_word = random.choice(word.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guessed_letter = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("cls")
    
    if guess in guessed_letter:
        print(f"You've already entered letter {guess}.")
    
    guessed_letter.append(guess)
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter is not in the word.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(art.stages[lives])