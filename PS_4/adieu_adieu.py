import inflect
# don't forget to install this package on your machine

p = inflect.engine()

names = []
while True:
    try:
        names.append(input('Name: '))
    except EOFError:
        print('\n', 'Adieu, adieu, to', p.join(names))
        break
