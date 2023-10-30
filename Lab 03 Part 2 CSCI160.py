"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 3 Part 2"""

print('Lab 3, Part 2')
"""Create a program that asks the user to input a number between 20 and 49. The program must
then print out the number in English words. If the user does not enter a value between 20 and
49 display an error message stating that the input is not within a valid range.

No credit will be given for programs that have a separate print statement for each value. Break
up the input number to the ten’s value and the one’s value and generate output individually for
those two values.

For additional challenge, try including numbers between 0 and 20. Try adding a way to print
negative numbers, this will require coming up with a new system for asking the user to exit the
program."""

print()
number1 = int(input('Please enter a number between 20 and 49: '))
numberTens = number1 // 10  # used to find the tens digit number.
numberOnes = number1 % 10  # used to find the ones digit number.
if 20 <= number1 <= 49:  # used to verify the value is within the range.
    if numberTens == 2:
        tensDigit = 'twenty'
    elif numberTens == 3:
        tensDigit = 'thirty'
    else:
        tensDigit = 'forty'

    if numberOnes == 1:
        onesDigit = 'one'
    elif numberOnes == 2:
        onesDigit = 'two'
    elif numberOnes == 3:
        onesDigit = 'three'
    elif numberOnes == 4:
        onesDigit = 'four'
    elif numberOnes == 5:
        onesDigit = 'five'
    elif numberOnes == 6:
        onesDigit = 'six'
    elif numberOnes == 7:
        onesDigit = 'seven'
    elif numberOnes == 8:
        onesDigit = 'eight'
    elif numberOnes == 9:
        onesDigit = 'nine'
    else:
        onesDigit = ''
    print('The number is', tensDigit, onesDigit, sep=' ')
else:
    print('The number is not within a valid range.')

