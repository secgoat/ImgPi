class Observable(object):

  def __init__(self):
    self.__observers = []

  def add_observer(self, obs):
    self.__observers.append(obs)

  def notify(self, *args, **kwargs):
    for o in self.__observers:
      o.update(self, *args, **kwargs)