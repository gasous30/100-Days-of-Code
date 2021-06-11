from art import logo
import os
import random

os.system("cls")
print(logo)
THE_NUMBER = random.randint(1,100)

def check_guess(num):
    cont = True
    if(num > THE_NUMBER):
        print("Too high.")
        return cont
    elif(num < THE_NUMBER):
        print("Too low.")
        return cont
    else:
        print("You're right. You Win.")
        cont = False
        return cont

print(f"This is the answer: {THE_NUMBER}")
print(f"I'm thinking of a number between 1 and 100.")
difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard'.\n").lower()

if difficulty == 'easy':
    lives = 10
else:
    lives = 5

cont = True
while(lives != 0 and cont):
    print(f"Remaining lives: {lives}")
    guess = int(input(f"What is your guess?: "))
    cont = check_guess(guess)
    lives -= 1

if(lives == 0):
    print(f"You've ran out of lives. Game Over.")
    print(f"The number is {THE_NUMBER}")