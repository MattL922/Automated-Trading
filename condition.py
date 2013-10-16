class Condition(object):
    def __init__(self):
        pass

class PriceCrossesMovingAverage(Condition):
    def __init__(self, ma, above=False, below=False):
        self.ma    = ma
        self.above = above
        self.below = below
    
    def evaluate(self, quotes, seq_id):
        quote  = quotes[seq_id]
        ma_val = self.ma.calculate(quotes, seq_id)
        if self.above:
            if quote.open < ma_val and quote.high > ma_val:
                return True
        elif self.below:
            if quote.open > ma_val and quote.low < ma_val:
                return True
        return False

class 
