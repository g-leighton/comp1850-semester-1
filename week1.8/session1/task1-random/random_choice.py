import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
num = int(input("Enter the amount of names you want to be chosen: "))

# Display the chosen names, one per line
for i in range (0, num):
    choice = random.choice(names)
    names.remove(choice)
    print(choice)