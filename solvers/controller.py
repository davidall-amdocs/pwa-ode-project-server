from sympy import *
from sympy.abc import x
from flask import jsonify
from sympy.parsing.sympy_parser import parse_expr

from parsers.parse_sympy import parseLatex
from solvers.sys_solvers.solve_separable import solveSeparable
from solvers.sys_solvers.solve_linear import solveLinear
from solvers.sys_solvers.solve_homogeneous import solveHomogeneous
from solvers.sys_solvers.solve_exact import solveExact
from solvers.sys_solvers.solve_reducible_linear import solveReducibleToLinear
from classficators.classificator import classify

def solve(inputString):
    try:
        print(inputString)
        equation = parseLatex(inputString)
        print(equation)
    except Exception as e:
        raise e

    odeType = classify(str(equation) + "= 0")
    print(odeType)

    if odeType == "separable":
        solveArray = solveSeparable(str(equation) + "= 0", 'y')
        return solveArray[1]
    elif odeType == "linear":
        solveArray = solveLinear(str(equation) + "= 0", 'y')
        return solveArray[1]
    elif odeType == "reducible":
        solveArray = solveReducibleToLinear(str(equation) + "= 0")
        return solveArray[1]
    elif odeType == "homogeneous":
        solveArray = solveHomogeneous(str(equation) + "= 0")
        return solveArray[1]
    elif odeType == "exact":
        solveArray = solveExact(str(equation) + "= 0")
        return solveArray[1]
    else:
        solveSingle = dsolve(Eq(equation, 0), Function('y')(x))
        return [[latex("- Solve by DSolve: ") + "\\\\ \\\\", [latex(solveSingle) + "\\\\ \\\\"]]]
