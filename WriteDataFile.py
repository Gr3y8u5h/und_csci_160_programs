import FileUtils  # gives us access to professors file

# fileName = input('Enter name for the data file ')

# fileName = 'number2.txt'
# writing data

fileName = FileUtils.selectSaveFile('Select data file')  # saves a file...
if fileName == None:  # none means no value entered
    exit()

outFile = open(fileName, 'w')  # 'w' writes, 'r' reads
endValue = int(input('Enter end value: '))

for x in range(1, endValue + 1):
    outFile.write(str(x) + '\n')  # write needs to be a string.  needs a \n per line
    # outFile.write(str(1))
    # outFile.write('\n')

outFile.close()