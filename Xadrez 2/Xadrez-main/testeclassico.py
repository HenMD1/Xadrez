import pygame


sc = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()



surf = pygame.surface.Surface((50, 50))
surf.fill((0, 200, 0, 50))
surf.set_alpha(100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    sc.fill('white')
    sc.blit(surf, (10, 10))


    pygame.display.update()
    clock.tick(30)