from __future__ import annotations
import numpy as np
from pieces import Piece
from setup import *


def board_limits(X, Y):
    if (0 <= X < 8) and (0 <= Y < 8):
        return True
    else:
        return False

def is_empty(X, Y, game: Game):
    for piece in game.board:
        if (X,Y) == piece.coordinates:
            return False
    return True



def moves (piece: Piece, game: Game):
    (X,Y) = piece.coordinates
    BlankBoard = np.full((8,8), False)
    
    if piece.type == 'WhitePawn':
        BlankBoard[X-1, Y] = True
        if X == 6:
            if is_empty(X-1,Y, game):
                BlankBoard[X-2, Y] = True
    else:
        BlankBoard = np.full((8,8), True)
    
    return BlankBoard



