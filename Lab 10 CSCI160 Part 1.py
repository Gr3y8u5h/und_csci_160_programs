"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 10 Part 1"""

"""Part 1
Write a program to ask for a series of part names and prices. Ask for a part name
until the user enters a blank value. For every valid part name ask for a price. The
prices may be floating point values. Fill a dictionary with this data. Once the user
has finished entering data ask for a file name. You may use input or FileUtils
to ask for the file name. Write out each part name/price pair in the dictionary to
the data file, one pair per line. Separate the part name and price with a tab
(“\t”).

Run Part 1 AT LEAST TWICE. This will create at least two different data files that
can be tested in part 2."""


def main():

    inventory = {}
    while True:
        partName = input('Enter a part name: ')
        if partName != '':  # if blank then exit the while loop
            partPrice = float(input('Enter a part price: '))  # unsure the reason for float if must be string to write.
        else:
            break
        inventory[partName] = partPrice  # adding the key value pair to the dictionary

    fileName = input('Enter filename to store data: ')
    inFile = open(fileName, 'w')
    for key in inventory:
        inFile.write(key)  # writing the key
        inFile.write('\t')  # tab between key value pair
        inFile.write(str(inventory[key]))  # converting value to string to write
        inFile.write('\n')  # adding a newline

    inFile.close()


main()
