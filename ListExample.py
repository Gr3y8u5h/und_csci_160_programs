def printValues(theList):
    print('ID of theList ', id(theList))
    total = 0
    for value in theList:
        total = total + value
    return total


def calcAverage(theList):
    if len(theList) > 0:
        total = printValues(theList)
        return total / len(theList)
    else:
        return None


def main():
    # numbers2 = []  # empty list
    numbers = [11, 22, 33, 44, 55]  # lists are always zero base
    numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # print('First value ', numbers2[0])  # crashes because list is empty
    print('First value ', numbers[0])
    print('Last value  ', numbers[-1])
    print('Last value  ', numbers[len(numbers) - 1])  # anything that is zero based must + or - 1
    print()
    print()

    numbers.append(0)  # append adds to the end
    numbers.append(66)
    numbers.insert(0, 77)  # insert adds 77 to position 0 but doesn't remove, just shifts
    numbers[7] = 88  # removes what's in position 7 and makes it 88
    numbers.remove(55)  # removes the first occurrence of 55, error if not there
    removedValue = numbers.pop(2)  # remove and return value at index 2
    print(removedValue)
    numbers.sort()  # sort is smart, compares two values (similar) or list in order
    numbers.reverse()  # reverses the order, strings goes by first character, then second, ....
    print('Number of items after append ', len(numbers))
    average = calcAverage(numbers)
    if average != None:
        print('Average of numbers ', average)


    # for value in numbers:
    #     print(value, end=' ')
    # print()
    print('ID of numbers ', id(numbers))
    printValues(numbers)
    print('ID of numbers3 ', id(numbers3))
    printValues(numbers3)
    print()

    for index in range(len(numbers)):
        print(numbers[index], end=' ')
    print()
    print()

    total = 0
    for value in numbers:
        total += value
    print('Total of the list is ', total)
    print()
    print()


main()
