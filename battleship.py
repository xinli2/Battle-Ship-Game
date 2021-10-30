""" File:battleship.py
    Author: Xin Li
    Purpose: Classes and Core logic for battleship game
"""
import copy

class Pos:
    """ This class represents the position on our battleship game board
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x,y)

    def rotate(self, rot):
        """
        This function rotate a coordinate based on the rotation Id
        :argument rot: the rotation id for current rotation operation
        :return: rotated Pos object
        """
        assert 3 >= rot >= 0
        if rot == 0:
            return Pos(self.x, self.y)
        elif rot == 1:
            return Pos(self.y, -self.x)
        elif rot == 2:
            return Pos(-self.x, -self.y)
        elif rot == 3:
            return Pos(-self.y, self.x)

class Board:
    """ This class represents board where the battleship game
    is played on and its main logic, including
    interactions user can have with the board, certain checks
    on game progress and presenting the progress to users
     """
    def __init__(self, size):
        self.board = []
        self.fleet = []
        if size < 1:
            self.size = 1
            print("invalid board size.")
            return
        self.size = size
        for i in range(size):
            self.board.append(["."]*size)

    def print(self):
        """
        This function will print the current board with
        x and y axies
        :return:
        """
        output = copy.deepcopy(self.board)
        i = self.size-1
        for line in output:
            if i<10:
                line.insert(0, " "+ str(i)+" |")
            else:
                line.insert(0, str(i)+" |")
            line.append("|")
            i = i-1
        boundary = ["   +"] + ["-"]*self.size + ["+"]
        print('-'.join(boundary))
        print('\n'.join([' '.join([str(cell) for cell in row])
                         for row in output]))
        print('-'.join(boundary))
        for lower in self._getLowerIndex():
            print(' '.join(lower))

    def add_ship(self, ship, pos):
        """
        This function allows the game to add ships when board
        is being initialized
        :argument ship: ship object that represent a battlship
        :argument pos: position info about where the ship should
        be added on the board
        :return:
        """
        if len(ship.shape) > self.size:
            print("This ship is too big.")
            return
        self.fleet.append(ship)
        i = 0
        for p in ship.shape:
            newCoord = self._getActualCoordFromPos(pos, p)
            self.board[newCoord[0]][newCoord[1]] = ship.name[0]
            ship.shape[i] = Pos(newCoord[0], newCoord[1])
            i = i + 1

    def _getActualCoordFromPos(self, pos, coord):
        """
        This private function will transform the user input
         coordinate to actual location on our board
        :argument pos: User input position
        :argument coord: Offset
        :return: actual index in our 2 dimensional array
        """
        return [self.size - pos.y - coord.y - 1, pos.x + coord.x]

    def _getLowerIndex(self):
        """
        This private function generate the X axis for the board
        :return: X axis for the board
        """
        lowerBase = ["    "]
        lowerExtra = ["      "] + [" "]*9
        for i in range(self.size):
            if (i<10):
                lowerBase.append(str(i))
            else:
                lowerBase.append(str((i)%10))
                lowerExtra.append(str(i)[0])
        if len(lowerExtra)>10:
            return [lowerExtra, lowerBase]
        else:
            return [lowerBase]

    def has_been_used(self, pos):
        """
        This function checkes if the position has been operated
         in an earlier round
        :argument pos: User input position
        :return: True if this position has been operated;
        False if this position is fresh
        """
        realPos = self._getActualCoordFromPos(pos, Pos(0, 0))
        posChar = self.board[realPos[0]][realPos[1]]
        if posChar == 'o' or posChar == '*' or posChar == 'X':
            return True
        return False

    def attempt_move(self, pos):
        """
        This function registers user operation in the current
        round, updates ship information and board
        :argument pos: User input position
        :return: Whether this operation is a "Hit" or a "Miss"
        """
        assert -1 < pos.x < self.size
        assert -1 < pos.y < self.size
        realPos = self._getActualCoordFromPos(pos, Pos(0,0))
        posChar = self.board[realPos[0]][realPos[1]]
        if posChar.isalpha():
            self.board[realPos[0]][realPos[1]] = '*'
            for ship in self.fleet:
                i = 0
                for p in ship.shape:
                    if p.x == realPos[0] and p.y == realPos[1]:
                        ship.status = self._updateString(i, "*", ship.status)
                        if ship.is_sunk():
                            for s in ship.shape:
                                self.board[s.x][s.y] = 'X'
                            return "Sunk ("+ ship.name+ ")"
                        return "Hit"
                    i = i + 1
        elif posChar == '.':
            self.board[realPos[0]][realPos[1]] = 'o'
        return "Miss"

    def _updateString(self, index, value, oldStr):
        """
        This private function will update a string based index
        and value
        :argument index: Index in string where you want the letter
        to be replaced
        :argument value: Letter to replace the target index position
        :argument oldStr: Original string
        :return: Updated string
        """
        stringList = list(oldStr)
        stringList[index] = value
        return "".join(stringList)

class Ship:
    """
    This class represents a battleship.
    """
    def __init__(self, name, shape):
        self.name= name
        self.shape = shape
        self.status = self.name[0] * len(self.shape)

    def is_sunk(self):
        """
        This function check if the current battleship
        is sunk during the fight
        :return: True if the ship is sunk, False if the
        ship still has hit point(s)
        """
        for letter in self.status:
            if letter != '*':
                return False
        return True

    def print(self):
        """
        This function prints information and status
        of a battleship
        :return:
        """
        print (self.status+ " "* (10-len(self.status))+ self.name)
