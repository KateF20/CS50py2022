def main():
    g = input("Greeting: ").strip().lower()
    print(value(g))


def value(g):
    if g[: 5] == "hello":
        return 0
    elif g.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()