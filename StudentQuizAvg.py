studentNum = 1
numOfStudents = int(input('Enter the number of students taking the quiz: '))
totalPoints = 0
highScore = -1  # need to initialize so no errors.  0 makes sure first score is high score after entered.
# -1 makes sure it initializes something it can't be.
lowScore = 100
while studentNum <= numOfStudents:
    # reason for the loop
    quizScore = int(input('Enter quiz score for student ' + str(studentNum) + ': '))
    if quizScore > highScore:  # will keep cycling to a new highScore when a new number higher is entered.
        highScore = quizScore
    if quizScore < lowScore:
        lowScore = quizScore
    totalPoints += quizScore  # accumulator for running total of points
    studentNum += 1  # same as studentNum = studentNum + 1
if numOfStudents > 0:
    average = totalPoints / numOfStudents
    print('Average    ', format(average, '5.2f'))  # 1.2f because 1 will take as much as it needs. .2 after the decimal.
    # format to creat columns, tables, or if floating point and need to take control of decimal.
    print('High Score ', format(highScore, '5d'))
    print('Low Score  ', format(lowScore, '5d'))
else:
    average = 0
    print('Average ', average)
