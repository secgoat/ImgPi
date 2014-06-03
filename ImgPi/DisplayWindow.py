import os
import pygame
import ImgPiTimer


pygame.init()

'''
use the following code to g et current screen resolution and set the mygame wiondow to that size
vidInfo = pygame.display.Info()
print(type(vidInfo))
WIDTH = vidInfo.current_w
HEIGHT = vidInfo.current_h
'''

#time = pygame.time.Clock()
timer = ImgPiTimer.ImgPiTimer()
screen = pygame.display.set_mode((640,400))
running = True

font  = pygame.font.Font('./font/Alpaca54.ttf', 20)
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
imgs = []  # ctreate a blank list, we will store the pygame image renders in here to display later
for img in images:
    pyImg = pygame.image.load(os.path.join('images', img))
    imgs.append(pyImg)

screen.fill((0,0,0))
imgCounter = 0

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False



    #timer.updateTimes()
    elapsedTime = timer.checkAmountTime()
    delayTime = timer.convertSecToMs(5)
    print(str(timer.currentTime))
    timeBlit = font.render("Current Time: " + str(timer.currentTime / 1000) + " Seconds",1,(255,255,255))
    pastBlit = font.render("past Time: " + str(timer.previousTime / 1000),1,(255,255,255))


    if imgCounter > 4:
        imgCounter = 0

    if elapsedTime > delayTime:
        timer.previousTime = timer.currentTime
        screen.fill((0,0,0))
        pyImgRect = imgs[imgCounter].get_rect()
        screen.blit(imgs[imgCounter], pyImgRect)
        screen.blit(timeBlit, (0,0))
        screen.blit(pastBlit, (400,0))
        imgCounter += 1
    #time = pygame.time.get_ticks()




    pygame.display.flip()
    #timer.clock.tick(50)

'''  for img in images:
        pyImg = pygame.image.load(os.path.join('images', img))
        pyImgRect = pyImg.get_rect()
        screen.blit(pyImg, pyImgRect)
        pygame.display.flip()
'''

