import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class Cactus(Obstacle):
    CACTUS = [LARGE_CACTUS, SMALL_CACTUS]
    def __init__(self):
        random_cactus = random.randint(0, 1)
        random_img = random.randint(0, 2)
        if self.CACTUS[random_cactus] == self.CACTUS[0]:
            super().__init__(LARGE_CACTUS[random_img], pos_y = 300)
        else:

            super().__init__(SMALL_CACTUS[random_img], pos_y = 330)
        