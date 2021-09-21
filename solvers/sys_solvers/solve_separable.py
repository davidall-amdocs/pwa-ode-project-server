from anomalies.completeness_anomaly import CompletenessAnomaly
from sympy import * 
from sympy.abc import x 
from sympy.parsing import parse_expr 
from algebraics.operations import *
from integrals.integrator import *

def solveSeparable(odeString, functionName): 

  '''
    ------------------------------------------------------
    # Init solve
    ------------------------------------------------------
  '''
  solveArray = []

  try:
    '''
    ------------------------------------------------------
    # Initial algebraic analysis
    ------------------------------------------------------
    '''
    odeLeftString = odeString.split("=")[0]
    odeRightString = odeString.split("=")[1]
    odeLeftSym = parse_expr(odeLeftString)
    odeRightSym = parse_expr(odeRightString)
    y = Function(functionName)

    equation = Eq(alg_subs(odeLeftSym, odeRightSym), 0)
    left = equation.args[0]
    express = alg_solve(Eq(left, Integer(0)), Derivative(y(x), x))
    aux = alg_simplify(express[0])
    aux = alg_expand(aux)
    aux = alg_factor(aux)

    '''
    ------------------------------------------------------
    # Step 01: Detect separable structure
    ------------------------------------------------------
    '''
    solveArray.append([])
    step = solveArray[0]
    step.append(latex("- Identify the separable equation and its parts") + "\\\\ \\\\")
    step.append([])
    subSteps = step[1]

    functionF = Integer(1)
    functionG = Integer(1)

    # if (((type(aux) is Integer) or (type(aux) is Rational)) or (aux == 1/2)) or (type(aux) is Float):
    #       functionF = aux

    if type(aux) is Add:
      if functionName in str(aux):
        functionG = aux
      else:
        functionF = aux
    else:
      if not (functionName in str(aux)):
        functionF = aux
      else:
        for term in aux.args:
          if functionName in str(term):
            functionG = alg_mul(functionG, term)
          else:
            functionF = alg_mul(functionF, term)

    functionG = alg_mul_inv(functionG)
    expr = alg_div(functionF, functionG)

    h0 = latex("With algebra, transform the expression: ") + "\\\\ \\\\"
    subSteps.append(h0)

    eq0 = "$" + latex(Eq(odeLeftSym, odeRightSym)) + "$" + "\\\\ \\\\"
    subSteps.append(eq0)

    h1 = latex("into the equation: ") + "\\\\ \\\\"
    subSteps.append(h1)

    eq1 = "$" + latex(Derivative(y(x), x)) + " = " + latex(expr) + "$" + "\\\\ \\\\"
    subSteps.append(eq1)
    
    h2 = latex("wich has the form: ") + "\\\\ \\\\"
    subSteps.append(h2)

    eq2 = "$" + latex(Derivative(y(x), x)) + " = " + latex(alg_div(Function('f')(x), \
      Function('g')(Symbol(functionName)))) + "$" + "\\\\ \\\\"
    subSteps.append(eq2)
    
    h3 = latex("where: ") + "\\\\ \\\\"
    subSteps.append(h3)

    eq3 = "$g{\\left("+functionName+"\\right)} = " + latex(functionG) + "$ \\\\ \\\\"
    subSteps.append(eq3)

    eq4 = "$f{\\left(x \\right)} = " + latex(functionF) + "$ \\\\ \\\\"
    subSteps.append(eq4)

    h4 = latex("So, it is 1st order separable") + "\\\\ \\\\"
    subSteps.append(h4)    

    '''
    ------------------------------------------------------
    # Step 02: Separate functions
    ------------------------------------------------------
    '''
    solveArray.append([])
    step = solveArray[1]
    step.append(latex("- Separate functions") + "\\\\ \\\\")
    step.append([])
    subSteps = step[1]

    functionG = alg_substitution(functionG, y(x), Symbol(functionName))
    left = alg_mul(functionG, Symbol('(d'+functionName+')'))
    right = alg_mul(functionF, Symbol('(dx)'))
    
    h0 = latex("Multiply by the differential of x and multiply by ") + \
      "$g{\\left(" + functionName + " \\right)}$" + latex(", so the result is ") + \
      "$g{\\left("+functionName+" \\right)}$" + latex(" and ") + "$f{\\left(x \\right)}$" + \
      latex(" with their respective differentials") + "\\\\ \\\\"
      
    subSteps.append(h0)

    eq0 = "$" + latex(left) + " = " + latex(right)+ "$" + "\\\\ \\\\"
    subSteps.append(eq0)    
    
    '''
    ------------------------------------------------------
    # Step 03: Integrate Left Side
    ------------------------------------------------------
    '''
    solveArray.append([])
    step = solveArray[2]
    step.append(latex("- Solve left") + "\\\\ \\\\")
    step.append([])
    subSteps = step[1]

    left = alg_div(left, Symbol('(d'+functionName+')'))

    h0 = latex("Integrate left side with respect to " + functionName) + "\\\\ \\\\"
    subSteps.append(h0)

    eq0 = "$\int{" +  latex(left) +"} d"+functionName+"$" 
    subSteps.append(eq0 + "\\\\ \\\\")

    left = alg_expand(left)
    left = int_solve(left, Symbol(functionName))

    eq1 = eq0 + " = $" + latex(left) + "$" + "\\\\ \\\\"
    subSteps.append(eq1)    

    '''
    ------------------------------------------------------
    # Step 04: Integrate Right Side
    ------------------------------------------------------
    '''
    right = Mul(right, Pow(Symbol('(dx)'), Integer(-1)))
    exp1s4 = "$\int{" +  latex(right) +"} dx$" 
    right = expand(right, force=True)
    right = int_solve(right, x)

    h1s4 = latex("Integrate right side with respect to x") + "\\\\ \\\\"
    eq1s4 = exp1s4 + " = $" + latex(right) + "$" + "\\\\ \\\\"

    step = []
    step.append(latex("- Solve right") + "\\\\ \\\\")
    subSteps = []
    subSteps.append(h1s4)
    subSteps.append(exp1s4 + "\\\\ \\\\")
    subSteps.append(eq1s4)    
    step.append(subSteps)
    solveArray.append(step)

    '''
    ------------------------------------------------------
    # Step 05: Equate Both Sides
    ------------------------------------------------------
    '''
    express = Add(left, Mul(right, Integer(-1)), Symbol('C'))
    h1s5 = latex("Equate both sides") + "\\\\ \\\\"
    exp1s5 ="$" + latex(left) + " = " + latex(right) + "$" + "\\\\ \\\\"
    h2s5 = latex("Substract right side from both sides and add the arbitrary constant C. " + \
      "The implicit answer is: ") + "\\\\ \\\\"
    eq1s5 = "$" + latex(express) + "$ = 0"+ "\\\\ \\\\"

    step = []
    step.append(latex("- Get implicit solution") + "\\\\ \\\\")
    subSteps = []
    subSteps.append(h1s5)
    subSteps.append(exp1s5)
    subSteps.append(h2s5)
    subSteps.append(eq1s5)    
    step.append(subSteps)
    solveArray.append(step)

    finalSolve = []

    try:
      finalSolve = solve(express, Symbol(functionName))
      step = []
      step.append(latex("- Get the explicit solution solving for " + functionName) + "\\\\ \\\\")
      subSteps = []
      for singleSolve in finalSolve:
        eq1s6 = Eq(y(x), singleSolve)
        subSteps.append("$" + latex(eq1s6) + "$" + "\\\\ \\\\") 
      step.append(subSteps)
      solveArray.append(step)
    except:
      step = []
      step.append(latex("- Can not get the explicit solution solving for " + functionName) + "\\\\ \\\\")
      subSteps = []
      step.append(subSteps)
      solveArray.append(step)

    def display_step(step):
        stepStr = ""
        for subStep in step:
          stepStr += str(subStep)
        return stepStr

    def display_solve():
        solveStr = ""
        for stepAux in solveArray:
          solveStr += stepAux[0]
          solveStr += display_step(stepAux[1])
        return solveStr    
    return [display_solve(), solveArray, finalSolve]

  except CompletenessAnomaly as ca:
    ca.set_partial_solution(solveArray)
    raise ca
