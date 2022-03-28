import pandas as pd

nato = pd.read_csv('nato_phonetic_alphabet.csv')
#TODO 1. Create a dictionary in this format:
dict_nato = {name.letter:name.code for (index, name) in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_name = input('What is your name? \n').upper()
phonetic_name = [dict_nato[letter] for letter in input_name]
print(phonetic_name)
