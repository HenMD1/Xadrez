import pygame

pygame.init()

#===========================================================#
# O REI NÃO PODE TOMAR UMA PEÇA DEFENDIDA !!!! ARRUMAR !!!! #
#===========================================================#

class Piece:
    selected = False
    defended = False
    def __init__(self, color, coord) -> None:
        self.color = color
        self.coord = coord

    def changeCoords(self, newCoords):
        self.coord = newCoords

    def updatePos(self):
        self.rect = self.img.get_rect(topleft = (self.coord[1] * 150, self.coord[0] * 150))

##
##
##

class King(Piece):
    inCheck = False
    bimg = pygame.image.load('Chess/Imgs/KingB.png')
    wimg = pygame.image.load('Chess/Imgs/KingW.png')

    def __init__(self, color, coord) -> None:
        super().__init__(color, coord)
        self.img = self.bimg if self.color == 'b' else self.wimg
        self.img = pygame.transform.smoothscale(self.img, (145, 145))
        self.rect = self.img.get_rect(topleft = (self.coord[1] * 150, self.coord[0] * 150))

    def possibleMoves(self, board):
        possMoves = list()
        
        # Esquerda
        if self.coord[1] > 0:
            if self.color == 'w':
                if board[self.coord[0]][self.coord[1] - 1] == '-' or board[self.coord[0]][self.coord[1] - 1].color == 'b':
                    possMoves.append((self.coord[0], self.coord[1] - 1))

            elif self.color == 'b':
                if board[self.coord[0]][self.coord[1] - 1] == '-' or board[self.coord[0]][self.coord[1] - 1].color == 'w':
                    possMoves.append((self.coord[0], self.coord[1] - 1))

        # Direita
        if self.coord[1] < 7:
            if self.color == 'w':
                if board[self.coord[0]][self.coord[1] + 1] == '-' or board[self.coord[0]][self.coord[1] + 1].color == 'b':
                    possMoves.append((self.coord[0], self.coord[1] + 1))

            elif self.color == 'b':
                if board[self.coord[0]][self.coord[1] + 1] == '-' or board[self.coord[0]][self.coord[1] + 1].color == 'w':
                    possMoves.append((self.coord[0], self.coord[1] + 1))
            
        # Cima
        if self.coord[0] > 0:
            if self.color == 'w':
                if board[self.coord[0] - 1][self.coord[1]] == '-' or board[self.coord[0] - 1][self.coord[1]].color == 'b':
                    possMoves.append((self.coord[0] - 1, self.coord[1]))

            elif self.color == 'b':
                if board[self.coord[0] - 1][self.coord[1]] == '-' or board[self.coord[0] - 1][self.coord[1]].color == 'w':
                    possMoves.append((self.coord[0] - 1, self.coord[1]))

        # Baixo
        if self.coord[0] < 7:
            if self.color == 'w':
                if board[self.coord[0] + 1][self.coord[1]] == '-' or board[self.coord[0] + 1][self.coord[1]].color == 'b':
                    possMoves.append((self.coord[0] + 1, self.coord[1]))

            elif self.color == 'b':
                if board[self.coord[0] + 1][self.coord[1]] == '-' or board[self.coord[0] + 1][self.coord[1]].color == 'w':
                    possMoves.append((self.coord[0] + 1, self.coord[1]))
            
        # Cima Esquerda
        if self.coord[0] > 0 and self.coord[1] > 0:
            if self.color == 'w':
                if board[self.coord[0] - 1][self.coord[1] - 1] == '-' or board[self.coord[0] - 1][self.coord[1] - 1].color == 'b':
                    possMoves.append((self.coord[0] - 1, self.coord[1] - 1))

            elif self.color == 'b':
                if board[self.coord[0] - 1][self.coord[1] - 1] == '-' or board[self.coord[0] - 1][self.coord[1] - 1].color == 'w':
                    possMoves.append((self.coord[0] - 1, self.coord[1] - 1))
            
        # Cima Direita
        if self.coord[0] > 0 and self.coord[1] < 7:
            if self.color == 'w':
                if board[self.coord[0] - 1][self.coord[1] + 1] == '-' or board[self.coord[0] - 1][self.coord[1] + 1].color == 'b':
                    possMoves.append((self.coord[0] - 1, self.coord[1] + 1))

            elif self.color == 'b':
                if board[self.coord[0] - 1][self.coord[1] + 1] == '-' or board[self.coord[0] - 1][self.coord[1] + 1].color == 'w':
                    possMoves.append((self.coord[0] - 1, self.coord[1] + 1))

        # Baixo Esquerda
        if self.coord[0] < 7 and self.coord[1] > 0:
            if self.color == 'w':
                if board[self.coord[0] + 1][self.coord[1] - 1] == '-' or board[self.coord[0] + 1][self.coord[1] - 1].color == 'b':
                    possMoves.append((self.coord[0] + 1, self.coord[1] - 1))

            elif self.color == 'b':
                if board[self.coord[0] + 1][self.coord[1] - 1] == '-' or board[self.coord[0] + 1][self.coord[1] - 1].color == 'w':
                    possMoves.append((self.coord[0] + 1, self.coord[1] - 1))
            
        # Baixo Direita
        if self.coord[0] < 7 and self.coord[1] < 7:
            if self.color == 'w':
                if board[self.coord[0] + 1][self.coord[1] + 1] == '-' or board[self.coord[0] + 1][self.coord[1] + 1].color == 'b':
                    possMoves.append((self.coord[0] + 1, self.coord[1] + 1))

            elif self.color == 'b':
                if board[self.coord[0] + 1][self.coord[1] + 1] == '-' or board[self.coord[0] + 1][self.coord[1] + 1].color == 'w':
                    possMoves.append((self.coord[0] + 1, self.coord[1] + 1))
            
        return possMoves
    
