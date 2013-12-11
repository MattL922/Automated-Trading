from parser import Parser

class System(object):
    def __init__(self, path):
        self.parser         = Parser(path)
        self.portfolio      = Portfolio()
        self.buy_strategy   = Strategy()
        self.sell_strategy  = Strategy()
        self.short_strategy = Strategy()
        self.cover_strategy = Strategy()
        self.quotes         = self.parser.parse_quotes()
    
    def add_buy_condition(self, condition):
        self.buy_strategy.add_condition(condition)
    
    def add_sell_condition(self, condition):
        self.sell_strategy.add_condition(condition)
    
    def add_short_condition(self, condition):
        self.short_strategy.add_condition(condition)
    
    def add_cover_condition(self, condition):
        self.cover_strategy.add_condition(condition)
    
    def run_backtest(self):
        for i in xrange(len(self.quotes)):
            if self.portfolio.is_long():
                sell_prices = self.sell_strategy.eval_conditions(self.quotes, i)
                if sell_prices:
                    print "Sold at {0} on {1}".format(max(sell_prices), self.quotes[i].d)
                    t = Trade(self.quotes[i].d, max(sell_prices), Trade.SELL)
                    self.portfolio.add_trade(t)
            elif self.portfolio.is_short():
                cover_prices = self.cover_strategy.eval_conditions(self.quotes, i)
                if cover_prices:
                    print "Covered at {0} on {1}".format(min(cover_prices), self.quotes[i].d)
                    t = Trade(self.quotes[i].d, min(cover_prices), Trade.COVER)
                    self.portfolio.add_trade(t)
            else:
                buy_prices = self.buy_strategy.eval_conditions(self.quotes, i)
                if buy_prices:
                    print "Bought at {0} on {1}".format(min(buy_prices), self.quotes[i].d)
                    t = Trade(self.quotes[i].d, min(buy_prices), Trade.BUY)
                    self.portfolio.add_trade(t)
                    continue
                short_prices = self.short_strategy.eval_conditions(self.quotes, i)
                if short_prices:
                    print "Shorted at {0} on {1}".format(max(short_prices), self.quotes[i].d)
                    t = Trade(self.quotes[i].d, max(short_prices), Trade.SHORT)
                    self.portfolio.add_trade(t)
                    continue
        if self.portfolio.is_long():
            t = Trade(self.quotes[-1].d, self.quotes[-1].c, Trade.SELL)
            self.portfolio.add_trade(t)
        elif self.portfolio.is_short():
            t = Trade(self.quotes[-1].d, self.quotes[-1].c, Trade.COVER)
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
    CLOSED = 0
    LONG   = 1
    SHORT  = 2
    
    def __init__(self):
        self.tradelog = []
        self.position = Portfolio.CLOSED
    
    def is_closed(self):
        return self.position is Portfolio.CLOSED
    
    def is_long(self):
        return self.position is Portfolio.LONG
    
    def is_short(self):
        return self.position is Portfolio.SHORT
    
    def add_trade(self, trade):
        self.tradelog.append(trade)
        if (trade.trade_type is Trade.SELL) or (trade.trade_type is Trade.COVER):
            self.position = Portfolio.CLOSED
        elif trade.trade_type is Trade.BUY:
            self.position = Portfolio.LONG
        else:
            self.position = Portfolio.SHORT
    
    def calculate_return(self):
        return reduce(lambda x, y: x * y, [t2.price / t1.price for t1,t2 in zip(self.tradelog[::2], self.tradelog[1::2])])

class Trade(object):
    BUY   = 1
    SELL  = 2
    SHORT = 3
    COVER = 4
    
    def __init__(self, date, price, trade_type):
        self.date       = date
        self.price      = price
        self.trade_type = trade_type

