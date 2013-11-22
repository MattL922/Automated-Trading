class Condition(object):
    
    """
    Evaluates to true or false via the evaluate method.
    
    Each Condition subclass will override the evaluate method.
    """
    
    def __init__(self):
        pass
    
    def evaluate(self):
        raise Exception("evaluate method not implemented.")

class PriceCrossesMovingAverage(Condition):
    
    """
    Evaluates if the price crossed the moving average.
    
    Data Attributes
    ---------------
    ma (MovingAverage)
        The moving average to compare the price against
    above (boolean)
        If true, check if the price crossed above the moving average
    below (boolean)
        If true, check if the price crossed below the moving average
    """
    
    def __init__(self, ma, above=False, below=False):
        super(PriceCrossesMovingAverage, self).__init__()
        self.ma              = ma
        self.above           = above
        self.below           = below
        self.crossover_price = None
    
    def evaluate(self, quotes, i):
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
        quote      = quotes[i]
        prev_quote = quotes[i-1]
        try:
            ma_val      = self.ma.calculate(quotes, i)
            prev_ma_val = self.ma.calculate(quotes, i-1)
        except:
            return False
        if self.above:
            # Two day crossover
            if prev_quote.c < prev_ma_val and quote.h > ma_val:
                self.crossover_price = max(quote.o, ma_val + 0.01)
                return True
            # One day crossover
            if (quote.l < ma_val < quote.h) and (quote.c > ma_val or quote.o < ma_val):
                self.crossover_price = ma_val + 0.01
                return True
        elif self.below:
            # Two day crossover
            if prev_quote.c > prev_ma_val and quote.l < ma_val:
                self.crossover_price = min(quote.o, ma_val - 0.01)
                return True
            # One day crossover
            if (quote.l < ma_val < quote.h) and (quote.c < ma_val or quote.o > ma_val):
                self.crossover_price = ma_val - 0.01
                return True
        return False

# Maybe change this class to PriceRelativeToMovingAverage (o,h,l, AND c)
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
    
    def evaluate(self, quotes, i):
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
        ma_val = self.ma.calculate(quotes, i)
        if self.above:
            if quote.c > ma_val:
                return True
        elif self.below:
            if quote.c < ma.val:
                return True
        return False

