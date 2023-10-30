def printList(message, theList):
    print(message)
    # for item in theList:
    #     print(item, ' ', end='')
    # or
    for index in range(len(theList)):
        print(theList[index], ' ', end='')
    print()
    print()


def mySort(theList):  # writing our own sort
    # pass  # don't do anything (yet)
    for numOfPasses in range(len(theList) - 1):
        for index in range(0, len(theList) - 1):
            if theList[index].lower() > theList[index + 1].lower():  # go through values not been sorted
                temp = theList[index]  # always need an index variable to swap variables within the list
                theList[index] = theList[index + 1]
                theList[index + 1] = temp


def mySort2(theList):
    for indexToPutInPlace in range(0, len(theList) - 1):
        for index in range(indexToPutInPlace + 1, len(theList)):
            if theList[index] < theList[indexToPutInPlace]:
                temp = theList[index]
                theList[index] = theList[indexToPutInPlace]
                theList[indexToPutInPlace] = temp


def binarySearch(theList):
    letterToFind = input('Look for what letter?: ')
    while letterToFind != '':
        lowIndex = 0
        highIndex = len(theList) - 1
        foundLetter = False
        while lowIndex <= highIndex:
            mid = (highIndex + lowIndex) // 2
            if theList[mid] == letterToFind:
                print('Found it')
                foundLetter = True
                break  # kicks us out of the loop we are in and takes us to the next
            elif theList[mid] > letterToFind:
                highIndex = mid - 1
            else:
                lowIndex = mid + 1
        if lowIndex > highIndex:
            print('Unable to find', letterToFind, 'in the list')
        print()
        letterToFind = input('Now look for what letter?: ')


def main():
    values = ['q', 'z', 'v', 'e', 'p', 'y', 'h', 't', 'o', 'a', 'f', 'w', 'm', 'b', 'i']
    printList('Initial list', values)
    values.sort()
    printList('After Built-in list', values)
    values = ['q', 'z', 'v', 'E', 'p', 'y', 'h', 'T', 'o', 'a', 'f', 'w', 'm', 'b', 'i']
    mySort(values)
    printList('After our sort', values)
    mySort2(values)
    printList('After our sort2', values)
    binarySearch(values)


main()
