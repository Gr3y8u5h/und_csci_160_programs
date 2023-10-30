import FileUtils

"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 6 Part 2"""

'''
Part 2 (separate program)
Ask for a file name. Don’t let the program crash if you enter the name of a file that does not
exist. Detecting this will also be discussed on Wednesday. If the file doesn't exist gracefully
display an error message stating the file doesn't exist and quit the program.

It the file does exist read all the values in the file. You will only need to read the file once, or
more to the point, only read the file once. After the program has finished reading all the data,
display the following information to the screen:
• The minimum value
• The maximum value
• If any values were 100. No output if no values were 100.
• If any values were 0. No output if no values were 0.
• The average – display with 2 places after the decimal point
• The total number of values
• The total number of values greater than or equal to 90
• The total number of values less than 90
• The value closest to 70 (can be 70, less than 70 or greater than 70). abs will be useful for this value.
• The value closest to 70 WITHOUT going over 70 (can be 70, WILL NOT be greater than 70)

If no data exists in the file, write out a simple message indicating that there was no data in the
file and nothing else.

Requirements
Complete comment section that includes your name, id number, program number and a brief
description of the program.
'''


def main():
    fileName = FileUtils.selectOpenFile('Enter in a file name.txt: ')  # used FileUtils in this scenario.
    if fileName != None:  # used to verify a filename exists
        outFile = open(fileName, 'r')
        total = 0
        numOfValues = 0
        greaterThanNinety = 0
        lessThanNinety = 0
        equalsZero = 0
        equalsHundred = 0
        maxLine = 0
        minLine = 100000000
        values = []
        values2 = []
        givenValue = 70

        for line in outFile:
            line = int(line.rstrip())
            if line >= 90:  # greater than 90
                greaterThanNinety += 1
            if line <= 90:  # less than 90
                lessThanNinety += 1
            if line == 0:  # equal to zero
                equalsZero += 1
            if line == 100:  # equal to 100
                equalsHundred += 1
            if line > maxLine:  # Greatest value
                maxLine = line
            else:
                maxLine = maxLine
            if line < minLine:  # Lowest value
                minLine = line
            else:
                minLine = minLine

            # could not figure out how to do the closest to 70 section, so I used google.
            # I'm unsure of lambda, but it worked.
            # also tried not using lists, but couldn't in this scenario.
            if line <= 70:
                values2.append(line)
            values.append(line)
            absoluteDifferenceFunction = lambda values: abs(values - givenValue)
            closestValue = min(values, key=absoluteDifferenceFunction)
            absoluteDifferenceFunction = lambda values2: abs(values2 - givenValue)
            closestValue2 = min(values2, key=absoluteDifferenceFunction)

            total += line
            numOfValues += 1
        if equalsHundred > 0:
            print('Total values that equal 100         :{:10d}' .format(equalsHundred))
        if equalsZero > 0:
            print('Total values that equal zero        :{:10d}' .format(equalsZero))
        print('The average of the the values       :{:10.2f}'.format(total / numOfValues))
        print('Total number of values              :{:10d}' .format(numOfValues))
        print('Total number greater than 90        :{:10d}' .format(greaterThanNinety))
        print('Total number less than 90           :{:10d}' .format(lessThanNinety))
        print('The Maximum value is                :{:10d}' .format(maxLine))
        print('The Minimum value is                :{:10d}' .format(minLine))
        print('Value closest to 70                 :{:10d}' .format(closestValue))
        print('Value closest to 70 W/O going over  :{:10d}' .format(closestValue2))
    else:
        print('File does not exist.')
        exit()
    outFile.close()


main()
