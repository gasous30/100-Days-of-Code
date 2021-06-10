import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    for resources_type in resources:
        print(f"{resources_type.title()}: {resources[resources_type]}")
    print(f"Money: ${stored_money}")

def check_resources(user_drink):
    for resource_type in resources:
        if(resources[resource_type] < MENU[user_drink]['ingredients'][resource_type]):
            print(f"Sorry, the {resource_type} is not enough.")
            return False
        else:
            return True

stored_money = 0

coin = {
    "quarters": {
        "value": 0.25,
        "sum": 0
    }, 
    "dimes": {
        "value": 0.1,
        "sum": 0
    }, 
    "nickels": {
        "value": 0.05,
        "sum": 0
    }, 
    "pennies": {
        "value": 0.01,
        "sum": 0
    },             
}

def insert_coin(user_drink):
    total_value = 0
    print(f"Please insert your coin.")
    for coin_type in coin:
        coin[coin_type]['sum'] = float(input(f"How much {coin_type}?: "))
        total_value += coin[coin_type]['sum'] * coin[coin_type]['value']
    if total_value > MENU[user_drink]['cost']:
        change = total_value - MENU[user_drink]['cost']
        print (f"Here your ${change:.2f} in change.")

        for resource_type in resources:
            resources[resource_type] -= MENU[user_drink]['ingredients'][resource_type]

        print (f"Enjoy your {user_drink}.")
        return MENU[user_drink]['cost']
    else:
        print (f"Sorry, money is not enough. Money refunded")
        return


os.system("cls")
repeat = True
while repeat:
    user_drink = input(f"What would you like? (espresso/latte/cappuccino): ")
    if(user_drink == 'report'):
        report()
        repeat = True
    elif(user_drink == 'off'):
        repeat = False
    else:
        if(check_resources(user_drink)):
            stored_money += insert_coin(user_drink)
            repeat = True
        else:
            repeat = True
