def main():
    print(get_gauge(get_fuel()))


def get_fuel():
    while True:
        try:
            a, b = input("Fraction: ").split('/')
            valid_fuel = round(float(int(a) / int(b)) * 100)
        except ValueError:
            print('ValueError')
            continue

        except ZeroDivisionError:
            print('ZeroDivisionError')
            continue

        else:
            return valid_fuel


def get_gauge(fuel):
    if int(fuel) <= 1:
        return 'E'
    elif int(fuel) >= 99:
        return 'F'
    else:
        return str(fuel) + '%'


if __name__ == "__main__":
    main()