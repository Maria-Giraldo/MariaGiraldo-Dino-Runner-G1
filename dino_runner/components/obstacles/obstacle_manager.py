import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle


class ObstacleManager:
    OBSTACLES = [Bird(), Cactus()]
    def __init__(self):
        self.obstacles: list[Obstacle] = []
        

    def update(self, game):
        if not self.obstacles: 
            obstacle_type = random.randint(0, 1)
            if self.OBSTACLES[obstacle_type] == self.OBSTACLES[0]:
                self.obstacles.append(Bird())
            else:
                self.obstacles.append(Cactus())
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                game.playing = False


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)