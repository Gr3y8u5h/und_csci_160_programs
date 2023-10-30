import FileUtils
"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 11 Part 2"""

"""
Part 2
Write a program that asks the user for a data file and then displays some information
about the data.
First ask the user for the name of the text file. You may use input or FileUtils to ask
for the file name. Fill a dictionary with the values from the data file.
Next, after the dictionary has been filled, write functions that will return various
information about the students and their lockers. Write a function to display a menu with
the following choices, and a function to implement each choice. Do not use a global
variable to store the dictionary. Remember, unless the function specifically requests that
you write information to the display, do not write anything to the display.
Make sure your main program thoroughly tests each required function. Make sure your
function headers are written EXACTLY as specified below.
"""


def mainMenu(theDictionary):

    while True:
        print()  # creating the repeating Main Menu
        print('Select the options # to begin')
        print()
        print(' 1. # students with a locker')
        print(' 2. # students with matching names')
        print(' 3. # students with locker # near')
        print(' 4. Smallest locker #')
        print(' 5. Highest locker #')
        print(' 6. Locker # of specific student')
        print(' 7. Student name of specific locker #')
        print(' 8. Print info by student name')
        print(' 9. Print info by locker #')
        print('10. Exit the program')
        print()
        menuSelection = int(input('Enter option #: '))

        if 1 <= menuSelection <= 10:  # verifying the menu option is within range

            if menuSelection == 1:
                print("Total number of students with locker #'s: ", totalStudents(theDictionary))

            elif menuSelection == 2:
                firstLetter = input("Enter the first letter of the students name: ")
                if firstLetter == '':  # exits if no letter is entered
                    print('Invalid Data Selection')
                    exit()
                else:
                    print('List of students with names starting with that letter: ', matchingByName(theDictionary, firstLetter))

            elif menuSelection == 3:
                lowerLimit = int(input('Enter the lower locker number limit: '))
                upperLimit = int(input('Enter the upper locker number limit: '))
                if 0 <= lowerLimit <= 999 and 0 <= upperLimit <= 999:  # verifying if inputs are within range
                    print('List of students with a locker # between the upper and lower limit: ', matchingByLocker(theDictionary, lowerLimit, upperLimit))

            elif menuSelection == 4:
                print('The smallest locker # is: ', firstLocker(theDictionary))

            elif menuSelection == 5:
                print('The largest locker # is: ', lastLocker(theDictionary))

            elif menuSelection == 6:
                studentName = input('Enter the students name: ')
                if studentName != '':  # exits if no name entered
                    print('That students locker # is: ', findLocker(theDictionary, studentName))
                else:
                    print('Invalid Data Selection')
                    exit()

            elif menuSelection == 7:
                lockerNum = int(input('Enter the students locker number: '))
                if 0 <= lockerNum <= 999:  # verifying if input is within range
                    studentFound = findStudent(theDictionary, lockerNum)
                    if studentFound != -1:
                        print('The student with that locker # is: ', studentFound)
                    else:  # if return = -1
                        print('Student not found.')

            elif menuSelection == 8:
                printInfoSortedByStudent(theDictionary)

            elif menuSelection == 9:
                printInfoSortedByLocker(theDictionary)

            else:
                exit()

        else:
            print('Invalid Data Selection')
            exit()


def totalStudents(theDictionary):
    """Returns the number of students with a locker."""

    totalKeys = 0
    for key in theDictionary:
        totalKeys += 1  # accumulating every dictionary entry
    return totalKeys


def matchingByName(theDictionary, firstLetter):
    """Returns a list of the student names where the first letter of their name starts with firstLetter .
    The list should be created in the function. For example, Using the sample data mentioned earlier,
    if the function was used like this: names = matchingStudents (lockingInfo, “S”) names would be a list
    containing two values, “Scott” and “Sue”"""

    nameList = []
    firstLetter.lower()  # lowering the firstLetter input for comparison
    for locker, name in theDictionary.items():
        nameSegmented = list(name.lower())  # splitting the name into characters and lowering
        if nameSegmented[0] == firstLetter:  # comparing the first letter in the split name with firstLetter
            nameList.append(name)  # storing names that are equal
    return nameList


