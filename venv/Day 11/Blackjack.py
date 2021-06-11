import random
import os
from art import logo

def score(list):
    summ = 0
    for number in list:
        summ += number
    return summ

def change_11(user_card):
    count = 0
    for x in user_card:
        if x == 11:
            count += 1
    if count > 1:
        user_card[user_card.index(11)] = 1


card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


os.system("cls")
print(logo)

player_card = [random.choice(card), random.choice(card)]
computer_card = [random.choice(card), random.choice(card)]
duel = True
change_11(player_card)
change_11(computer_card)
print(f"Your card is {player_card}. Your current score: {score(player_card)}.")
print(f"The first computer's card is {computer_card[0]}.")

take_card = input("Want to take card? Type 'y' to take cards or 'n' no: ")
while(take_card == 'y'):
    player_card.append(random.choice(card))
    change_11(player_card)
    print(f"Your card is {player_card}. Your score: {score(player_card)}.")
    if(score(player_card) > 21):
        print(f"Computer card is: {computer_card}. Computer score: {score(computer_card)}.")      
        print(f"You Lose.")
        take_card = 'n'
        duel = False
    else:
        take_card = input("Want to take card? Type 'y' to take cards or 'n' no: ")
        duel = True

if(duel):
    print(f"Computer card is: {computer_card}. Computer score: {score(computer_card)}.")
    if(score(player_card) > score(computer_card)):
        print(f"You Win.")
    elif(score(player_card) == score(computer_card)):
        print(f"Draw.")
    else:
        print(f"You Lose.")
