import string

uppers = list(string.ascii_uppercase)
case = input("camelCase: ")

for i in case:
    if i in uppers:
        print(case.replace(i, "_" + i.lower()))