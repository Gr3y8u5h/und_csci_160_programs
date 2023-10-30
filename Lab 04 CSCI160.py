"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 4"""

'''Part A 
Write individual while loops to meet the following criteria. Print text before each loop, such as 
“Part 1” or “Part 2”, with a little whitespace between each part to break up the output. 
 
1) Count from 10 to 25 (inclusive) by 1 - output one value per line 
2) Count from 20 to 0 (inclusive, counting down by 1) – all output must be on a single line 
3) Count from 0 to 10 (inclusive) by ½ - output one value per line and right justified. 
4) Count from 1792 to 2020 by 4’s - output one value per line. 
5) Use a loop to raise a value to a specific power. 24 is 2 * 2 * 2 * 2. Ask for a base value 
and an exponent. Multiply base value times itself “exponent” times. In the case of 2 
for the base value and 4 for the exponent, the output should be 16.'''

print()
print('Lab 4 Part A')
print('---------------------------------------------------------')


print('     Section 1')
value = 10
while value in range(10, 25 + 1):  # range to count 10 to 25
    print(value)  # single value per line
    value += 1
print()
print('---------------------------------------------------------')


print('     Section 2')
value2 = 20
while 0 <= value2 <= 20:  # used while instead of range for this example
    print(value2, end=' ')  # printed all values on one line
    value2 -= 1
print()
print()
print('---------------------------------------------------------')


print('     Section 3')
value3 = 0
while 0 <= value3 <= 10:
    print('{:>4}'.format(value3))  # right justified 4 places
    value3 += .5  # used this expression to divide by half as range does not allow steps in fractions
print()
print('---------------------------------------------------------')


print('     Section 4')
for value4 in range(1792, 2020 + 1, 4):  # used range as it was the easiest
    print(value4)  # printed each value on a new line
print()
print('---------------------------------------------------------')


print('     Section 5')
baseNum = int(input('Enter a base number: '))
expoNum = int(input('Enter a exponential number: '))
resultNum = 1  # declared one as base value to make the first loop keep the expression correct
for i in range(expoNum):  # used for loops to perform an exponential multiplication
    resultNum *= baseNum
print(baseNum, " to the power of ", expoNum, " is ", resultNum, '.', sep="")
print()
print('---------------------------------------------------------')

'''Part B
Write a program that asks for a letter grade. Continue to ask for letter grades until the user
enters the grade ‘q’ or ‘Q’ (for ‘quit’). Then tell how many A’s, B’s, C’s, D’s, F’s, or unknowns
(anything other than A, B, C, D, or F) were entered. The letter grades can be entered in upper or
lower case.'''

print('Lab 4 Part B')
print('Enter a letter grade, uppercase or lowercase, enter q or Q to quit.')
# felt I needed to declare all variables to zero before hand
aCount = 0
bCount = 0
cCount = 0
dCount = 0
fCount = 0
unknownCount = 0
letterGrade = '-'  # declared a generic string variable
while True:  # took a bit to get the while True to work
    letterGrade = input('Enter a letter grade: ')
    # if q or Q then the loop breaks out
    if letterGrade == 'q' or letterGrade == 'Q':
        break
    # each letter and the unknowns has there own counter
    if letterGrade == "a" or letterGrade == "A":
        aCount += 1
    elif letterGrade == "b" or letterGrade == "B":
        bCount += 1
    elif letterGrade == "c" or letterGrade == "C":
        cCount += 1
    elif letterGrade == "d" or letterGrade == "D":
        dCount += 1
    elif letterGrade == "f" or letterGrade == "F":
        fCount += 1
    else:
        unknownCount += 1
print()
# prints each count per grade or unknown
print('There are', aCount, 'A(s)')
print('There are', bCount, 'B(s)')
print('There are', cCount, 'C(s)')
print('There are', dCount, 'D(s)')
print('There are', fCount, 'F(s)')
print('There are', unknownCount, 'unknown grades.')
print()
print('---------------------------------------------------------')

'''Part C
Write a program that asks for integer values until the user enters 0. Once the user has finished
entering values, display the average of the positive values that were entered and the average of
the negative values that were entered. DO NOT make any assumptions regarding the data that
will be entered. If you are not able to calculate an average, state that no values of that type were
entered. Print out the average with 2 places after the decimal point.'''

print('Lab 4 Part C')
print('Enter multiple integer values, enter 0(zero) to finish and compute')
valueNum2 = 1
# declared two lists to store integers as either positive or negative
valueListPos = []
valueListNeg = []
while valueNum2 != 0:
    valueNum2 = float(input('Enter an integer value: '))  # used float as not to assume data types
    if valueNum2 < 0:
        valueListNeg.append(valueNum2)  # adding to the negative list
    elif valueNum2 > 0:
        valueListPos.append(valueNum2)  # adding to the positive list
print()
# if else statements in case no negatives or positives were entered and not to divide by zero
if len(valueListPos) > 0:
    print('Average of the positive values: {:>8.2f}' .format(sum(valueListPos) / len(valueListPos)))
else:
    print('No positive values to average.')
if len(valueListNeg) > 0:
    print('Average of the negative values: {:>8.2f}' .format(sum(valueListNeg) / len(valueListNeg)))
else:
    print('No negative values to average.')
# was worried I needed to clear the loop afterwords or it'd have built up, but it clears properly on its own
print()
print('---------------------------------------------------------')

'''Part D
Write a program that creates a small, single value multiplication table using a for loop. The
program will ask for a value between 1 and 10. If the value is less than 1 or greater than 10,
display an error message stating that the input is invalid and end the program.
If the input is valid, display a table that shows the results of multiplying the input value times the
numbers one through ten. Make all the columns of numbers be right justified . Write a label for
the table at the top of the table.'''

print('Lab 4 Part D')
valueNum1 = int(input('Enter a value between 1 and 10: '))
if 1 <= valueNum1 <= 10:
    for a in range(1, 10+1, 1):
        print('{:>2} * {:>1} = {:>3}'.format(a, valueNum1, valueNum1 * a), sep='')  # used format to right justify
else:
    print('The input value is invalid.')
print()
print('---------------------------------------------------------')