##
##
##

class Queen(Piece):

    bimg = pygame.image.load('Chess/Imgs/QueenB.png')
    wimg = pygame.image.load('Chess/Imgs/QueenW.png')

    def __init__(self, color, coord) -> None:
        super().__init__(color, coord)
        self.img = self.bimg if self.color == 'b' else self.wimg
        self.img = pygame.transform.smoothscale(self.img, (145, 145))
        self.rect = self.img.get_rect(topleft = (self.coord[1] * 150, self.coord[0] * 150))

    def possibleMoves(self, board):
        possMoves = list()

        # Esquerda
        if self.coord[1] > 0:
            for square in range(1, 8):
                place = board[self.coord[0]][self.coord[1] - square]
                if place == '-':
                    possMoves.append((self.coord[0], self.coord[1] - square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0], self.coord[1] - square))
                        break
                    elif place.color == 'w' or self.coord[1] - square == 0:
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0], self.coord[1] - square))
                        break
                    elif place.color == 'b' or self.coord[1] - square == 0:
                        break

        # Direita
        if self.coord[1] < 7:
            for square in range(1, 8):
                place = board[self.coord[0]][self.coord[1] + square]
                if place == '-':
                    possMoves.append((self.coord[0], self.coord[1] + square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0], self.coord[1] + square))
                        break
                    elif place.color == 'w' or self.coord[1] + square == 7:
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0], self.coord[1] + square))
                        break
                    elif place.color == 'b' or self.coord[1] + square == 7:
                        break
                
                if self.coord[1] + square == 7:
                    break

        # Cima
        if self.coord[0] > 0:
            for square in range(1, 8):
                place = board[self.coord[0] - square][self.coord[1]]
                if place == '-':
                    possMoves.append((self.coord[0] - square, self.coord[1]))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0] - square, self.coord[1]))
                        break
                    elif place.color == 'w' or self.coord[0] - square == 0:
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0] - square, self.coord[1]))
                        break
                    elif place.color == 'b' or self.coord[0] - square == 0:
                        break

        # Baixo
        if self.coord[0] < 7:
            for square in range(1, 8):
                if self.coord[0] + square <= 7:
                    place = board[self.coord[0] + square][self.coord[1]]
                    if place == '-':
                        possMoves.append((self.coord[0] + square, self.coord[1]))
                    elif self.color == 'w':
                        if place.color == 'b':
                            possMoves.append((self.coord[0] + square, self.coord[1]))
                            break
                        elif place.color == 'w' or self.coord[0] + square == 7:
                            break
                    elif self.color == 'b':
                        if place.color == 'w':
                            possMoves.append((self.coord[0] + square, self.coord[1]))
                            break
                        elif place.color == 'b' or self.coord[0] + square == 7:
                            break

        #Diagonal direita cima
        if self.coord[1] < 7 and self.coord[0] > 0:
            for square in range(1, 8):
                place = board[self.coord[0] - square][self.coord[1] + square]
                if place == '-':
                    possMoves.append((self.coord[0] - square, self.coord[1] + square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0] - square, self.coord[1] + square))
                        break
                    elif place.color == 'w':
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0] - square, self.coord[1] + square))
                        break
                    elif place.color == 'b':
                        break

                if self.coord[1] + square == 7 or self.coord[0] - square == 0:
                    break


        #Diagonal direita baixo
        if self.coord[1] < 7 and self.coord[0] < 7:
            for square in range(1, 8):
                place = board[self.coord[0] + square][self.coord[1] + square]
                if place == '-':
                    possMoves.append((self.coord[0] + square, self.coord[1] + square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0] + square, self.coord[1] + square))
                        break
                    elif place.color == 'w':
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0] + square, self.coord[1] + square))
                        break
                    elif place.color == 'b':
                        break

                if self.coord[1] + square == 7 or self.coord[0] + square == 7:
                    break

        
        #Diagonal esquerda baixo
        if self.coord[1] > 0 and self.coord[0] < 7:
            for square in range(1, 8):
                place = board[self.coord[0] + square][self.coord[1] - square]
                if place == '-':
                    possMoves.append((self.coord[0] + square, self.coord[1] - square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0] + square, self.coord[1] - square))
                        break
                    elif place.color == 'w':
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0] + square, self.coord[1] - square))
                        break
                    elif place.color == 'b':
                        break

                if self.coord[1] - square == 0 or self.coord[0] + square == 7:
                    break

        
        #Diagonal esquerda cima
        if self.coord[1] > 0 and self.coord[0] > 0:
            for square in range(1, 8):
                place = board[self.coord[0] - square][self.coord[1] - square]
                if place == '-':
                    possMoves.append((self.coord[0] - square, self.coord[1] - square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0] - square, self.coord[1] - square))
                        break
                    elif place.color == 'w':
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0] - square, self.coord[1] - square))
                        break
                    elif place.color == 'b':
                        break

                if self.coord[1] - square == 0 or self.coord[0] - square == 0:
                    break

        return possMoves

