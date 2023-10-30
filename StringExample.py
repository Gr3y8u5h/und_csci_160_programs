# name = "First Last"
name = input('Enter your name, first and last ')

print('First char   ', name[0])
print('Second char  ', name[1])

# print('Last char    ', name[9])  # only works if name has 10 characters, thinking for everyone.
print('Last char    ', name[-1])  # works with any string, but mostly just in Python
print('Last char    ', name[len(name) - 1])  # universal with strings in all languages

print('Number of characters in name ', len(name))

for char in name:
    print(char, end=' ')
print()

for index in range(0, len(name)):  # don't need to add + 1 because generally it'll be len(name) - 1 and range goes 1 less
    print(name[index], end=' ')  # loops through the indexes of the strings.

print()
print('Character in reverse order')
for index in range(len(name) - 1, -1, -1):
    print(name[index], end=' ')
print()
print()

name.strip()
blankAt = name.find(' ')
if blankAt != -1:
    firstName = name[0:blankAt].strip()  # Grabs the first 5 indexes
    lastName = name[blankAt + 1:].strip()  # only works with strings.  or name[blankAt:len(name)]
    print('First Name ', firstName)
    print('Last Name  ', lastName)
else:
    print('Name', name)

sentence = 'This is the sample text for the string example'
blankAt = sentence.find(' ')
while blankAt != -1:  # we have at least one word in a string
    word = sentence[0:blankAt]
    print(word)
    sentence = sentence[blankAt + 1:]
    blankAt = sentence.find(' ')
print(sentence)



