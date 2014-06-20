class Observer(object):

  def __init__(self, observable):
    observable.addObserver(self)

  def update(self, observable, *args, **kwargs):
    print('Got', args, kwargs, 'From', observable)
