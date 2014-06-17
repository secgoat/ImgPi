import os
import pygame
import ImgPiTimer


class ImgPiDisplay:

    def __init__(self):
        self.timer = ImgPiTimer.ImgPiTimer()
        self.screen = None#screen  # placeholder for the screen variable as it will be different based on windows or rPi
        self.running = True  #bool to keep track of program state, however this may need ot be moved up to imgpi.py (main)
        self.imgur_images = [] #list of images file names from the directory
        self.pygame_images = [] #list of rendered pygame images form the image files
        self.image_iterator = 0 #use this to load different images from the pygame_image list
        self.font = None  #placeholder for pygamefont
        #2 variables for displaying my times during debug
        self.timeBlit = None
        self.pastBlit = None
        self.width = None
        self.height = None

        self.LoadContent()


    def LoadContent(self):
        self.font = pygame.font.Font('./font/Alpaca54.ttf', 20) #load a font to use for debugging or display on screen
        self.imgur_images = os.listdir('./images/') #get all images in the images directory
        for img in self.imgur_images:
            #read all images in the directory and load them into pygame
            new_img = pygame.image.load(os.path.join('images', img)).convert()
            scale_img = pygame.transform.scale(new_img, (pygame.display.Info().current_w, pygame.display.Info().current_h))
            self.pygame_images.append(scale_img)
            #self.pygame_images.append(pygame.image.load(os.path.join('images', img)))


    def Update(self, time, key):
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
            print("current Time: ", self.timer.currentTime)
            self.image_iterator += 1

            if self.image_iterator > 4:
                self.image_iterator = 0


    def Draw(self, screen):
        screen.fill((0,0,0))
        pyImgRect = self.pygame_images[self.image_iterator].get_rect()
        screen.blit(self.pygame_images[self.image_iterator], pyImgRect)
        screen.blit(self.timeBlit, (0,0))
        #Bam font.size to get the size of the font
        text_w = self.font.size("past Time: " + str(self.timer.previousTime / 1000))[0]
        #get the screen width so we know where ot place the text.
        screen_w = pygame.display.Info().current_w
        screen.blit(self.pastBlit, (screen_w - text_w,0))
