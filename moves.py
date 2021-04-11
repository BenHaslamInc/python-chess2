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

def what_colour(X, Y, game: Game):
    for piece in game.board:
        if (X,Y) == piece.coordinates:
            return piece.colour



def moves (piece: Piece, game: Game):
    (X,Y) = piece.coordinates
    BlankBoard = np.full((8,8), False)
    
    if piece.type == 'WhitePawn' or piece.type == 'BlackPawn':

        if piece.colour == 0:
            x = -1
        else:
            x = 1

        if is_empty(X+x,Y, game):
            BlankBoard[X+x, Y] = True
            print ('one')
            print (X+x, Y)

        if not is_empty(X+x,Y+1, game):
            if piece.colour != what_colour(X+x,Y+1, game):
                BlankBoard[X+x,Y+1] = True
        
        if not is_empty(X+x,Y-1, game):
            if piece.colour != what_colour(X+x,Y-1, game):
                BlankBoard[X+x,Y-1] = True

        if X == 6 or X == 1:
            if is_empty(X+x,Y, game) and is_empty(X+x*2,Y, game):
                BlankBoard[X+x*2, Y] = True
                print ('two')
                print (X+x, Y)
        
        if not is_empty(X+x*2,Y+1, game):
            if piece.colour != what_colour(X+x*2,Y+1, game):
                BlankBoard[X+x*2,Y+1] = True
        
        if not is_empty(X+x*2,Y-1, game):
            if piece.colour != what_colour(X+x*2,Y-1, game):
                BlankBoard[X+x*2,Y-1] = True
    else:
        BlankBoard = np.full((8,8), True)
    
    return BlankBoard



