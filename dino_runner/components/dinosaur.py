import pygame 
from pygame import surface
from pygame.sprite import Sprite


from dino_runner.utils.constants import  DEFAULT_TYPE, DUCKING_HAMMER, DUCKING_SHIELD, DUCKING_WEAPON, FIRE_TYPE, HAMMER_TYPE, HEART, HEART_TYPE, JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, JUMPING_WEAPON, RUNNING, DUCKING, RUNNING_HAMMER, RUNNING_SHIELD, RUNNING_WEAPON, SHIELD_TYPE, WEAPON_TYPE

DINO_JUMPING = "JUMPING"
DINO_RUNNING = "RUNNING"
DINO_DUCKING = "DUCKING"

IMG_DUCKING = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, HEART_TYPE: DUCKING, WEAPON_TYPE: DUCKING_WEAPON, FIRE_TYPE: DUCKING}
IMG_JUMPING = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, HEART_TYPE: JUMPING, WEAPON_TYPE: JUMPING_WEAPON, FIRE_TYPE: JUMPING}
IMG_RUNNING = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, HEART_TYPE: RUNNING, WEAPON_TYPE: RUNNING_WEAPON, FIRE_TYPE: RUNNING}

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    POS_Y_DUCK = 340
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.update_image(IMG_RUNNING[self.type][0])
        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.power_up_time_up = 0
        self.sound_jump = pygame.mixer.Sound("dino_runner/assets/sounds/SoundJump.wav")
        self.sound_jump_shield = pygame.mixer.Sound("dino_runner/assets/sounds/SoundJumpShield.wav")
  
    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()

        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:       
                if self.type == SHIELD_TYPE:
                    self.sound_jump_shield.play()
                else:
                    self.sound_jump.play()

                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING

        if self.step >= 10:
            self.step = 0

    def run(self ):
        self.update_image(IMG_RUNNING[self.type][self.step // 5])
        self.step += 1

    def jump(self):
        pos_y = self.rect.y - self.jump_velocity * 4
        self.update_image(IMG_JUMPING[self.type], pos_y=pos_y)
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.action = DINO_RUNNING
            self.rect.y = self.POS_Y
            self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.update_image(IMG_DUCKING[self.type][self.step //5], pos_y=self.POS_Y_DUCK)
        self.step += 1
   
    def update_image(self, image: pygame.Surface, pos_x = None, pos_y = None, on_death = False):
        self.image = image
        if not on_death:
           self.rect = image.get_rect()
           self.rect.x = pos_x or self.POS_X
           self.rect.y = pos_y or self.POS_Y

    def draw(self, screen: surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.type == HEART_TYPE:
            screen.blit(HEART, (1000, 100))
             
    def on_pick_power_up(self, power_up):
        self.type = power_up.type
        self.power_up_time_up = power_up.start_time + power_up.duration * 1000

    def draw_power_up(self, menu):
        if self.type != DEFAULT_TYPE:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                if self.type == HEART_TYPE:
                    menu(f"You have infinite life for {time_to_show} seconds" , 450, 50, (0, 0, 0))
                
                else: 
                    menu(f"{self.type.capitalize()} enabled for {time_to_show} seconds", 450, 50, (0, 0, 0))

            else:
                self.type = DEFAULT_TYPE
                self.power_up_time_up = 0






