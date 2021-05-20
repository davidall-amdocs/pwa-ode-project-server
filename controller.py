from sympy import dsolve, Function 
from sympy.abc import x
from flask import jsonify
from sympy.parsing.sympy_parser import parse_expr

from parse_sympy import parseLatex
from solve import solveLinear

def solve(inputString):
    try:
        equation = parseLatex(inputString)
    except Exception as e:
        raise e

    solve = solveLinear(str(equation) + "= 0")
    return solve[1]