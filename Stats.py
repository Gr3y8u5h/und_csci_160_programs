def readFile(fileName):
    theList = []
    inFile = open(fileName, 'r')
    for line in inFile:
        line = int(line.strip())
        theList.append(line)
    inFile.close()
    return theList


def getMedian(theList):
    """
    Returns the median from the list
    Returns the "middle' value for a list with an odd number of values
    Returns the average of the middle two values for a list with an even number of values
    Returns None if passed an empty list
    """

    if len(theList) == 0: return None
    sortedList = sorted(theList)
    middleIndex = len(theList) // 2
    if len(sortedList) % 2 == 1:
        return sortedList[middleIndex]
    else:
        return sortedList[middleIndex] + sortedList[middleIndex - 1] / 2


def getMode(theList):
    """Mode means the number that occurs the most
    Returns a mode(s) in a list
    Returns None if passed an empty list"""

    pairs = {}
    if len(theList) == 0:
        return None
    for value in theList:
        if value in pairs:
            pairs[value] = pairs[value] + 1
        else:
            pairs[value] = 1
    valuesList = list(pairs.values())
    maxValue = valuesList[0]
    for value in valuesList:
        if value > maxValue:
            maxValue = value
    valueToReturn = []
    for key in pairs:
        if pairs[key] == maxValue:
            valueToReturn.append(key)
    print()
    valueToReturn.sort()
    return valueToReturn


def main():
    values = readFile('numberList.txt')
    print(values)
    print()

    median = getMedian(values)
    print('Median', median)
    print()

    mode = getMode(values)
    print('Mode', mode)
    print()


main()
