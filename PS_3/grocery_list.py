li = {}
while True:
    try:
        item = input().upper()
        li[item] = li.get(item, 0) + 1  # if there's no item in a list, add; else increment count

    except EOFError:
        [print(li[key], key) for key in sorted(li.keys())]  # list comprehensions with print

        break