##
##
##

class Knight(Piece):
    bimg = pygame.image.load('Chess/Imgs/KnightB.png')
    wimg = pygame.image.load('Chess/Imgs/KnightW.png')

    def __init__(self, color, coord) -> None:
        super().__init__(color, coord)
        self.img = self.bimg if self.color == 'b' else self.wimg
        self.img = pygame.transform.smoothscale(self.img, (145, 145))
        self.rect = self.img.get_rect(topleft = (self.coord[1] * 150, self.coord[0] * 150))

    def possibleMoves(self, board):
        possMoves = list()

        #  Esquerda Cima
        if self.coord[0] > 0 and self.coord[1] > 1:
            if board[self.coord[0] - 1][self.coord[1] - 2] == '-':
                possMoves.append((self.coord[0] - 1, self.coord[1] - 2))
                
            elif self.color == 'w' and board[self.coord[0] - 1][self.coord[1] - 2].color == 'b':
                possMoves.append((self.coord[0] - 1, self.coord[1] - 2))  

            elif self.color == 'b' and board[self.coord[0] - 1][self.coord[1] - 2].color == 'w':
                possMoves.append((self.coord[0] - 1, self.coord[1] - 2))

        #  Esquerda Baixo
        if self.coord[0] < 7 and self.coord[1] > 0:
            if board[self.coord[0] + 1][self.coord[1] - 2] == '-':
                possMoves.append((self.coord[0] + 1, self.coord[1] - 2))

            if board[self.coord[0] + 1][self.coord[1] - 2] != '-':
                if self.color == 'w' and board[self.coord[0] + 1][self.coord[1] - 2].color == 'b':
                    possMoves.append((self.coord[0] + 1, self.coord[1] - 2))  

            if board[self.coord[0] + 1][self.coord[1] - 2] != '-':
                if self.color == 'b' and board[self.coord[0] + 1][self.coord[1] - 2].color == 'w':
                    possMoves.append((self.coord[0] + 1, self.coord[1] - 2))

        
        #  Cima Esquerda
        if self.coord[0] > 1 and self.coord[1] > 0:
            if board[self.coord[0] - 2][self.coord[1] - 1] == '-':
                possMoves.append((self.coord[0] - 2, self.coord[1] - 1))
                
            elif self.color == 'w' and board[self.coord[0] - 2][self.coord[1] - 1].color == 'b':
                possMoves.append((self.coord[0] - 2, self.coord[1] - 1))  

            elif self.color == 'b' and board[self.coord[0] - 2][self.coord[1] - 1].color == 'w':
                possMoves.append((self.coord[0] - 2, self.coord[1] - 1))

        #  Cima Direita
        if self.coord[0] > 1 and self.coord[1] < 7:
            if board[self.coord[0] - 2][self.coord[1] + 1] == '-':
                possMoves.append((self.coord[0] - 2, self.coord[1] + 1))
                
            elif self.color == 'w' and board[self.coord[0] - 2][self.coord[1] + 1].color == 'b':
                possMoves.append((self.coord[0] - 2, self.coord[1] + 1))  

            elif self.color == 'b' and board[self.coord[0] - 2][self.coord[1] + 1].color == 'w':
                possMoves.append((self.coord[0] - 2, self.coord[1] + 1))


        #  Direita Cima
        if self.coord[0] > 0 and self.coord[1] < 6:
            if board[self.coord[0] - 1][self.coord[1] + 2] == '-':
                possMoves.append((self.coord[0] - 1, self.coord[1] + 2))
                
            elif self.color == 'w' and board[self.coord[0] - 1][self.coord[1] + 2].color == 'b':
                possMoves.append((self.coord[0] - 1, self.coord[1] + 2))  

            elif self.color == 'b' and board[self.coord[0] - 1][self.coord[1] + 2].color == 'w':
                possMoves.append((self.coord[0] - 1, self.coord[1] + 2))


        #  Direita Baixo
        if self.coord[0] < 7 and self.coord[1] < 6:
            if board[self.coord[0] + 1][self.coord[1] + 2] == '-':
                possMoves.append((self.coord[0] + 1, self.coord[1] + 2))
                
            elif self.color == 'w' and board[self.coord[0] + 1][self.coord[1] + 2].color == 'b':
                possMoves.append((self.coord[0] + 1, self.coord[1] + 2))  

            elif self.color == 'b' and board[self.coord[0] + 1][self.coord[1] + 2].color == 'w':
                possMoves.append((self.coord[0] + 1, self.coord[1] + 2))


        #  Baixo Esquerda
        if self.coord[0] < 6 and self.coord[1] > 0:
            if board[self.coord[0] + 2][self.coord[1] - 1] == '-':
                possMoves.append((self.coord[0] + 2, self.coord[1] - 1))
                
            elif self.color == 'w' and board[self.coord[0] + 2][self.coord[1] - 1].color == 'b':
                possMoves.append((self.coord[0] + 2, self.coord[1] - 1))  

            elif self.color == 'b' and board[self.coord[0] + 2][self.coord[1] - 1].color == 'w':
                possMoves.append((self.coord[0] + 2, self.coord[1] - 1))


        #  Baixo Direita
        if self.coord[0] < 6 and self.coord[1] < 7:
            if board[self.coord[0] + 2][self.coord[1] + 1] == '-':
                possMoves.append((self.coord[0] + 2, self.coord[1] + 1))
                
            elif self.color == 'w' and board[self.coord[0] + 2][self.coord[1] + 1].color == 'b':
                possMoves.append((self.coord[0] + 2, self.coord[1] + 1))  

            elif self.color == 'b' and board[self.coord[0] + 2][self.coord[1] + 1].color == 'w':
                possMoves.append((self.coord[0] + 2, self.coord[1] + 1))


        return possMoves
    
