months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    print(validate())


def validate():
    while True:
        date_input = input('Date: ').strip()
        try:
            if '/' in date_input and date_input[0].isnumeric():
                month, day, year = date_input.split('/')
            else:
                month_day, year = date_input.split(',')
                month, day = month_day.split(' ')

            if month in months:
                month = months.index(month) + 1

            if int(month) < 1 or int(month) > 12 or int(day) > 31 or int(day) < 1:
                raise Exception('Invalid date. Try MM/DD/YYYY')

            return f'{int(year)}-{int(month):02}-{int(day):02}'

        except ValueError:
            print('Invalid value')
            continue


main()