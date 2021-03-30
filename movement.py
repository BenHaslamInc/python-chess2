import numpy as np

def MoveLetter ():
    
    L = str (input('Select a square A-H: '))
    print ('you have selected: ', L)

    if L == 'A' or L == 'a':
        return 0
    elif L == 'B' or  L == 'b':
        return 1
    elif L == 'C' or  L == 'c':
        return 2
    elif L == 'D' or  L == 'd':
        return 3
    elif L == 'E' or  L == 'e':
        return 4
    elif L == 'F' or  L == 'f':
        return 5
    elif L == 'G' or  L == 'g':
        return 6
    elif L == 'H' or  L == 'h':
        return 7
    else:
        print ('That is not an option, try again')
        MoveLetter ()

def MoveNumber ():

    N = int (input('Select a square 1-8 '))

    if 1 <= N <= 8:
        return N -1
    else:
        print ('That is not an option, try again')
        MoveNumber () 