import random

while True:
    try:
        level = int(input("Level: "))  # prompt user for the largest number
        if level <= 0:  # if it's a word or an int < 0, prompt again
            raise ValueError

    except ValueError:  # handle the error appropriately
        pass

    else:
        number = random.randint(1, level)
        while True:
            try:
                users_guess = int(input("Guess: "))
                if users_guess > number:
                    print("Too large!")
                elif users_guess < number:
                    print("Too small!")
                else:
                    print("Just right!")
                    break
            except:
                pass
        break