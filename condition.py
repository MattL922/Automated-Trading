class Condition(object):
    def __init__(self):
        pass

class PriceCrossesMA(Condition):
    def __init__(self, ma_period, above, below):
        self.ma_period = ma_period
        self.above     = above
        self.below     = below
    
    def evaluate(self, quote_dict, seq_id):
        if quote_dict[seq_id-1].high <= 
