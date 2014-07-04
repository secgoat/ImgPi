#import Observable


class BaseState(object):

    def __init__(self):
        self.__observers = []
        self.active = True # is this state active should we update it?
        self.hidden = False # is this state hidden, shoudl we draw it?
        super().__init__()

    def draw(self):
        pass

    def update(self):
        pass


    def add_observer(self, obs):
        self.__observers.append(obs)

    def notify(self, *args, **kwargs):
        for o in self.__observers:
            o.update(self, *args, **kwargs)