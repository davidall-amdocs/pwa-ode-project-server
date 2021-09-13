from sympy import * 
from sympy.abc import x 
from sympy.parsing import parse_expr 
from sympy.parsing.latex import parse_latex
from anomalies.completeness_anomaly import CompletenessAnomaly

def solveExact(odeString):
  odeLeftString = odeString.split("=")[0]
  odeRightString = odeString.split("=")[1]

  odeLeftSym = parse_expr(odeLeftString)
  odeRightSym = parse_expr(odeRightString)

  # init solve array
  solveArray = [] 

  y = Function('y')
  equation = Eq(odeLeftSym - odeRightSym, 0)
  equation = equation.subs(y(x), Symbol('y'))

  h0 = latex("With algebra, transform the expression: ") + "\\\\ \\\\"
  eq0 = "$" + latex(Eq(odeLeftSym, odeRightSym)) + "$" + "\\\\ \\\\"
  h1 = latex("into the equation: ") + "\\\\ \\\\"
  eq1 = "$" + latex(equation) + "$" + "\\\\ \\\\"

  functionP = Integer(0)
  functionQ = Integer(0)
  functionF = Integer(0)
  leftPartial = Integer(0)
  functionG = Function('g')

  for term in equation.args[0].args:
    if 'Derivative' in str(term):
      functionQ = Add(functionQ, Mul(term, Pow(Derivative(Symbol('y'), x), Integer(-1))))
    else:
      functionP = Add(functionP, term)

  h2 = latex("wich has the form: ") + "\\\\ \\\\"
  eq2 = "$" + latex(Function('P')(Symbol('x,y'))) + " + " + latex( Mul(Function('Q')(Symbol('x,y')), Derivative(y(x),x))) + " = 0" +  "$" + "\\\\ \\\\"
  h3 = latex("where: ") + "\\\\ \\\\"
  eq3 = "$" + latex(Function('Q')(Symbol('x,y'))) + " = " + latex(functionQ) + "$ \\\\ \\\\"
  eq4 = "$" + latex(Function('P')(Symbol('x,y'))) + " = " + latex(functionP) + "$ \\\\ \\\\"
  h4 = latex("So, it is an exact differential equation") + "\\\\ \\\\"

  step = []
  step.append(latex("- Identify the exact equation and its parts") + "\\\\ \\\\")
  subSteps = []
  subSteps.append(h0)
  subSteps.append(eq0)
  subSteps.append(h1)
  subSteps.append(eq1)
  subSteps.append(h2)
  subSteps.append(eq2)
  subSteps.append(h3)
  subSteps.append(eq3)
  subSteps.append(eq4)
  subSteps.append(h4)    
  step.append(subSteps)
  solveArray.append(step)

  #Step 2

  h1s2 = latex("Lets integrate respect x the function ") + "$" + latex(Function('P')(Symbol('x'), Symbol('y'))) + "\\\\ \\\\"
  eqAux = Eq(Function('F')(Symbol('x'), Symbol('y')), Integral(Function('P')(Symbol('x'), Symbol('y')),x))
  eq1s2 = "$" +  latex(eqAux) + "$" + "\\\\ \\\\"
  h2s2 = latex("Substituting ") + "$" + latex(Function('P')(Symbol('x'), Symbol('y'))) + " = " + latex(functionP) + "$" + "\\\\ \\\\"
  eqAux = Eq(Function('F')(Symbol('x'), Symbol('y')), Integral(functionP,x))
  eq2s2 = "$" + latex(eqAux) + "$" + "\\\\ \\\\"
  h3s2 = latex("Integrating: ")  + "\\\\ \\\\"

  functionF = integrate(functionP, x)
  functionF = Add(functionF, functionG(Symbol('y')))
  eqAux = Eq(Function('F')(Symbol('x'), Symbol('y')), functionF)
  eq3s2 = "$" + latex(eqAux) + "$" + "\\\\ \\\\"

  step = []
  step.append(latex("- Obtain F(x,y) as a result of P(x,y) ") + "\\\\ \\\\")
  subSteps = []
  subSteps.append(h1s2)
  subSteps.append(eq1s2)
  subSteps.append(h2s2)
  subSteps.append(eq2s2)
  subSteps.append(h3s2)
  subSteps.append(eq3s2)
  step.append(subSteps)
  solveArray.append(step)

  #Step 3

  partialF = diff(functionF, Symbol('y'))

  h1s3 = latex("To find g(y) differentiate respect y the function ") + "$" + latex(Function('F')(Symbol('y'), Symbol('x'))) +  "$" + "\\\\ \\\\"
  eq1s3 = "$" +  latex(Derivative(Function('F')(Symbol('x'), Symbol('y')), Symbol('y')))  +  " = " + latex(partialF) + "$" + "\\\\ \\\\"
  h2s3 = latex("This by definition of a exact diferential equation must be equal to ") + "$" + latex(Function('Q')(Symbol('x'), Symbol('y'))) + "$" + "\\\\ \\\\"
  h3s3 = latex("Hence equating: ")  + "\\\\ \\\\"

  leftPartial = Add(partialF, Mul(functionQ, Integer(-1)))
  rightGSolveSide = solve(leftPartial, Derivative(functionG(Symbol('y')), Symbol('y')))

  eq2s3 = "$" +  latex(partialF)  +  " = " + latex(functionQ) + "$" + "\\\\ \\\\"
  h4s3 = latex("Solving for: ") + "$" + latex(Derivative(Function('g')(Symbol('y')), Symbol('y'))) +  "$"  + "\\\\ \\\\"
  eq3s3 = "$" +  latex(Derivative(Function('g')(Symbol('y')), Symbol('y')))  +  " = " + latex(rightGSolveSide[0]) + "$" + "\\\\ \\\\"

  step = []
  step.append(latex("- Use the properties of the exact equation to find (y)") + "\\\\ \\\\")
  subSteps = []
  subSteps.append(h1s3)
  subSteps.append(eq1s3)
  subSteps.append(h2s3)
  subSteps.append(h3s3)
  subSteps.append(eq2s3)
  subSteps.append(h4s3) 
  subSteps.append(eq3s3)
  step.append(subSteps)
  solveArray.append(step)

  #Step 4

  gIntValue = integrate(rightGSolveSide[0], Symbol('y'))
  functionF = Add(functionF, Mul(functionG(Symbol('y')), Integer(-1)), gIntValue)
  h1s4 = latex("Integrating both sides to get ") + "$" + latex(Function('g')(Symbol('y'))) +  "$" + "\\\\ \\\\"
  eq1s4 = "$" + latex(Function('g')(Symbol('y'))) +  " = " + latex(Integral(rightGSolveSide[0], Symbol('y'))) + "$" + "\\\\ \\\\"
  eq2s4 = "$" + latex(Function('g')(Symbol('y'))) +  " = " + latex(gIntValue) + "$" + "\\\\ \\\\"
  h2s4 = latex("Substituting this result into F(x,y)") +  "\\\\ \\\\"
  eq3s4 = "$" + latex(Function('F')(Symbol('x,y'))) +  " = " + latex(functionF) + "$" + "\\\\ \\\\"
  functionF = Add(functionF, Symbol('C'))
  h3s4 = latex("Simplifying and using F(x,y) as a constant C, we get: ") + "\\\\ \\\\"
  functionF = simplify(functionF)
  eq4s4 = "$" + latex(Integer(0)) +  " = " + latex(functionF) + "$" + "\\\\ \\\\"

  step = []
  step.append(latex("- Get g(y) and particular F(x,y) ") + "\\\\ \\\\")
  subSteps = []
  subSteps.append(h1s4)
  subSteps.append(eq1s4)
  subSteps.append(eq2s4)
  subSteps.append(h2s4)
  subSteps.append(eq3s4)
  subSteps.append(h3s4)
  subSteps.append(eq4s4)
  step.append(subSteps)
  solveArray.append(step)

  try:
    solveY = solve(functionF, Symbol('y'))
    step = []
    step.append(latex("- Get the explicit solution solving for y") + "\\\\ \\\\")
    subSteps = []
    for singleSolve in solveY:
      eq1s5 = Eq(y(x), singleSolve)
      subSteps.append("$" + latex(eq1s5) + "$" + "\\\\ \\\\") 
    step.append(subSteps)
    solveArray.append(step)
  except:
    step = []
    step.append(latex("- Can not get the explicit solution solving for y") + "\\\\ \\\\")
    subSteps = []
    step.append(subSteps)
    solveArray.append(step)

  def display_step(step):
    stepStr = ""
    for subStep in step:
      stepStr += str(subStep)
    return stepStr

  def display_solve(solveArray):
    solveStr = ""
    for stepAux in solveArray:
      solveStr += stepAux[0]
      solveStr += display_step(stepAux[1])
    return solveStr    
  return [ display_solve(solveArray), solveArray ]