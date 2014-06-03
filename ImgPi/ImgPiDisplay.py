import os
import pygame
import ImgPiTimer


class ImgPiDisplay:

    def __init__(self):
        self.timer = ImgPiTimer.ImgPiTimer()
        self.screen = None  # placeholder for the screen variable as it will be different based on windows or rPi
        self.running = True  #bool to keep track of program state, however this may need ot be moved up to imgpi.py (main)
        self.imgur_images = [] #list of images file names from the directory
        self.pygame_images = [] #list of rendered pygame images form the image files
        self.image_iterator = 0 #use this to load different images from the pygame_image list
        self.font = None  #placeholder for pygamefont
        #2 variables for displaying my times during debug
        self.timeBlit = None
        self.pastBlit = None

        #check if windows or rPi to init pygame displays
        if os.name == "nt":
            #windows / Development
            pygame.init()
            self.screen = pygame.display.set_mode((640,400))
        else:
            #rPi / live
            #https://learn.adafruit.com/pi-video-output-using-pygame/pointing-pygame-to-the-framebuffer
            pass

        self.LoadContent()


    def LoadContent(self):
        self.font = pygame.font.Font('./font/Alpaca54.ttf', 20) #load a font to use for debugging or siplay on screen
        self.imgur_images = os.listdir('./images/') #get all images in the images directory
        for img in self.imgur_images:
            #read all images in the directory and load them into pygame
            self.pygame_images.append(pygame.image.load(os.path.join('images', img)))


    def Update(self):
        self.timer.updateTime() #update current time interval
        elapsedTime = self.timer.checkAmountTime()
        delayTime = self.timer.convertSecToMs(5)

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.running = False

        self.timeBlit = self.font.render("Current Time: " + str(self.timer.currentTime / 1000) + " Seconds",1,(255,255,255))
        self.pastBlit = self.font.render("past Time: " + str(self.timer.previousTime / 1000),1,(255,255,255))

        if elapsedTime >= delayTime:  # need to only update previous time when time interval has actually passed otherwise it will never happen as previous and current wil always be almost identical
            self.timer.previousTime = self.timer.currentTime #set the previous tim interval
            self.image_iterator += 1
            if self.image_iterator > 4:
                self.image_iterator = 0


    def Draw(self):
        self.screen.fill((0,0,0))
        pyImgRect = self.pygame_images[self.image_iterator].get_rect()
        self.screen.blit(self.pygame_images[self.image_iterator], pyImgRect)
        self.screen.blit(self.timeBlit, (0,0))
        self.screen.blit(self.pastBlit, (400,0))
        pygame.display.flip()

'''
pygame.init()

#just playing around
print(str(os.name))
#done playing


use the following code to g et current screen resolution and set the mygame wiondow to that size
vidInfo = pygame.display.Info()
print(type(vidInfo))
WIDTH = vidInfo.current_w
HEIGHT = vidInfo.current_h


#time = pygame.time.Clock()
timer = ImgPiTimer.ImgPiTimer()
screen = pygame.display.set_mode((640,400))
running = True

font = pygame.font.Font('./font/Alpaca54.ttf', 20)
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


    timer.updateTime()
    elapsedTime = timer.checkAmountTime()
    delayTime = timer.convertSecToMs(5)
    #print(str(timer.currentTime))
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

  for img in images:
        pyImg = pygame.image.load(os.path.join('images', img))
        pyImgRect = pyImg.get_rect()
        screen.blit(pyImg, pyImgRect)
        pygame.display.flip()


'''