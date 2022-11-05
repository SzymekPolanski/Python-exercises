"""
Check the current value of the bitcoin
1. Insert in command line python .\current_bitcoin.py "number of bitcoins to show prices"

Example:
python .\current_bitcoin.py 1
Output: current price of one bitcoin in $

"""

import requests
import sys

if len(sys.argv) == 1 :
    sys.exit("Missing command-line argument")
elif sys.argv[1].isdigit() == False and sorted(sys.argv[1])[2] == ".":
    sys.exit("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = response.json()
usd = o["bpi"]["USD"]["rate"]

comma = usd.index(",")
dot = usd.index(".")
usd_float = float(usd[0 : comma]) * 1000 + float(usd[comma + 1:])

equation = float(sys.argv[1]) * usd_float

import math

thousands = math.floor(equation/1000)
hundreds = round(equation - (thousands * 1000), len(usd[dot + 1:]))

str_thousands = str(thousands)
str_hundreds = str(hundreds)

print("$" + str_thousands + "," + str_hundreds)
