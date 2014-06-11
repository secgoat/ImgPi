import os

import pygame

import ImgPiDisplay
import Imgur
import DeviantArt



class ImgPi:

    def __init__(self):
        self.screen = None # placeholder will be a pygame display object
        #self.font = None #placeholder for a pygame font

        self.timer = None # will be ImgPiTimer object
        self.running = True # this wil be used for later to stop th eloop possible and kill the program

        self.mainState = ImgPiDisplay.ImgPiDisplay()
        self.imgur = Imgur.Imgur()
        self.deviant = DeviantArt.DeviantArt()

        #make gamestate objects so we can set each one to active inactive etc.
        self.states = {'Main': None, 'Menu': None} #dict to hold the different gamestate objects
        self.activeState = None #use this to keep track of which state is currently th active and being updated one


        #check for images folder if it doesn't exist make it
        if not os.path.exists('images'):
            os.mkdir('images')
            '''
            os.chdir('images')
            if not os.path.exists('imgur'):
                os.mkdir('imgur')
            if not os.path.exists('deviantart'):
                os.mkdir('deviantart')
            '''

    def init_pygame(self):

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

        #self.font = pygame.font.Font('./font/Alpaca54.ttf', 20) #load a font to use for debugging or display on screen

    def downloadImages(self):
        self.imgur.getSubredditGallery()
        self.imgur.downloadFromImgur()
        self.deviant.getRSS()
        self.deviant.downloadRSSContent()

    def Update(self, screen):
        time = None
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        screen.Update(time)
        screen.Draw(self.screen)
        pygame.display.flip()



if __name__ == "__main__":
    imgpi = ImgPi()
    imgpi.init_pygame()
    #imgpi.screen = ImgPiDisplay.ImgPiDisplay()
    while imgpi.running:
        imgpi.Update(imgpi.mainState)

