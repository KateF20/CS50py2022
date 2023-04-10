from datetime import date
import sys
import inflect  # don't forget to install this package on your machine
p = inflect.engine()  # this function creates instance of the InflectionEngine class


def main():
    valid_date = validate(input('Date of Birth: '))
    delta = (date.today() - valid_date).days * 24 * 60  # get delta between today and date of birth + count minutes
    print(get_words(delta))  # call a function to convert numbers to words


def validate(date_of_birth):
    try:
        return date.fromisoformat(date_of_birth)  # ISO format in YYYY-MM-DD
    except ValueError:
        sys.exit('Invalid date')


def get_words(delta):
    in_words = p.number_to_words(delta, andword = '')  # this method converts numbers to word-written numbers
    return in_words.capitalize() + ' minutes'


if __name__ == "__main__":
    main()