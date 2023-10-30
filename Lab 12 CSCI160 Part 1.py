import FileUtils

"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 12 Part 1"""

"""
Write a program to ask for a list of songs. Each entry for a song will require a title and a
time, as a string, in minutes:seconds format. Part 1 should ask for a file name and then
a series of songs until the user enters a blank artist. Do not ask the title and time when
a blank artist has been entered. Write the data for each song out to the file, with each
piece of information separated by a colon ( “:” ) (so don’t put a colon in the artist name
or song title). You do not need a dictionary for this part

A sample session of this part might be:
Enter data file name: playlist1.txt

Enter the artist and song, enter “” to quit:
Title: Rush - Freewill
Time: 5:25

Enter the artist and song, enter “” to quit:
Title: Squeeze - Tempted
Time: 4:05

Enter the artist and song, enter “” to quit:
Title:

After the above session the contents of playlist1.txt would be:
Rush – Freewill:5:25
Squeeze – Tempted:4:05
"""


def main():
    """Asks to create a file name.  If the file name does not exist sends an error.  The file opens new
    or will be overwritten.  Asks for an artist.  If nothing entered then exits.
    If an artist is entered then ask for song title and then length time, and stores to the file.  The file
    closes when no artist is entered.

    I decided to use selectSaveFile in this scenario so that a new file can be created or overwritten.  I also
    seperated artist from title from time.  So, my file will have three pieces of data per line; Artist, Song Title,
    and Song Length.  The way the instructions were written it could go either way and all I did was add myself more
    work.  So remember in this scenario I am pulling from three pieces of data per line, instead of two.  The same
    goes for Part 2, I am utilizing three pieces of data, not two.
    """

    fileName = FileUtils.selectSaveFile()

    if fileName is None:  # Show error if no file selected
        print('Data file not selected.')
        exit()

    inFile = open(fileName, 'w')  # opens file to be written

    while True:  # while loop until nothing is entered for artist
        print()
        print('Enter the artist name.')
        print("ENTER only to quit")
        artist = input('Artist: ')
        if artist != '':  # if no artist entered then exits
            songTitle = input('Title: ')
            songTime = input('Time, min:sec: ')
            inFile.write(artist)
            inFile.write(':')
            inFile.write(songTitle)
            inFile.write(':')
            inFile.write(str(songTime))
            inFile.write('\n')
        else:
            break

    inFile.close()


main()
