import sys
import csv  # don't forget to download initial .csv filesin the same directory


def main():
    check_command_line()
    read_write()


def check_command_line():
    if len(sys.argv) < 3:  # check there's correct number of files given
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:  # check both files are .csv files
        sys.exit('Not a CSV file')


def read_write():
    firstName_lastName_house = []  # make an empty list
    try:
        with open(sys.argv[1], 'r') as b_file:
            reader = csv.DictReader(b_file)  # create the dictionary from the .csv file
            for row in reader:
                first_name, last_name = row['name'].split(',')
                firstName_lastName_house.append({
                    'first': first_name, 'last': last_name, 'house': row['house']
                })

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

    fieldnames = ['first', 'last', 'house']
    with open(sys.argv[2], 'w') as a_file:
        writer = csv.DictWriter(a_file, fieldnames=fieldnames)  # write into a new .csv file
        writer.writeheader()
        writer.writerows(firstName_lastName_house)


if __name__ == "__main__":
    main()