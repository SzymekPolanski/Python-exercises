"""Insert your birthday date in format YYYY-MM-DD and see how much time do you live in minutes"""

import datetime
import re
import sys


class ChanngingSec:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def prompt(date):

        if re.search(r"^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$", date):

            indx_fist_dash = date.index('-')
            index_second_dash = date.rfind('-')

            year = date[0:indx_fist_dash]
            month = date[indx_fist_dash + 1:index_second_dash]
            day = date[index_second_dash + 1:]
            if month[0] == '0':
                month = month.strip('0')
            if day[0] == '0':
                day = day.strip('0')

            return (int(year), int(month), int(day))
        else:
            sys.exit("Invalid date")

    def to_sec(value):
        date = datetime.date(value[0], value[1], value[2])
        timesince = datetime.date.today() - date
        minutessince = int(timesince.total_seconds() / 60)
        return round(minutessince)


def main():
    insert_date = input("Date of Birth: ")
    prompt = ChanngingSec.prompt(insert_date)
    seconds = ChanngingSec.to_sec(prompt)
    word_num = to_words(seconds)
    print(word_num + " minutes")


def to_words(number):
    import inflect
    inflector = inflect.engine()
    word_number = inflector.number_to_words(number, andword="")
    return word_number.capitalize()


if __name__ == "__main__":
    main()
