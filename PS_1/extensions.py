extensions = ['gif', 'jpg', 'jpeg', 'png', 'pdf', 'txt', 'zip']


def main():
    n = input("Document name: ").split('.')
    print(*name(n[1]), sep='') # print elements of the list


def name(n):
    if n == 'gif' or n == 'png':
        return 'image/', n

    elif n == 'jpeg' or n == 'jpg':
        return "image/jpeg"

    elif n == 'pdf' or n == 'zip':
        return 'application/', n

    elif n == 'txt':
        return "text/plain"

    else:
        return "application/octet-stream"


main()