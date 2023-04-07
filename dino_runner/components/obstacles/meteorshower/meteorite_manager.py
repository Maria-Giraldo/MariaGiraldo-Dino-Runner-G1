import pygame
from dino_runner.components.obstacles.meteorshower.meteorite import Meteorito


class Meteorito_Manager:
    def __init__(self):
        self.meteoritos :list[Meteorito] = []
        
    def update(self, player, on_death):
        if not self.meteoritos:
            for i in range(10):
                meteorito = Meteorito()
                self.meteoritos.append(meteorito)

        for meteorito in self.meteoritos:
            meteorito.update()
            if meteorito.rect.colliderect(player.rect):
                on_death()

    def draw(self, screen):
        for meteorito in self.meteoritos:
            meteorito.draw(screen)
    
    def reset(self):
        self.meteoritos = []
    