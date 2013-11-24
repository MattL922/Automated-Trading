from parser import Parser

class System(object):
    def __init__(self, path):
        self.parser         = Parser(path)
        self.portfolio      = Portfolio()
        self.entry_strategy = Strategy()
        self.exit_strategy  = Strategy()
        self.quotes         = self.parser.parse_quotes()
    
    def add_entry_condition(self, condition):
        self.entry_strategy.add_condition(condition)
    
    def add_exit_condition(self, condition):
        self.exit_strategy.add_condition(condition)
    
    def run_backtest(self):
        for i in xrange(len(self.quotes)):
            if not self.portfolio.long:
                entry_prices = self.entry_strategy.eval_conditions(self.quotes, i)
                if len(entry_prices):
                    print "Bought at {0}".format(min(entry_prices))
                    t = Trade(self.quotes[i].d, min(entry_prices), buy=True)
                    self.portfolio.add_trade(t)
                    self.portfolio.long = True
            if self.portfolio.long:
                exit_prices = self.exit_strategy.eval_conditions(self.quotes, i)
                if len(exit_prices):
                    print "Sold at {0}".format(max(exit_prices))
                    t = Trade(self.quotes[i].d, max(exit_prices), sell=True)
                    self.portfolio.add_trade(t)
                    self.portfolio.long = False
        if self.portfolio.long:
            t = Trade(self.quotes[-1].d, self.quotes[-1].c, sell=True)
            self.portfolio.add_trade(t)
        print self.portfolio.calculate_return()

class Strategy(object):
    def __init__(self):
        self.conditions = []
    
    def add_condition(self, condition):
        self.conditions.append(condition)
    
    def eval_conditions(self, quotes, i):
        return filter(None, (c.evaluate(quotes, i) for c in self.conditions))

class Portfolio(object):
    def __init__(self):
        self.tradelog = []
        self.long     = False
        self.short    = False
    
    def add_trade(self, trade):
        self.tradelog.append(trade)
    
    def calculate_return(self):
        return reduce(lambda x, y: x * y, [t2.price / t1.price for t1,t2 in zip(self.tradelog[::2], self.tradelog[1::2])])

class Trade(object):
    def __init__(self, date, price, buy=False, sell=False):
        self.date = date
        self.price = price
        self.buy = buy
        self.sell = sell

