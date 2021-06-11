import art
from game_data import data
import os
import random

A = data[random.randint(0,len(data)-1)]
B = data[random.randint(0,len(data)-1)]

cond = True
score = 0
print(art.logo)
while (cond):
    os.system("cls")


    print(A['follower_count'])
    print(B['follower_count'])
    
    if(A['follower_count'] > B['follower_count']):
        ans = "A"
        ans_data = A
    else:
        ans = "B"
        ans_data = B

    print(f"Your current score: {score}")
    print('COMPARE: ')
    print(f"A. {A['name']}, {A['description']}, from {A['country']}")
    print(art.vs)
    print(f"B. {B['name']}, {B['description']}, from {B['country']}")


    guess = input(f"Who has more followers? Type 'A' or 'B': ").upper()
    if(guess != ans):
        cond = False
    else:
        score += 1
        A = ans_data
        B = data[random.randint(0,len(data)-1)]
        while(A == B):
            B = data[random.randint(0,len(data)-1)]

if not cond:
    os.system("cls")
    print(art.logo)
    print(f"Your current score: {score}")
