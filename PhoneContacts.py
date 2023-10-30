FIELD_DELIM = ":"


def printContactsByName(phoneContacts):
    print(format("Name", "10s"), end='')
    print(format("Cell", "15s"), end='')
    print(format("Work", "15s"))
    sortedNames = list(phoneContacts.keys())
    # sortedNames = []
    # for key in phoneContacts.keys():
    #   sortedNames.append(key)
    sortedNames.sort()
    for name in sortedNames:  # phoneContacts:
        print(format(name, "10s"), end='')
        for key in phoneContacts[name]:
            print(format(phoneContacts[name][key], "15s"), end='')
        print()
    print()


def printContactsByCell(phoneContacts):
    print(format("Name", "10s"), end='')
    print(format("Cell", "15s"), end='')
    print(format("Work", "15s"))
    sortedNames = list(phoneContacts.keys())
    sortedNames.sort(key=lambda n: phoneContacts[n]['cell'])
    for name in sortedNames:  # phoneContacts:
        print(format(name, "10s"), end='')
        for key in phoneContacts[name]:
            print(format(phoneContacts[name][key], "15s"), end='')
        print()
    print()


def addContacts(phoneContacts, name, cell, work):
    phoneContacts[name] = {}
    phoneContacts[name]['cell'] = cell
    phoneContacts[name]['work'] = work


def saveContacts(fileName, phoneContacts):
    outFile = open(fileName, "w")
    for name in phoneContacts:
        line = name + FIELD_DELIM + phoneContacts[name]['cell'] + FIELD_DELIM + phoneContacts[name]['work']
        line = name
        for key in phoneContacts[name]:
            line = line + FIELD_DELIM + phoneContacts[name][key]

        outFile.write(line)
        outFile.write("\n")
    outFile.close()


def readContacts(fileName):
    phoneContacts = {}
    inFile = open(fileName, "r")
    for line in inFile:
        line = line.rstrip()
        name, cell, work = line.split(FIELD_DELIM)
        addContacts(phoneContacts, name, cell, work)
    inFile.close()
    return phoneContacts


def getInfo(phoneContacts, name, key):
    if name in phoneContacts:
        if key in phoneContacts[name]:
            return phoneContacts[name][key]
        else:
            return ""  # or None
    else:
        return ""  # or None


def main():
    phoneContacts = readContacts("phoneContacts.txt")

    # phoneContacts = {}

    # addContacts (phoneContacts, "Tom", "701-741-cell", "701-777-work")
    # addContacts (phoneContacts, "Issac", "218-773-cell", "218-281-work")
    # addContacts (phoneContacts, "Hayden", "543-555-cell", "543-555-work")
    # addContacts (phoneContacts, "Jeremy", "212-215-0000", "")

    printContactsByName(phoneContacts)

    printContactsByCell(phoneContacts)

    saveContacts("phoneContacts.txt", phoneContacts)


main()