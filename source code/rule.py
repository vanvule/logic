from fact import Fact
from unify import Unify
from substitute import Substitution

class Rule:
    def __init__(self, conclusion=Fact(), premises=[]):
        self.conclusion = conclusion
        self.premises = premises
        self.predicates = self.GetPredicates()
        self.premises.sort()
        self.dup_predicate = self.FindDupPredicate()

    def __repr__(self):
        return '{}:-{}'.format(str(self.conclusion), ','.join([str(condition) for condition in self.premises]))

    def copy(self):
        return Rule(self.conclusion.copy(), self.premises.copy())

    def GetNumPremises(self):
        return len(self.premises)

    # get all predicates from premises
    def GetPredicates(self):  # premise is a fact, premises is a list of facts
        predicates = set()
        for premise in self.premises:
            predicates.add(premise.predicate)
        return predicates

    def MayNeccessary(self, fact_predicate):
        return fact_predicate in self.predicates

    def MayTriggered(self, new_facts):
        for new_fact in new_facts:
            for premise in self.premises:
                if Unify(new_fact, premise, Substitution()):
                    return True
        return False

    def FindDupPredicate(self):
        num_premises = self.GetNumPremises()
        for i in range(num_premises - 1):
            if self.premises[i].predicate == self.premises[i+1].predicate:
                return True
        return False

    @staticmethod
    def ParseRule(rule_str):
        rule_str = rule_str.strip().rstrip('.').replace(' ', '')
        index = rule_str.find(':-')

        conclusion = Fact.ParseFact(rule_str[:index])
        premises = []
        premises_str = rule_str[index + 2:].split('),')
        if 'not' in premises_str[len(premises_str) - 1]:
            premises_str.remove(premises_str[len(premises_str) - 1])
        for idx, premise_str in enumerate(premises_str):
            if idx != len(premises_str) - 1:
                premise_str += ')'
            premise = Fact.ParseFact(premise_str)
            premises.append(premise)
        return Rule(conclusion, premises)
