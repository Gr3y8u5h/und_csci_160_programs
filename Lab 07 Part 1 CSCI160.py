"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 7 Part 1"""

'''
Part 1
Assignment
Write each of the following functions using Python. The function header MUST be written as
specified. In your main code test all of the specified functions. Each function must have a
comment block explaining what it does, what the parameters are and what the return value is.

Please remember the following two guidelines:
• unless the purpose of the function is to generate output DO NOT write to the screen
within the function (output for debugging purposes does not apply)
• unless the purpose of the function is to ask the user for a value DO NOT ask the user for
a value within the function

Required functions
def square (intValue):
This function returns the square of intValue.

def summation (intValue):
This function returns the summation of 1 to intValue. You can assume that intValue will be
positive. For example, summation (5) would return 15 (1 + 2 + 3 + 4 + 5).

def sumOfSquare (intValue):
This function returns the sum of the squares from 1 to intValue. For example,
sumOfSquares(5) would return 55 (1 + 4 + 9 + 16 + 25). You MUST use a loop and the square
function to determine the returned value.

def factorial (intValue):
This function returns the factorial of 1 to intValue. You can assume that intValue will be
positive. For example, factorial (5) would return 120 (1 * 2 * 3 * 4 * 5).

def compare (intValue1, intValue2):
The functions returns -1 if intValue1 is less than intValue2, returns 1 if intValue1 is greater
than intValue2, or returns 0 if intValue1 is equal to intValue2.

def isOdd (intValue):
This function will return True if intValue is odd, otherwise it returns False.
def isEven (intValue):

This function will return True if intValue is even, otherwise it return False. This function MUST
use isOdd to determine the returned value. The point behind this function is to minimize the
amount of redundant work that is done in our code, not that determining odd or even is a lot of
work. It’s the concept more than the reality of the code in this case.
'''


def square(intValue):
    """This function returns the square of intValue."""
    squareValue = intValue ** 2
    return squareValue


def summation(intValue):
    """This function returns the summation of 1 to intValue. You can assume that intValue will be
    positive. For example, summation (5) would return 15 (1 + 2 + 3 + 4 + 5)."""
    summationValue = 0
    for i in range(1, intValue + 1):
        summationValue += i
    return summationValue


def sumOfSquare(intValue):
    """This function returns the sum of the squares from 1 to intValue. For example,
    sumOfSquares(5) would return 55 (1 + 4 + 9 + 16 + 25)."""
    sumOfSquareValue = 0
    for i in range(1, intValue + 1):
        sumOfSquareValue += (i ** 2)
    return sumOfSquareValue


def factorial(intValue):
    """This function returns the factorial of 1 to intValue. You can assume that intValue will be
    positive. For example, factorial (5) would return 120 (1 * 2 * 3 * 4 * 5)."""
    factorialValue = 1
    for i in range(1, intValue + 1):
        factorialValue *= i
    return factorialValue


def compare(intValue1, intValue2):
    """The functions returns -1 if intValue1 is less than intValue2, returns 1 if intValue1 is greater
    than intValue2, or returns 0 if intValue1 is equal to intValue2."""
    if intValue1 < intValue2:
        compareValue = -1
    elif intValue1 > intValue2:
        compareValue = 1
    else:
        compareValue = 0
    return compareValue


def isOdd(intValue):
    """This function will return True if intValue is odd, otherwise it returns False."""
    if intValue % 2 == 0:
        isOddValue = False
    else:
        isOddValue = True
    return isOddValue


def isEven(intValue):
    """This function will return True if intValue is even, otherwise it return False. This function MUST
    use isOdd to determine the returned value."""
    if isOdd(intValue) == True:
        isEvenValue = False
    else:
        isEvenValue = True
    return isEvenValue


def main():
    """Tests all of the specified functions.  Printed output to verify operation is correct."""

    print()
    print()
    intValue = int(input('Enter 1st integer: '))
    intValue1 = intValue
    intValue2 = int(input('Enter 2nd integer: '))

    squareValue = square(intValue)
    summationValue = summation(intValue)
    sumOfSquareValue = sumOfSquare(intValue)
    factorialValue = factorial(intValue)
    compareValue = compare(intValue1, intValue2)
    isOddValue = isOdd(intValue)
    isEvenValue = isEven(intValue)

    print()
    print()
    print('Square of the 1st int:                                 ', squareValue)
    print('Summation from 1 to 1st int:                           ', summationValue)
    print('Sum of the square from 1 to 1st int:                   ', sumOfSquareValue)
    print('Factorial from 1 to 1st int:                           ', factorialValue)
    print('1st int < 2nd int return -1, > returns 1, = returns 0: ', compareValue)
    print('1st int is odd returns True, False if even:            ', isOddValue)
    print('1st int is even returns True, False if odd:            ', isEvenValue)



main()



