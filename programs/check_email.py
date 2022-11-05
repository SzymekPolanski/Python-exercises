"""Check if the email is valid"""

from validator_collection import checkers

def main():
    print(check_email(input("What's your email address?: ")))

def check_email(email):

    if checkers.is_email(email):
        return 'Valid'
    else:
        return 'Invalid'

main()
