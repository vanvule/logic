class Conditions:
    def __init__(self, operator='', args=[], negative=False):
        self.operator = operator
        self.args = args
        self.negative = negative

    def __repr__(self):
        return '{}{}{}'.format(self.args[0],self.operator,self.args[1])

    def __hash__(self):
        return hash(str(self))

    @staticmethod
    def ParseCondition(condition_str):
        condition_str = condition_str.strip().rstrip('.').replace(' ','')
        if 'not' in condition_str:
            temp_condition_str = condition_str[4:len(condition_str)-1]
            if '=' in temp_condition_str:
                args = temp_condition_str.split('=')
                operator = '='
                negative = True
                return(operator,args,negative)
            if '>' in temp_condition_str:
                args = temp_condition_str.split('>')
                operator = '>'
                negative = True
                return(operator,args,negative)
            if '<' in temp_condition_str:
                args = temp_condition_str.split('<')
                operator = '<'
                negative = True
                return(operator,args,negative)
            if '>=' in temp_condition_str:
                args = temp_condition_str.split('>=')
                operator = '>='
                negative = True
                return(operator,args,negative)
            if '<=' in temp_condition_str:
                args = temp_condition_str.split('<=')
                operator = '<='
                negative = True
                return(operator,args,negative)
        else:
            if '=' in condition_str:
                args = condition_str.split('=')
                operator = '='
                negative = False
                return(operator,args,negative)
            if '>' in condition_str:
                args = condition_str.split('>')
                operator = '>'
                negative = False
                return(operator,args,negative)
            if '<' in condition_str:
                args = temp_condition_str.split('<')
                operator = '<'
                negative = False
                return(operator,args,negative)
            if '>=' in condition_str:
                args = temp_condition_str.split('>=')
                operator = '>='
                negative = False
                return(operator,args,negative)
            if '<=' in condition_str:
                args = temp_condition_str.split('<=')
                operator = '<='
                negative = False
                return(operator,args,negative)