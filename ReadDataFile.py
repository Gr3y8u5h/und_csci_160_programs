import FileUtils

fileName = FileUtils.selectOpenFile('Select data file: ')  # comes up with a file name

if fileName == None:
    print('Data file not selected.')
    exit()  # and we will now leave the program.  Do this if file not selected.

# if os.path.isfile(fileName) == False:
#     print(fileName, 'is not a valid file ')
#     exit()

print('File name returned from selectOpenFile ', fileName)

# fileName = 'numbers.txt'  # relative path, look in the current directory of the file
#  absolute path below.  Have to add a \ to every \ so that it accepts
# fileName = 'C:\\Users\\jim\\iCloudDrive\\UND\\CSCI 160\\CSCI 160 LabPrograms\\numbers.txt'
# have to tell it where to look or save the file in the same folder as program
# filename and then mode, read or write is basic modes

inFile = open(fileName, 'r')

total = 0  # adding an accumulator
numOfValues = 0  # there is no counter for files.  Have to accumulate.
for line in inFile: # range is collection of numbers, file is a collection of lines
    line = int(line.rstrip())  # returns a copy with whitespace stripped front and back, int here
    # line = int(line)  # works but not what we should do
    print(line)  # includes the end of line \n that's why they are double spaced
    # solution is to turn the string to a number, strip strips the front and back
    total += line
    numOfValues += 1

inFile.close()  # methods are built in variables. close is a methods. This closes the file.

print('The average is ', format(total / numOfValues, '1.2f'))
print('All done')

''' files make it easier to bring lots of data into your program
comes in with a \n and comes in as string, so need to convert if needed. 
use strip, open, close
'''