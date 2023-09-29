import pygame
from pygame.locals import *
import random


pygame.init()

width, height = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Игра")
screen.fill((255, 255, 255))
SCORE = 0

player = pygame.Surface((50, 50))
player.fill((0, 0, 0))
position = [300, 200]

foods:list[pygame.Surface] = [
    pygame.Surface((50, 50)),
    pygame.Surface((50, 50)),
]
foods_positions:list[list[int]] = [
    [50, 50],
    [200, 100]
]
for food in foods:
    food.fill((200, 0, 100))


done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_w:
                position[1] -= 50
            if event.key == K_a:
                position[0] -= 50
            if event.key == K_s:
                position[1] += 50
            if event.key == K_d:
                position[0] += 50
    
    for index, food in enumerate(foods):
        if position[0] == foods_positions[index][0] and position[1] == foods_positions[index][1]:
            foods_positions[index] = [random.randint(0, 15) * 50, random.randint(0, 11) * 50]
            SCORE += 1
                
    screen.fill((255, 255, 255))
    
    for index, food in enumerate(foods):
        screen.blit(food, foods_positions[index])
        
    screen.blit(player, position)
    
    
    pygame.display.flip()

pygame.quit()
print(f"Ваш счет составил: {SCORE}")