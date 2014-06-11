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
        self.width = None
        self.height = None
        #check if windows or rPi to init pygame displays
        if os.name == "nt":
            #windows / Development
            pygame.init()
            self.screen = pygame.display.set_mode((640,400))
        else:
            #rPi / live "posix"
            #https://learn.adafruit.com/pi-video-output-using-pygame/pointing-pygame-to-the-framebuffer

            # Based on "Python GUI in Linux frame buffer"
            # http://www.karoltomala.com/blog/?p=679
            disp_no = os.getenv("DISPLAY")
            if disp_no:
                print("I'm running under X display = {}".format(disp_no))
            # Check which frame buffer drivers are available
            # Start with fbcon since directfb hangs with composite output
            drivers = ['fbcon', 'directfb', 'svgalib']
            found = False
            for driver in drivers:
                # Make sure that SDL_VIDEODRIVER is set
                if not os.getenv('SDL_VIDEODRIVER'):
                    os.putenv('SDL_VIDEODRIVER', driver)
                try:
                    pygame.init()
                    pygame.display.init()
                except pygame.error:
                    print("Driver {} Failed".format(driver))
                    continue
                found = True
                break

            if not found:
                raise Exception("no suitable driver found")

            size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
            print("Framebuffer size is %d x %d" % (size[0], size[1]))
            self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)


        self.LoadContent()


    def LoadContent(self):
        self.font = pygame.font.Font('./font/Alpaca54.ttf', 20) #load a font to use for debugging or siplay on screen
        self.imgur_images = os.listdir('./images/') #get all images in the images directory
        for img in self.imgur_images:
            #read all images in the directory and load them into pygame
            new_img = pygame.image.load(os.path.join('images', img)).convert()
            scale_img = pygame.transform.scale(new_img, (pygame.display.Info().current_w, pygame.display.Info().current_h))
            self.pygame_images.append(scale_img)
            #self.pygame_images.append(pygame.image.load(os.path.join('images', img)))


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
            print("current Time: ", self.timer.currentTime)
            self.image_iterator += 1

            if self.image_iterator > 4:
                self.image_iterator = 0


    def Draw(self):
        self.screen.fill((0,0,0))
        pyImgRect = self.pygame_images[self.image_iterator].get_rect()
        self.screen.blit(self.pygame_images[self.image_iterator], pyImgRect)
        self.screen.blit(self.timeBlit, (0,0))
        #Bam font.siz to get the size of the font
        text_w = self.font.size("past Time: " + str(self.timer.previousTime / 1000))[0]
        #get the screen width so we know where ot place the text.
        screen_w = pygame.display.Info().current_w
        self.screen.blit(self.pastBlit, (screen_w - text_w,0))
