import pygame , random
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(300, 600)
        self.y = random.randint(50, 300)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self, game):
        self.x -= game.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(700, 1000)
            self.y = random.randint(50, 300)

    def draw(self, screen):

        screen.blit(self.image, (self.x, self.y))