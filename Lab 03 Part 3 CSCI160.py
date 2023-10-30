"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 3 Part 3"""

print('Lab 3, Part 3')
"""Write a program that asks for the number of credits you have earned to date (may be zero for
freshman). Then ask for the number of credits you are taking this semester. Make sure all inputs
have an appropriate prompt. By appropriate, I mean a prompt anyone would understand, not
just someone who is writing the program."""

print()
numCreditsCurrent = int(input('Enter the number of credits you have earned to date: '))
numCreditsSemester = int(input('Enter the number of credits you are taking this semester: '))
numCreditsTotal = numCreditsCurrent + numCreditsSemester
if numCreditsCurrent >= 0:  # used to limit the program from negative numbers.
    if numCreditsCurrent >= 90:  # used to find the current status of the student.
        currentStatus = 'senior'
    elif 90 > numCreditsCurrent >= 60:
        currentStatus = 'junior'
    elif 60 > numCreditsCurrent >= 24:
        currentStatus = 'sophomore'
    else:
        currentStatus = 'freshman'
    if numCreditsTotal >= 90:  # used to find the future status of the student.
        futureStatus = 'senior'
    elif 90 > numCreditsTotal >= 60:
        futureStatus = 'junior'
    elif 60 > numCreditsTotal >= 24:
        futureStatus = 'sophomore'
    else:
        futureStatus = 'freshman'
    print()
    print('Your current class status is a ', currentStatus, '.', sep='')
    print('Your class status after this semester will be a ', futureStatus, '.', sep='')
if numCreditsTotal >= 120:
    print('You will have enough credits to graduate.')  # used in leu if credits to graduate has been reached.
else:
    graduateCredits = 120 - numCreditsTotal  # difference till graduation.
    print('The number of credits you need to graduate is ', graduateCredits, ".", sep='')
