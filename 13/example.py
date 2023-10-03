import pygame
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 10

screen.fill(WHITE)

""" font module
font = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 60)
text1 = font.render('My first text', True, BLACK)
# text2 = font.render('Second text', False, BLACK)
screen.blit(text1, (100, 100))
# screen.blit(text2, (100, 400))

# font2 = pygame.font.get_fonts()
font2 = pygame.font.SysFont('romansiv50', 30)
text2 = font2.render('Second font type', True, (100, 200, 100))
screen.blit(text2, (100, 400))
"""

image = pygame.image.load("src/snake.jpg")
# image = pygame.transform.scale(image, (512, 288))
# image = pygame.transform.scale_by(image, (0.2, 0.1))
image = pygame.transform.scale_by(image, 0.2)
# image = pygame.transform.smoothscale_by(image, 2)
# image = pygame.transform.rotate(image, 20)
# image = pygame.transform.flip(image, True, True)

screen.blit(image, (width // 2 - 256, height // 2 - 144 - 25))

FOOD_PLACE_UPDATE = USEREVENT + 1
timer = pygame.time.set_timer(FOOD_PLACE_UPDATE, 2_000)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == FOOD_PLACE_UPDATE:
            print('Food coordinates changed')
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()