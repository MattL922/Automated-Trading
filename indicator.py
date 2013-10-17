class Indicator(object):
    def __init__(self):
        pass
    
    def calculate(self):
        raise Exception("calculate method not implemented.")

class MovingAverage(Indicator):
    def __init__(self, period, open=False, high=False, low=False, close=True):
        self.period = period
        self.open   = open
        self.high   = high
        self.low    = low
        self.close  = close

class SimpleMovingAverage(MovingAverage):
    def __init__(self, period, open=False, high=False, low=False, close=True):
        super(SimpleMovingAverage, self).__init__(period, open, high, low, close)
    
    def calculate(self, quotes, seq_id):
        if seq_id < self.period-1:
            raise Exception("Not enough Quotes to calculate a {0} period MA.".format(self.period))
        if self.open:
            return sum([q.open for q in quotes[seq_id-self.period+1:seq_id+1]])/self.period
        elif self.high:
            return sum([q.high for q in quotes[seq_id-self.period+1:seq_id+1]])/self.period
        elif self.low:
            return sum([q.low for q in quotes[seq_id-self.period+1:seq_id+1]])/self.period
        else: # self.close
            return sum([q.close for q in quotes[seq_id-self.period+1:seq_id+1]])/self.period
