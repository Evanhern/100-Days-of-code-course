import sys

print("Welcome to Treasure Island.\nYou're mission is to find the treasure.")
choice = input("You are at a cross road. Where do you want to go?\n       Type 'Left' or 'Right'\n")
if choice == "Left":
    choice = input("You've come to a lake. There is an island in the middle of the lake.\n  Type 'Wait' to wait for a boat. Type 'Swim' to swim across.\n")
else:
    print("You fell in a hole and died. GAME OVER!")
    sys.exit()

if choice == "Wait":
    choice = input("A boat arrives and takes you safely to the island. There are three doors to go through.\n  Type 'Red' for the Red door. Type 'Yellow' for the Yellow door. Type 'Blue' for the Blue door.\n ")
else:
    print("You were attacked by a trout and drowned. GAME OVER!")
    sys.exit()

if choice == "Yellow":
    print("Congratulations! You found the treasure! You win!")
elif choice == "Blue":
    print("You were eaten by massive beasts. GAME OVER!")
elif choice == "Red":
    print("You were burned by fire. GAME OVER!")
else:
    print("You chose no door available and were struck by lightening. GAME OVER!")


