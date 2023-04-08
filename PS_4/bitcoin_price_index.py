import requests  # don't forget to install this package
import sys


if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif float(sys.argv[1]) is False:
    sys.exit("Command-line is not a number")
else:
    n = float(sys.argv[1])

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
o = response.json()
bpi = o['bpi']
USD = bpi['USD']
rate = USD['rate_float']
r = float(rate)

print(o)