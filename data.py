class Quote(object):
    """
    Price and volume action for a single trading day.
    
    Quotes are stored sequentially in a dictionary with their seq_id being the
    key.
    
    """
    
    def __init__(self, seq_id, d, o, h, l, c, v, prev, next):
        self.seq_id = seq_id
        self.date   = d
        self.open   = o
        self.high   = h
        self.low    = l
        self.close  = c
        self.volume = v
