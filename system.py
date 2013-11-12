from parser import Parser

class System(object):
    def __init__(self, path):
        self.parser = Parser(path)
        self.entry_strategy = Strategy()
        self.exit_strategy = Strategy()
        self.quotes = None
    
    def add_entry_condition(self, condition):
        self.entry_strategy.add_condition(condition)
    
    def add_exit_condition(self, condition):
        self.exit_strategy.add_condition(condition)
    
    def init_quotes(self):
        self.quotes = self.parser.parse_quotes()

class Strategy(object):
    def __init__(self):
        self.conditions = []
    
    def add_condition(self, condition):
        self.conditions.append(condition)
    
    def eval_conditions(self):
        """What if not all conditions are necessary for entry/exit?"""
        return all([c.evaluate() for c in self.conditions])

class Portfolio(object):
    def __init__(self):
        self.tradelog = []
    
    def calculate_return(self):
        return reduce(lambda x, y: x * y, [t2.price / t1.price for t1,t2 in zip(self.tradelog[::2], self.tradelog[1::2])])

class Trade(object):
    def __init__(self, date, price, buy=False, sell=False):
        self.date = date
        self.price = price
        self.buy = buy
        self.sell = sell
