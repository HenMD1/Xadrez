import pygame
from Pieces import Pawn, King
from Board import ChessBoard
from sys import exit

pygame.init()

class Game:
    sc = pygame.display.set_mode((760, 760))
    pygame.display.set_caption('Xadrez')
    clock = pygame.time.Clock()
    chess_board = ChessBoard()
    validMoves = list()
    pieceList = list()
    turn = 'w'
    selectedPiece = None
    selectedPieceValidMoves = None

    def drawPieces(self):
        for piece in self.pieceList:
            self.sc.blit(piece.img, piece.rect)

    def getPiecesList(self):
        self.pieceList = list()
        for row in self.chess_board.board:
            for piece in row:
                if piece != '-':
                    self.pieceList.append(piece)


    def checkSelection(self):
        for piece in self.pieceList:
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
            if not self.validMoves and self.selectedPieceValidMoves:
                for move in self.selectedPieceValidMoves:
                        self.validMoves.append(pygame.rect.Rect(move[1] * 95, move[0] * 95, 95, 95))

        for move in self.validMoves:
            surf = pygame.surface.Surface((95, 95))
            surf.fill((0, 200, 0, 100))
            surf.set_alpha(100)
            self.sc.blit(surf, move)


    def checkCheck(self, color):
        otherMoves = list()

        for piece in self.pieceList:
            if isinstance(piece, King) and piece.color == color:
                king = piece

        for piece in self.pieceList:
            if piece != '-':
                if not isinstance(piece, King) and piece.color != color:
                    for move in piece.possibleMoves(self.chess_board.board):
                        otherMoves.append(move)

        list(set(otherMoves))

        if king.coord in otherMoves:
            return True
        
    def removeUnCheckMoves(self):
        KeepCheckMoves = list()
        if self.turn == 'w':
            for piece in self.pieceList:
                if piece.color == 'w':
                    KeepCheckMoves = list()
                    possMoves = piece.possibleMoves(self.chess_board.board)
                    print(piece)
                    print(piece.coord)
                    for move in possMoves:
                        prevPos = piece.coord
                        piece.changeCoords(move)
                        if self.checkCheck('w') and move not in KeepCheckMoves:
                            print(move)
                            KeepCheckMoves.append(move)
                        piece.changeCoords(prevPos)

        print('34875934875345')
        print(KeepCheckMoves) # KeepCheckMoves sempre vazio!!!!


        if self.selectedPiece:
            print(self.selectedPiece)
            print(self.selectedPiece.coord)
            print(KeepCheckMoves)
            self.selectedPieceValidMoves = list(set(self.selectedPiece.possibleMoves(self.chess_board.board)) - set(KeepCheckMoves))


    def run(self):
        self.getPiecesList()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.changePosition()
                        self.selectedPiece = None
                        self.getPiecesList()
                        self.checkSelection()

                    if self.selectedPiece:
                        self.selectedPieceValidMoves = self.selectedPiece.possibleMoves(self.chess_board.board)
                        
                    self.removeUnCheckMoves()

            self.sc.blit(self.chess_board.img, (0, 0))

            self.drawPieces()
            self.drawPossibleMoves()
            


            pygame.display.update()
            self.clock.tick(60)

game = Game()
game.run()
