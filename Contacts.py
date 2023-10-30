import os


def printContacts(contacts):
    nameWidth = "9"
    emailWidth = "20"
    print(format("Name", nameWidth + "s"), format("Email", emailWidth + "s"))
    for contact in contacts:
        # print (format (contact, nameWidth + "s"), format (contacts[contact], emailWidth + "s"))
        # print ("%-8s %-20s" % (contact, contacts[contact])) #use a negative width to left justify, everything is right justified by default
        print(("%-" + nameWidth + "s %-" + emailWidth + "s") % (
        contact, contacts[contact]))  # use a negative width to left justify, everything is right justified by default
    print()


def printSortedContacts(contacts):
    nameWidth = "9"
    emailWidth = "20"
    contactsList = list(contacts.keys())
    contactsList.sort()
    print(format("Name", nameWidth + "s"), format("Email", emailWidth + "s"))
    for contact in contactsList:
        print(("%-" + nameWidth + "s %-" + emailWidth + "s") % (
        contact, contacts[contact]))  # use a negative width to left justify, everything is right justified by default
    print()


def printSortedContactsByEmail(contacts):
    nameWidth = "9"
    emailWidth = "20"
    contactsList = list(contacts.keys())
    contactsList.sort(key=lambda n: contacts[n].lower())
    print(format("Name", nameWidth + "s"), format("Email", emailWidth + "s"))
    for contact in contactsList:
        print(("%-" + nameWidth + "s %-" + emailWidth + "s") % (
        contact, contacts[contact]))  # use a negative width to left justify, everything is right justified by default
    print()


def saveAsContacts(contacts):
    fileName = 'contacts.txt'  # we would ask for the fileName when done for real
    if fileName != None:
        saveContacts(fileName, contacts)


def saveContacts(fileName, contacts):
    '''
    saveContacts writes the key/value pairs from the provided dictionary to a file created from the provided fileName
    Each line of the file will contain a contact name and an email address separated by the tab characters ("\t")
    No error checking is performed on fileName
    '''
    outFile = open(fileName, "w")
    for contact in contacts:
        outFile.write(contact)
        outFile.write("\t")
        outFile.write(contacts[contact])
        outFile.write("\n")
    outFile.close()


def loadContacts(fileName):
    '''
    loadContacts reads the file contain a list of contacts
    Each line of the file needs to contain a contact name and an email address separated by the tab characters ("\t")
    A local dictionary will be created and returned from the function
    Returns an empty dictionary if the fileName is invalid or does not exist
    '''
    contacts = {}  # create local dictionary
    if os.path.isfile(fileName):
        inFile = open(fileName, "r")
        for line in inFile:
            line = line.strip()
            contact, emailAddr = line.split("\t")
            contacts[contact] = emailAddr  # adding and/or updating
        return contacts
    else:
        return contacts


def addContacts(contacts):
    contactToAdd = input("Enter contact to add ")
    while contactToAdd != "":
        emailToAdd = input("Enter email address for " + contactToAdd + ": ")

        if contactToAdd in contacts:
            overwriteEntry = input(contactToAdd + " already exists in the contact list - update (y/n)? ")
            if overwriteEntry.lower().lstrip()[0] == 'y':
                contacts[contactToAdd] = emailToAdd
        else:
            contacts[contactToAdd] = emailToAdd

        print()
        contactToAdd = input("Enter next contact to add ")


def searchByName(contacts):
    contactToFind = input("Enter contact to find ")
    while contactToFind != "":
        if contactToFind in contacts:
            print("Email address for ", contactToFind, ": ", contacts[contactToFind], sep='')
        else:
            print("Unable to find an email address for ", contactToFind)
        print()
        contactToFind = input("Enter next contact to find ")


def searchByNameNoCase(contacts):
    contactToFind = input("Enter contact to find ")
    while contactToFind != "":
        foundMatch = False
        for contact in contacts:
            if contact.lower() == contactToFind.lower():
                print("Email address for ", contact, ": ", contacts[contact], sep='')
                foundMatch = True
                break

        if not foundMatch:
            print("Unable to find an email address for ", contactToFind)

        print()
        contactToFind = input("Enter next contact to find ")


def searchByEmail(contacts):
    emailToFind = input("Enter email address to find ")
    while emailToFind != "":

        foundMatch = False
        for contact in contacts:
            if contacts[contact] == emailToFind:
                print("Contact for ", emailToFind, ": ", contact, sep='')
                foundMatch = True
                break

        if not foundMatch:
            print("Unable to find a contact for email address ", emailToFind)

        print()
        emailToFind = input("Enter next email address to find ")


def main():
    # contacts = {
    #   "Tom" : "thomas.stokke@und.edu",
    #   "Scott" : "scott@minotstate.edu",
    #   "Bob": "bob@undeerc.org",
    #   "Angie" : "angie@gmail.com",
    #   }
    fileName = 'contacts.txt'
    contacts = loadContacts(fileName)
    addContacts(contacts)

    # searchByName (contacts)
    # searchByNameNoCase (contacts)
    searchByEmail(contacts)

    # printContacts (contacts)
    print("Contacts sorted by contact")
    printSortedContacts(contacts)

    print("Contacts sorted by email address")
    printSortedContactsByEmail(contacts)

    saveContacts(fileName, contacts)


main()