def printList(message, theList):
    print(message)
    for index in range(len(theList)):
        print(theList[index])
    print()
    print()


def main():
    letters = [
        'aaaaaaaaaaaaaa',
        'BBBBBBB',
        'D',
        'ddddddddd',
        'FFFFF',
        'eee'
    ]
    print()
    printList('Original letters\n', letters)

    letters.sort()
    printList('After basic sort\n', letters)

    letters.sort(key=lambda n: n.lower())  # lambda, pick a variable n: then whatever you want to do to n, n.lower()
    printList('After using LAMBDA in sort\n', letters)

    letters.sort(key=lambda n: len(n))
    printList('After sorting by size\n', letters)

main()