def matchingByLocker(theDictionary, lowerLimit, upperLimit):
    """Returns a list of student names whose locker number falls within the inclusive range of lowerLimit
    to upperLimit . The list should be created in the function."""

    nameList = []
    for locker, name in theDictionary.items():
        locker = int(locker)  # converting the locker # to integer for comparison
        if lowerLimit <= locker <= upperLimit:
            nameList.append(name)  # storing names that have equal locker #'s
    return nameList


def firstLocker(theDictionary):
    """Returns the smallest locker number."""

    minLocker = 1000  # setting min to a value larger than can be entered
    for locker, name in theDictionary.items():
        locker = int(locker)  # converting locker # to integer for comparison
        if locker <= minLocker:
            minLocker = locker  # setting a new minLocker # if lower
    return minLocker


def lastLocker(theDictionary):
    """Returns the largest locker number."""

    maxLocker = -1  # setting max to a value smaller than can be entered
    for locker, name in theDictionary.items():
        locker = int(locker)  # converting locker to integer for comparison
        if locker >= maxLocker:
            maxLocker = locker  # setting a nem maxLocker # if higher
    return maxLocker


def findLocker(theDictionary, studentName):
    """Returns the locker number of the specified student ( studentName ). Returns an empty string if
    studentName is not the name of a current student."""

    studentNameLower = studentName.rstrip().lower()  # converting studentName for comparison
    for locker, name in theDictionary.items():
        nameLower = name.rstrip().lower()  # converting dictionary name for comparison
        if nameLower == studentNameLower:
            return int(locker)  # returning locker # in integer form of student name
    return ''  # returning an empty string if no current student


def findStudent(theDictionary, lockerNum):
    """Returns the student name associated with the specified locker ( lockerNum ). Returns -1 if lockerNum
    is not the locker number of a current student."""

    for locker, name in theDictionary.items():
        intLocker = int(locker)  # converting locker # to integer for comparison
        if lockerNum == intLocker:
            return name  # returning the name of the student if found
    return -1  # returning -1 if not found


def printInfoSortedByStudent(theDictionary):
    """This function WILL write to the display a table of each student and their locker number. Include column
    headers in the output. Also make sure the columns are neatly aligned, with the student name being left
    justified and the locker number being right justified. This function should not return a value. The info
    should be sorted by student name."""

    print()
    print(format('List sorted by student name', '^30s'))  # Header 1
    print(format('Student Name', '15s'), end='')  # Header 2
    print(format('Student Locker #', '15s'))  # Header 3
    print('-------------------------------')  # Header 4
    sortedDict = sorted(theDictionary.values())  # sorting the dictionary using the values (names)
    for sortedName in sortedDict:  # going through the sorted names
        for locker, name in theDictionary.items():  # finding the sorted names in the dictionary
            if sortedName == name:  # comparing sorted name to original dictionary to print
                intLocker = int(locker)  # converting locker # to integer for right justified printing
                print(format(name, '15s'), end='')
                print(format(intLocker, '16d'))


def printInfoSortedByLocker(theDictionary):
    """This function is identical to the printInfoSortedByStudent , with the difference that the info should be
    sorted by locker number."""

    print()
    print(format('List sorted by locker #', '^30s'))  # Header 1
    print(format('Student Name', '15s'), end='')  # Header 2
    print(format('Student Locker #', '15s'))  # Header 3
    print('-------------------------------')  # Header 4
    updatedDict = {}  # creating a new dictionary to store keys in integer form to sort later
    for key, value in theDictionary.items():
        updatedDict[int(key)] = value  # updating new dictionary with integer keys
    sortedDict = sorted(updatedDict.keys())  # creating new list with the integer keys of new dictionary
    for sortedKey in sortedDict:  # going through the sorted keys list
        for locker, name in updatedDict.items():
            if sortedKey == locker:  # comparing sorted keys list with dictionary key (locker #)
                print(format(name, '15s'), end='')
                print(format(locker, '16d'))


def main():

    theDictionary = {}  # initializing the main dictionary
    fileName = FileUtils.selectOpenFile()

    if fileName is None:  # exits if no file is selected
        print()
        print('Invalid Data Selection')
        exit()

    inFile = open(fileName, 'r')

    for line in inFile:  # creating the new dictionary
        name, locker = line.rstrip().split(':')
        theDictionary[locker] = name

    mainMenu(theDictionary)  # calling the mainMenu that will access all the other functions

    
main()
