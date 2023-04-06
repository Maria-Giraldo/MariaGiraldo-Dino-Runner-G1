import pygame

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.fire_ball import FireBall
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, DEAD, DEFAULT_TYPE, FIRE_TYPE, GAMEOVER, HAMMER_TYPE, HEART_TYPE, ICON, ICON_DEAD, ICON_MOV, ICON_VOLUM1, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, START, TITLE, FPS, DOWN, UP, MAX, MUTED, WEAPON_TYPE
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
        self.running = False
        self.score = Score()
        self.death_count = 0
        self.power_up_manager = PowerUpManager()
        self.fire_ball = FireBall()
        
    def run(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def reset(self):
        self.game_speed = 20
        self.score.reset()
        self.obstacle_manager.reset()
        self.power_up_manager.reset()

    def play(self):
        self.playing = True
        pygame.mixer.music.load("dino_runner/assets/sounds/SoundMain.wav")
        pygame.mixer.music.play(-1)
        self.reset()
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
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death, user_input)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed, self.score.score, self.player)

    def draw(self):
        user_input = pygame.key.get_pressed()
        self.clock.tick(FPS)
        self.screen.fill((112, 211, 231))
        self.draw_background()
        self.cloud.draw(self.screen)
        self.player.draw(self.screen)
        self.player.draw_power_up(self.menu)
        self.obstacle_manager.draw(self.screen, self.player)
        self.score.draw(self.menu)
        self.power_up_manager.draw(self.screen)
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
        if user_input[pygame.K_e] and pygame.mixer.music.get_volume() > 0.0:
            pygame.mixer.music.set_volume( pygame.mixer.music.get_volume() - 0.01)
            self.screen.blit(DOWN, (10, 60))
        elif user_input[pygame.K_e] and pygame.mixer.music.get_volume() == 0.0:
            self.screen.blit(MUTED, (10, 60))

        #subir volumen
        if user_input[pygame.K_r] and pygame.mixer.music.get_volume() < 1.0:
            pygame.mixer.music.set_volume( pygame.mixer.music.get_volume() + 0.01)
            self.screen.blit(UP, (10, 60))
        elif user_input[pygame.K_r] and pygame.mixer.music.get_volume() == 1.0:
            self.screen.blit(MAX, (10, 60))

    def on_death(self):
        if self.player.type == HEART_TYPE:
            self.game_speed = 20
        if self.player.type != SHIELD_TYPE:
            self.player.update_image(DEAD, on_death=True)
            self.draw()
            self.playing = False
            self.death_count += 1
            pygame.mixer.music.load("dino_runner/assets/sounds/SoundDeath.wav")
            pygame.mixer.music.play()
            pygame.time.delay(3000)

    def menu(self, message, width, height, color):
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.screen.fill((255, 255, 255))
        if self.death_count:
            self.menu("Pres any key to reset", half_screen_width, half_screen_height, (83, 83, 83))
            self.menu(f'Total deaths: {self.death_count}', half_screen_width, 420, (83, 83, 83))
            self.menu(f"Score: {self.score.score}", half_screen_width, 380, (83, 83, 83))
            self.screen.blit(GAMEOVER, (half_screen_width - 200, half_screen_height - 150))
            self.screen.blit(ICON_DEAD, (half_screen_width - 45, half_screen_height - 100)) 
        else: 
            self.menu("Press any key to start", half_screen_width, half_screen_height, (0, 0, 0))
            self.screen.blit(START, (half_screen_width - 45, half_screen_height - 140))
            self.screen.blit(ICON_MOV, (half_screen_width - 600, half_screen_height + 90))
            self.screen.blit(ICON_VOLUM1, (half_screen_width + 100, half_screen_height + 90))

        pygame.display.flip()
        self.menu_events()

    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()

        
       
        
        
