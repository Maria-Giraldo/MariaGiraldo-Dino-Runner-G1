import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.score import Score

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, START, TITLE, FPS, DOWN, UP, MAX, MUTED
from dino_runner.components.cloud import Cloud
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.cloud = Cloud()
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        pygame.mixer.music.load("dino_runner/assets/sounds/SoundMain.wav")
        pygame.mixer.music.play(-1)
        self.running = False
        self.score = Score()
        self.death_count = 0


    def run(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def play(self):
        self.playing = True
        self.score.reset()
        self.obstacle_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.cloud.update(self)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)

    def draw(self):
        user_input = pygame.key.get_pressed()
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.cloud.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.volume(user_input)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def volume(self, user_input):
        #bajar volumen
        if user_input[pygame.K_s] and pygame.mixer.music.get_volume() > 0.0:
            pygame.mixer.music.set_volume( pygame.mixer.music.get_volume() - 0.01)
            self.screen.blit(DOWN, (10, 25))
        elif user_input[pygame.K_s] and pygame.mixer.music.get_volume() == 0.0:
            self.screen.blit(MUTED, (10, 25))

        #subir volumen
        if user_input[pygame.K_w] and pygame.mixer.music.get_volume() < 1.0:
            pygame.mixer.music.set_volume( pygame.mixer.music.get_volume() + 0.01)
            self.screen.blit(UP, (10, 25))
        elif user_input[pygame.K_w] and pygame.mixer.music.get_volume() == 1.0:
            self.screen.blit(MAX, (10, 25))


        #Desactivar sonido
        if user_input[pygame.K_d]:
            pygame.mixer.music.set_volume(0.0)
            self.screen.blit(MUTED, (10, 25))
        #activar sonido
        if user_input[pygame.K_a]:
            pygame.mixer.music.set_volume(1.0)
            self.screen.blit(MAX, (10, 25))

    def on_death(self):
        pygame.mixer.music.load("dino_runner/assets/sounds/SoundDeath.wav")
        pygame.mixer.music.play()
        pygame.time.delay(3000)
        self.playing = False
        self.death_count += 1
        print("i'm death")
        

    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.screen.fill((255, 255, 255))
        if self.death_count:
            pass
        else: 
            font = pygame.font.Font("freesansbold.ttf", 30)
            text = font.render("Press any key to start", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
            self.screen.blit(START, (half_screen_width - 45, half_screen_height - 140))
        pygame.display.flip()
        self.menu_events()

    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()
        


        
        
