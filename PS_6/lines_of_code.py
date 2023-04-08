import sys


def main():
    print(command_line())


def command_line():
    counter = 0
    if len(sys.argv) < 2:  # check there's a file to operate on
        return sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:  # and there's only one
        return sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):  # check it's a python file
        return sys.exit("Not a Python File")
    else:
        try:
            file = open(sys.argv[1], "r")  # read the file
            lines = file.readlines()  # read line by line
        except FileNotFoundError:
            return sys.exit("File doesn't exist")
        for line in lines:
            if check_lines(line) is False:
                counter += 1
        return counter


def check_lines(line):
    if line.lstrip().startswith('#') or line.isspace():  # exclude empty lines or comments
        return True
    return False


main()