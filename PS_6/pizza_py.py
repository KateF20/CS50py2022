import sys
from tabulate import tabulate  # don't forget to download this package on your machine
import csv  # don't forget to add both .csv files to the same directory

if len(sys.argv) < 2:  # check correct input
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:  # check there's only one file given
    sys.exit('Too many command-line arguments')
elif not sys.argv[1].endswith('.csv'):  # check the file is a .csv file
    sys.exit('Not a CSV file')

menu = []
try:
    with open(sys.argv[1], "r") as file:  # open the file in read mode
        reader = csv.reader(file)
        for row in reader:
            menu.append(row)
    print(tabulate(menu[1:], headers = menu[0], tablefmt = 'grid'))  # choose the header and the format of the table

except FileNotFoundError:
    sys.exit('File does not exist')

