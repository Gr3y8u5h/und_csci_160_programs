import FileUtils
"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 11 Part 1"""

"""
Part 1
Write a program to ask for a series of student names and locker numbers. You can
assume that each student will have their own locker. Ask for a student name until the
user enters a blank value. For every valid student name ask for their locker number. Fill
a dictionary with this data. Once the user has finished entering data ask for a file name.
You may use input or FileUtils to ask for the file name. Write out each part
name/locker number pair in the dictionary to the data file, one pair per line. Separate the
part name and price with a colon, so do not enter a colon as part of the student name.
For this assignment limit the student names to the single name, such as “Tom”, “Scott”,
or “Sue”. The locker numbers will be integer values, with a maximum of 3 digits.
"""


def getInfo():
    """Asks user for student names and locker numbers.  Stores the values to a dictionary.
    Exits user input if a blank value is enter in name or if locker number
    is less than 0 or greater than 999"""

    studentInfoDict = {}
    while True:
        print()
        studentName = input('Enter in a students name: ')  # Student name outside the loop to repeat
        if studentName != '':  # a blank student name will exit
            studentLockerNum = int(input('Enter in the students locker number: '))
            if 0 <= studentLockerNum <= 999:  # only accepting integers of 3 values
                studentInfoDict[studentName] = studentLockerNum  # creating the dictionary
            else:
                break
        else:
            break
    return studentInfoDict


def writeFile(myDict):
    """Writes the dictionary to a file utilizing FileUtils, one pair key/value per line,
    seperated by a colon. Closes the file."""

    fileName = FileUtils.selectOpenFile()



    if fileName is None:  # Show error if no file selected
        print('Data file not selected.')
        exit()

    inFile = open(fileName, 'w')

    for key, value in myDict.items():  # writing to the file and creating the database as specified
        inFile.write(key)
        inFile.write(':')
        inFile.write(str(value))
        inFile.write('\n')

    inFile.close()


def main():
    """Calls the two functions getInfo and writeFile"""

    studentDict = getInfo()
    writeFile(studentDict)


main()
