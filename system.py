class System(object):
    def __init__(self):
        pass

class Strategy(object):
    def __init__(self, entry=None, exit=None):
        self.entry = entry
        self.exit  = exit

class Entry(object):
    def __init__(self):
        self.conditions = []

class Exit(object):
    def __init__(self):
        self.conditions = []
