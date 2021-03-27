
from __future__ import annotations
from board import Board
import numpy as np


class Game:
    def __init__(self: Game) -> None:
        self.board = get_starting_pieces()
        self.Boards = Board

    def over(self: Game) -> bool:
        return False

class Piece:
    def __init__(self: Piece) -> None:
        self.coordinates: tuple[int, int] = (0, 0)
        self.symbol = '| P  '


def get_starting_pieces() -> list[Piece]:
    list_of_pieces: list[Piece] = []

    for i in range(32):
        list_of_pieces.append(Piece())

    K = 0
    for piece in list_of_pieces:
        Y = int(K%8)
        X = int((K/8)%8)
        if (X == 2):
            X = 6
        if (X == 3):
            X = 7
        piece.coordinates = (X, Y)
        K+=1

    return list_of_pieces


def print_board(board: list[Piece]) -> None:

    # Build the board
    BlankBoard = np.full((8,8), '|    ')

    for piece in game.board:
        (X,Y) = piece.coordinates
        BlankBoard[X][Y] = piece.symbol

    # Display the board

    Y_Coordinates = "    A    B    C    D    E    F    G    H  "

    print ('', end='\n')
    print (Y_Coordinates, end='\n')
    K = 0
    for row in BlankBoard:
        print ('', end='\n')
        K+=1
        print (K, end=' ')
        for collum in row:
            print (collum, end='')
        print ('|', end='\n')

game = Game()

while not game.over():
    print_board(game.board)
    break


