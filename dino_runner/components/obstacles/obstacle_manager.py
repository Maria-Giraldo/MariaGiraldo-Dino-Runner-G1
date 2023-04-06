import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.power_ups.fire_ball import FireBall
from dino_runner.utils.constants import  FIRE_TYPE, HAMMER_TYPE, HEART_TYPE, WEAPON_TYPE


class ObstacleManager:
    OBSTACLES = [Cactus, Bird]
    def __init__(self):
        self.obstacles: list[Obstacle] = []
        self.sound_hammer = pygame.mixer.Sound("dino_runner/assets/sounds/hammerSound.wav")
        self.sound_weapon = pygame.mixer.Sound("dino_runner/assets/sounds/WeaponSound.wav")
        self.fire_ball = FireBall()

    def update(self, game_speed, player, on_death, user_input):
        if not self.obstacles: 
            obstacle_type = random.choice(self.OBSTACLES)
            self.obstacles.append(obstacle_type())
            
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.type == WEAPON_TYPE and user_input[pygame.K_SPACE]: 
                if obstacle.rect.x <= 950:
                    self.sound_weapon.play() 
                    self.obstacles.remove(obstacle)
            if player.type == FIRE_TYPE:
                self.fire_ball.update(game_speed, user_input)
                if obstacle.rect.colliderect(self.fire_ball.rect):
                    self.obstacles.remove(obstacle)

            if obstacle.rect.colliderect(player.rect):           
                if player.type == HAMMER_TYPE and user_input[pygame.K_SPACE]:
                    self.sound_hammer.play()
                    self.obstacles.remove(obstacle)
                elif player.type == HEART_TYPE:
                    self.obstacles.remove(obstacle)
                    
                else:
                    on_death()
                
    def draw(self, screen, player):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        if player.type ==FIRE_TYPE:
            self.fire_ball.draw(screen)
            
    def reset(self):
        self.obstacles = []