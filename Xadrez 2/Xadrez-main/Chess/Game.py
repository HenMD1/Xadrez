import pygame
from Pieces import Pawn
from Board import ChessBoard
from sys import exit

pygame.init()

class Game:
    sc = pygame.display.set_mode((760, 760))
    pygame.display.set_caption('Xadrez')
    clock = pygame.time.Clock()
    chess_board = ChessBoard()
    validMoves = list()
    turn = 'w'
    selectedPiece = None

    def drawPieces(self):
        for row in self.chess_board.board:
            for square in row:
                if square != '-':
                    self.sc.blit(square.img, square.rect)

    def checkSelection(self):
        for row in self.chess_board.board:
            for piece in row:
                if piece != '-':
                    if piece.color == self.turn:
                        piece.selected = False
                        self.validMoves = list()
                        if piece.rect.collidepoint(pygame.mouse.get_pos()):
                            piece.selected = True
                            self.selectedPiece = piece

    def changePosition(self):
        if self.validMoves and self.selectedPiece:
            for move in self.validMoves:
                if move.collidepoint(pygame.mouse.get_pos()):
                    x = round(move.x / 95)
                    y = round(move.y / 95)
                    self.chess_board.board[self.selectedPiece.coord[0]][self.selectedPiece.coord[1]] = '-'
                    self.selectedPiece.changeCoords((y, x))
                    self.chess_board.board[y][x] = self.selectedPiece
                    if isinstance(self.selectedPiece, Pawn):
                        self.selectedPiece.ftmove = False
                    self.selectedPiece.updatePos()

                    if self.turn == 'w':
                        self.turn = 'b'
                    elif self.turn == 'b':
                        self.turn = 'w'
                    break

    def drawPossibleMoves(self):
        if self.selectedPiece:
            if not self.validMoves:
                for move in self.selectedPiece.possibleMoves(self.chess_board.board):
                        self.validMoves.append(pygame.rect.Rect(move[1] * 95, move[0] * 95, 95, 95))

        for move in self.validMoves:
            surf = pygame.surface.Surface((95, 95))
            surf.fill((0, 200, 0, 100))
            surf.set_alpha(100)
            self.sc.blit(surf, move)




    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.changePosition()
                        self.selectedPiece = None
                        self.checkSelection()

                    elif event.button == 2:
                        self.selectedPiece = None

            self.sc.blit(self.chess_board.img, (0, 0))

            self.drawPieces()
            self.drawPossibleMoves()



            pygame.display.update()
            self.clock.tick(60)

game = Game()
game.run()