##
##
##

class Bishop(Piece):
    bimg = pygame.image.load('Chess/Imgs/BishopB.png')
    wimg = pygame.image.load('Chess/Imgs/BishopW.png')

    def __init__(self, color, coord) -> None:
        super().__init__(color, coord)
        self.img = self.bimg if self.color == 'b' else self.wimg
        self.img = pygame.transform.smoothscale(self.img, (145, 145))
        self.rect = self.img.get_rect(topleft = (self.coord[1] * 150, self.coord[0] * 150))

    def possibleMoves(self, board):
        possMoves = list()

        #Diagonal direita cima
        if self.coord[1] < 7 and self.coord[0] > 0:
            for square in range(1, 8):
                place = board[self.coord[0] - square][self.coord[1] + square]
                if place == '-':
                    possMoves.append((self.coord[0] - square, self.coord[1] + square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0] - square, self.coord[1] + square))
                        break
                    elif place.color == 'w':
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0] - square, self.coord[1] + square))
                        break
                    elif place.color == 'b':
                        break

                if self.coord[1] + square == 7 or self.coord[0] - square == 0:
                    break


        #Diagonal direita baixo
        if self.coord[1] < 7 and self.coord[0] < 7:
            for square in range(1, 8):
                place = board[self.coord[0] + square][self.coord[1] + square]
                if place == '-':
                    possMoves.append((self.coord[0] + square, self.coord[1] + square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0] + square, self.coord[1] + square))
                        break
                    elif place.color == 'w':
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0] + square, self.coord[1] + square))
                        break
                    elif place.color == 'b':
                        break

                if self.coord[1] + square == 7 or self.coord[0] + square == 7:
                    break

        
        #Diagonal esquerda baixo
        if self.coord[1] > 0 and self.coord[0] < 7:
            for square in range(1, 8):
                place = board[self.coord[0] + square][self.coord[1] - square]
                if place == '-':
                    possMoves.append((self.coord[0] + square, self.coord[1] - square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0] + square, self.coord[1] - square))
                        break
                    elif place.color == 'w':
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0] + square, self.coord[1] - square))
                        break
                    elif place.color == 'b':
                        break

                if self.coord[1] - square == 0 or self.coord[0] + square == 7:
                    break

        
        #Diagonal esquerda cima
        if self.coord[1] > 0 and self.coord[0] > 0:
            for square in range(1, 8):
                place = board[self.coord[0] - square][self.coord[1] - square]
                if place == '-':
                    possMoves.append((self.coord[0] - square, self.coord[1] - square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0] - square, self.coord[1] - square))
                        break
                    elif place.color == 'w':
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0] - square, self.coord[1] - square))
                        break
                    elif place.color == 'b':
                        break

                if self.coord[1] - square == 0 or self.coord[0] - square == 0:
                    break


        return possMoves
    
