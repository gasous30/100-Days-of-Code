#Step 1 
import random


word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
choosen_word = word_list[random.randint(0,len(word_list) - 1)]

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter. Use LowerCase.\n").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for x in range(0, len(choosen_word)):
    if(guess == choosen_word[x]):
        print(f"Right")
    else:
        print(f"Wrong")