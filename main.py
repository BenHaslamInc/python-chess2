
from __future__ import annotations
import numpy as np
from setup import *
from movement import *


class Game:
    def __init__(self: Game) -> None:
        self.board = get_starting_pieces()

    def over(self: Game) -> bool:
        return False


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



def play(turn):

    print_board(game.board)

    if turn == 0:
        print ('White turn!')
    else:
        print ('Blacks turn!')

    print ('Select which piece to move')
    inputX = MoveNumber ()
    inputY = MoveLetter ()

    print ("Selected piece", inputX, inputY )

    print ('Select where to move')
    outputX = MoveNumber ()
    outputY = MoveLetter ()

    print ("Selected piece", outputX, outputY )
    SelectPiece(inputX, inputY, outputX, outputY, turn)

    if turn == 0:
        turn = 1
    else:
        turn = 1
        
    play(turn)


        
    

def SelectPiece(inputX, inputY, outputX, outputY, turn):
    Moved = False
    for piece in game.board:
        (X,Y) = piece.coordinates
        # print ('Piece coordinates: ', (X,Y))
        input = (int(inputX), int(inputY))
        # print ('input: ', input)
        output = (int (outputX), int(outputY))

        if (X,Y) == input:
            piece.coordinates = output
            if turn == 0:
                turn = 1
            else:
                turn = 0
            print(piece.coordinates)
            Moved = True
            break
    if Moved == False:
        print ('There is no piece there, try again!')
    play(turn)

game = Game()

while not game.over():
    turn = 0
    print ('Piece coordinates: ')
    for piece in game.board:
        print (piece.coordinates)

    play(turn)

    break




