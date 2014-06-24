import Observable


class BaseState(Observable):

    def __init__(self):
        self.active = True # is this state active should we update it?
        self.hidden = False # is this state hidden, shoudl we draw it?
        super().__init__()

