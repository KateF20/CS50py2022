import string


def main():
    if is_valid(input('Plate: ')):
        return 'Valid'
    else:
        return 'Invalid'


def is_valid(s):
    punctuation_marks = string.punctuation
    digits = [i for i in s if i.isdigit()]
    print(digits)

    if len(s) < 2 or len(s) > 6:  # check length
        return False

    elif s[0].isdigit() or s[1].isdigit():  # check the first two elements to be letters
        return False

    elif s[-1].isalpha():  # check the last element is not letter
        return False

    for i in range(len(s)):
        if s[i] in punctuation_marks:  # check punctuation marks
            return False

    if len(digits) < 2 or digits[0] == '0':  # check there're at least 2 digits in the place
        return False

    return True


if __name__ == "__main__":
    print(main())