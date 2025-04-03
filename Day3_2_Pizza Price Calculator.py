
# Option 1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?\nS:$15, M:$20, L:$25\nS, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza?\nS:$2, M/L:$3\nY or N: ")
extra_cheese = input("Do you want extra cheese?\nIt's $1\nY or N: ")

price = 0

if size.lower() == "s" : 
    price += 15
    if pepperoni.lower() == "y" : 
        price += 2

elif size.lower() == "m" : 
    price += 20
    if pepperoni.lower() == "y" : 
        price += 3

elif size.lower() == "l" :
    price += 25
    if pepperoni.lower() == "y" : 
        price += 3

else : 
    print("You have chosen an invalid size.")

if extra_cheese.lower() == "y" : 
    price += 1

print(f"Your final bill is : ${price}.\n")

# Option 2

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?\nS:$15, M:$20, L:$25\nS, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza?\nS:$2, M/L:$3\nY or N: ")
extra_cheese = input("Do you want extra cheese?\nIt's $1\nY or N: ")

price = 0

if size.lower() == "s" : 
    price += 15

elif size.lower() == "m" : 
    price += 20

elif size.lower() == "l" : 
    price += 25

else : 
    print("You have chosen an invalid size.")

if pepperoni.lower() == "y" : 
    if size.lower() == "s" : 
        price += 2
    else : 
        price += 3

if extra_cheese.lower() == "y" : 
    price += 1

print(f"Your final bill is : ${price}.")
