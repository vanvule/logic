from fact import Fact
from rule import Rule
from forward_reasoning import ForwardReasoning
from clause import Clause


class KB:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def AddFact(self, fact):
        self.facts.add(fact)

    def AddRule(self, rule):
        self.rules.append(rule)

    def Query(self, alpha):
        return ForwardReasoning(self, alpha)

    def GetRelevantFacts(self, rule):
        relevant_facts = []
        for fact in self.facts:
            if rule.MayNeccessary(fact.predicate):
                relevant_facts.append(fact)
        return relevant_facts

    @staticmethod
    def CreateKB(kb, clauses):
        while clauses:
            clause, clauses = Clause.NextClause(clauses)
            clause_type = Clause.Categorize(clause)
            if clause_type == 'fact':
                fact = Fact.ParseFact(clause)
                kb.AddFact(fact)
            elif clause_type == 'rule':
                if ';' in clause:
                    idx = clause.index(':-')
                    temp_clause = clause[idx + 2:].rstrip('.')
                    conclusion = clause[0:idx]
                    conditions_raw = temp_clause.split(';')
                    conditions = []
                    for condition in conditions_raw:
                        temp = condition.strip()
                        temp = temp[1:len(temp) - 1]
                        conditions.append(temp)

                    rules = []
                    for condition in conditions:
                        rule_str = conclusion + ':-' + condition + '.'
                        rules.append(rule_str)
                    for clause in rules:
                        rule = Rule.ParseRule(clause)
                        kb.AddRule(rule)
                elif ';' not in clause:
                    rule = Rule.ParseRule(clause)
                    kb.AddRule(rule)
