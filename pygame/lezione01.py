import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test Pygame")

clock = pygame.time.Clock()

x, y = 320, 240
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if x < 0:
        x = 0   
    if x > 640:
        x = 640
    if y < 0:
        y = 0
    if y > 480:
        y = 480
    #in una lista metti i colori rosso blu e verde e ogni volta che premi spazio scrola la lista cambiando colore del cerchio e deve rimanere di quel colore finché non premi di nuovo spazio
    colors = [(255, 0,0), (0, 255, 0), (0, 0, 255)]
    color_i = 0
    click = False
    if keys[pygame.K_SPACE]:
        color_i += 1
     
        if color_i >= len(colors):
            color_i = 0
    pygame.K_SPACE
            
    
    screen.fill((30, 30, 50))
    pygame.draw.circle(screen, colors[color_i], (x, y), 30)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()