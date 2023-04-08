import random


def main():
    print("Score: ", get_score(get_level()))


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def get_score(level):
    rounds = 1
    total = 0
    while rounds < 11:
        first_elem = generate_integer(level)
        second_elem = generate_integer(level)
        result = math_problem(first_elem, second_elem)
        if result is True:
            total += 1
        rounds += 1
    return total


def generate_integer(level):
    if level == 1:
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10, 99)
    elif level == 3:
        integer = random.randint(100, 999)

    return integer


def math_problem(x, y):
    errors = 0
    while errors < 3:
        try:
            task = int(input(f'{x} + {y} = '))
        except ValueError:
            pass

        else:
            if task == (x + y):
                return True
            else:
                print("EEE")
                errors += 1

    if errors == 3:
        print(f'{x} + {y} = {x+y}')
    return False





if __name__ == "__main__":
    main()