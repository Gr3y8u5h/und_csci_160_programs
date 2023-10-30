import FileUtils

"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 12 Part 2"""

"""
For the following function/method headers:
fileName – string
song – string containing artist and song
time – string contain song time in the format of “MM:”SS” or “M:SS”
musicInfo – dictionary containing the song/time information

Write the following functions. The function header MUST be exactly as specified.
Remember, the functions should not write to the display unless specifically asked to do
so.
"""


def readParts(fileName):
    """Creates a dictionary in the function and fills the dictionary
    with the information from filename. Return the dictionary after the file has been
    completely read. No error checking is required. This will read the file created in part 1."""

    inFile = open(fileName, 'r')  # sets the file for read only

    musicInfo = {}  # initialize the dictionary

    for line in inFile:  # creating the new dictionary
        artist, songTitle, songTime = line.rstrip().split(':', 2)
        musicInfo[artist] = [songTitle, songTime]

    inFile.close()  # closes the fileName

    return musicInfo  # returns the dictionary


def totalSongs(musicInfo):
    """Returns the number of songs in the dictionary."""

    totalSongsAll = 0  # initializing a counter

    for key in musicInfo:
        totalSongsAll += 1
        '''accumulating the counter by one.  Only counts the artist in this scenario.  So if an 
        artist, the key, has more than one song, this scenario would not work.  But it would work if
        I had artist - song as one data'''

    return totalSongsAll  # returns the count


def updateSongs(musicInfo, song, time):
    """If song exists, update the time to time
    and return True . If the son does not exist in the dictionary return False ."""

    for artist in musicInfo:
        if musicInfo[artist][0] == song:  # looking at song, which is index 0 of my nested list within the dict
            musicInfo[artist][1] = time  # updates time, which is index 1 of my nested list with the dict
            return True  # returns True if found
    return False  # returns False if not found


def totalTime(musicInfo):
    """This function will return the total time of all songs in the
    dictionary in a string in the format of “MM:SS” or “MMM:SS” . It is possible that the overall
    time could go over 99 minutes."""

    totalSongMin = 0
    totalSongSec = 0

    for artist in musicInfo:
        minutes, seconds = musicInfo[artist][1].split(':')  # splitting time, which is index 1
        totalSongMin += int(minutes)  # converting to integer
        totalSongSec += int(seconds)  # converting to integer

    totalMinToSec = totalSongMin * 60  # finding the total seconds in all the minutes
    totalAllSec = totalMinToSec + totalSongSec  # adding all seconds together
    totalAllMin = totalAllSec // 60  # getting the minutes from total seconds
    totalAllSec = totalAllSec % 60  # finding the remainder seconds
    total = str(totalAllMin) + ':' + str(totalAllSec)  # creating the correct return format

    return total  # returning the total time in mmm:ss or mm:ss string format


def findShortestSong(musicInfo):
    """Returns the song with the shortest time."""

    firstKey = list(musicInfo.keys())[0]  # grabbing the first key to split and to compare later
    shortestMin, shortestSec = musicInfo[firstKey][1].split(':')  # splitting time into min and sec
    shortestMin = int(shortestMin)  # converting to integer
    shortestSec = int(shortestSec)  # converting to integer
    shortestMinToSec = shortestMin * 60  # finding the total seconds in all the minutes
    shortestTotal = shortestMinToSec + shortestSec  # adding all the seconds together and creating a comparable variable

    for artist in musicInfo:
        minutes, seconds = musicInfo[artist][1].split(':')  # splitting time into min and sec
        minutes = int(minutes)  # converting to integer
        seconds = int(seconds)  # converting to integer
        minToSec = minutes * 60  # finding the total seconds in all the minutes
        totalTimeAll = minToSec + seconds  # adding all the seconds together
        if totalTimeAll <= shortestTotal:  # comparing individuals to first shortestTotal
            shortestSong = musicInfo[artist][0]  # storing the shortest song after compared

    return shortestSong  # returning the shortest song


def findLongestSong(musicInfo):
    """Returns the song with the largest time."""

    firstKey = list(musicInfo.keys())[0]  # grabbing the first key to split and to compare later
    longestMin, longestSec = musicInfo[firstKey][1].split(':')  # splitting time into min and sec
    longestMin = int(longestMin)  # converting to integer
    longestSec = int(longestSec)  # converting to integer
    longestMinToSec = longestMin * 60  # finding the total seconds in all the minutes
    longestTotal = longestMinToSec + longestSec  # adding all the seconds together and creating a comparable variable

    for artist in musicInfo:
        minutes, seconds = musicInfo[artist][1].split(':')  # splitting time into min and sec
        minutes = int(minutes)   # converting to integer
        seconds = int(seconds)   # converting to integer
        minToSec = minutes * 60  # finding the total seconds in all the minutes
        totalTimeAll = minToSec + seconds  # adding all the seconds together
        if totalTimeAll >= longestTotal:  # comparing individuals to first longestTotal
            longestSong = musicInfo[artist][0]  # storing the longest song after compared

    return longestSong  # returning the longest song


