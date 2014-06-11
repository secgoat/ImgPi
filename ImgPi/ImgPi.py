import os

import pygame

import ImgPiDisplay
import Imgur
import DeviantArt



class ImgPi:
    CLIENT_ID = "efed10c55d16860"

    def __init__(self):
        self.display = None # placeholder will be a ImgPiDisplay object
        self.timer = None # will be ImgPiTimer object
        self.imageList = None
        self.imgur = Imgur.Imgur()
        self.deviant = DeviantArt.DeviantArt()

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
    def downloadImages(self):
        self.imgur.getSubredditGallery()
        self.imgur.downloadFromImgur()
        self.deviant.getRSS()
        self.deviant.downloadRSSContent()

    def Update(self, screen):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        screen.Update()
        screen.Draw()
        pygame.display.flip()



if __name__ == "__main__":
    imgpi = ImgPi()
    #imgpi.downloadImages()
    imgpi.display = ImgPiDisplay.ImgPiDisplay()
    while imgpi.display.running:
        imgpi.Update(imgpi.display)
        #imgpi.display.Update()
        #imgpi.display.Draw()
