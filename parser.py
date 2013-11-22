from quote import Quote

class Parser(object):
    
    """
    Parses daily historical data and creates a Quote object for each line.
    
    Data Attributes
    ---------------
    path (string)
        Path of the data file to read in
    """
    
    def __init__(self, path):
        self.path = path
    
    def parse_quotes(self):
        """
        Read and parse the data file located at self.path.
        Create a Quote object for each line.
        
        Returns a list of Quotes
        """
        quotes = []
        with open(self.path, "r") as f:
            lines = f.readlines()
            lines.reverse()
            for i, line in enumerate(lines[:-1]):
                line   = line.split(",")
                d = line[0].strip()
                o = float(line[1].strip())
                h = float(line[2].strip())
                l = float(line[3].strip())
                c = float(line[4].strip())
                v = int(line[5].strip())
                quote  = Quote(d, o, h, l, c, v)
                quotes.append(quote)
        return quotes

