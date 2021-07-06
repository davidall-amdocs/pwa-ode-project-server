from sympy import *
from sympy.abc import x,z
from sympy.parsing import parse_expr

def checkSeparable(odeString):
    odeLeftString = odeString.split("=")[0]
    odeRightString = odeString.split("=")[1]
    odeLeftSym = parse_expr(odeLeftString)
    odeRightSym = parse_expr(odeRightString)
    y = Function('y')
    equation = Eq(odeLeftSym - odeRightSym, 0)
    left = equation.args[0]
    try:
        express = solve(Eq(left, Integer(0)), Derivative(y(x), x))
    except:
        return False

    if (len(express) == 0):
        return False

    aux = simplify(express[0])
    aux = aux.expand(force=True)
    aux = factor(aux)

    functionF = Integer(1)
    functionG = Integer(1)

    if type(aux) is Add:
        if 'y' in str(aux):
            functionG = aux
        else:
            functionF = aux
    else:
        if not ('y' in str(aux)):
            functionF = aux
        else:
            for term in aux.args:
                if 'y' in str(term):
                    functionG = Mul(functionG, term)
                else:
                    functionF = Mul(functionF, term)

    if 'y' in str(functionF):
        return False

    functionG = functionG.subs(y(x), Symbol('y'))
    functionG = functionG.subs(Symbol('x'), Symbol('u'))

    if 'u' in str(functionG):
        return False

    functionG = functionG.subs(Symbol('u'), Symbol('x'))
    functionG = functionG.subs(Symbol('y'), y(x))

    if (Mul(functionF, functionG)) == aux:
        return True

    return False

def checkLinear(odeString):
    odeLeftString = odeString.split("=")[0]
    odeRightString = odeString.split("=")[1]

    odeLeftSym = parse_expr(odeLeftString)
    odeRightSym = parse_expr(odeRightString)

    y = Function('y')
    equation = Eq(odeLeftSym - odeRightSym, 0)
    left = equation.args[0]
    try:
        express = solve(Eq(left, Integer(0)), Derivative(y(x), x))
    except:
        return False
    
    if (len(express) == 0):
        return False
    
    aux = expand(express[0])

    left = Derivative(y(x), x)

    functionF = parse_expr("0")
    functionG = parse_expr("0")

    for term in aux.args:
        if "y" in str(term):
            functionF = Add(functionF, Mul(term, Pow(y(x), Integer(-1))))
        else:
            functionG = Add(functionG, term)

    functionF = Mul(functionF, Integer(-1))
    functionF = simplify(functionF)
    functionG = simplify(functionG)

    if 'y' in str(functionF):
        return False
    
    if 'y' in str(functionG):
        return False

    right = Add(functionG, Mul(Integer(-1), functionF, y(x)))
    right = right.expand(force=True)

    if Add(aux, Mul(Integer(-1), right)).simplify() == Integer(0):
        return True

    return False

def checkReducibleLinear(odeString):
    odeLeftString = odeString.split("=")[0]
    odeRightString = odeString.split("=")[1]

    odeLeftSym = parse_expr(odeLeftString)
    odeRightSym = parse_expr(odeRightString)

    y = Function('y')
    equation = Eq(odeLeftSym - odeRightSym, 0)
    
    left = equation.args[0]
    exp = solve(left, Derivative(y(x), x))
    aux = expand(exp[0])

    functionF = parse_expr("0")
    functionG = parse_expr("0")
    
    aux = Mul(aux, Pow(y(x), Integer(-1)))
    aux = simplify(aux)

    for term in aux.args:
        if 'y' in str(term):
            for subTerm in term.args:
                if 'y' in str(subTerm):
                    try:
                        n = Add(subTerm.args[1], Integer(1))
                        subG = Mul(term, Pow(subTerm, Integer(-1)))
                        functionG = Add(functionG, subG)
                    except:   
                        n = None             
        else:
            functionF = Add(functionF, term)
  
    if functionG != 0 and functionF != 0:
        return True
    else:
        return False

