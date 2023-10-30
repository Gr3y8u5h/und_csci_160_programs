"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 8"""

'''
Assignment

Write each of the following functions. The function header must be implemented exactly as
specified. Write a main function that tests each of your functions.

Specifics

In the main function ask for a filename from the user and call fillListFromFile . This will
return a list with the values from the file. Each file should have one numeric value per line.
Reading numbers from a file has been done numerous times in class. You can create the data
file using a text editor or the example given in class – do not create this file in this program.
Then call each of the required functions and then display the results returned from the functions.
Remember that the functions themselves will not display any output, they will return values that
can then be written to the screen.

If there are built in functions in Python that will accomplish the tasks lists below YOU CANNOT
USE THEM. The purpose of this lab is to get practice working with lists, not to get practice
searching for methods. DO NOT sort the list, that changes the order of the items. The order of
the values in the list should be the same as the order of the values in the file.

For each function that returns a numeric value determined from the list, unless otherwise stated
in the function , if you are unable to determine a value return None .
'''


def fillListFromFile(fileName):
    """Creates a list in the function and fills the list with the values from the fileName file.
    Then it returns the list. The file should have one number per line. No error checking is required."""

    theList = []
    for line in fileName:
        line = int(line.rstrip())
        theList += [line]  # creating the list without using methods
    return theList


def findMax(theList):
    """Return the largest integer value found in the list."""

    temp = theList[0]  # using the first integer in the list to start the compare
    for i in theList:
        if temp <= i:
            maxValue = i  # I probably only need to use maxValue or temp, but I used both.
            temp = i
    return maxValue


def findMin(theList):
    """Return the smallest integer value found in the list."""

    temp = theList[0]  # using the first integer in the list to start the compare
    for i in theList:
        if temp >= i:
            minValue = i  # I probably only need to use maxValue or temp, but I used both.
            temp = i
    return minValue


def calcRange(theList):
    """Return the range of values found in the list. The range is the difference between the
    largest and smallest values. This function MUST USE findMax and findMin to determine the
    value to return. This function CANNOT have its own loop."""

    calcRange = findMax(theList) - findMin(theList)
    return calcRange


def calcAverage(theList):
    """Return the average of all the values found in the list."""

    listTotal = 0
    for i in theList:
        listTotal += i
    calcAverage = listTotal / len(theList)
    return calcAverage


def calcGeometricMean(theList):
    """Multiple all of the values in the list together, and then return the nth root of the product,
    where n is the number of items in the list. To calculate the nth root of a value use 1/n as the
    power in an exponential expression. For example, if a lists contains 2, 3, and 7 you would
    multiple 2 * 3 * 7, which returns 42. Then take the 3rd root (n = 3) of 42, which is 3.4760266448864496."""

    listMultiplied = 1
    for i in theList:
        listMultiplied *= i
    calcGeometricMean = listMultiplied ** (1./3)  # found this equation online
    return calcGeometricMean


def findFirst(theList, valueToFind):
    """Return the index of the first occurrence of valueToFind . If valueToFind does not exist
    in the list return -1."""

    indexCount = 0
    for index in theList:
        if valueToFind == index:
            return indexCount
        else:
            indexCount += 1
    return -1


def findLast(theList, valueToFind):
    """Return the index of the last occurrence of valueToFind . If valueToFind does not exist
    in the list return -1."""

    indexCount = len(theList) - 1
    for index in range(len(theList), 0, -1):
        if valueToFind == theList[indexCount]:
            return indexCount
        else:
            indexCount -= 1
    return -1


def findClosestValue(theList, valueToFind):
    """Return the value from the list that is closest (less than or greater than) to valueToFind ."""
    """I will admit I used google for this one, if it seems different in respect to the usual way I code"""

    minValue = findMin(theList)
    closest = None
    closestDist = None
    for i in theList:
        dist = abs(i - valueToFind)
        if closestDist is None or dist < closestDist:
            closest = i
            closestDist = dist
        elif dist == closestDist:
            closest = minValue
    return closest



def calcCount(theList, valueToFind):
    """Return the number of occurrences of valueToFind within the list."""

    totalCount = 0
    for value in theList:
        if value == valueToFind:
            totalCount += 1
    return totalCount


def isInList(theList, valueToFind):
    """Return True if valueToFind occurs at least once in the list, otherwise return False ."""

    for value in theList:
        if value == valueToFind:
            return True
    return False


def main():
    fileName = input('Enter the filename: ')
    inFile = open(fileName, 'r')

    print()
    theList = fillListFromFile(inFile)
    print('The list of the file: ', theList)

    print()
    print('Max Value of the list: ', findMax(theList))

    print()
    print('Min Value of the list: ', findMin(theList))

    print()
    print('The range of the list: ', calcRange(theList))

    print()
    print('The Average of the list: {:.2f}'.format(calcAverage(theList)))

    print()
    print('Geometric Mean of the list: {:.2f}' .format(calcGeometricMean(theList)))

    print()
    valueToFind = int(input('Enter in a int value: '))

    print()
    print('The first occurrence of the int is at index: ', findFirst(theList, valueToFind))

    print()
    print('The last occurrence of the int is at index: ', findLast(theList, valueToFind))

    print()
    print('The value that is closest to the int: ', findClosestValue(theList, valueToFind))

    print()
    print('Number of occurrences of the int in list: ', calcCount(theList, valueToFind))

    print()
    print('If int is in the list then True, otherwise False: ', isInList(theList, valueToFind))

    inFile.close()


main()
