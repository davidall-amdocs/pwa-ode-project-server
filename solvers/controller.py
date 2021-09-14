from anomalies.classification_anomaly import ClassificationAnomaly
from anomalies.completeness_anomaly import CompletenessAnomaly
from sympy import *
from sympy.abc import x

from parsers.parse_sympy import parseLatex
from solvers.sys_solvers.solve_separable import solveSeparable
from solvers.sys_solvers.solve_linear import solveLinear
from solvers.sys_solvers.solve_homogeneous import solveHomogeneous
from solvers.sys_solvers.solve_exact import solveExact
from solvers.sys_solvers.solve_reducible_linear import solveReducibleToLinear
from classficators.classificator import classify

def solve(inputString):
    # Parse Latex expression 
    try:
        print(inputString)
        equation = parseLatex(inputString)
        print(equation)
    except Exception as e:
        raise e

    # Trying to catch a completeness anomaly 
    try:
        # Classify ODE. Could raise a Classification Anomaly
        odeType = classify(str(equation) + "= 0")
        print(odeType)

        # Global difficulty 
        global global_difficulty
        global_difficulty = 0

        if odeType == "separable":
            solveArray = solveSeparable(str(equation) + "= 0", 'y')
            print("Global Difficulty: " + str(global_difficulty))
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
            # Launch DSolve intervention for solving an undefined ODE type 
            solveSingle = dsolve(Eq(equation, 0), Function('y')(x))
            return [[latex("- Solve by DSolve: ") + "\\\\ \\\\", [latex(solveSingle) + "\\\\ \\\\"]]]

    # Classification error on classify call
    except ClassificationAnomaly as clsa:
        print("undefined classification")
        raise clsa

    # Completeness error on some solve call
    except CompletenessAnomaly as ca:
        print("unsolvable")
        raise ca