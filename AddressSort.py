def printList(message, theList):
    print(message)
    for index in range(len(theList)):
        print(theList[index])
    print()
    print()


def addressesSort(theList):
    for numOfPasses in range(len(theList) - 1):
        for index in range(0, len(theList) - 1 - numOfPasses):  # go through indexes of place not yet in place
            if theList[index] > theList[index + 1]:
                temp = theList[index]
                theList[index] = theList[index + 1]
                theList[index + 1] = temp


def mySort(theList):
    for numOfPasses in range(len(theList) - 1):
        for index in range(0, len(theList) - 1):  # go through indexes of place not yet in place
            firstNumber, firstStreet = theList[index].split(' ', 1)  # only look for the first blank space
            secondNumber, secondStreet = theList[index + 1].split(' ', 1)  # only look for the first blank space
            firstNumber = int(firstNumber)
            secondNumber = int(secondNumber)

            if firstNumber > secondNumber:  # compare by street number
            # if theList[index].lower() > theList[index + 1].lower():  # compare by entire string
                temp = theList[index]
                theList[index] = theList[index + 1]
                theList[index + 1] = temp


def main():

    addresses = [
        '2400 University Ave',
        '1500 University Ave',
        '60 University Ave',
        '900 University Ave'
        ]
    print()
    printList('Initial sort \n', addresses)

    addresses.sort()
    printList('After sort method \n', addresses)

    # back to the original list
    addresses = [
        '2400 University Ave',
        '1500 University Ave',
        '60 University Ave',
        '900 University Ave'
    ]
    addressesSort(addresses)
    printList('After our sort \n', addresses)

    # back to original list
    addresses = [
        '2400 University Ave',
        '1500 University Ave',
        '60 University Ave',
        '900 University Ave'
    ]
    mySort(addresses)
    printList('After mySort \n', addresses)


main()
