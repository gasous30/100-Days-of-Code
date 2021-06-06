# FINAL PROJECT

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper,  scissors]

user = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

user_rps = rps[user]
comp_choices = random.randint(0,2)
comp_rps = rps[comp_choices]
print("You choose: \n")
print(user_rps)

print("Computer choose: \n")
print(comp_rps)

if(user == 2):
    if(comp_choices == 2):
        print("DRAW")
    elif(comp_choices == 1):
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
elif(user == 1):
    if(comp_choices == 1):
        print("DRAW")
    elif(comp_choices == 0):
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
elif(user == 0):
    if(comp_choices == 0):
        print("DRAW")
    elif(comp_choices == 2):
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
else:
    print("Invalid Number")