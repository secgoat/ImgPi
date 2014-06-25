import os
import pygame
import random
import ImgPiTimer


class ImgPiDisplay:

    def __init__(self):
        self.timer = ImgPiTimer.ImgPiTimer()
        self.screen = None#screen  # placeholder for the screen variable as it will be different based on windows or rPi
        self.running = True  #bool to keep track of program state, however this may need ot be moved up to imgpi.py (main)
        self.raw_images = [] #list of images file names from the directory
        self.current_image = None # keep one image that has been converted and scaled for pygame display
        self.pygame_images = [] #list of rendered pygame images form the image files
        self.image_iterator = 0 #use this to load different images from the pygame_image list
        self.font = None  #placeholder for pygamefont
        #2 variables for displaying my times during debug
        self.timeBlit = None
        self.pastBlit = None
        self.width = None
        self.height = None

        self.load_content()


    def load_content(self):
        self.font = pygame.font.Font('./font/Alpaca54.ttf', 20) #load a font to use for debugging or display on screen
        self.raw_images = os.listdir('./images/') #get all images in the images directory

        rand_img_num = random.randint(0, len(self.raw_images))
        self.convert_image(self.raw_images[rand_img_num])
        '''need to move the following to a new method, so we only convert 1 image at atime when needed, otherwise
        there is a terrible delay on start up

        for img in self.imgur_images:
            #read all images in the directory and load them into pygame
            new_img = pygame.image.load(os.path.join('images', img)).convert()
            scale_img = pygame.transform.scale(new_img, (pygame.display.Info().current_w, pygame.display.Info().current_h))
            self.pygame_images.append(scale_img)
            #self.pygame_images.append(pygame.image.load(os.path.join('images', img)))
        '''

    def convert_image(self, image):
        new_img = pygame.image.load(os.path.join('images', image)).convert()
        scaled_img = pygame.transform.scale(new_img, (pygame.display.Info().current_w, pygame.display.Info().current_h))
        self.current_image = scaled_img

    def update(self, time, key):
        self.timer.update_time() #update current time interval
        elapsedTime = self.timer.check_amount_time()
        delayTime = self.timer.convert_sec_ms(5)

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.running = False

        self.timeBlit = self.font.render("Current Time: " + str(self.timer.currentTime / 1000) + " Seconds",1,(255,255,255))
        self.pastBlit = self.font.render("past Time: " + str(self.timer.previousTime / 1000),1,(255,255,255))

        if elapsedTime >= delayTime:  # need to only update previous time when time interval has actually passed otherwise it will never happen as previous and current wil always be almost identical
            self.timer.previousTime = self.timer.currentTime #set the previous tim interval
            print("current Time: ", self.timer.currentTime)
            rand_img_num = random.randint(0, len(self.raw_images))
            self.convert_image(self.raw_images[rand_img_num])
            #self.image_iterator += 1

            #if self.image_iterator > len(self.raw_images):
            #    self.image_iterator = 0


    def draw(self, screen):
        screen.fill((0,0,0))

        pyImgRect = self.current_image.get_rect()
        screen.blit(self.current_image, pyImgRect)

        screen.blit(self.timeBlit, (0,0))
        #Bam font.size to get the size of the font
        text_w = self.font.size("past Time: " + str(self.timer.previousTime / 1000))[0]
        #get the screen width so we know where ot place the text.
        screen_w = pygame.display.Info().current_w
        screen.blit(self.pastBlit, (screen_w - text_w,0))
