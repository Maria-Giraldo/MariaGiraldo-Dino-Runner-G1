import random
from pygame.sprite import Sprite
from pygame import Surface
from dino_runner.utils.constants import METEORITO_TAM1, METEORITO_TAM2, METEORITO_TAM3, SCREEN_HEIGHT, SCREEN_WIDTH


class Meteorito(Sprite):
    def __init__(self):
        self.image_aleatoria = random.randint(0, 2)
        if self.image_aleatoria == 0:
            self.image = METEORITO_TAM1
        elif self.image_aleatoria == 1:
            self.image = METEORITO_TAM2
        else:
            self.image = METEORITO_TAM3

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = -self.rect.width
        self.velocidad = random.randint(5, 10)

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH)
            self.rect.y = -self.rect.width
            self.velocidad = random.randint(5, 10)


    def draw(self, screen: Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))