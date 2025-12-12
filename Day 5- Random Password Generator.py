import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcom to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password_list?\n"))
num_numbers = int(input("How many numbers would you like in your password_list?\n"))
num_symbols = int(input("How many symbols would you like in your password_list?\n"))
characters = [num_letters,num_numbers,num_symbols]
for number in range(1,3):
    if characters[number] == 0:
        del characters[number]

password_list = []
for char in range(0,num_letters):
    rand_char = random.choice(letters)
    up_or_low = random.randint(1,2)
    if up_or_low == 1:
        rand_char = rand_char.upper()
    
    password_list += rand_char

for char in range(0,num_numbers):
    password_list += random.choice(numbers)

for char in range(0,num_symbols):
    password_list += random.choice(symbols)
    
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
    

