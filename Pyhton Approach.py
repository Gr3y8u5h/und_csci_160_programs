numOfStudents = 0
totalPoints = 0
highScore = -1  # need to initialize so no errors.  0 makes sure first score is high score after entered.
# -1 makes sure it initializes something it can't be.
lowScore = 11
# primed loop, same equation on inside and outside of the loop.

while True:
    quizScore = int(input('Enter quiz score, enter -1 to quit: '))
    while quizScore < -1 or quizScore > 10:
        print('Please enter a quiz score between 0-10, or -1 to quit')
        quizScore = int(input('Enter the quiz score: '))

    if quizScore == -1:
        break
    # no additional inputs
    # increment counter do right away
    numOfStudents += 1
    # reason for the loop
    if quizScore > highScore:  # will keep cycling to a new highScore when a new number higher is entered.
        highScore = quizScore
    if quizScore < lowScore:
        lowScore = quizScore
    totalPoints += quizScore  # accumulator for running total of points


if numOfStudents > 0:
    average = totalPoints / numOfStudents
    print('Average           ', format(average, '5.2f'))  # 1.2f because 1 will take as much as it needs. .2 after the decimal.
    # format to creat columns, tables, or if floating point and need to take control of decimal.
    print('High Score        ', format(highScore, '5d'))
    print('Low Score         ', format(lowScore, '5d'))
    print('Number of students', format(numOfStudents, '5d'))
else:
    average = 0
    print('Average ', average)
