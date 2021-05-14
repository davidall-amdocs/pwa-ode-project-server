from sympy import parse_expr
from sympy.parsing.latex import parse_latex

def parseSympy(inputString):
    inputString = inputString.replace("D", "Derivative")    
    inputString = inputString.replace("^", "**")
    inputString = inputString.replace("y", "y(x)")

    therms = inputString.split("=")
    if (len(therms) != 2):
        raise Exception("Invalid equation. Must be exactly one equal sign (=)")

    leftString = inputString.split("=")[0]
    rightString = inputString.split("=")[1]
    leftSymbol = parse_expr(leftString)
    rightSymbol = parse_expr(rightString)
    return leftSymbol - rightSymbol

def parseLatex(inputString):
    inputString = inputString.replace("\\\\", "\\")
    inputString = inputString.replace("y{\\left(x \\right)}", "{\\left(M \\right)}")

    print(inputString)

    therms = inputString.split("=")
    if (len(therms) != 2):
        raise Exception("Invalid equation. Must be exactly one equal sign (=)")

    leftString = inputString.split("=")[0]
    
    leftSymbol = parse_latex(leftString)
    print(str(leftSymbol))
    leftSymbolStr = str(leftSymbol)
    leftSymbolStr = leftSymbolStr.replace("M", "y(x)")
    leftSymbol = parse_expr(leftSymbolStr)

    return leftSymbol