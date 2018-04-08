from utils import randomPlace
from texttable import Texttable


class Game:
    def __init__(self, size):
        self._size = size
        self._nWumpus = 1
        self._nPits = self._size - 2
        self._nGold = 1
        self._board = self.initializeBoard()
        self._player = [self._size - 1, 0]
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

    def placeWumpus(self, lin, col):
        self.placeInBoard(lin, col, "WUMPUS")

        # CHECK TOP
        if((lin - 1) >= 0):
            self.placeInBoard((lin - 1), col, "ODOR")

        # CHECK RIGHT
        if((col + 1) < self._size):
            self.placeInBoard(lin, col + 1, "ODOR")

        # CHECK BOTTOM
        if((lin + 1) < self._size):
            self.placeInBoard((lin + 1), col, "ODOR")
        # CHECK LEFT
        if((col - 1) >= 0):
            self.placeInBoard(lin, col - 1, "ODOR")
        
        

    def generateWorld(self):
        # GENERATE GOLD
        while(True):
            goldRandomPosition = randomPlace(self._size)
            if(not(goldRandomPosition == self._player)):
                self.placeInBoard(
                    goldRandomPosition[0], goldRandomPosition[1], "GOLD")
                break

        # GENERATE WUMPUS
        while(True):
            wumpusRandomPosition = randomPlace(self._size)
            if(not(self._board[wumpusRandomPosition[0]][wumpusRandomPosition[1]] == None and goldRandomPosition == self._player)):
                # self.placeInBoard(
                #     wumpusRandomPosition[0], wumpusRandomPosition[1], "WUMPUS")
                self.placeWumpus(
                    wumpusRandomPosition[0], wumpusRandomPosition[1])

                break

                # TODO GENERATE PITS AND BREEZES