##
##
##

class Pawn(Piece):
    ftmove = True
    bimg = pygame.image.load('Chess/Imgs/PawnB.png')
    wimg = pygame.image.load('Chess/Imgs/PawnW.png')

    def __init__(self, color, coord) -> None:
        super().__init__(color, coord)
        self.img = self.bimg if self.color == 'b' else self.wimg
        self.img = pygame.transform.smoothscale(self.img, (145, 145))
        self.rect = self.img.get_rect(topleft = (self.coord[1] * 150, self.coord[0] * 150))

    def possibleMoves(self, board):
        possMoves = list()

        # Branco
        if self.color == 'w':

            # 1 Casa a frente
            if self.coord[0] - 1 >= 0:
                if board[self.coord[0] - 1][self.coord[1]] == '-':
                    possMoves.append((self.coord[0] - 1, self.coord[1]))

                    # 2 Casa a frente
                    if possMoves and self.ftmove:
                        if board[self.coord[0] - 2][self.coord[1]] == '-':
                            possMoves.append((self.coord[0] - 2, self.coord[1]))

            # Diagonais:
            if self.coord[1] > 0 and self.coord[0] > 0:
                if board[self.coord[0] - 1][self.coord[1] - 1] != '-':
                    if board[self.coord[0] - 1][self.coord[1] - 1].color == 'b':
                        possMoves.append((self.coord[0] - 1, self.coord[1] - 1))

            if self.coord[1] < 7 and self.coord[0] > 0:
                if board[self.coord[0] - 1][self.coord[1] + 1] != '-':
                    if board[self.coord[0] - 1][self.coord[1] + 1].color == 'b':
                        possMoves.append((self.coord[0] - 1, self.coord[1] + 1))
        # Preto
        elif self.color == 'b':

            # 1 Casa a frente
            if self.coord[0] + 1 <= 7:
                if board[self.coord[0] + 1][self.coord[1]] == '-':
                    possMoves.append((self.coord[0] + 1, self.coord[1]))

                    # 2 Casa a frente
                    if possMoves and self.ftmove:
                        if board[self.coord[0] + 2][self.coord[1]] == '-':
                            possMoves.append((self.coord[0] + 2, self.coord[1]))

            # Diagonais:
            if self.coord[1] > 0 and self.coord[0] < 7:
                if board[self.coord[0] + 1][self.coord[1] - 1] != '-':
                    if board[self.coord[0] + 1][self.coord[1] - 1].color == 'w':
                        possMoves.append((self.coord[0] + 1, self.coord[1] - 1))

            if self.coord[1] < 7 and self.coord[0] < 7:
                if board[self.coord[0] + 1][self.coord[1] + 1] != '-':
                    if board[self.coord[0] + 1][self.coord[1] + 1].color == 'w':
                        possMoves.append((self.coord[0] + 1, self.coord[1] + 1))

        return possMoves 

