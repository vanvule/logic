class Fact:
    def __init__(self, predicate='', args=[], negative=False):
        self.predicate = predicate      # function | relation
        self.args = args          # list contain var and const
        self.negative = negative    # check negative
    
    def __repr__(self): 
        return '{}({})'.format(self.predicate, ', '.join(self.args))

    def __lt__(self, other):
        if self.predicate != other.predicate:
            return self.predicate < other.predicate
        if self.negative != other.negative:
            return self.negative < other.negative
        return self.args < other.args

    def __eq__(self, other):
        if self.predicate != other.predicate:
            return False
        if self.negative != other.negative:
            return False
        return self.args == other.args

    def __hash__(self):
        return hash(str(self))

    def copy(self):
        return Fact(self.predicate, self.args.copy(), self.negative)

    def negate(self):
        self.negative = 1 - self.negative

    def GetArgs(self):
        return self.args

    def GetPredicate(self):
        return self.predicate

    @staticmethod
    def ParseFact(fact_str):
        fact_str = fact_str.strip().rstrip('.').replace(' ','')
        if 'not' not in fact_str:
            index = fact_str.index('(')

            predicate = fact_str[:index]
            args = fact_str[index + 1 : -1].split(',')
            negative = False
            return Fact(predicate, args, negative)

        if 'not' in fact_str:
            temp_fact_str = fact_str[4:]
            index = temp_fact_str.index('(')

            predicate = temp_fact_str[:index]
            args = temp_fact_str[index + 1 : -1].split(',')
            negative = True
            return Fact(predicate, args, negative)
