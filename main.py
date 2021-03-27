
from __future__ import annotations
import numpy as np
from pieces import *


class Game:
    def __init__(self: Game) -> None:
        self.board = get_starting_pieces()

    def over(self: Game) -> bool:
        return False


def get_starting_pieces() -> list[Piece]:

    # Create list
    list_of_pieces: list[Piece] = []

    # Fill the list
    list_of_pieces.append(CastleBlack())
    list_of_pieces.append(KnightBlack())
    list_of_pieces.append(BishopBlack())
    list_of_pieces.append(QueenBlack())
    list_of_pieces.append(KingBlack())
    list_of_pieces.append(BishopBlack())
    list_of_pieces.append(KnightBlack())
    list_of_pieces.append(CastleBlack())

    for i in range (8,16):
        list_of_pieces.append(PawnBlack())

    for i in range (16,24):
        list_of_pieces.append(Pawn())

    list_of_pieces.append(Castle())
    list_of_pieces.append(Knight())
    list_of_pieces.append(Bishop())
    list_of_pieces.append(Queen())
    list_of_pieces.append(King())
    list_of_pieces.append(Bishop())
    list_of_pieces.append(Knight())
    list_of_pieces.append(Castle())

    # Set coordinates
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
    
    # Set piece types

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


