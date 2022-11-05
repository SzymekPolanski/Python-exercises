"""
1. Insert the level in range 1-3
2. Try to solve the problems
3. See your score
"""

import random

def main():
    generate_integer(get_level())

def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                continue
            else:
                break
        except ValueError:
            continue
    return level

def generate_integer(level):
    score = 0
    n = 0
    while n != 10:
        if level == 1:
            x = random.randrange(0,10)
            y = random.randrange(0,10)
        elif level == 2:
            x = random.randrange(10,100)
            y = random.randrange(10,100)

        elif level == 3:
            x = random.randrange(100,1000)
            y = random.randrange(100,1000)

        equation = x + y
        print(x, "+", y, "= ", end="")
        user_result = int(input())

        i = 1
        while i < 4:
            if user_result != equation:
                print("EEE")
                if i == 3:
                    print(x, "+", y, "=", equation)
                else:
                    print(x, "+", y, "=", end="")
                    user_result = int(input())
                i += 1
            else:
                score = score + 1
                break
        n += 1
    print("Score:", score)


if __name__ == "__main__":
    main()
