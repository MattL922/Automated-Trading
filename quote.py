class Quote(object):
    
    """
    Price and volume action for a single trading day.
    
    Quotes are stored sequentially in a list with their seq_id being the index.
    """
    
    def __init__(self, d, o, h, l, c, v):
        self.d = d
        self.o = o
        self.h = h
        self.l = l
        self.c = c
        self.v = v
