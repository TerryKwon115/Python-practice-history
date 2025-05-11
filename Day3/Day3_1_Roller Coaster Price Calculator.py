# Roller Coaster Ticket Price 

print("Welcome to roller coaster.")
height = int(input("What is your height in cm?\n"))

if height > 150 : 
    print("You can ride.")
    age = int(input("What is your age?\n"))
    price = 0
    if age < 12 : 
        print("Child tickets are $5.")
        price += 5
    elif age <= 18 : 
        print("Youth tickets are $7.")
        price += 7
    else : 
        print("Adult tickets are $12.")
        price += 12
    
    # Picture price
    
    picture = input("Do you want to have a photo? It's $3. Y/N\n")
    if picture.lower() == "y" : 
        price += 3
    print(f"Your final bill is ${price}.")

else : 
    print("Sorry. You cannot ride.")
