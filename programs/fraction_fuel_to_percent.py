"""
Insert how much do you have in the tank of the car in fraction and see it in percent or 'F' - full or 'E'- empty

Example
Fraction: 1/2
Output: 50%

"""


def main():
    while True:
        try:
            entry = input("Fraction: ")
            print(gauge(convert(entry)))
            break
        except (ValueError, ZeroDivisionError, TypeError):
            pass

def convert(fraction):
    while True:
        indx = fraction.find("/")
        x = fraction[:indx]
        y = fraction[indx+1:]
        solution = (int(x) / int(y) * 100)
        solution = round(solution)
        if 0 <= solution <= 100:
            return solution
        else:
            break

def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif 1 < percentage < 99:
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()
