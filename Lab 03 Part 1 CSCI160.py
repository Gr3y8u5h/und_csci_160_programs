"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 3 Part 1"""

print('Lab 3, Part 1, a)')
"""a) Ask for a year. State whether or not the year is with the range of 2020 to 2029 inclusive."""
print()
year = int(input('Please enter a year to determine if range is between 2020 and 2029: '))
if 2020 <= year <= 2029:
    print('That year is within the range of 2020 to 2029.')
else:
    print('That year is not within the range of 2020 to 2029.')
print()

print('Lab 3, Part 1, b)')
"""b) Ask for the number of credits a student has passed. State whether the student is a
freshman (0-23), sophomore (24-59), junior (60-89), or senior (90 or greater)."""
print()
creditsPassed = int(input('Enter number of credits passed to determine grade level: '))
if creditsPassed > 0:
    if creditsPassed >= 90:
        student = 'senior'
    elif 60 <= creditsPassed < 90:
        student = 'junior'
    elif 24 <= creditsPassed < 59:
        student = 'sophomore'
    else:
        student = 'freshman'
    print('You are a', student)
else:  # used in case a negative inappropriate number used.
    print('Number should be greater than or equal to zero(0)')
print()

print('Lab 3, Part 1, c)')  # combined parts c and d.
print('Lab 3, Part 1, d)')
"""c) Ask for a grade point average. Using labels from some table I found, state whether the
student’s gpa is “Excellent” (= 4.0), “Very good” (>= 3.7), “Good” (>= 3.0), “Above
average” (>= 2.7), “Average” (>= 2.4), “Satisfactory” (>= 2.0), or “Poor” (< 2.0)."""
"""d) Using the inputs from the previous two questions, state whether the student is eligible for
graduation. For this question, to be able to graduate the student needs a gpa >= 2.2 and
have passed 120 credits. Do not ask for additional inputs in this question."""
print()
gradePointAvg = float(input('Enter your gpa to determine if gpa is adequate and your graduation eligibility: '))
if 0.0 <= gradePointAvg <= 4.0:  # used double if's in case integer enter is not with range.
    if gradePointAvg >= 2.0:
        if gradePointAvg == 4.0:
            gpaLabels = 'Excellent'
        elif 3.7 <= gradePointAvg < 4.0:
            gpaLabels = 'Very good'
        elif 3.0 <= gradePointAvg < 3.7:
            gpaLabels = 'Good'
        elif 2.7 <= gradePointAvg < 3.0:
            gpaLabels = 'Above average'
        elif 2.4 <= gradePointAvg < 2.7:
            gpaLabels = 'Average'
        elif 2.0 <= gradePointAvg < 2.4:
            gpaLabels = 'Satisfactory'
    else:
        gpaLabels = 'Poor'
    print('Your gpa is ', gpaLabels, '.', sep='')
else:
    print('Number must be between 0.0 and 4.0.  Try again.')
if 0.0 <= gradePointAvg <= 4.0:  # used to verify eligibility.
    if 2.2 <= gradePointAvg <= 4.0 and creditsPassed >= 120:
        graduationEligible = 'eligible'
    else:
        graduationEligible = 'not eligible'
    print('You are', graduationEligible, 'to graduate.')
else:  # used in case the integer is not within gpa range.
    print('Eligibility is uncertain.  Retry with an appropriate gpa.')
print()

print('Lab 3, Part 1, e)')
"""e) Have the user enter an integer value. State whether that value is, or is not, a multiple of
5. IF the value is a multiple of 5, then state if it is even or odd."""
print()
value1 = int(input("Enter an integer value to find out if it's a multiple of 5 and even or odd: "))
if value1 % 5 == 0:  # to determine if multiple of 5.
    print(value1, 'is a multiple of 5.')
else:
    print(value1, 'is not a multiple of 5.')
if value1 % 2 == 0:  # to determine if even or odd.
    print(value1, 'is an even number.')
else:
    print(value1, 'is an odd number.')
print()

print('Lab 3, Part 1, f)')
"""f) Ask for an integer value. State is the value is, or is not, within the 100’s, meaning is it a
three-digit number which starts with 1. This can be done at least two different ways. Feel
free to challenge yourself to find both ways. No bonus points, just bonus knowledge. """
print()
number1 = int(input("Enter am integer value to determine if it's within the 100's range, 2 types: "))
if 100 <= number1 <= 199:  # type 1 being via if statement's.
    print(number1, "is within the 100's, type 1.")
else:
    print(number1, "is not within the 100's, type 1.")
if number1 in range(100, 200):  # type 2 utilizes range.
    print(number1, "is within the 100's, type 2.")
else:
    print(number1, "is not within the 100's, type 2.")
