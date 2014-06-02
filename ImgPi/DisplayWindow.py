import pygame

pygame.init()

'''
use the following code to g et current screen resolution and set the mygame wiondow to that size
vidInfo = pygame.display.Info()
print(type(vidInfo))
WIDTH = vidInfo.current_w
HEIGHT = vidInfo.current_h
'''

screen = pygame.display.set_mode((640,400))
running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    screen.fill((0,0,0))
    pygame.display.flip()

for x in range(0,10):
    print(x)

