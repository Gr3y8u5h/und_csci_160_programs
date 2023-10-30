total = 0
for value in [1, 3, 5, 7, 9]:
    print(value)
    total = total + value

print('Total of all values', total)

total = 0
for value in []: # empty list of values
    print(value)
    total = total + value

print('Total of all values', total)

total = 0
for day in ['s', 'm', 't', 'w', 't', 'f', 's']: # empty list of values
    print(day, end=' ')
print()

for value in range(1, 10 + 1):  # or (1, 11)
    print(value, end=' ')
print()

startValue = int(input('Enter start value '))
endValue = int(input('Enter end value '))
step = int(input('Enter step value '))
for value in range(startValue, endValue + 1, step):
    print(value, end=' ')
print()

fullName = 'First Last'
for letter in fullName:
    print(letter, end=' ')
print()