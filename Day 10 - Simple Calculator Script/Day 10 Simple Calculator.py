import Day_10_assets as assets
import os


def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def print_header():
    if n1_check == False:
        os.system("cls")
        print(assets.logo)


mainDict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
n1 = 0
operator = ""
n2 = 0
n1_check = False
running = True
while running:
    print_header()
    if n1_check == False:
        n1 = float(input("What's the first number?: "))
    operator = input("+\n-\n*\n/\nPick an operation: ")
    n2 = float(input("What's the next number?: "))
    answer = mainDict[operator](n1,n2)
    print(f"{n1} {operator} {n2} = {answer}")
    event = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'exit' to close the program.\n").lower()
    if event == 'exit':
        running = False
        break
    elif event == 'y':
        n1 = answer
        n1_check = True
    elif event == 'n':
        n1_check = False
    