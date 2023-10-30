import FileUtils

"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Project 2 - Fall 2021"""

"""
Assignment

Write each of the following functions. The function header must be implemented exactly as
specified. Write a main function that tests each of your functions.

Specifics

In the main function ask for a filename and use the required function to fill a list with the values
from the file. Each file should have one numeric value per line. This has been done numerous
times in class, and in a previous lab assignment. You can create the data file using a text editor
or the example given in class – do not create this file in this program. Then call each of the
required functions and then display the results returned from the functions. Remember, unless it
is specifically stated to do so, the functions themselves will not display any output. They will
return values that can then be written to the screen, or they may alter the list passed to the
function.

If there are built in functions in Python that will accomplish the tasks lists below YOU CANNOT
USE THEM. The purpose of this lab is to get practice working with lists, not to get practice
searching for methods. DO NOT sort the list, that changes the order of the items. The order of
the values in the list should be the same as the order of the values in the file.

Do not alter the list unless the function specifically asks you to alter the list.

Do not return a list, or any value, unless the function specifically asks you to do so.

Your main program can ask for input, but it does not have to. It DOES need to test all of your
functions, and more than once, with different data each time.

Exit the program immediately if the file name specified does not exist.
"""


def fillList(fileName):
    """Creates, fills, and returns a list with values read from the specified file.
    Returns None is filename does not exist."""

    if fileName is None:
        print('Filename does not exist.')
        return None

    inFile = open(fileName, 'r')

    theList = []

    for line in inFile:
        line = line.rstrip()
        line = int(line)
        theList.append(line)

    inFile.close()

    return theList


def printList(message, theList):
    """Prints the message on one line, then all of the values
    on a single line, with each value taking 5 spaces total, and then two blank lines. This function
    prints a total of 4 lines of output when called."""

    print(message)
    for value in theList:
        print('%-5d' % value, end='')
    print()
    print()


def updateList(theList, change):
    """Adds change to each value in theList . This function does not return anything."""

    for i in range(len(theList)):
        j = change + theList[i]
        theList[i] = j


def mergeLists(theList1, theList2):
    """ Creates a new list, appending the values from
    theList1 and theList2 (in that order) and returns the new list."""

    newList = theList1 + theList2

    return newList


def adjustList(theList, lowerLimit, upperLimit):
    """Adjusts the values in theList such that if any value is less than lowerLimit it is adjusted to lowerLimit,
    or if any value is greater than upperLimit it is adjusted to upperLimit . This function does not return anything."""

    for digit in range(len(theList)):
        if theList[digit] < lowerLimit:
            theList[digit] = lowerLimit
        elif theList[digit] > upperLimit:
            theList[digit] = upperLimit


def count(theList, valueToCount):
    """returns the number of occurrences of valueToCount in theList."""

    valueCount = 0
    for digit in theList:
        if digit == valueToCount:
            valueCount += 1

    return valueCount


def valuesAreUnique(theList):
    """returns True if every value in the list is unique(only occurs once), otherwise returns False."""

    valueCount = 0
    for val in theList:
        tmp = val  # holds each value as tmp for testing
        for val in theList:
            if val == tmp:
                valueCount += 1  # when the value == tmp valueCount will progress
    if valueCount == len(theList):
        return True  # if valueCount == length of the list then all values are unique
    else:
        return False



def inAscendingOrder(theList):
    """Returns True if the list is in ascending order, otherwise returns False."""

    isAscending = False
    for val in range(len(theList) - 1):
        if theList[val] <= theList[val + 1]:  # goes through and compares each value to the next one
            isAscending = True
        else:
            return False  # if a value is greater than the value to the right then returns False
    return isAscending



def inDescendingOrder(theList):
    """Returns True if the list is in descending order, otherwise returns False."""


    isDescending = False
    for val in range(len(theList) - 1):
        if theList[val] >= theList[val + 1]:  # goes through and compares each value to the next one
            isDescending = True
        else:
            return False  # if a value is less than the value to the right then returns False
    return isDescending


def matchingValues(theList, lowerLimit, upperLimit):
    """Creates, fills, and returns a
    list with all of the values from theList that fall within the inclusive range of lowerLimit and
    upperLimit . DO NOT alter the original list."""

    theListAdjusted = []  # created a new list as not to alter the original

    for digit in range(len(theList)):
        if lowerLimit <= theList[digit] <= upperLimit:  # if between lower and upper
            theListAdjusted.append(theList[digit])  # append the value to the new list

    return theListAdjusted  # returning the new list


def main():
    """In the main function ask for a filename and use the required function to fill a list with the values
from the file. Each file should have one numeric value per line. This has been done numerous
times in class, and in a previous lab assignment. You can create the data file using a text editor
or the example given in class – do not create this file in this program. Then call each of the
required functions and then display the results returned from the functions. Remember, unless it
is specifically stated to do so, the functions themselves will not display any output. They will
return values that can then be written to the screen, or they may alter the list passed to the
function."""

    fileName = FileUtils.selectOpenFile('Select data file: ')

    theList = (fillList(fileName))

    print()
    message = 'Data File List'
    printList(message, theList)

    change = int(input('How much of a change would you like to add?: '))
    updateList(theList, change)
    print()

    theList1 = [1, 2, 4, 6, 8, 9]  # a generic list
    theList2 = [10, 12, 15, 20, 21]  # a generic list
    print('theList1 =', theList1)
    print('theList2 =', theList2)
    print('The lists merged')
    print(mergeLists(theList1, theList2))
    print()

    lowerLimit = int(input('Enter in a lower limit: '))
    upperLimit = int(input('Enter in an upper limit: '))
    adjustList(theList, lowerLimit, upperLimit)
    print('The list adjusted')
    print(theList)
    print()

    valueToCount = int(input('Enter a value to count in the list: '))
    print('That number occurs ', count(theList, valueToCount), ' times.', sep='')
    print()

    print('All values are unique: ', valuesAreUnique(theList))
    print()

    print('All values are in Ascending order: ', inAscendingOrder(theList))
    print()

    print('All values are in Descending order: ', inDescendingOrder(theList))
    print()

    lowerLimit = int(input('Enter in a lower limit: '))
    upperLimit = int(input('Enter in an upper limit: '))
    print('All values that fall within the limits: ', matchingValues(theList, lowerLimit, upperLimit))
    print()

main()
