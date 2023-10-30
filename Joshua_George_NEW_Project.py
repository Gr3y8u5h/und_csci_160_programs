# Joshua W George - georgejw22@hotmail.com - 812-910-0924

"""
The Project

Write a python program that iterates the integers from 1 to 50.
For multiples of three print "Cloud" instead of the number
For multiples of seven print "Computing"
For numbers which are multiples of both three and seven print "CloudComputing"
"""

def main():
    """This function prints out the iteration 1-50, with the multiples of 3 printing 'Cloud' instead, multiples
    of 7 printing 'Computing' instead, and multiples of both 3 & 7 printing 'CloudComputing' instead."""

    print()
    for i in range(1, 51):  # creating the iteration
        if i % 3 == 0 and i % 7 == 0:
            # used first to find the iteration with both multiples, otherwise would be skipped
            print('CloudComputing')
        elif i % 3 == 0:  # used to find iterations with multiples of 3
            print('Cloud')
        elif i % 7 == 0:  # used to find iterations with multiples of 7
            print('Computing')
        else:
            print(i)  # used to print iterations with neither multiples


main()  # calling the function
