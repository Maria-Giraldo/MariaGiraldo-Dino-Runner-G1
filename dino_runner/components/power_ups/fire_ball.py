import pygame
from dino_runner.utils.constants import FIREBALL

class FireBall:
    def __init__(self):
        self.image = FIREBALL
        self.width = self.image.get_width()
        self.rect = self.image.get_rect()
        self.rect.x = 180
        self.rect.y = 330

    def update(self, game_speed, user_input):
        if user_input[pygame.K_d]:
            self.rect.x += game_speed
        elif user_input[pygame.K_w]:
            self.rect.y -= game_speed
        elif user_input[pygame.K_s]: 
            self.rect.y += game_speed
        elif user_input[pygame.K_a]:
            self.rect.x -= game_speed

        if self.rect.x > 990 and self.rect.x < 50:
            self.rect.x = 100
        if self.rect.y > 350 and self.rect.x < 50:
            self.rect.y = 330

    def draw(self, screen):
        screen.blit(self.image, (self.rect))