class Indicator(object):
    
    """
    Calculates the value of a technical indicator via the calculate method.
    
    Each Indicator subclass will override the calculate method.
    """
    
    def __init__(self):
        pass
    
    def calculate(self):
        raise Exception("calculate method not implemented.")

class MovingAverage(Indicator):
    
    """
    Calcualtes a moving average via the calculate method.
    
    Data Attributes
    ---------------
    period (integer)
        The number of trading days to calculate the moving average over
    open (boolean)
        If true, calculate the moving average from the open prices
    high (boolean)
        If true, calculate the moving average from the high prices
    low (boolean)
        If true, calculate the moving average from the low prices
    close (boolean)
        If true, calculate the moving average from the close prices
    
    Subclasses
    ----------
    SimpleMovingAverage
    ExponentialMovingAverage
    """
    
    def __init__(self, period, open=False, high=False, low=False, close=True):
        self.period = period
        self.open   = open
        self.high   = high
        self.low    = low
        self.close  = close
    
    def calculate(self):
        pass

class SimpleMovingAverage(MovingAverage):
    
    """
    Calculates a simple moving average.
    """
    
    def __init__(self, period, open=False, high=False, low=False, close=True):
        super(SimpleMovingAverage, self).__init__(period, open, high, low, close)
    
    def calculate(self, quotes, seq_id):
        """
        Calculates the simple moving average from a list of Quotes.
        
        Returns the value of the moving average as a float.
        
        Arguments
        ---------
        quotes (list<Quote>)
            List of Quotes to calculate the moving average from
        seq_id (integer)
            The index of the last Quote in quotes to calculate the moving
            average from
        """
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

