from sympy import dsolve, Function 
from sympy.abc import x
from flask import jsonify

from parsing.parse_sympy import parseSympy

def solve(inputString):
    try:
        equation = parseSympy(inputString)
    except Exception as e:
        raise e

    y = Function("y")   
    solve = dsolve(equation, y(x))
    return solve