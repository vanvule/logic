from kb import KB
from fact import Fact
import sys
kb = KB()

kb_file = sys.argv[1]
query_file = sys.argv[2]
answer_file = sys.argv[3]
kb_file = open(kb_file, 'r')
clauses = kb_file.readlines()
KB.CreateKB(kb, clauses)

query_file = open(query_file, 'r')
answer_file = open(answer_file, 'w')
count_query = 1
for query in query_file.readlines():
    alpha = Fact.ParseFact(query)
    alpha_str = str(alpha) + '.'
    print(str(count_query) + "/", alpha_str)
    substs = set(kb.Query(alpha))  
    substs_str = ' ;\n'.join([str(subst) for subst in substs]) + '.\n'
    print(substs_str)
    answer_file.write(alpha_str + '\n')
    answer_file.write(substs_str + '\n')
    count_query += 1