import random

names_string = input("Please input list of names with comma and spaces. Ex: Angela, Joe, Kun, Doewar, Poetra \n")

name = names_string.split(", ")

random_name = name[random.randint(0,len(name)-1)]

print(f"{random_name} is going to buy the meal today.")