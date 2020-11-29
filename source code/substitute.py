# dung de thay the bien bang hang 
class Substitution:
    def __init__(self):
        self.subst_table = dict()

    def __repr__(self):
        return ', '.join('{} = {}'.format(key, value) for key, value in self.subst_table.items())
    
    def __eq__(self, other):
        return self.subst_table == other.subst_table
    
    def __hash__(self):
        return hash(frozenset(self.subst_table.items()))
    
    def Empty(self):
        return len(self.subst_table) == 0
    
    def Contains(self, var):
        return var in self.subst_table

    def SubstituteValueOf(self, var):
        return self.subst_table[var]

    def Substitute(self, fact):
        for index, arg in enumerate(fact.args):
            if self.Contains(arg):
                fact.args[index] = self.SubstituteValueOf(arg)
    
    def AddToSubstTable(self, var, x): # x is values of var
        self.subst_table[var] = x
