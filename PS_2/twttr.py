def main():
    print(shorten(input('Input: ')))


def shorten(word):
    wrd = ''
    for i in range(len(word)):
        if not word[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            wrd += word[i]
    return wrd


if __name__ == "__main__":
    main()