def checkExact(odeString):
    odeLeftString = odeString.split("=")[0]
    odeRightString = odeString.split("=")[1]

    odeLeftSym = parse_expr(odeLeftString)
    odeRightSym = parse_expr(odeRightString)

    y = Function('y')
    equation = Eq(odeLeftSym - odeRightSym, 0)
    equation = equation.subs(y(x), Symbol('y'))

    functionP = Integer(0)
    functionQ = Integer(0)

    for term in equation.args[0].args:
        if 'Derivative' in str(term):
            functionQ = Add(functionQ, Mul(term, Pow(Derivative(Symbol('y'), x), Integer(-1))))
        else:
            functionP = Add(functionP, term)
    
    partialP = diff(functionP, Symbol('y'))
    partialQ = diff(functionQ, Symbol('x'))
    if Add(partialP, Mul(Integer(-1), partialQ)).simplify() == Integer(0):
        return True                                                                                                                           

    return False

def checkHomogeneous(odeString):
    odeLeftString = odeString.split("=")[0]
    odeRightString = odeString.split("=")[1]

    odeLeftSym = parse_expr(odeLeftString)
    odeRightSym = parse_expr(odeRightString)

    y = Function('y')
    equation = Eq(odeLeftSym - odeRightSym, 0)
    
    left = equation.args[0]
    exp = solve(left, Derivative(y(x), x))
    aux = expand(exp[0])
    
    left = Derivative(y(x), x)
    functionF = aux
  
    u = Function('u')

    functionF = functionF.subs(y(x), Mul(u(x), x))
    left = Add(Mul(Derivative(u(x), x), x), u(x))
    
    left = Add(left, Mul(functionF, Integer(-1)))
    left = expand(left)
    separableODE = Eq(left, Integer(0))

    return checkSeparable(separableODE)

def checkSuperiorOrder(odeString):
    odeLeftString = odeString.split("=")[0]
    odeRightString = odeString.split("=")[1]

    odeLeftSym = parse_expr(odeLeftString)
    odeRightSym = parse_expr(odeRightString)
    y = Function('y')
    equation = Eq(odeLeftSym - odeRightSym, 0)
    equation = equation.subs(y(x), Symbol('y'))
    equationsolve = parse_expr("E**(r*z)")

    for term in equation.args[0].args:
        if 'Derivative' in str(term):
            if type(term) is Mul:
                for subterm in term.args:
                    if 'Derivative' in str(subterm):
                        try:
                            expression = term.subs(Derivative(equationsolve, z, subterm.args[1].args[1]), diff( equationsolve, x, subterm.args[1].args[1]))
                            functionF = Add( functionF , expression)
                            if 'x' in str(functionF):
                                return False
                        except:
                            expression = term.subs(Derivative(equationsolve, z), diff( equationsolve, x))
                            functionF = Add( functionF , expression)
                            if 'x' in str(functionF):
                                return False
            else:
                expression = term.subs(Derivative(equationsolve, z, term.args[1].args[1]), diff( equationsolve, z , term.args[1].args[1]))
                functionF = Add( functionF , expression)
                if 'x' in str(functionF):
                    return False
        else:
            if 'r' in str(term):
                functionF = Add( functionF , term)
                if 'x' in str(functionF):
                    return False
            else:
                functionT = Mul(term, -1)

    return True

def classify(odeString):
    try:
        if checkSeparable(odeString):
            return "separable"
    except:
        print("Non Separable")

    try:
        if checkLinear(odeString):
            return "linear"
    except:
        print("Non Linear")
    
    try:
        if checkReducibleLinear(odeString):
            return "reducible"
    except:
        print("Non reducible")

    try:
        if checkExact(odeString):
            return "exact"
    except:
        print("Non Exact")
    
    try:
        if checkHomogeneous(odeString):
            return "homogeneous"
    except:
        print("Non Homogeneous")
    
    try:
        if checkSuperiorOrder(odeString):
            return "superior"
    except:
        print("Superior Order")

    return "undefined"

