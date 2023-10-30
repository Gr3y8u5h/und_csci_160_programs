import FileUtils

"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Project 3 - Fall 2021 Part 2"""

"""
Part 2
Requirements:
The only possible grades received are A,B,C,D, or F
The letter grades will always be in upper case
You can set up a separate initialized dictionary for the grades, with the grade as the key
and the associated number of honor points as the value – this will be of help when
determining the GPA. An A is worth 4 honor points, a B is 3 honor points, a C is 2 honor
points, a D is 1 honor point, and an F receives no honor points.

Write each of the following functions. The function headers MUST be written as
specified and each must have a comment block.

REMEMBER TO COMMENT YOUR CODE!
"""

gradesInit = {'A': 4,
              'B': 3,
              'C': 2,
              'D': 1,
              'F': 0}  # used to play with the idea, used occasionally though out to bring in integer honor points.


def readClassInfo(fileName):
    """This function creates a dictionary, and fills it by reading in the information stored in the
    filename variable. Each line in the file will contain a class name, grade for the class, and
    the number credits for the class. Each piece of information is separated by a ':' (colon).
    This must call the function addClass to add the information to the dictionary."""

    inFile = open(fileName, 'r')

    classes = {}  # initializing the dictionary

    for line in inFile:
        className, grade, credits = line.rstrip().split(':', 3)  # splitting up the three data pieces.
        classes[className] = [grade, gradesInit[grade]]  # building the dictionary

    inFile.close()

    print()
    print('The original dictionary list printed')
    printClasses(classes)  # prints the original classes dictionary

    print()
    className = 'Geometry'  # hard coded new className
    print('Hard coded className to add, Geometry')
    classGrade = 'B'  # hard coded className grade
    print('Hard coded className grade to add, B')
    print()

    # used a double variable below to bring back the updated dictionary if updated.
    # also called the function addClass from within this function
    findOrUpdateClass, classes = addClass(classes, className, classGrade, gradesInit[classGrade])
    if not findOrUpdateClass:  # returned False
        print('Returned False; class was already in the dictionary')
    elif findOrUpdateClass:  # returned True
        print('Returned True; classes dictionary was updated with new class.')

    print('The dictionary list with added class printed, or original if class found')
    printClasses(classes)  # prints the added classes dictionary

    return classes  # returned classes as to have the updated dictionary if updated, original if not


def addClass(classes, className, grade, credits):
    """This function will add a class with className to the classes dictionary and return
    True if it was added or False if it is already in the dictionary (meaning the information
    for the class was updated). Note that the classes dictionary will have className for
    key. You do not have to worry about invalid letter grades, if will always be A,B,C, D, or
    F."""

    updatedClass = [grade, credits]  # building the list of grade and credits  to nest within dictionary

    if className in classes:
        return False, classes  # return False if it is already in the dictionary
    else:
        classes[className] = updatedClass  # updating classes with new className, grade, and credits
        return True, classes  # return True if it was added


def attemptedCredits(classes):
    """This function will return the number of attempted credits (NOT classes) – the total of all
    classes taken."""

    classesAccumulated = 0  # initializing the accumulator

    for key in classes:
        classesAccumulated += 1  # created an accumulator for the below expression

    classesCreditAttempted = classesAccumulated * 4  # doing the math to find the attempted credits

    return classesCreditAttempted  # returning the number of attempted credits


def passedCredits(classes):
    """This function will return the number of credits where the students received a passing
    grade (A, B, C, or D)."""

    totalPassedCredits = 0   # initializing the accumulator

    for key in classes:
        credits = int(classes[key][1])  # converting the honor points to integer and assigning a variable
        if classes[key][0] != 'F':  # for A, B, C, or D
            totalPassedCredits = totalPassedCredits + credits  # counts the total of passed credits

    return totalPassedCredits  # returning the number of passed credits


