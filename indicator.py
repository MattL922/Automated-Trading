class Indicator(object):
    def __init__(self):
        pass

class MovingAverage(Indicator):
    def __init__(self, period):
        self.period = period

class SimpleMovingAverage(MovingAverage):
    def __init__(self, period):
        super(SimpleMovingAverage, self).__init__(period)
    
    def calculate(self, quotes, seq_id):
        if seq_id < self.period-1:
            raise Exception("Not enough Quotes to calculate a {0} period MA.".format(self.period))
        return sum([q.close for q in quotes[seq_id-self.period+1:seq_id+1]])/self.period
