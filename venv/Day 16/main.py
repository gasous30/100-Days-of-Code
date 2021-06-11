from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
Coffee_Maker = CoffeeMaker()
Money_Machine = MoneyMachine()

repeat = True
while repeat:
    user_order = input(f"What do you want to drink? We have: {Menu.get_items()}: ")

    if(user_order == 'report'):
        Coffee_Maker.report()
        Money_Machine.report()
    elif(user_order == 'off'):
        print("Machine OFF")
        repeat = False
    else:
        MenuItem = Menu.find_drink(user_order)
        if(Coffee_Maker.is_resource_sufficient(MenuItem)):
            if(Money_Machine.make_payment(MenuItem.cost)):
                Coffee_Maker.make_coffee(MenuItem)
