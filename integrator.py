from atomic_integrals import *

def checkIntegral(expression):
    if expression == BASIC_01:
        return SOLVE_01
    else:
        return integrate(expression)