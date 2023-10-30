"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Activity 9"""

"""
Assignment
Today’s In Class Lab is about asking the user to enter a string and printing whether it is
palindrome or not.

Algorithm
Ask for a string. For each string entered state whether it is an odd palindrome, and even
palindrome, or not a palindrome. Continue to ask for strings until the user enters an empty
string.

One option that will let you work with the individual characters in a string is to use the square
brackets [ ] to access individual characters. You can also use the for loop to iterate through the
individual characters in a string. Regardless of the approach, you can then use those characters
to build the reverse of the original string.

Then compare the original string with reversed string, print the reversed string and the result
(whether it is palindrome or not). If it is a palindrome, it is an odd palindrome if there are an
odd number of characters in the original string, otherwise it is an even palindrome.

Enter a String: radar
Reverse string: radar
It is an odd palindrome.

Enter a String: add
Reverse string: dda
It is not a palindrome.

Enter a String: 1221
Reverse string: 1221
It is an even palindrome.

Enter a String:
<<program ends>>"""


def main():
    """Ask the user for a string, then the function strips the whitespace, lowercases the characters,
    reverses the string, and compares the reverse to the original.  Print functions then shows the value reversed and
    then states if its an odd or even palindrome, or not a palindrome.  If the input is empty the program ends."""

    while True:
        print()
        userInput = input('Enter a string: ')
        userInput = userInput.strip().lower()
        reversedInput = userInput[::-1]  # storing the reversed input
        if userInput != '':
            print('Reverse string:', reversedInput)
            if userInput == reversedInput:
                if len(userInput) % 2 == 0:
                    print('It is an even palindrome.')
                else:
                    print('It is an odd palindrome.')
            else:
                print('It is not a palindrome.')
        else:
            break


main()
