from __future__ import annotations
import numpy as np
from pieces import *


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
        piece.coordinates = (X,Y)
        K+=1
    
    # Set piece types

    return list_of_pieces