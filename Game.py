from utils import randomPlace
from texttable import Texttable

BREEZE = "BREEZE"


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
        self.placeInBoard(self._player[0], self._player[1], "PLAYER")

        self.generateWorld()

    def placeInBoard(self, lin, col, content):
        self._board[lin][col].append(content)

    def initializeBoard(self):
        return [[[] for x in range(self._size)] for lin in range(self._size)]

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

    def checkPosition(self, lin, col, content):
        return content in self._board[lin][col]

    def isEmpty(self, lin, col):
        return len(self._board[lin][col]) == 0

    def placePit(self, lin, col):
        self.placeInBoard(lin, col, "PIT")
        self._pits.append([lin, col])

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

    def generateWorld(self):
        # GENERATE PITS AND BREEZES
        for i in range(self._nPits):
            while(True):
                pitRandomPosition = randomPlace(self._size)

                if(not(pitRandomPosition == self._player) and (pitRandomPosition not in self._pits)):
                    self.placePit(pitRandomPosition[0], pitRandomPosition[1])
                    break
            self.putBreezes()
