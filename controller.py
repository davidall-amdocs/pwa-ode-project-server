from sympy import *
from sympy.abc import x
from flask import jsonify
from sympy.parsing.sympy_parser import parse_expr

from parse_sympy import parseLatex
from solve import solveSeparable
from classificator import classify

def solve(inputString):
    try:
        equation = parseLatex(inputString)

    except Exception as e:
        raise e

    odeType = classify(str(equation) + "= 0")

    if odeType == "separable":
        solveArray = solveSeparable(str(equation) + "= 0")    
        print(solveArray[1])
        return solveArray[1]
    else:
        solveSingle = dsolve(Eq(equation, 0), Function('y')(x))
        print(solveSingle)
        return [ [latex("- Solve by DSolve: ") + "\\\\ \\\\", [ latex(solveSingle) + "\\\\ \\\\" ] ] ]
    

    # eqType = classify(str(equation) + "= 0")

    # if eqType == "separable":
    #     solve = solveSeparable(str(equation) + "= 0")
    #     return solve[1]
    # else:
    #     solve = dsolve(Eq(equation, 0), Function('y')(x))    
    #     return [ [ latex("Single solution"),  [ solve ] ] ]