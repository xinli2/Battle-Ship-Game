""" File:my_test_board_size.py
    Author: Xin Li
    Purpose: additional test cases for board initiation
"""

from battleship import Board

print("******** BEGINNING TESTCASE ********")

board = Board(20)
board.print()

boardInValid = Board(-1)

print("Testcase completed successfully.")
