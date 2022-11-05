"""
1. Insert the level
2. Guess the number in range of your level
"""

while True:
    try:
        entry = int(input("Level: "))
        if entry > 0:
            break
        else:
            continue
    except ValueError:
        continue

import random

changed_entry = random.randrange(1, entry + 1)

while True:
    try:
        answer = int(input("Guess: "))
        if answer <= 0:
            continue
        elif answer < changed_entry:
            print("Too small!")
            continue
        elif answer > changed_entry:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
    except ValueError:
        continue
