from bank import value


def main():
    test_hello()
    test_h()
    test_else()


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO!") == 0


def test_h():
    assert value("HEY") == 20
    assert value("Hi") == 20
    assert value("how are you?") == 20


def test_else():
    assert value("Good afternoon") == 100


if __name__ == "__main__":
    main()