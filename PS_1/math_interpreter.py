def interpreter(x, y, z):
    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '*':
        return x * z
    elif y == '/':
        return x / z


x, y, z = input("Expression: ").split(" ")
print("{:.1f}".format(interpreter(int(x), y, int(z))))