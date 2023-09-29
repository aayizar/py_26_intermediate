import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = [0, 0, 0]

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('First game')

screen.fill(WHITE)

pygame.draw.line(screen, BLACK, (150, 80), (550, 120), 5)

pygame.draw.rect(screen, RED, (300, 300, 200, 50))

pygame.draw.circle(screen, BLACK, (500, 450), 50)

word = ''

working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('W button clicked!')
                word += 'w'
            if event.key == pygame.K_BACKSPACE:
                word = word[:-1]
            if event.key == pygame.K_s:
                print('S button clicked!')
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Left button clicked")

    if RED[0] < 255:
        RED[0] = RED[0] + 1
        
    pygame.draw.rect(screen, tuple(RED), (300, 300, 200, 50))
    print(word)
    
    pygame.display.update()


pygame.quit()