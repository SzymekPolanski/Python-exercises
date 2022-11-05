"""If you are from Massachusetts (or not :) ), you can check if text on your registration is valid"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


    for x in s:
            if x in punctuations:
                return False

    for el in s:

        if 2 <= len(s) <= 6 and s[0:1].isdigit() == False:

            if (s[-1].isdigit() == True and s[-2].isdigit() == False ) or (s[-1].isdigit() == False and s[-2].isdigit() == True):
                return False

            elif (el != "0" and el.isdigit() == True and s[-1].isdigit() == True and s[2] != 0) or \
                (s[0:2].isdigit() == False and s[2] != "0"):
                return True

            else:
                return False
        else:
            return False


if __name__ == "__main__":
    main()