##
##
##

class Rook(Piece):
    bimg = pygame.image.load('Chess/Imgs/RookB.png')
    wimg = pygame.image.load('Chess/Imgs/RookW.png')

    def __init__(self, color, coord) -> None:
        super().__init__(color, coord)
        self.img = self.bimg if self.color == 'b' else self.wimg
        self.img = pygame.transform.smoothscale(self.img, (145, 145))
        self.rect = self.img.get_rect(topleft = (self.coord[1] * 150, self.coord[0] * 150))

    def possibleMoves(self, board):
        possMoves = list()

        # Esquerda
        if self.coord[1] > 0:
            for square in range(1, 8):
                place = board[self.coord[0]][self.coord[1] - square]
                if place == '-':
                    possMoves.append((self.coord[0], self.coord[1] - square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0], self.coord[1] - square))
                        break
                    elif place.color == 'w' or self.coord[1] - square == 0:
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0], self.coord[1] - square))
                        break
                    elif place.color == 'b' or self.coord[1] - square == 0:
                        break

        # Direita
        if self.coord[1] < 7:
            for square in range(1, 8):
                place = board[self.coord[0]][self.coord[1] + square]
                if place == '-':
                    possMoves.append((self.coord[0], self.coord[1] + square))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0], self.coord[1] + square))
                        break
                    elif place.color == 'w' or self.coord[1] + square == 7:
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0], self.coord[1] + square))
                        break
                    elif place.color == 'b' or self.coord[1] + square == 7:
                        break
                
                if self.coord[1] + square == 7:
                    break

        # Cima
        if self.coord[0] > 0:
            for square in range(1, 8):
                place = board[self.coord[0] - square][self.coord[1]]
                if place == '-':
                    possMoves.append((self.coord[0] - square, self.coord[1]))
                elif self.color == 'w':
                    if place.color == 'b':
                        possMoves.append((self.coord[0] - square, self.coord[1]))
                        break
                    elif place.color == 'w' or self.coord[0] - square == 0:
                        break
                elif self.color == 'b':
                    if place.color == 'w':
                        possMoves.append((self.coord[0] - square, self.coord[1]))
                        break
                    elif place.color == 'b' or self.coord[0] - square == 0:
                        break

        # Baixo
        if self.coord[0] < 7:
            for square in range(1, 8):
                if self.coord[0] + square <= 7:
                    place = board[self.coord[0] + square][self.coord[1]]
                    if place == '-':
                        possMoves.append((self.coord[0] + square, self.coord[1]))
                    elif self.color == 'w':
                        if place.color == 'b':
                            possMoves.append((self.coord[0] + square, self.coord[1]))
                            break
                        elif place.color == 'w' or self.coord[0] + square == 7:
                            break
                    elif self.color == 'b':
                        if place.color == 'w':
                            possMoves.append((self.coord[0] + square, self.coord[1]))
                            break
                        elif place.color == 'b' or self.coord[0] + square == 7:
                            break

        return possMoves
