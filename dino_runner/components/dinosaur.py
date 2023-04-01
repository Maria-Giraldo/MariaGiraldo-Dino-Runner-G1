import pygame 
from pygame import surface
from pygame.sprite import Sprite
from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING

DINO_JUMPING = "JUMPING"
DINO_RUNNING = "RUNNING"
DINO_DUCKING = "DUCKING"

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    POS_Y_DUCK = 340
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY

    def pos(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        if self.action == DINO_RUNNING:
            self.rect.y = self.POS_Y 
        else: 
            self.rect.y = self.POS_Y_DUCK
        

    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()

        if self.action != DINO_JUMPING and self.action != DUCKING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING
        if self.step >= 10:
            self.step = 0

    def run(self):
        self.image = RUNNING[self.step // 5]
        self.pos()
        self.step += 1

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.action = DINO_RUNNING
            self.rect.y = self.POS_Y
            self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.image = DUCKING[self.step // 5]
        self.pos()
        self.step += 1
        
    def draw(self, screen: surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))