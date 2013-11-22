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
    o (boolean)
        If true, calculate the moving average from the open prices
    h (boolean)
        If true, calculate the moving average from the high prices
    l (boolean)
        If true, calculate the moving average from the low prices
    c (boolean)
        If true, calculate the moving average from the close prices
    
    Subclasses
    ----------
    SimpleMovingAverage
    ExponentialMovingAverage
    """
    
    def __init__(self, period, o=False, h=False, l=False, c=True):
        self.period = period
        self.o      = o
        self.h      = h
        self.l      = l
        self.c      = c
    
    def calculate(self):
        pass

class SimpleMovingAverage(MovingAverage):
    
    """
    Calculates a simple moving average.
    """
    
    def __init__(self, period, o=False, h=False, l=False, c=True):
        super(SimpleMovingAverage, self).__init__(period, o, h, l, c)
    
    def calculate(self, quotes, i):
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
        if i < self.period-1:
            raise Exception("Not enough Quotes to calculate a {0} period MA.".format(self.period))
        if self.o:
            return sum([q.o for q in quotes[i-(self.period-1):i+1]])/self.period
        elif self.h:
            return sum([q.h for q in quotes[i-(self.period-1):i+1]])/self.period
        elif self.l:
            return sum([q.l for q in quotes[i-(self.period-1):i+1]])/self.period
        else: # self.close
            return sum([q.c for q in quotes[i-(self.period-1):i+1]])/self.period

