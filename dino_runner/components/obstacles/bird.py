import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        self.step = 0
        super().__init__(BIRD[0], pos_y = random.randint(200, 300))
        

    def update(self, game_speed, obstacles):
        self.image = BIRD[self.step // 5]
        super().update(game_speed + 3 , obstacles)
        if self.step >= 9:  
            self.step = 0
        self.step += 1

    
