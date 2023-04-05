import pygame
from pygame.sprite import Sprite

class Score(Sprite):
    def __init__(self):
        self.score = 0

    def update(self, game):
        self.score +=1
        if self.score % 100 == 0:
            game.game_speed += 2

    
    def draw(self, position_menu):
        position_menu(f"Score: {self.score}", 1000, 50, (0, 0, 0))


    def reset(self, ):
        self.score = 0


