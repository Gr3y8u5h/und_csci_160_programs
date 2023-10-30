"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 5"""

'''Assignment 
In this lab we will ask the user for information about the classes they are taking this semester, 
and then determine their grade point average (GPA) for that semester. To determine a student’s 
GPA, you divide the number of honor points by the number of attempted (nor passed) credits. 
To determine honor points, for each class multiple the number of credits by either the grades 
honor points; 4 for an A, 3 for a B, 2 for a C, 1 for a D, or 0 for an F. This program will ignore 
grades of pass, fail, or incomplete.  

The program will ask the user for the name of a class. If a class has been entered (such as 
CS160), ask for the number of credits and the grade. Continue to ask for class, and then the 
credits and grade, until the user enters nothing (an empty string) for the class. Do not ask for 
the number of credits and grade if the user does not enter a class.  

For example, if you received a 4 credit A and a 3 credit B in a semester, this is how you 
determine the honor points: 
4 (credits) * 4 (determined from the entered A) = 16 
3 (credits) * 3 (determined from the entered B) = 9  

This input would result in 25 honor points / 7 attempted credits = 3.571429, which would be 
truncated in the output to 3.571.  

Requirements/Assumptions 
You can safely assume that no grade other than A, B, C, D, or F will be entered. 
The grade MUST be entered as a letter grade; it cannot be entered as a number. 
You cannot assume that the grade will be entered as an upper-case letter, if could be upper- or 
lower-case. 
A student’s GPA defaults to 0.0 if their GPA cannot be calculated.   

Output 
Once the user is done entering their classes, print out the following: 
Grade point average, with 3 places after the decimal point 
Number of credits attempts 
Number of credits passed (any grade other than an F) 
Number of classes attempted 
Number of classes passed (any grade other than an F) 
 
Ensure that the final output it in table format, using aligned columns with the text left justified 
and all the numbers right justified. '''

print()  # Brief description of the program and how it works.
print('This program will ask you for the name of your class, the number of credits of the class, and your grade.')
print('When finished leave class name blank and hit enter to see your GPA and credit/class summary.')
print()

# created three lists to store numbers for later use.
honorPointsList = []
studentCreditList = []
creditsPassedList = []

# initialized variables.  Unsure if all variables need initialized, but it doesn't error.
gpaTotal = 0
creditAttempts = 0
creditsPassed = 0
classesAttempted = 0
classesPassed = 0

# first loop to repeat the base questions of the program.
while True:
    print()
    studentClass = input('Enter the name of your class: ')

    # if loop that breaks to finish program if class name left blank.
    if studentClass > '':
        classesAttempted += 1  # running accumulator for classes attempted if a class name entered.

        studentCredit = input('Enter the classes credit hours: ')

        # if loop to verify credits is an integer and > 0.
        # I chose to perform this instead of int(input()) above as to have no program errors.
        # if I chose int(input()) an error would occur if not a integer.
        if studentCredit.isdigit():
            studentCredit = int(studentCredit)
            if studentCredit > 0:
                studentCreditList.append(studentCredit)
            else:
                print('Credits must be greater than zero, Error.')
                break
        else:
            print('Credits must be an integer, Error.')
            break

        studentGrade = input('Enter your grade for the class: ')

        # if loop to assign grade to honor points.
        if studentGrade == "a" or studentGrade == "A":
            studentGrade = 4
        elif studentGrade == "b" or studentGrade == "B":
            studentGrade = 3
        elif studentGrade == "c" or studentGrade == "C":
            studentGrade = 2
        elif studentGrade == "d" or studentGrade == "D":
            studentGrade = 1
        elif studentGrade == "f" or studentGrade == "F":
            studentGrade = 0
        else:  # else, if an inappropriate grade entered.
            print('Grade must be A, B, C, D, or F, Error.')
            break

        # if loop for all passing grades. to accumulate classes passed and create list of passed credits.
        if studentGrade != 0:
            creditsPassedList.append(studentCredit)
            classesPassed += 1

        # honor point expression and list
        honorPoints = studentGrade * studentCredit
        honorPointsList.append(honorPoints)

    else:
        break

# summing lists for final outputs
honorPointsSum = sum(honorPointsList)
creditAttempts = sum(studentCreditList)
creditsPassed = sum(creditsPassedList)
print()

# if loop to help from dividing from zero and to default GPA to 0.0 if found error.
# formatting for outputs as specified.
if creditAttempts > 0:
    gpaTotal = (honorPointsSum / creditAttempts)
    print('GPA:              ', format(gpaTotal, '4.3f'))
else:
    print('GPA, Error:       ', format(int(0), '4.3f'))

print('Credit attempts:  ', format(creditAttempts, '5d'))
print('Credits Passed:   ', format(creditsPassed, '5d'))
print('Classes attempted:', format(classesAttempted, '5d'))
print('Classes passed:   ', format(classesPassed, '5d'))
