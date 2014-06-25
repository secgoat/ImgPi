import pygame.time


class ImgPiTimer:
    """

    """

    def __init__(self):
        self.clock = pygame.time.Clock()  # start the clock object to keep track of time
        self.currentTime = pygame.time.get_ticks()  # this and previousTime will be used to keep track of how much time has passed
        self.previousTime = pygame.time.get_ticks() #init both to current time as we haven't made nay changes ot time yet

    def convert_ms_sec(self, milliseconds):
        seconds = milliseconds / 1000
        return seconds

    def convert_sec_ms(self, seconds):
        milliseconds = seconds * 1000
        return milliseconds

    def update_time(self):
        #self.previousTime = self.currentTime
        self.currentTime = pygame.time.get_ticks()

    def check_amount_time(self):
        elapsedTime = self.currentTime - self.previousTime
        return elapsedTime

