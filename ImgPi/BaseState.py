import Observable


class BaseState(Observable):

    def __init__(self):
        self.active = True
        self.hidden = False
        

