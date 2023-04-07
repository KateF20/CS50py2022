money = 0
coins = [5, 10, 25]
while money < 50:
    n = int(input("Insert coins: "))
    if n in coins and n <= 50:
        money += n
        print("Amount due: ", (50 - money))


print("Change owed: ", (money - 50))
