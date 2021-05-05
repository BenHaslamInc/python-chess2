from __future__ import annotations
import numpy as np
from setup import *
from movement import *
from moves import moves
import copy


def print_board(board: list[Piece]) -> None:

    # Build the board
    BlankBoard = np.full((8, 8), '|    ')

    for piece in game.board:
        (X, Y) = piece.coordinates
        BlankBoard[X][Y] = piece.symbol

    # Display the board

    Y_Coordinates = "    A    B    C    D    E    F    G    H  "

    for piece in game.taken_blacks:
        print(piece.symbol, end='')
    print('', end='\n')
    for piece in game.taken_whites:
        print(piece.symbol, end='')

    print('', end='\n')
    print(Y_Coordinates, end='\n')
    K = 0
    for row in BlankBoard:
        print('', end='\n')
        K += 1
        print(K, end=' ')
        for collum in row:
            print(collum, end='')
        print('|', end='\n')


def play(turn):

    while not game.over():

        print_board(game.board)

        if turn == 0:
            print('White turn!')
        else:
            print('Blacks turn!')

        if inCheck(turn, game):
            print('You are in check, protect your king!')

        print('Select which piece to move')
        inputX = MoveNumber()
        inputY = MoveLetter()

        # print ("Selected piece", inputX, inputY )

        print('Select where to move')
        outputX = MoveNumber()
        outputY = MoveLetter()

        # print ("Selected piece", outputX, outputY )
        if SelectPiece(inputX, inputY, outputX, outputY, turn, game):

            if turn == 0:
                turn = 1
            else:
                turn = 0

            continue

        continue


def SelectPiece(inputX, inputY, outputX, outputY, turn, game):
    Moved = False
    game_2 = copy.deepcopy(game)
    for piece in game_2.board:
        (X, Y) = piece.coordinates
        input = (int(inputX), int(inputY))
        output = (int(outputX), int(outputY))

        if (X, Y) == input:

            Moves = moves(piece, game_2)
            if not Moves[outputX][outputY]:
                print("That is not a possible move, try again!")
                return False

            if turn != piece.colour:
                print("That is not your piece, try again!")
                return False

            K = taken(output, turn, game_2)
            if K == 0:
                return False

            piece.coordinates = output

            # Check if your in check

            if inCheck(turn, game_2):
                print('This move puts you in check!')
                return False

            # If not in check, make the changes permenant

            piece_index = game_2.board.index(piece)
            print('piece index: ', piece_index)

            K = taken(output, turn, game)
            if K == 0:
                return False

            piece = game.board[piece_index]
            print(piece)
            piece.coordinates = output

            Moved = True
            return True
    if Moved == False:
        print('There is no piece there, try again!')
    return False


def inCheck(turn, game):

    # Get king coordinates

    for piece in game.board:
        if piece.colour == turn and piece.type == 'King':
            (X, Y) = piece.coordinates

    for piece in game.board:
        if piece.colour != turn:
            piece_moves = moves(piece, game)
            if piece_moves[X, Y]:
                return True

    return False


game = Game()


turn = 0

play(turn)
