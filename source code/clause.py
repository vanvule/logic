class Clause:
    @staticmethod
    def Categorize(clause_str):
        clause_str = clause_str.strip()
        if not clause_str:
            return 'blank'
        if clause_str.startswith('/*') and clause_str.endswith('*/'):
            return 'cmt'
        if ':-' in clause_str:
            return 'rule'
        return 'fact'

    @staticmethod
    def NextClause(input_str):
        index = 0
        next_str = input_str[index].strip()
        if next_str.startswith('/*'):
            while not next_str.endswith('*/'):
                index += 1
                next_str += input_str[index].strip()
        elif next_str:
            while not next_str.endswith('.'):
                index += 1
                next_str += input_str[index].strip()

        return next_str, input_str[index + 1:]