def printClasses(classes):
    """This function will print out all the classes in a neat table, with headings, followed by the
    GPA, with 3 places after the decimal point. An example, with completely made up data,
    might be:

         Class    Grade   Credits
    1. CSci 160:    A           4
    2. CSci 161:    B           4
    3. CSci 289     A           3
    4 . …

    Overall GPA:  3.456
    
    Instead of just using once, I used throughout the program to show different dictionary changes
    """

    count = 1  # creating a count to print along with table so that the classes are numbered

    print()
    print('{:^15s}' .format('Class'), end='')  # Header 1
    print('{:^5s}' .format('Grade'), end='')  # Header 2
    print('%10s' % 'Credits')  # Header 3
    print('------------------------------')  # Header 4

    for key in classes:
        print('{:2d}'.format(count), '.', end='', sep='')  # printing the count
        count += 1  # accumulating the count
        print(' %-15s' % key, end='')  # print the className
        print('{:^5s}' .format(classes[key][0]), end='')  # printing the className grade
        print('{:>6d}' .format(classes[key][1]))  # printing the grade honor point

    print()
    print('Overall GPA: {:.3f}'.format(getGPA(classes)))  # calling getGPA function to print in the table


def getGPA(classes):
    """This function will return the student’s GPA. Remember, GPA is calculated by
    determining the total honor points divided by the total number of credits.
    The honor points for a class are the number of credits multiplied by 4 for an A, 3 for a B,
    2 for a C, 1 for a D and 0 for an F.
    To find the GPA
        • Sum the honor points for each class.
        • Divide the total number of honor points by the total number of credits.

    For example, if a student has a 4 credit A and a 3 credit C, the total number of honor
    points would be 4 * 4 (for the A) + 3 * 2 (for the C), or 16 + 6, or 22.
    The total number of credits would be 4 + 2, or 6.
    The GPA would be 22 / 6, or 3.667 (rounded to three places)."""

    totalClasses = 0  # initializing an accumulator
    creditsList = []  # initializing a list

    for key in classes:  # for every key in the dictionary, class in the dictionary
        credits = int(classes[key][1])  # converting honor points to integer and assigning to a variable
        totalClasses += 1  # counting the number of classes in the dictionary
        creditsList.append(credits)  # adding honor points to a list

    totalGPA = sum(creditsList) / totalClasses  # adding the sum of all the honor points and dividing by the number of classes

    return totalGPA  # returning the totalGPA to the function printClasses


def updateGrade(classes, className, newGrade):
    """If the class exists in the dictionary this function will update the grade of the specified
    class to newGrade and return True . If the class is not in the dictionary return False ."""

    for key in classes:
        if className in classes:  # seeing if hard coded className is in the dictionary
            classes[key][0] = newGrade  # if in the dictionary then update with new grade
            classes[key][1] = gradesInit[newGrade]  # and new honor point
            return True, classes  # returns True and updated classes dictionary
        else:
            return False, classes  # returns False and original classes dictionary


def main():
    """This function will test all the other functions. THERE IS NO NEED TO USE INPUT
    STATEMENTS OR A MENU. You can hardcode all the values when testing. You can
    ask questions in your main program, but it is not a requirement."""

    fileName = FileUtils.selectOpenFile('Select data file: ')  # selects fileName

    if fileName is None:  # if None found then sends an error
        print('Filename does not exist.')

    classes = readClassInfo(fileName)  # calls the function readClassInfo to build the original dictionary

    print()
    # calls the function attemptedCredits and prints the return
    print('Total amount of class credits attempted: ', attemptedCredits(classes))

    print()
    # calls the function passedCredits and prints the return
    print('Total amount of passed credits earned: ', passedCredits(classes))

    print()
    className = 'Math'  # hard coded new className
    print('Hard coded className to update, Math')
    newGrade = 'C'  # hard coded new className grade
    print('Hard coded className grade, C')
    print()
    print('The dictionary list with updated class printed, or original if class not found')
    # calls the function updateGrade and returns two variables
    wasFound, updatedDict = updateGrade(classes, className, newGrade)
    if not wasFound:  # if updateGrade returns False
        print('Return False; class not found')
    if wasFound:  # if updateGrade returns True
        print('Return True; class was found and updated')

    printClasses(updatedDict)  # printing the final dictionary with all updates if added
    print()


main()
