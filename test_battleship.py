""" File:test_battleship.py
    Author: Xin Li
    Purpose: additional test cases for battleship
"""

from battleship import Board
from battleship import Ship
from battleship import Pos
from standard_ships import *

print("******** BEGINNING TESTCASE ********")

board = Board(10)
board.print()

player_A_ships = [Battleship(3),
                  Cruiser(0),
                  Carrier(0),
                  Submarine(0),
                  Destroyer(3)]

board.add_ship(player_A_ships[0], Pos(1, 5))
board.add_ship(player_A_ships[1], Pos(1, 2))
board.add_ship(player_A_ships[2], Pos(4, 5))
board.add_ship(player_A_ships[3], Pos(5, 8))
board.add_ship(player_A_ships[4], Pos(9, 2))

moveMiss = Pos(0,1)
move1 = Pos(1, 2)
move2 = Pos(2, 2)
move3 = Pos(3, 2)

board.attempt_move(move1)
board.attempt_move(move2)
board.attempt_move(move3)

board.print()
for s in player_A_ships:
    s.print()
print()

print("Testcase completed successfully.")
