class Observer(object):

  def __init__(self, observable):
    observable.add_observer(self)

  def update(self, observable, *args, **kwargs):
    print('Got', args, kwargs, 'From', observable)
