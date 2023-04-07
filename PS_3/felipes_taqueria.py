menu = {
    'Baja Taco': 4.00,
    'Burrito': 7.50,
    'Bowl': 8.50,
    'Nachos': 11.00,
    'Quesadilla': 8.50,
    'Super Burrito': 8.50,
    'Super Quesadilla': 9.50,
    'Taco': 3.00,
    'Tortilla Salad': 8.00
}
orders = 0

while True:
    try:
        order = input("Your order: ").title()
        if order in menu:
            orders += menu[order]
            print("Total: $", "{:.2f}".format(orders), sep="")
    except EOFError:
        print('Your order is ', orders)
        break
