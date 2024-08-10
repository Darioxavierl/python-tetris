import pygame
import configs
import assets
from objects.pieza import Pieza 


pygame.init()

screen =  pygame.display.set_mode((configs.SCREEN_WIDTH,configs.SCREEN_HEIGHT))

clock = pygame.time.Clock()
pygame.display.set_caption(configs.GAME_NAME)

running = True

all_pieces = pygame.sprite.Group()
pieza = Pieza(all_pieces, shape=assets.shapes["O"],color=assets.colors["O"],block_size=configs.BLOCK_SIZE,fall_speed=60)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False
    screen.fill(color=configs.BACKGROUND_FILL)

    # Actualizar y dibujar las piezas
    all_pieces.update()
    all_pieces.draw(screen)


    pygame.display.flip()
    clock.tick(configs.FPS)


pygame.quit()
