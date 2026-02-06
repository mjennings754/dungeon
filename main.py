import pygame
import os
pygame.init()

clock = pygame.time.Clock()

FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_bg():
    screen.fill("#093C27B5")
    pygame.draw.line(screen, WHITE, (0, 300), (SCREEN_WIDTH, 300))



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        

        animation_types = ['idle']
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(f'images/player/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'images/player/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height()) * scale))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = img.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.scale = scale
        self.speed = speed
        self.vel_y = 0
        self.flip = False
        self.in_air = True

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0


player = Player(200, 200, 3, 5)
running = True
while running:
    clock.tick(FPS)
    draw_bg()
    player.draw()
    player.update_animation()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()