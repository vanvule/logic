import itertools
from fact import Fact
from unify import Unify
from substitute import Substitution

def SUBST(p1, p2): # generalize modus ponens
    if len(p1) != len(p2):
        return False

    for i,j in zip(p1, p2):
        if i.GetPredicate() != j.GetPredicate():
            return False
            
    return Unify(p1, p2, Substitution())

def ForwardReasoning(kb, alpha): # alpha is a query 
    
    resolution = set()
    for fact in kb.facts:
        omega = Unify(fact, alpha, Substitution())
        if omega:
            if omega.Empty():
                resolution.add('True')
                return resolution
            resolution.add(omega)
    newest_generated_facts = kb.facts.copy()

    while True:
        new_facts = set()

        for rule in kb.rules:
            if not rule.MayTriggered(newest_generated_facts):
                continue
            
            num_premises = rule.GetNumPremises()
            relevant_facts = kb.GetRelevantFacts(rule)
            if not rule.dup_predicate:
                relevant_premises = list(itertools.combinations(sorted(relevant_facts), num_premises))
            else:
                relevant_premises = list(itertools.permutations(relevant_facts, num_premises))
            # relevant_premises = itertools.permutations(relevant_facts, num_premises)

            for combination_premise in relevant_premises:
                premises =  [premise for premise in combination_premise]
                theta = SUBST(rule.premises, premises)
                if not theta:
                    continue

                new_fact = rule.conclusion.copy()
                theta.Substitute(new_fact)

                if (new_fact not in new_facts) and (new_fact not in kb.facts):
                    new_facts.add(new_fact)
                    omega = Unify(new_fact, alpha, Substitution())
                    if omega:
                        if omega.Empty():
                            kb.facts.update(new_facts)
                            resolution.add('True')
                            return resolution
                        resolution.add(omega)

        newest_generated_facts = new_facts
        if not new_facts:
            if not resolution:
                resolution.add('False')
            return resolution
        kb.facts.update(new_facts)
