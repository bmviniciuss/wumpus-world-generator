from utils import randomPlace
from texttable import Texttable

# CONSTANTS
PIT = "PIT"
PLAYER = "PLAYER"
BREEZE = "BREEZE"
STENCH = "STENCH"
WUMPUS = "WUMPUS"
GOLD = "GOLD"

# GAME
class Game:
    def __init__(self, size):
        self._size = size
        # WUMPUS
        self._nWumpus = 1
        self._wumpus = []
        # PITS
        self._nPits = self._size - 2
        self._pits = []
        # GOLD
        self._nGold = 1
        self._gold = []
        # PLAYER
        self._player = [self._size - 1, 0]

        self._board = self.initializeBoard()
        self.placeInBoard(self._player[0], self._player[1], PLAYER)

        self.generateWorld()

    # INITIALIZE MATRIX
    def initializeBoard(self):
        return [[[] for x in range(self._size)] for lin in range(self._size)]

    # PLACE A CONSTANT ON THE BOARD
    def placeInBoard(self, lin, col, content):
        self._board[lin][col].append(content)

    # PRINT BOARD
    def printBoard(self):
        row = []
        for lin in self._board:
            subRow = []
            for e in lin:
                subRow.append(e)
            row.append(subRow)
        t = Texttable()
        t.add_rows(row)
        print(t.draw())

    # CHECK IF GIVEN PLACE CONTAINS PARAMETER
    def checkPosition(self, lin, col, content):
        return content in self._board[lin][col]

    # PLACE A PIT IN THE BOARD
    def placePit(self, pos):
        self.placeInBoard(pos[0], pos[1], PIT)
        self._pits.append(pos)

    # LOOP OVER THE PITS AND PLACES ALL THE BREEZES
    def putBreezes(self):
        for pit in self._pits:
            pLin = pit[0]
            pCol = pit[1]
            # TOP
            if(pLin - 1 >= 0):
                top = [pLin - 1, pCol]
                if(top not in self._pits):
                    if(not(self.checkPosition(pLin - 1, pCol, BREEZE))):
                        self.placeInBoard(pLin - 1, pCol, BREEZE)
            # BOTTOM
            if(pLin + 1 < self._size):
                bottom = [pLin + 1, pCol]

                if(bottom not in self._pits):
                    if(not(self.checkPosition(pLin + 1, pCol, BREEZE))):
                        self.placeInBoard(pLin + 1, pCol, BREEZE)
            # RIGHT
            if(pCol + 1 < self._size):
                right = [pLin, pCol + 1]
                if(right not in self._pits):
                    if(not(self.checkPosition(pLin, pCol + 1, BREEZE))):
                        self.placeInBoard(pLin, pCol + 1, BREEZE)
            # LEFT
            if(pCol - 1 < self._size):
                left = [pLin, pCol - 1]
                if(left not in self._pits):
                    if(not(self.checkPosition(pLin, pCol - 1, BREEZE))):
                        self.placeInBoard(pLin, pCol - 1, BREEZE)

    # PLACE WUMPUS AND CHECK AND PUT STENCHS
    def placeWumpus(self, pos):
        self.placeInBoard(pos[0], pos[1], WUMPUS)

        pLin = pos[0]
        pCol = pos[1]
        # TOP
        if(pLin - 1 >= 0):
            top = [pLin - 1, pCol]
            if(top not in self._pits):
                if(not(self.checkPosition(pLin - 1, pCol, STENCH))):
                    self.placeInBoard(pLin - 1, pCol, STENCH)
        # BOTTOM
        if(pLin + 1 < self._size):
            bottom = [pLin + 1, pCol]

            if(bottom not in self._pits):
                if(not(self.checkPosition(pLin + 1, pCol, STENCH))):
                    self.placeInBoard(pLin + 1, pCol, STENCH)
        # RIGHT
        if(pCol + 1 < self._size):
            right = [pLin, pCol + 1]
            if(right not in self._pits):
                if(not(self.checkPosition(pLin, pCol + 1, STENCH))):
                    self.placeInBoard(pLin, pCol + 1, STENCH)
        # LEFT
        if(pCol - 1 < self._size):
            left = [pLin, pCol - 1]
            if(left not in self._pits):
                if(not(self.checkPosition(pLin, pCol - 1, STENCH))):
                    self.placeInBoard(pLin, pCol - 1, STENCH)

    # PLACE GOLD IN THE BOARD
    def placeGold(self, goldPos):
        self.placeInBoard(goldPos[0], goldPos[1], GOLD)

    # GENERATE WORLD
    def generateWorld(self):
        # GENERATE PITS AND BREEZES
        for i in range(self._nPits):
            while(True):
                pitRandomPosition = randomPlace(self._size)

                if(not(pitRandomPosition == self._player) and (pitRandomPosition not in self._pits)):
                    self.placePit(pitRandomPosition)
                    break
        self.putBreezes()

        # GENERATE WUMPUS
        while(True):
            wumpusRandomPosition = randomPlace(self._size)
            if(not(wumpusRandomPosition == self._player) and wumpusRandomPosition not in self._pits):
                self.placeWumpus(wumpusRandomPosition)
                break

        # GENERATE GOLD
        while(True):
            goldRandomPosition = randomPlace(self._size)
            if(not(goldRandomPosition == self._player) and (goldRandomPosition not in self._pits)):
                self.placeGold(goldRandomPosition)
                break
