import string
import random
import sys

def generator():
    command_list = sys.argv
    lst1 = list(string.ascii_lowercase)
    lst2 = list(string.ascii_uppercase)
    lst3 = list(string.punctuation)
    lst4 = list(string.digits)
    random.shuffle(lst1)
    random.shuffle(lst2)
    random.shuffle(lst3)
    random.shuffle(lst4)
    number_of_characters = int(command_list[1])
    part1 = max(round(number_of_characters * (30 / 100)), 1)
    part2 = max(round(number_of_characters * (20 / 100)), 1)
    password = []
    for i in range(part1):
        password.append(random.choice(lst1))
        password.append(random.choice(lst2))
    for i in range(part2):
        password.append(random.choice(lst3))
        password.append(random.choice(lst4))
    # Ensure password contains at least one character from each type of character
    if len(password) < number_of_characters:
        password.append(random.choice(lst1))
    random.shuffle(password)
    password = "".join(random.sample(password, number_of_characters))
    return password

print(generator())
