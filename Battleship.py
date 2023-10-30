LETTERS = "ABCDEFGHIJ"  # or LETTERS = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J" )
MAXROW = 10
HIT = " X "
MISS = " O "
BLANK = " . "
SHIP = ' S '
HITSHIP = '(S)'


def createGrid():
    grid = {}
    for letter in LETTERS:
        grid[letter] = []
        for x in range(MAXROW + 1):  # creating a list one larger than need to we can ignore index 0
            grid[letter].append(BLANK)
    return grid


def printGrid(title, grid):
    print()
    print(format(title, "^33s"))
    print()
    print(format('', "3s"), end='')
    # print ('   ', end='')
    for letter in LETTERS:
        print(format(letter, "^3s"), end='')
    print()
    for number in range(1, MAXROW + 1):
        print(format(number, "^3d"), end='')
        for letter in LETTERS:
            print(grid[letter][number], end='')
        print()


def splitLocation(location):
    letter = location[0]
    number = int(location[1:])
    return letter, number


def storeShipInfo(shipInfo, ship, startLoc, endLoc):
    shipInfo[ship] = []
    startLetter, startNumber = splitLocation(startLoc)
    endLetter, endNumber = splitLocation(endLoc)
    if startLetter == endLetter:  # ship is vertical
        for number in range(startNumber, endNumber + 1):
            # print ("Ship is at ", startLetter, number)
            shipInfo[ship].append(startLetter + str(number))
    else:  # ship is horizontal
        for value in range(ord(startLetter), ord(endLetter) + 1):
            shipInfo[ship].append(chr(value) + str(startNumber))


def addShipstoGrid(myShips, shipInfo):
    for ship in shipInfo:
        for location in shipInfo[ship]:
            letter, number = splitLocation(location)
            myShips[letter][number] = SHIP


def guessIsAHit(userGuess, shipInfo):
    '''
    creates a guess again the ship locations
    returns the name of the ship if the guess was a hit
    returns MISS if the guess did not hit a ship

    assumes the guess is in capital letter
    
    '''
    for ship in shipInfo:
        if userGuess in shipInfo[ship]:
            return ship
    return MISS


def main():
    myGuesses = createGrid()
    myShips = createGrid()
    shipInfo = {}

    storeShipInfo(shipInfo, 'tugboat', 'D2', 'D3')
    storeShipInfo(shipInfo, 'battleship', 'A6', 'D6')
    storeShipInfo(shipInfo, 'carrier', 'J6', 'J10')
    addShipstoGrid(myShips, shipInfo)

    myGuesses['B'][1] = HIT

    printGrid("My Guesses", myGuesses)
    printGrid("My Ships", myShips)

    usersGuess = input("Enter the oppenent's guess ")
    while usersGuess != "":
        status = guessIsAHit(usersGuess, shipInfo)
        if status != MISS:
            print(usersGuess, "is a hit")
            letter, number = splitLocation(usersGuess)
            myShips[letter][number] = HITSHIP
            shipName = status  # status returns the name of the ship, if a ship was hit
            # if shipIsSunk(hitShip, myShips, shipInfo):
            #   print ("some ship has been sunk")
        else:
            print(usersGuess, "is a miss")
            letter, number = splitLocation(usersGuess)
            myShips[letter][number] = MISS

        printGrid("My Guesses", myGuesses)
        printGrid("My Ships", myShips)

        usersGuess = input("Enter the opponent's next guess ")


main()
