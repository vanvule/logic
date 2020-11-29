from fact import Fact
from substitute import Substitution
def IsVar(v):
    return isinstance(v, str) and v[0].isupper()

def IsCompound(c):
    return isinstance(c, Fact)

def IsList(l):
    return isinstance(l, list)

def Unify(x, y, theta):
    if theta is False:
        return False
    if x == y:
        return theta
    if IsVar(x):
        return UnifyVar(x, y, theta)
    if IsVar(y):
        return UnifyVar(y, x, theta)
    if IsCompound(x) and IsCompound(y):
        return Unify(x.GetArgs(), y.GetArgs(), Unify(x.GetPredicate(), y.GetPredicate(), theta))
    if IsList(x) and IsList(y) and len(x) == len(y):
        return Unify(x[1:], y[1:], Unify(x[0], y[0], theta))
    return False

def UnifyVar(var, x, theta): # theta is substitutions
    if theta.Contains(var):
        return Unify(theta.SubstituteValueOf(var), x, theta)
    if theta.Contains(x):
        return Unify(var, theta.SubstituteValueOf(x), theta)
    if OccurCheck(var, x):
        return False
    theta.AddToSubstTable(var,x)
    return theta

def OccurCheck(var,x):
    if IsCompound(x):
        temp_x = x.strip()
        idx = temp_x.index('(')
        args_str = temp_x[(idx + 1):(len(x) - 1)]
        args = args_str.split(',')
        if var in args:
            return True
    return False
