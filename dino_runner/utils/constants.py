import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

START = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoStart.png'))
ICON_DEAD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))
GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

MUTED = pygame.image.load(os.path.join(IMG_DIR, 'Other/mute.png'))
MAX = pygame.image.load(os.path.join(IMG_DIR, 'Other/max.png'))
DOWN = pygame.image.load(os.path.join(IMG_DIR, 'Other/down.png'))
UP = pygame.image.load(os.path.join(IMG_DIR, 'Other/up.png'))

MUTED = pygame.transform.scale(MUTED, (100, 100))
MAX = pygame.transform.scale(MAX, (100, 100))
DOWN = pygame.transform.scale(DOWN, (100, 100))
UP = pygame.transform.scale(UP, (100, 100))

DEAD = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDead.png'))
ICON_MOV = pygame.image.load(os.path.join(IMG_DIR, 'Other/InstruccionMover.png'))
ICON_MOV = pygame.transform.scale(ICON_MOV, (310, 200))
ICON_VOLUM1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/InstruccionVolumen1.png'))
ICON_VOLUM1 = pygame.transform.scale(ICON_VOLUM1, (310, 200))
ICON_VOLUM2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/InstruccionVolumen2.png'))
ICON_VOLUM2 = pygame.transform.scale(ICON_VOLUM2, (310, 200))
FIREBALL = pygame.image.load(os.path.join(IMG_DIR, 'Other/FireBola.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
