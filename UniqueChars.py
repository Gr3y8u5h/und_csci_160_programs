str = 'asd faskejf asldff asdof lkasdf asdfER'

uniqueCharsList = []
uniqueChars = {}
for char in str:
    # print(char)
    if char.isalpha():  # if char >= 'a' and char <= 'z':
        if not char.lower() in uniqueCharsList:
            uniqueCharsList.append(char.lower())
        uniqueChars[char.lower()] = True  # or 0 or -1 -r '' or 42
        uniqueChars[char.lower()] = uniqueChars[char.lower()] + 1

print('Number of Chars ', len(uniqueCharsList), ' - ', uniqueCharsList)
print('Number of Chars ', len(uniqueChars), ' - ', uniqueChars)

uniqueChars.clear()
for char in str:
    if char.isalpha():
        if char.lower() in uniqueChars:
            uniqueChars[char.lower()] = uniqueChars[char.lower()] + 1
        else:
            uniqueChars[char.lower()] = 1

print('Sorted by char')
sortedChars = list(uniqueChars.keys())
sortedChars.sort()
for char in sortedChars:
    print('%5s %5d' % (char, uniqueChars[char]))

print('Sorted by count')
sortedChars = list(uniqueChars.keys())
sortedChars.sort(key=lambda n: uniqueChars[n])
sortedChars.reverse()
for char in sortedChars:
    print('%5s %5d' % (char, uniqueChars[char]))
