import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Level 1 – Easy : Create a password using letters, followed by symbols, and then numbers.
# Level 2 – Hard : Create a password using a random mix of letters, symbols, and numbers.

# Level 1 – Easy (Version 1)

letter = ""
number = ""
symbol = ""

for let in range(nr_letters) : 
    letter += random.choice(letters)

for num in range(nr_numbers) : 
    number += random.choice(numbers)

for sym in range(nr_symbols) : 
    symbol += random.choice(symbols)

password_first = letter + number + symbol

print(f"\nLevel 1 - Easy (Version 1) password : {password_first}\n")

# Level 2 – Hard (Version 1)

password_second = ""

for passwords in range(len(password_first)) : 
    password_second += random.choice(password_first)

print(f"Level 2 - Hard (Version 1) password : {password_second}\n")

# Level 1 – Easy (Version 2)

password = ""

for char in range(0, nr_letters) : 
    password += random.choice(letters)

for char in range(0, nr_numbers) : 
    password += random.choice(numbers)

for char in range(0, nr_symbols) : 
    password += random.choice(symbols)

print(f"Level 1 - Easy (Version 2) password : {password}\n")

# Level 2 – Hard (Version 2)

password_list = []

for char in range(0, nr_letters) : 
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers) : 
    password_list.append(random.choice(numbers))

for char in range(0, nr_symbols) : 
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""

for char in password_list : 
    password += char

print(f"Level 2 - Hard (Version 2) password : {password}\n")
