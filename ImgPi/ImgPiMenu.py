import pygame
import Observable

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

    def IsMouseSelection(self,position):
        posx = position[0]
        posy = position[1]
        if (posx >= self.posx and posx <= self.posx + self.width) and \
                (posy >= self.posy and posy <= self.posy + self.height):
            return True
        return False


class ImgPiMenu:

    #http://nebelprog.wordpress.com/2013/08/14/create-a-simple-game-menu-with-pygame-pt-1-writing-the-menu-options-to-the-screen/

    def __init__(self, menuItems = ("Continue", "Quit"), fontColor = (255,255,255), selectedColor = (255,0,0)):

        self.menu_action = Observable.Observable()
        self.fontColor = fontColor
        self.selectedColor = selectedColor
        self.mouseVisible = True
        self.font = pygame.font.Font('./font/Alpaca54.ttf', 20)
        self.items = menuItems
        self.menuItems = [] #placeholder for the font renderend strings plus pos etc.
        self.curItem = None #keep track of which menu Item is selected
        self.PrepareMenuItems()


    def PrepareMenuItems(self):
        for index, item in enumerate(self.items):
            menuItem = ImgPiMenuItem(item)

            screen_w = pygame.display.Info().current_w
            screen_h = pygame.display.Info().current_h
            posx = (screen_w / 2) - (menuItem.width / 2)
            #t_h total height of text block
            t_h = len(self.items) * menuItem.height
            posy = (screen_h / 2) - (t_h / 2) + (index * menuItem.height)
            menuItem.SetPOS(posx, posy)
            self.menuItems.append(menuItem)

    def SetMouseVisibility(self):
        if self.mouseVisible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

    def SetMouseSelection(self, item, mousePOS):
        """Marks the menu item the mouse is hovering on"""
        if item.IsMouseSelection(mousePOS):
            item.setFontColor(self.selectedColor)
        else:
            item.setFontColor(self.fontColor)

    def SetItemSelection(self, key):
        """marks menu item chooses by keyboard"""
        #reset all menu items to default state
        for item in self.menuItems:
            item.setFontColor(self.fontColor)

        if self.curItem is None:
            self.curItem = 0
        else:
            #send a click signal first and return the current menu item to the listener(observer)
            if key == pygame.K_RETURN:
                #if self.curItem == 0:
                self.menu_action.notify(self.menuItems[self.curItem].text)

            #find the chosen item
            if key == pygame.K_UP and self.curItem > 0:
                self.curItem -= 1
            elif key == pygame.K_UP and self.curItem == 0:
                self.curItem = len(self.menuItems) - 1
            elif key == pygame.K_DOWN and self.curItem < len(self.menuItems) -1:
                self.curItem += 1
            elif key == pygame.K_DOWN and self.curItem == len(self.menuItems) -1:
                self.curItem = 0

        self.menuItems[self.curItem].setFontColor(self.selectedColor)



    def Update(self, time, key):

        position = pygame.mouse.get_pos()

        if key is not None:

            self.mouseVisible = False
            self.SetItemSelection(key)

        if pygame.mouse.get_rel() != (0,0):
            self.mouseVisible = True
            self.curItem = None

        self.SetMouseVisibility()

        for item in self.menuItems:
            if self.mouseVisible:
                mousePOS = pygame.mouse.get_pos()
                self.SetMouseSelection(item, mousePOS)


    def Draw(self, screen):
        screen.fill((0,0,0))
        for item in self.menuItems:
            screen.blit(item.label, item.position)
'''
class MenuAction(Observable):

    def __init__(self):
        super().__init__(self)

'''

