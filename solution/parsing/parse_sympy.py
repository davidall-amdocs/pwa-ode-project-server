from sympy import parse_expr

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