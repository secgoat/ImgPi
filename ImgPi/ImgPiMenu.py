import pygame


class ImgPiMenuItem():

    def __init__(self, text, font= None, fontSize= 20, fontColor = (255,255,255), posx = 0, posy= 0):
        self.text = text
        self.font = pygame.font.Font('./font/Alpaca54.ttf', 20)
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.label = self.font.render(self.text, 1, self.fontColor)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.posx = posx
        self.posy = posy
        self.position = posx, posy

    def SetPOS(self, x, y):
        self.position = (x,y)
        self.posx = x
        self.posy = y

    def setFontColor(self, rgb):
        self.fontColor = rgb
        self.label = self.font.render(self.text, 1, self.fontColor)

    def MouseHover(self,position):
        posx = position[0]
        posy = position[1]
        if (posx >= self.posx and posx <= self.posx + self.width) and \
                (posy >= self.posy and posy <= self.posy + self.height):
            return True
        return False


class ImgPiMenu:

    #http://nebelprog.wordpress.com/2013/08/14/create-a-simple-game-menu-with-pygame-pt-1-writing-the-menu-options-to-the-screen/

    def __init__(self, menuItems = ("Continue", "Quit")):
        self.fontColor = (255,255,255)
        self.selectedColor = (204,0,0)
        self.font = pygame.font.Font('./font/Alpaca54.ttf', 20)
        self.items = menuItems
        self.renderedItems = [] #placeholder for the font renderend strings plus pos etc.
        self.PrepareMenuItems()
        #for item in menuItems:
        #    self.items.append(self.font.render(item, 1, self.fontColor))

    def PrepareMenuItems(self):
        for index, item in enumerate(self.items):
            menuItem = ImgPiMenuItem(item)

            #label = self.font.render(item, 1, self.fontColor)
            #width = label.get_rect().width
            #height = label.get_rect().height
            screen_w = pygame.display.Info().current_w
            screen_h = pygame.display.Info().current_h
            posx = (screen_w / 2) - (menuItem.width / 2)
            #t_h total height of text block
            t_h = len(self.items) * menuItem.height
            posy = (screen_h / 2) - (t_h / 2) + (index * menuItem.height)
            menuItem.SetPOS(posx, posy)
            self.renderedItems.append(menuItem)

    def Update(self, time):
        position = pygame.mouse.get_pos()
        for item in self.renderedItems:
            if item.MouseHover(position):
                item.setFontColor((255,0,0))
            else:
                item.setFontColor((255,255,255))

    def Draw(self, screen):
        screen.fill((0,0,0))
        for item in self.renderedItems:
            screen.blit(item.label, item.position)
     



