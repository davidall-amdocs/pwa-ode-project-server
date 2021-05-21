from sympy import *
from sympy.abc import x
from flask import jsonify
from sympy.parsing.sympy_parser import parse_expr

from parse_sympy import parseLatex
from solve import solveSeparable
from solve import solveLinear
from solve import solveExact
from classificator import classify


def solve(inputString):
    try:
        equation = parseLatex(inputString)
        print(equation)
    except Exception as e:
        raise e

    odeType = classify(str(equation) + "= 0")
    print(odeType)

    if odeType == "separable":
        solveArray = solveSeparable(str(equation) + "= 0")
        return solveArray[1]
    elif odeType == "linear":
        solveArray = solveLinear(str(equation) + "= 0")
        return solveArray[1]
    elif odeType == "exact":
        solveArray = solveExact(str(equation) + "= 0")
        return solveArray[1]
    else:
        solveSingle = dsolve(Eq(equation, 0), Function('y')(x))
        return [[latex("- Solve by DSolve: ") + "\\\\ \\\\", [latex(solveSingle) + "\\\\ \\\\"]]]
