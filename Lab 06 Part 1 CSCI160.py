"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 6 Part 1"""

'''
Assignment
Part 1
Ask for a file name. The file should exist in the same folder as the program. If using input() to
receive the file name do not give it a path, just give it a name like “number1.txt” or something
similar (without the quotes when you enter the name). Then ask for test scores (0-100) until the
user enters a specific value, in this case, -1. Write each value to the file as it has been entered.
Make sure to close the file once the user has finished entering in the data.

Specifics
You can use input() or FileUtils.selectOpenFile/FileUtils.selectSaveFile for
receiving the file name from the user in either part. The FileUtils functions will be discussed
in class Wednesday. The file can be downloaded from the examples folder in Blackboard. There
may be LOTS of different FileUtils files available in the wild, make sure you get my file from
Blackboard. Keep in mind that entering no actual data is legal (after entering a file name you
enter -1 right away) and should be considered in part 1 and part 2.

Requirements
Complete comment section that includes your name, id number, program number and a brief
description of the program.
'''

# I opted to use the input() method for this Lab.  I tried to minimize crashes as much as possible.
# The only crash that occurs is if the input for the test score is more than one blankspace or
# if the test score is an actual alpha string.

def main():
    fileName = input('Enter in a file name.txt: ')
    outFile = open(fileName, 'w')  # creates a file using the input name and sets it to write.
    while True:
        testScore = input('Enter a test score (0-100): ')
        if testScore == '':  # testing for accidental blank inputs.
            print('Test score must be between 0 and 100')
        else:
            testScore = int(testScore)  # opted to convert to integer for further testing.
            if testScore != -1:
                if 0 <= testScore <= 100:
                    testScore = str(testScore)  # converted back to string to write the file.
                    outFile.write(testScore)  # writing the string to the file.
                    outFile.write('\n')  # added a newline so that the values are in a column
                else:
                    print('Test score must be between 0 and 100')
            else:
                outFile.close()
                break


main()
