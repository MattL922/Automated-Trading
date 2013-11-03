class Condition(object):
    
    """
    Evaluates to true or false via the evaluate method.
    
    Each Condition subclass will override the evaluate method.
    """
    
    def __init__(self, is_required):
        self.is_required = is_required
    
    def evaluate(self):
        raise Exception("evaluate method not implemented.")

class PriceCrossesMovingAverage(Condition):
    
    """
    Evaluates if the price crossed the moving average.
    
    Data Attributes
    ---------------
    is_required (boolean)
        Is this condition required for a buy or sell signal?
    ma (MovingAverage)
        The moving average to compare the price against
    above (boolean)
        If true, check if the price crossed above the moving average
    below (boolean)
        If true, check if the price crossed below the moving average
    """
    
    def __init__(self, is_required, ma, above=False, below=False):
        super(PriceCrossesMovingAverage, self).__init__(is_required)
        self.ma    = ma
        self.above = above
        self.below = below
    
    def evaluate(self, quotes, seq_id):
        """
        Evaluates if the price crossed the moving average.
        
        Returns true if the price crossed the moving average, false otherwise.
        
        Arguments
        ---------
        quotes (list<Quote>)
            List of Quotes
        seq_id (integer)
            Index of the Quote to evaluate in quotes
        """
        quote  = quotes[seq_id]
        ma_val = self.ma.calculate(quotes, seq_id)
        if self.above:
            if quote.open < ma_val and quote.high > ma_val:
                return True
        elif self.below:
            if quote.open > ma_val and quote.low < ma_val:
                return True
        return False

class CloseRelativeToMovingAverage(Condition):
    
    """
    Evaluates if the close is above or below the moving average.
    
    Data Attributes
    ---------------
    is_required (boolean)
        Is this condition required for a buy or sell signal?
    ma (MovingAverage)
        The moving average to compare the close against
    above (boolean)
        If true, check if the close is above the moving average
    below (boolean)
        If true, check if the close is below the moving average
    """
    
    def __init__(self, is_required, ma, above=False, below=False):
        super(CloseRelativeToMovingAverage, self).__init__(is_required)
        self.ma    = ma
        self.above = above
        self.below = below
    
    def evaluate(self, quotes, seq_id):
        """
        Evaluates if the close is on the specified side of the moving average.
        
        Returns true if the close is on the specified side of the moving
        average, false otherwise.
        
        Arguments
        ---------
        quotes (list<Quote>)
            List of Quotes
        seq_id (integer)
            Index of the Quote to evaluate in quotes
        """
        quote = quotes[seq_id]
        ma_val = self.ma.calculate(quotes, seq_id)
        if self.above:
            if quote.close > ma_val:
                return True
        elif self.below:
            if quote.close < ma.val:
                return True
        return False

