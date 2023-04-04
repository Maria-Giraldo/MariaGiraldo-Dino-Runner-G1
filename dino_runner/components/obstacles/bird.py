import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        self.step = 0
        super().__init__(BIRD[0], pos_y = random.randint(200, 300))
        

    def draw(self, screen):
        if self.step >= 9:  
            self.step = 0
        screen.blit(BIRD[self.step // 5], self.rect)
        self.step += 1

    
