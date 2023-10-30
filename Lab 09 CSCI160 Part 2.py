"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 9 Part 2"""

'''Write a program that will ask for a file name containing the information from part 1.
Open the file and fill a list with the contents. The format of the file will be the same as
the file format in part 1. You MUST use a list for this assignment.

Once the list is filled, write and use four different functions. The function header for each
of these functions MUST be written as listed below.

The first function will display to the students and their times in neat columns. The names
must be left justified, the times must be right justified.

def displayTeam (data):

An example of the screen display might be:

Joe Smith                           15:25
Bob Anderson                        18:25

The second function will return the total time of all the students, as a string in the format
of “MM:SS”. It’s possible the minutes could contain up to 3 places. As an example,
given the example data file from part 1, this function would return “”33:50” It might be a
good idea to total the individual minutes and individual seconds of all the students
before determining the overall time.

def findTotalTime (data):

The third function will return a student’s name given an index. Use the list indexes
(0 through the length of the list – 1). Return an empty string if the specified student does
not exist. Make sure the program does not crash if index is invalid.

def getStudent (data, index):

#example calling the function
studentNum = 0
studentName = getStudent (data, studentNum)
print (“Name: “, studentName) # prints Name: Joe Smith

studentNum = 2
studentName = getStudent (data, studentNum)
print (“Name: “, studentName) # prints Name: <<empty sting>>

The fourth function will return the time given a student name. Return an empty string if
the requested student.

def getStudentTime (data, nameToFind):

#example calling the function
nameToFind = “Bob Anderson”
studentTime = getStudentTime (data, nameToFind)
print (“Time for“, nameToFind, “: “, studentTime
# prints Time for Bob Anderson: 18:25

Challenge – no points, just knowledge ☺
Write displayTeam using a for loop that counts through the indexes, and then use
getStudent and getStudentTime to access the information from the list.'''


def displayTeam(data):
    """displayTeam will display the students and their times in neat columns. The names
    must be left justified, the times must be right justified."""

    print()
    for index in range(0, len(data)):
        if index % 2 == 0:
            print(format(data[index], '20s'), end=' ')
        else:
            print(format(data[index], '>8s'))


def findTotalTime(data):
    """findTotalTime will return the total time of all the students, as a string in the format
    of “MM:SS”. It’s possible the minutes could contain up to 3 places. As an example,
    given the example data file from part 1, this function would return “”33:50” It might be a
    good idea to total the individual minutes and individual seconds of all the students
    before determining the overall time."""

    minutesTotal = 0
    secondsTotal = 0
    for index in range(0, len(data)):
        if index % 2 != 0:
            time = data[index]
            minutes, seconds = time.split(':')
            minutes = int(minutes)
            seconds = int(seconds)
            minutesTotal += minutes
            secondsTotal += seconds
    minutesToSeconds = minutesTotal * 60
    totalSeconds = minutesToSeconds + secondsTotal
    totalMinutes = totalSeconds // 60
    totalSeconds = totalSeconds % 60
    totalReturn = str(totalMinutes) + ':' + str(totalSeconds)
    return totalReturn


def getStudent(data, index):
    """getStudent will return a student’s name given an index. Use the list indexes
    (0 through the length of the list – 1). Return an empty string if the specified student does
    not exist. Make sure the program does not crash if index is invalid."""

    if index in range(0, len(data)):
        for i in range(0, len(data)):
            if len(data) - 1 >= i >= 0 and i % 2 == 0:
                if i == index:
                    return data[index]
            elif len(data) - 1 >= i >= 0 and i % 2 == 1:
                if i == index:
                    studentName = data[index - 1]
                    return studentName
    else:
        return ''


def getStudentTime(data, nameToFind):
    """getStudentTime will return the time given a student name. Return an empty string if the
    requested student does not exist."""

    i = 0
    if nameToFind != "":
        foundMatch = False
        for line in data:
            i += 1
            if line.lower() == nameToFind.strip().lower():
                return data[i]
        if not foundMatch:
            return ''
    else:
        return ''


def main():
    """main will ask for a file name containing the information from Lab 09 Part 1.
    Open the file and fill a list with the contents. The format of the file will be the same as
    the file format in part 1. You MUST use a list for this assignment.
    Once the list is filled, write and use four different functions."""

    data = []
    inFile = open('StudentRunTimes.txt', 'r')
    for line in inFile:
        studentName, studentRunTime = line.split('|')
        studentName.strip()
        studentRunTime.strip()
        endOfLine = studentRunTime.find('\n')
        studentRunTime = studentRunTime[0:endOfLine]
        data.append(studentName)
        data.append(studentRunTime)

    print(data)

    print()
    displayTeam(data)

    print()
    print('The total time of all runners is', findTotalTime(data))

    print()
    indexSearch = int(input('Enter in Student #: '))
    print('Name: ', getStudent(data, indexSearch))

    print()
    studentName = input('Enter in a student name: ')
    print('Time for ', studentName, ': ', getStudentTime(data, studentName), sep='')

    inFile.close()


main()
