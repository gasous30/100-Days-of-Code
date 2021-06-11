from art import logo
import os

# Add
def add(n1, n2):
    return n1 + n2
# Substract
def substract(n1, n2):
    return n1 - n2
# Multiply
def multiply(n1, n2):
    return n1*n2
# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "x" : multiply,
    "/" : divide,
}

def calculator():
    num1 = float(input(f"What is the first number?: "))

    for symbol in operations:
        print(symbol)

    op = input(f"Pick an operation from above: ")
    num2 = float(input(f"What is the second number?: "))
    ans = operations[op](num1,num2)
    print(f"{num1} {op} {num2} = {ans}")

    repeat = input(f"Want to continue calculation with {ans}? Type 'y' for yes and 'n' for start new calculation: ")
    while(repeat == 'y'):
        for symbol in operations:
            print(symbol)

        op = input(f"Pick an operation from above: ")
        new_num = float(input(f"What is the number?: "))
        new_ans = operations[op](ans,new_num)
        print(f"{ans} {op} {new_num} = {new_ans}")
        repeat = input(f"Want to continue calculation with {new_ans}? Type 'y' for yes and 'n' for start new calculation: ")
        ans = new_ans
    return repeat

repeat = 'y'
while repeat == 'y':
    os.system("cls")
    print(logo)
    calculator()

