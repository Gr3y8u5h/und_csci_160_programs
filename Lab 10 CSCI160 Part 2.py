import FileUtils

"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 10 Part 2"""

"""Write a program that asks the user for a data file and then displays some
information about the data.

First ask the user for the name of the text file. You may use input or FileUtils
to ask for the file name. Fill a dictionary with the values from the data file.

Next, after the dictionary has been filled, write functions that will return various
information about the parts. Write a function to display a menu with the following
choices (very similar to the previous lab), and a function to implement each
choice. Do not use a global variable to store the dictionary.

Display:
• The total number of unique parts
• All parts with a price greater than or equal to $10
• The smallest price
• The largest price
• The average of all prices
• Print parts listRequired Functions

Challenges
Modify the program so that it can determine the mode. The mode is the most
commonly occurring value."""


def readParts(fileName):
    """– Creates a dictionary in the function and fills the
    dictionary with the information from filename file. Return the dictionary after the
    file has been completely read. No error checking is required."""

    inFile = open(fileName, 'r')

    theDictionary = {}

    for line in inFile:
        line = line.rstrip().split('\t')  # stripped of white space and tab
        key = line[0]
        value = float(line[1])  # converted to float early
        theDictionary[key] = value  # creating the dictionary
    inFile.close()
    return theDictionary


def totalParts(theDictionary):
    """– Returns the number of unique parts in
    the dictionary."""

    '''My issue with this function, and it's design, is the word unique.  I've established that the part
    name is the key and the price is the value.  Any data file I build with part names that are the same
    will be truncated to a single part name.  Even during part 1 of lab 10 if I enter a part name twice
    then the second ones value will be stored and the first ones value removed.  So all part names in
    the dictionary are and forever will be unique.  But it does not seem viable to use Price as the key
    and then if two parts have the same price you'll ultimately lose a part name'''

    uniqueCount = 0
    for key in theDictionary:
        uniqueCount += 1
    return uniqueCount


def partsLessThan(theDictionary, upperLimit):
    """– Returns a list of the
    part names with a price less than or equal to the upperLimit variable. The list
    should be created in the function. Return an empty list if no parts have a price
    less than the supplied value."""

    theList = []
    for key in theDictionary:
        if theDictionary[key] <= upperLimit:
            theList.append(key)
    return theList


def leastExpensivePart(theDictionary):
    """– Returns the part name with the
    least expensive price. You can assume that there will be only one part with the
    least expensive price. Return None if you are unable to determine the least
    expensive part."""

    if len(theDictionary) != 0:  # if no dictionary then return none, could not think of no other reason to return none
        leastExpensive = list(theDictionary.values())[0]  # found this on google, used first value to check all others
        for key in theDictionary:
            if theDictionary[key] <= leastExpensive:
                leastExpensive = theDictionary[key]
        return leastExpensive
    else:
        return None


def mostExpensivePart(theDictionary):
    """– Returns the part name with the
    most expensive price. You can assume that there will be only one part with the
    most expensive price. Return None if you are unable to determine the most
    expensive part."""

    if len(theDictionary) != 0:  # if no dictionary then return none, could not think of no other reason to return none
        mostExpensive = list(theDictionary.values())[0]  # found this on google, used first value to check all others
        for key in theDictionary:
            if theDictionary[key] >= mostExpensive:
                mostExpensive = theDictionary[key]
        return mostExpensive
    else:
        return None


def averagePrice(theDictionary):
    """– Returns the average of all parts in the
    dictionary. Return None if you are unable to determine the average."""

    total = 0.00
    if len(theDictionary) != 0:  # if no dictionary then return none, could not think of no other reason to return none
        for key in theDictionary:
            total += theDictionary[key]
        totalAvg = total / len(theDictionary)
        return totalAvg
    else:
        return None


def printParts(theDictionary):
    """- This function WILL write to the display a
    table of each part and its price. Include column headers in the output. Make sure
    the price has two places after the decimal point. Also make sure the columns are
    neatly aligned, with the part column being left justified and the price column being
    right justified. Also ensure that the parts are printed in ascending order. This
    function should not return a value."""

    print()
    print(format('Parts Name', '20s'), end=' ')
    print(format('Part Price', '>5s'))
    keys = list(theDictionary.keys())
    keys.sort()  # couldn't figure out how to lower() a dictionary, or list to apply sort without the upper/lower case
    for part in keys:
        print(format(part, '20s'), end=' ')
        print(format(theDictionary[part], '10.2f'))


def main():
    fileName = FileUtils.selectOpenFile('Select data file: ')

    if fileName is None:
        print('Data file not selected.')
        exit()

    theDictionary = readParts(fileName)

    print()
    print('The Total number of unique parts: ', totalParts(theDictionary))
    print()
    findLessThan = float(input('Enter a price value to find parts <= to that price: '))
    print()
    print('All parts with a price less than or equal to ${:.2f}'.format(findLessThan))
    print()
    print(partsLessThan(theDictionary, findLessThan))
    print()
    leastPrice = leastExpensivePart(theDictionary)
    if leastPrice is not None:
        print('The smallest price, ${:.2f}'.format(leastPrice))
    else:
        print(leastPrice)
    print()
    mostPrice = mostExpensivePart(theDictionary)
    if mostPrice is not None:
        print('The largest price, ${:.2f}'.format(mostPrice))
    else:
        print(mostPrice)
    print()
    avgPrice = averagePrice(theDictionary)
    if avgPrice is not None:
        print('The average of all prices, ${:.2f}'.format(avgPrice))
    else:
        print(avgPrice)
    printParts(theDictionary)


main()
