"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 9 Part 1"""

'''Part 1:
We need a program that stores information about a list of students who are members of
a cross country team. Write a program that will ask for a student name, and then the
time of their most run. The time will be entered as a string in the format of MM:SS. Stop
asking for a student info when the user enters an empty value for the name – don’t ask
for the time for the non-existent student. You don’t need a list for this part of the
assignment.

All of the info needs to be written to a file. The format of the file will be
student name|time
where the delimiter between the two pieces of information is the bar, or pipe character.

An example of a data file might be:
Joe Smith|15:25
Bob Anderson|18:25'''


def saveStudentInfo(studentName, studentRunTime):
    outFile = open('StudentRunTimes.txt', 'a')  # used append instead of write otherwise each call wold erase the last
    
    outFile.write(studentName)  # writing the information to the file
    outFile.write('|')
    outFile.write(studentRunTime)
    outFile.write('\n')
    
    outFile.close()
    

def main():
    while True:
        print()
        studentName = input("Students name, first & last   : ")
        if studentName == '':  # not asking for run time if no studentName
            break
        studentRunTime = input("Student run time, MM:SS format: ")
        if studentRunTime == '':
            studentRunTime = '00:00'
        saveStudentInfo(studentName, studentRunTime)  # called this every entry as not to create a list to pass


main()
