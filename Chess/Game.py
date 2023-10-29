import pygame
from Pieces import Pawn
from sys import exit
from Board import ChessBoard

pygame.init()

class Game:
    sc = pygame.display.set_mode((1200, 1200))
    clock = pygame.time.Clock()
    chess_board = ChessBoard()
    validMoves = list()
    turn = 'w'

    def drawPieces(self):
        for row in self.chess_board.board:
            for square in row:
                if square != '-':
                    self.sc.blit(square.img, square.rect)

    def checkSelection(self):
        for row in self.chess_board.board:
            for piece in row:
                if piece != '-':
                    piece.selected = False
                    self.validMoves = list()
                    if piece.rect.collidepoint(pygame.mouse.get_pos()):
                        piece.selected = True

    def changePosition(self):
        for row in self.chess_board.board:
            for piece in row:
                if piece != '-':
                    if piece.selected:
                        chPiece = piece


        if self.validMoves:
            for move in self.validMoves:
                if move.collidepoint(pygame.mouse.get_pos()):
                    x = round(move.x / 150)
                    y = round(move.y / 150)
                    self.chess_board.board[chPiece.coord[0]][chPiece.coord[1]] = '-'
                    chPiece.changeCoords((y, x))
                    self.chess_board.board[y][x] = chPiece
                    if isinstance(chPiece, Pawn):
                        chPiece.ftmove = False
                    chPiece.updatePos()


    def drawPossibleMoves(self):
        for row in self.chess_board.board:
            for square in row:
                if square != '-':
                    if square.selected:
                        for move in square.possibleMoves(self.chess_board.board):
                            self.validMoves.append(pygame.rect.Rect(move[1] * 150, move[0] * 150, 150, 150))
                            pygame.draw.rect(self.sc, (0, 200, 0, 50), pygame.rect.Rect(move[1] * 150, move[0] * 150, 150, 150))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.changePosition()
                        self.checkSelection()
                    

            self.sc.blit(self.chess_board.img, (0, 0))

            self.drawPieces()
            self.drawPossibleMoves()
            


            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.run()