def getSongTime(musicInfo, songToFind):
    """Returns the time (as a string) of the
    songToFind . Returns an empty string if songToFind is not a song in the dictionary."""

    for artist in musicInfo:
        if musicInfo[artist][0].rstrip().lower() == songToFind.rstrip().lower():  # comparing dict song to user input song
            return musicInfo[artist][1]  # returning song name if found
    return ''  # returning empty string if not found


def printMusic(musicInfo):
    """This function WILL write to the display a table of each
    song and its time. Include column headers in the output. Make sure the columns are
    neatly aligned, with the song column being left justified and the time column being right
    justified. This function should not return a value."""

    print('%-20s' % 'Artist Name', end=' ')  # header 1
    print('%-20s' % 'Song Title', end=' ')  # header 2
    print('%-11s' % 'Song Length')  # header 3
    print('-----------------------------------------------------')  # header 4

    for artist in musicInfo:
        print('%-20s' % artist, end=' ')  # prints artist name left justified
        print('%-20s' % musicInfo[artist][0], end=' ')  # prints song name left justified
        print('%11s' % musicInfo[artist][1])  # prints song length right justified

    # no return


def matchingSongs(musicInfo, textToFind):
    """Creates and returns a list of the songs
    that contain textToFind (case does not matter) in the song (as the artist or song title).
    Return an empty list if no songs contain the requested text. For example, if textToFind
    was “ee” both songs would be returned in a list (“ee” in Freewill, and “ee” in Squeeze)."""

    musicList = []  # initializing a list
    textToFind = textToFind.rstrip().lower()  # converting input for comparison
    for artist in musicInfo:
        # comparing each artist and song to user input
        if textToFind in artist.rstrip().lower() or textToFind in musicInfo[artist][0].rstrip().lower():
            musicList.append(artist)  # appending artist
            musicList.append(musicInfo[artist][0])  # appending song title

    return musicList  # returning list of both artist and song titles with user input text found


def main():
    """IMPORTANT - I seperated artist from title from time.  So, my file will have three pieces of data per line; Artist,
    Song Title, and Song Length.  The way the instructions were written it could go either way and all I did was
    add myself more work.  So remember in this scenario I am pulling from three pieces of data per line, instead
    of two.  The same goes for Part 1, I am utilizing three pieces of data, not two.

    Opens the fileName from part 1, exits if None.  Calls all the functions specified.  The functions returns
    as specified, and display if necessary.  Otherwise the function themselves will display as necessary.
    """

    fileName = FileUtils.selectOpenFile()

    if fileName is None:  # exits if no file is selected
        print()
        print('Invalid Data Selection')
        print()
        exit()

    musicInfo = (readParts(fileName))  # sends filename to fill the dictionary
    print()

    print('Total songs in dictionary: ', totalSongs(musicInfo))  # returns total # of songs
    print()

    songToUpdate = input('Enter a song to update the time: ')  # song to update
    if songToUpdate != '':  # if nothing entered then moves to next function call
        timeToUpdate = input('Enter updated time mm:ss: ')  # update time user input
        wasUpdated = updateSongs(musicInfo, songToUpdate, timeToUpdate)  # calls the function and assigns a variable
        if wasUpdated:  # if returns True prints that the song updated
            print('The songs time was updated.')
        if not wasUpdated:  # if returns False prints that song wasn't found or updated
            print('The song was not found nor updated.')
    print()

    print('The total time of all songs in the dictionary mmm:ss: ', totalTime(musicInfo))  # returns total time of all songs
    print()

    print('The shortest song in the dictionary is: ', findShortestSong(musicInfo))  # returns name of shortest song
    print()

    print('The longest song in the dictionary is: ', findLongestSong(musicInfo))  # returns name of longest song
    print()

    songToFind = input("Enter a song to find it's time: ")  # song to find user input
    if songToFind != '':  # if nothing enter then moves to next function call
        wasFound = getSongTime(musicInfo, songToFind)  # calls the function
        if wasFound != '':  # if returns a song then displays the song
            print('The songs time is: ', wasFound)
        else:  # if returns empty string then song was not found, displays not found
            print('The song was not found.')
    print()

    printMusic(musicInfo)  # calls function that prints output in function
    print()

    textToFind = input("Enter text to find in artist or song: ")  # user input to find text in artist or song title
    if textToFind != '':  # if found an artist or song, displays the output of both in list form
        print('The Artist/Songs found with supplied text: ', matchingSongs(musicInfo, textToFind))
    print()


main()
