'''
MailingLabel.py - Lab 1 - CS160 Computer Science 1 Online - by: Joshua George.

Instructions are as follows;

Using 6 string literals, one each for your first name, last name, address, city, state 
abbreviation, and zip code, create a mailing label with the following format:  

FirstName LastName 
Address 
City, State  Zip code

Write the information to the screen twice, once using EXACTLY 1 print statement, and once 
again using EXACTLY 6 print statements. This will require the use of end=, sep=, and “\n” in 
your code. Make sure there are no extra spaces in the output. Also make sure there are two 
spaces between the state and zip code and that the state abbreviation is in capital letters. 

Make sure to comment both files, using multiline comments to document the file and single 
line comments to document the various “sections” of code within the file.

'''

### This section requires the 6 string literals used. 
 
myFirstName = 'Joshua'              
myLastName = 'George'               
myAddress = '666 Crossroad Blvd.'   ### I do not, nor have I ever, associate with the devil or his minions.
myCity = 'Lake Fire'                ### This was only meant as a joke.
myState = 'GH'                      ### GH = Gates of Hell
myZipCode = '16661'

### Using one print statement layout the mailing address format specified.

print(myFirstName, ' ', myLastName,'\n', myAddress, '\n', myCity, ', ', myState, '  ', myZipCode, sep='')

print()
print()

### Using exactly six print statements layout the mailing address the same as before.

print(myFirstName, end=' ')
print(myLastName)
print(myAddress)
print(myCity, ', ', end='', sep='')
print(myState, end='  ')
print(myZipCode)

### Just a bit of ASCII Art to go with the theme of the program.

print()
print()
print('""        ""')
print('""        ""')
print('"" ""  "" ""')
print('"" ""  "" ""', '   ""')
print('""""""""""""', ' """')
print('""""""""""""""""')
print('""""""""""""""')
print('""""""""""""')
print('"""""""""""')
print('""""""""""')
print('"""""""""')