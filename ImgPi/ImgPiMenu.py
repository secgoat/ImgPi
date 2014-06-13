import pygame

class ImgPiMenu:

    def __init__(self, menuItems = ("Continue", "Quit")):
        self.fontColor = (255,255,255)
        self.selectedColor = (204,0,0)
        self.items = menuItems
        #self.font = pygame.font.Font('./font/Alpaca54.ttf', 20)

    def Update(self, time):
        pass

    def Draw(self, screen):

        screen.fill((204,0,0))
        screen.blit("test", (100,100,))
        #for item in self.items:
        #    screen.blit(item, (100,100))



