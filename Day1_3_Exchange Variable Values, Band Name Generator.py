
# Exchange Variable Values

glass1 = "milk"
glass2 = "juice"

glass3 = glass1
glass1 = glass2
glass2 = glass3

print(glass1)
print(glass2)

# Band Name Generator

print("Welcome to the Band Name Generator.")
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
print("Your band name could be " + city_name + " " + pet_name +".")
print(f"Your band name could be {city_name} {pet_name}.")
