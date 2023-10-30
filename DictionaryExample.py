theDictionary = {}  # empty dictionary

honorPoints = {'A': 4,
               'B': 3,
               'D': 1,
               'C': 2,
               'F': 0
               }  # an initialized dictionary

daysOfTheWeek = {0: 'Sunday',
                 1: 'Monday',
                 2: 'Tuesday',
                 3: 'Wednesday',
                 4: 'Thursday',
                 5: 'Friday',
                 6: 'Saturday'
                 }

print()
honorPoints['I'] = 10  # adds a key/value pair, if the key was not already in the dictionary - and 10 is wrong
honorPoints['I'] = 0  # updates the value associated with the key, if the key was already in the list - 0 is right

day = int(input('Enter numeric day of the week: '))  # the key is an int, so the input here needs to be an int
if day >= 0 and day <=6:
    print('That day is:', daysOfTheWeek[day])
else:
    print('Invalid day')

print()
print(theDictionary)
print()
print(honorPoints)
print()
print('Honor points for an A:', honorPoints['A'])
print('Honor points for an B:', honorPoints['B'])
print('Honor points for an C:', honorPoints['C'])  # keys are case specific, can't be 'c'
print('Honor points for an D:', honorPoints['D'])
print('Honor points for an F:', honorPoints['F'])
print()

grade = input('Enter grade: ')
print()
while grade != '':
    if grade in honorPoints:
        print('That grade has', honorPoints[grade], 'honor points.')
        print()
    else:
        print('Unknown letter grade')
    grade = input('Enter next letter grade: ')

# can not sort a dictionary - Quiz Question
# you can print a dictionary in a sorted order - Quiz Question
''' data is not necessarily going to be entered in a specific order, so find ways to have controls on how
 it's printed'''

print('Grade   Honor Points')
for key in honorPoints:
    print(format(key, '^5s'), format(honorPoints[key], '^15d'))  # will print the order of the key in the same order in dictionary
