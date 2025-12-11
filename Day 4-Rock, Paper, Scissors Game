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


user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

random_generation = random.randint(0,2)

if user_input == 0:
    print("You chose: Rock")
    print(rock)
    if random_generation == 0:
        print("Computer chose: Rock")
        print(f"{rock}\nThis round is a Draw.")
    elif random_generation == 1:
        print("Computer chose: Paper")
        print(f"{paper}\nThis round is a Loss.")
    elif random_generation == 2:
        print("Computer chose: Scissors")
        print(f"{scissors}\nThis round is a Win.")
    
elif user_input == 1:
    print("You chose: Paper")
    print(paper)
    if random_generation == 0:
        print("Computer chose: Rock")
        print(f"{rock}\nThis round is a Win.")
    elif random_generation == 1:
        print("Computer chose: Paper")
        print(f"{paper}\nThis round is a Draw.")
    elif random_generation == 2:
        print("Computer chose: Scissors")
        print(f"{scissors}\nThis round is a Loss.")
    
elif user_input == 2:
    print("You chose: Scissors")
    print(scissors)
    if random_generation == 0:
        print("Computer chose: Rock")
        print(f"{rock}\nThis round is a Loss.")
    elif random_generation == 1:
        print("Computer chose: Paper")
        print(f"{paper}\nThis round is a Win.")
    elif random_generation == 2:
        print("Computer chose: Scissors")
        print(f"{scissors}\nThis round is a Draw.")
else:
    print("Please type a valid selection.")
