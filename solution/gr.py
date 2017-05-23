import pygame


pygame.init()
screen = pygame.display.set_mode((600, 600))

board_image = pygame.image.load('graphics//board.png')
board_image = pygame.transform.scale(board_image, (600, 600))
clock = pygame.time.Clock()


running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.fill((200, 200, 200))
    screen.blit(board_image, (0, 0))
    pygame.display.flip()
