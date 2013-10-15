class Indicator(object):
    def __init__(self):
        pass

class MovingAverage(Indicator):
    def __init__(self, period):
        self.period = period

class SimpleMovingAverage(MovingAverage):
    def __init__(self, period):
        pass
