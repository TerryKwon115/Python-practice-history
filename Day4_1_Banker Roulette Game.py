import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1 

print(f"{random.choice(friends)} is the one to pay today.")

# Option 2

length_of_list = len(friends)
random_number = random.randint(0, length_of_list-1)
person_to_pay = friends[random_number]

print(f"{person_to_pay} is the one to pay today.")
