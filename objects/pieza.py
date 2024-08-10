import pygame

class Pieza(pygame.sprite.Sprite):
    def __init__(self, *groups, shape, color, block_size, fall_speed):
        super().__init__(*groups)
        self.shape = shape
        self.color = color
        self.block_size = block_size
        self.image = pygame.Surface((block_size*len(shape[0]),block_size*len(shape)))
        self.image.fill("pink")
        self.rect = self.image.get_rect()
        self.draw_shape()
        self.fall_speed = fall_speed
        self.update_counter = 0

    def draw_shape(self):
        for y,row in enumerate(self.shape):
            for x,cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.image,
                        self.color,
                        pygame.Rect(x * self.block_size, y*self.block_size,self.block_size,self.block_size)
                    )

    def update(self):
        self.update_counter += 1
        if self.update_counter >= self.fall_speed:
            self.rect.y += self.block_size
            self.update_counter = 0