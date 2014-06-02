import os
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

dirs = os.getcwd()


images = os.listdir('./images/')
#pyImages = [5]
#pyImageRect = 0
#count = 0
#for i in images:
#    pyImages[count] = pygame.image.load("./images/{}".format(i))
#    pyImageRect = pyImages[count].get_rect()
#    count += 1
#    print(i)

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    screen.fill((0,0,0))
    for img in images:
        pyImg = pygame.image.load(os.path.join('images', img))
        pyImgRect = pyImg.get_rect()
        screen.blit(pyImg, pyImgRect)
        pygame.display.flip()

for x in range(0,10):
    print(x)

