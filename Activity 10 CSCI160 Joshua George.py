import FileUtils
"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Activity 10"""

'''
Assignment:
This program will read a file of English words and their Spanish translation. It then asks
the user for an English word. If it exists in your dictionary the Spanish translation is
displayed. If the English word does not exist in the dictionary the program states that the
word does not exist in its list of words.

Specifics
Create a text file, with one English word and a Spanish word per line, separated by a
colon. You can create the language file using a text editor, you do not need to write a
program to create this file. An example of the file might be:

one:uno
two:dos
three:tres
four:cuatro
five:cinco
six:seis
seven:siete
eight:ocho
nine:nueve
ten:diez

After reading the text file, using it to fill up a dictionary, ask the user for an English word.
If the word exists, print out the Spanish version. If the word does not exist state that the
word is not in your list. Continue this process of asking for a word until the user does not
enter a word (just pressed Enter).

As you might have noticed, there is nothing in the program that limits this Spanish
words. This program can be written to work with any translation, so feel free to make it
be French, or German or any other language where you can come up with a list of
translated words. You also are not limited to 10 words, that is just the list I came up with
for the example. The number of key/values pairs that you have in your dictionary is
basically limited by the memory in your computer.

Hints
You will need to determine if the key (the English word) exists in the dictionary. Use the
in operator with the dictionary, or the get() method. Either can be used to avoid
crashing the program, which happens if you attempt to use a key that does not exist.
'''


def spanishPrint(englishSpanishDict):
    """Ask the user for an English word. If the word exists, print out the Spanish version. If
    the word does not exist state that the word is not in your list. Continue this process of
    asking for a word until the user does not enter a word (just pressed Enter)."""

    print()
    while True:  # keeps repeating the main question
        print('Enter an English word to find the Spanish equivalent.')  # header 1
        print('Press ENTER to quit.')  # header 2
        englishInput = (input('English word: '))  # english word input
        if englishInput != '':  # exits if ENTER only
            englishInput = englishInput.rstrip().lower()  # stripping and lowering the input
            if englishInput in englishSpanishDict:  # looking for input within dictionary
                print('Spanish equivalent: ', englishSpanishDict[englishInput])  # prints spanish equivalent
                print()
            elif englishInput in englishSpanishDict.values():  # if the input is already Spanish
                for key, value in englishSpanishDict.items():
                    if value == englishInput:
                        print("This is a Spanish word. It's English equivalent is : ", key)
                        print()
            else:  # prints if word is not in the key of the dictionary
                print('Word is not in the list')
                print()
        else:
            exit()


def main():
    """Opens a English:Spanish text file and fills a dictionary with the values.  English
    being the key and Spanish being the value.  Calls the function spanishPrint"""

    englishSpanishDict = {}  # initializing the dictionary
    fileName = FileUtils.selectOpenFile()

    if fileName is None:  # exits if no file is selected
        print()
        print('Invalid Data Selection')
        exit()

    inFile = open(fileName, 'r')

    for line in inFile:
        english, spanish = line.rstrip().split(':')
        english = english.lower()  # creating a lower of English word before filling the dict
        spanish = spanish.lower()  # creating a lower of Spanish word before filling the dict
        englishSpanishDict[english] = spanish  # creating the new dictionary
        
    spanishPrint(englishSpanishDict)


main()
