class System(object):
    def __init__(self):
        pass

class Strategy(object):
    def __init__(self):
        self.entry_conditions = []
        self.exit_conditions  = []
    
    def add_entry_condition(self, condition):
        self.entry_conditions.append(condition)
    
    def add_exit_condition(self, condition):
        self.exit_conditions.append(condition)
    
    def eval_entry_conditions(self):
        """What if not all conditions are necessary for entry?"""
        return all([c.evaluate() for c in self.entry_conditions])
    
    def eval_exit_conditions(self):
        """What if not all conditions are necessary for exit?"""
        return all([c.evaluate() for c in self.exit_conditions])
