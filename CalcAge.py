from datetime import datetime


def calcAge(birthMonth, birthDay, birthYear):
    currentMonth = datetime.now().month
    currentDay = datetime.now().day
    currentYear = datetime.now().year
    age = currentYear - birthYear
    if birthMonth > currentMonth:
        age -= 1
    elif birthMonth == currentMonth and birthDay > currentDay:
        age -= 1
    return age


def main():
    joshuaAge = calcAge(1, 22, 1980)
    print('Joshua is ', joshuaAge)

    joshuaAge = calcAge(9, 26, 2000)
    print('Should be 21 ', joshuaAge)

    joshuaAge = calcAge(9, 27, 2000)
    print('Should be 21 ', joshuaAge)

    joshuaAge = calcAge(9, 28, 2000)
    print('Should be 20 ', joshuaAge)

    joshuaAge = calcAge(12, 1, 2000)
    print('Should be 19 ', joshuaAge)


main()
