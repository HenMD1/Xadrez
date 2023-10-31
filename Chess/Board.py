import pygame
from Pieces import Pawn, Bishop, Rook, King, Queen, Knight

pygame.init()

class ChessBoard:

    img = pygame.image.load('Chess/Imgs/ChessPattern.png')
    #img = pygame.transform.smoothscale(img, (760, 760))

    board = [['-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-'],]
    
    board[0][0] = Rook('b', (0, 0))
    board[0][1] = Knight('b', (0, 1))
    board[0][2] = Bishop('b', (0, 2))
    board[0][3] = Queen('b', (0, 3))
    board[0][4] = King('b', (0, 4))
    board[0][5] = Bishop('b', (0, 5))
    board[0][6] = Knight('b', (0, 6))
    board[0][7] = Rook('b', (0, 7))

    board[1][0] = Pawn('b', (1, 0))
    board[1][1] = Pawn('b', (1, 1))
    board[1][2] = Pawn('b', (1, 2))
    board[1][3] = Pawn('b', (1, 3))
    board[1][4] = Pawn('b', (1, 4))
    board[1][5] = Pawn('b', (1, 5))
    board[1][6] = Pawn('b', (1, 6))
    board[1][7] = Pawn('b', (1, 7))



    board[7][0] = Rook('w', (7, 0))
    board[7][1] = Knight('w', (7, 1))
    board[7][2] = Bishop('w', (7, 2))
    board[7][3] = Queen('w', (7, 3))
    board[7][4] = King('w', (7, 4))
    board[7][5] = Bishop('w', (7, 5))
    board[7][6] = Knight('w', (7, 6))
    board[7][7] = Rook('w', (7, 7))

    board[6][0] = Pawn('w', (6, 0))
    board[6][1] = Pawn('w', (6, 1))
    board[6][2] = Pawn('w', (6, 2))
    board[6][3] = Pawn('w', (6, 3))
    board[6][4] = Pawn('w', (6, 4))
    board[6][5] = Pawn('w', (6, 5))
    board[6][6] = Pawn('w', (6, 6))
    board[6][7] = Pawn('w', (6, 7))


    def drawBoard(self):
        pass

