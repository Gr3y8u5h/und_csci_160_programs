import FileUtils


def printSongs(message, songs):
    print(message)
    for song in songs:
        print(song)
    print()
    print()


def saveAsSongs(songs):
    fileName = FileUtils.selectSaveFile("Select song file")
    if fileName != None:
        saveSongs(fileName, songs)


def saveSongs(fileName, songs):
    # option 1 - ask for the file name here
    outFile = open(fileName, "w")
    for song in songs:
        outFile.write(song + "\n")
    outFile.close()


'''
readSongs fills a list from a file
'''


def readSongs(fileName, songs):
    songs.clear()  # make sure the list if empty
    songFile = open(fileName, "r")
    for song in songFile:
        song = song.strip()
        songs.append(song)
    songFile.close()


def readSongs2(fileName):
    songs = []  # create a local list
    songFile = open(fileName, "r")
    for song in songFile:
        song = song.strip()
        songs.append(song)
    songFile.close()
    return songs


def searchForSong(songs):
    while True:
        songToFind = input("Enter song to find, press ENTER to quit ")
        if songToFind == "":
            break

        if songToFind in songs:  # performs a linear search
            print("Found", songToFind, "in the list")
        else:
            print("Unable to find", songToFind, "in the list")
        print()


def isSongInList(songs):
    '''isSongInList accepts a list of songs and a song
    Returns True if song is present in the list, otherwise returns false
    isSongInList performs a non-case specific comparison
    '''

    for song in songs:
        if song.lower().strip() == songToFind.lower().strip():
            return True
    return False


def searchForSong2(songs):
    while True:
        songToFind = input("Enter song to find, press ENTER to quit ")
        if songToFind == "":
            break

        # WORKS but using isSongInList as example of returning a boolean from a functio after a linear search
        # songFound = False  # noMatch = True
        # for song in songs:
        #     if song.lower().strip() == songToFind.lower().strip():
        #         print("Found", song, "in the list")
        #         songFound = True  # or noMatch = False
        #         break
        #
        # if songFound == False:  # or if not songFound or if noMatch == True
        #     print("Unable to find", songToFind, "in the list")

        if isSongInList(songs, songToFind):
            print('Found', song, 'in the list')
        else:
            print('Unable to find', songToFind, 'in the list')

        print()


def addSongs(songs):
    songToAdd = input('Enter song to add - press ENTER to quit ')
    while songToAdd != '':
        if not isSongInList(songs, songToAdd):
            songs.append(songToAdd)
        else:
            print(songToAdd, 'is already in the song list')

        print()
        songToAdd = input('Enter next song to add ')

def searchForSong3(songs):
    while True:
        textToFind = input("Enter text to find, press ENTER to quit ")
        if textToFind == "":
            break

        numOfMatches = 0  # textFound = False #noMatch = True
        for song in songs:
            if song.lower().find(textToFind.lower()) >= 0:
                print("Found", song, "in the list")
                numOfMatches = numOfMatches + 1  # textFound= True # or noMatch = False

        if numOfMatches == 0:  # textFound == False: #or if not songFound or if noMatch == True
            print("Unable to find", textToFind, "in the list")
        else:
            print("Found", numOfMatches, "of matches in the list")

        print()


def main():
    # songs = [
    #   "Frank Sinatra - That's Life",
    #   "Enimem - Rap God",
    #   "Stevie Wonder - Signed, Sealed and Delivered",
    #   "The Eagles - Take It Easy",
    #   "Justin Beiber - Baby"
    #   ]
    # option sending an empty list to the function
    # songs = []
    # fileName = FileUtils.selectOpenFile ("Select song file")
    # if fileName != None:
    #   readSongs (fileName, songs)

    # option returning a list from the function
    fileName = FileUtils.selectOpenFile("Select song file")
    if fileName != None:
        songs = readSongs2(fileName)

    printSongs("Original song list", songs)
    songs.sort()
    printSongs("After songs", songs)

    searchForSong3(songs)

    # option 2 - ask for the file name here and send it to the function
    # fileName = FileUtils.selectSaveFile ("Select song file")
    # if fileName != None:

    saveSongs(fileName, songs)


main()