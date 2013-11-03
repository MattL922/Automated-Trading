from data import Quote

class Parser(object):
    
    """
    Parses daily historical data and creates a Quote object for each line.
    
    Data Attributes
    ---------------
    path (string): Path of the data file to read in
    quotes (list): List of Quote objects
    """
    
    def __init__(self, path):
        self.path   = path
        self.quotes = []
    
    def parse_quotes(self):
        """
        Read and parse the data file located at self.path.
        Create a Quote object for each line.
        """
        with open(self.path, "r") as f:
            lines = f.readlines()
            lines.reverse()
            for i, line in enumerate(lines[:-1]):
                line   = line.split(",")
                date   = line[0].strip()
                open   = float(line[1].strip())
                high   = float(line[2].strip())
                low    = float(line[3].strip())
                close  = float(line[4].strip())
                volume = int(line[5].strip())
                quote  = Quote(i, date, open, high, low, close, volume)
                self.quotes.append(quote)

