from sympy import * 
from sympy.abc import x 
from sympy.parsing import parse_expr 
from sympy.parsing.latex import parse_latex

def solveSeparable(odeString): 
  odeLeftString = odeString.split("=")[0]
  odeRightString = odeString.split("=")[1]

  odeLeftSym = parse_expr(odeLeftString)
  odeRightSym = parse_expr(odeRightString)

  y = Function('y')
  equation = Eq(odeLeftSym - odeRightSym, 0)

  left = equation.args[0]

  express = solve(Eq(left, Integer(0)), Derivative(y(x), x))
  aux = simplify(express[0])
  aux = aux.expand(force = True)
  aux = factor(aux)

  # Init solve
  solveArray = []

  # Step 1
  functionF = Integer(1)
  functionG = Integer(1)

  # if (((type(aux) is Integer) or (type(aux) is Rational)) or (aux == 1/2)) or (type(aux) is Float):
  #       functionF = aux

  if type(aux) is Add:
    if 'y' in str(aux):
      functionG = aux
    else:
      functionF = aux
  else:
    if not ('y' in str(aux)):
      functionF = aux
    else:
      for term in aux.args:
        if 'y' in str(term):
          functionG = Mul(functionG, term)
        else:
          functionF = Mul(functionF, term)

  functionG = Pow(functionG, Integer(-1))

  expr = Mul(functionF, Pow(functionG, Integer(-1)))

  h0 = latex("With algebra, transform the expression: ") + "\\\\ \\\\"
  eq0 = "$" + latex(Eq(odeLeftSym, odeRightSym)) + "$" + "\\\\ \\\\"
  h1 = latex("into the equation: ") + "\\\\ \\\\"
  eq1 = "$" + latex(Derivative(y(x), x)) + " = " + latex(expr) + "$" + "\\\\ \\\\"
  h2 = latex("wich has the form: ") + "\\\\ \\\\"
  eq2 = "$" + latex(Derivative(y(x), x)) + " = " + latex(Mul(Function('f')(x), Pow(Function('g')(Symbol('y')), Integer(-1)))) + "$" + "\\\\ \\\\"
  h3 = latex("where: ") + "\\\\ \\\\"
  eq3 = "$g{\\left(y \\right)} = " + latex(functionG) + "$ \\\\ \\\\"
  eq4 = "$f{\\left(x \\right)} = " + latex(functionF) + "$ \\\\ \\\\"
  h4 = latex("So, it is 1st order separable") + "\\\\ \\\\"

  step = []
  step.append(latex("- Identify the separable equation and its parts") + "\\\\ \\\\")
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

  # Step 2: Separate functions
  functionG = functionG.subs(y(x), Symbol('y'))
  left = Mul(functionG, Symbol('(dy)'))
  right = Mul(functionF, Symbol('(dx)'))
  h1s2 = latex("Multiply by the differential of x and multiply by ") + "$g{\\left(y \\right)}$" + latex(", so the result is ") + "$g{\\left(y \\right)}$" + latex(" and ") + "$f{\\left(x \\right)}$" + latex(" with their respective differentials") + "\\\\ \\\\"
  eq1s2 = "$" + latex(left) + " = " + latex(right)+ "$" + "\\\\ \\\\"

  step = []
  step.append(latex("- Separate functions") + "\\\\ \\\\")
  subSteps = []
  subSteps.append(h1s2)
  subSteps.append(eq1s2)    
  step.append(subSteps)
  solveArray.append(step)

  # Step 3: Integrate left side
  left = Mul(left, Pow(Symbol('(dy)'), Integer(-1)))
  exp1s3 = "$\int{" +  latex(left) +"} dy$" 
  left = expand(left, force=True)
  left = integrate(left, Symbol('y'))

  h1s3 = latex("Integrate left side with respect to y") + "\\\\ \\\\"
  eq1s3 = exp1s3 + " = $" + latex(left) + "$" + "\\\\ \\\\"

  step = []
  step.append(latex("- Solve left") + "\\\\ \\\\")
  subSteps = []
  subSteps.append(h1s3)
  subSteps.append(exp1s3 + "\\\\ \\\\")
  subSteps.append(eq1s3)    
  step.append(subSteps)
  solveArray.append(step)

  # Step 4: Integrate right side
  right = Mul(right, Pow(Symbol('(dx)'), Integer(-1)))
  exp1s4 = "$\int{" +  latex(right) +"} dx$" 
  right = expand(right, force=True)
  right = integrate(right, x)

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

  # Step 5: Equate both sides
  express = Add(left, Mul(right, Integer(-1)), Symbol('C'))
  h1s5 = latex("Equate both sides") + "\\\\ \\\\"
  exp1s5 ="$" + latex(left) + " = " + latex(right) + "$" + "\\\\ \\\\"
  h2s5 = latex("Substract right side from both sides and add the arbitrary constant C. The implicit answer is: ") + "\\\\ \\\\"
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

  try:
    finalSolve = solve(express, Symbol('y'))
    step = []
    step.append(latex("- Get the explicit solution solving for y") + "\\\\ \\\\")
    subSteps = []
    for singleSolve in finalSolve:
      eq1s6 = Eq(y(x), singleSolve)
      subSteps.append("$" + latex(eq1s6) + "$" + "\\\\ \\\\") 
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

  def display_solve(solve):
      solveStr = ""
      for stepAux in solveArray:
        solveStr += stepAux[0]
        solveStr += display_step(stepAux[1])
      return solveStr    
  return [display_solve(solveArray), solveArray]

def solveLinear(odeString):
  odeLeftString = odeString.split("=")[0]
  odeRightString = odeString.split("=")[1]

  odeLeftSym = parse_expr(odeLeftString)
  odeRightSym = parse_expr(odeRightString)

  y = Function('y')
  equation = Eq(odeLeftSym - odeRightSym, 0)

  # Init solve
  solveArray = []

  left = equation.args[0]
  exp = solve(left, Derivative(y(x), x))
  aux = expand(exp[0])

  left = Derivative(y(x), x)

  functionF = parse_expr("0")
  functionG = parse_expr("0")

  for term in aux.args:
    if "y" in str(term):
      functionF = Add(functionF, Mul(term, Pow(y(x), Integer(-1))))
    else:
      functionG = Add(functionG, term)

  functionF = Mul(functionF, Integer(-1))
  functionF = simplify(functionF)
  functionG = simplify(functionG)

  right = Add(functionG, Mul(Integer(-1), functionF, y(x)))

  # Step 1 Identify the linear equation

  h0 = latex("With algebra, transform the expression: ") + "\\\\ \\\\"
  eq0 = "$" + latex(Eq(odeLeftSym, odeRightSym)) + "$" + "\\\\ \\\\"
  h1 = latex("into the equation: ") + "\\\\ \\\\"
  eq1 = "$" + latex(Derivative(y(x), x)) + " = " + latex(exp) + "$" + "\\\\ \\\\"
  h2 = latex("wich has the form: ") + "\\\\ \\\\"
  eq2 = "$" + latex(Derivative(y(x), x)) + " = " + latex(Add(Function('g')(x), Mul(Function('f')(x), Integer(-1), y(x)))) + "$" + "\\\\ \\\\"
  h3 = latex("where: ") + "\\\\ \\\\"
  eq3 = "$g{\\left(x \\right)} = " + latex(functionG) + "$ \\\\ \\\\"
  eq4 = "$f{\\left(x \\right)} = " + latex(functionF) + "$ \\\\ \\\\"
  h4 = latex("So, it is 1st order linear") + "\\\\ \\\\"

  step = []
  step.append(latex("- Identify the linear equation and its parts") + "\\\\ \\\\")
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

  # Step 2 Calculate integral factor

  h1s2 = latex("Lets propose a function ") + "$" + latex(Function('M')(x)) + "$" + latex(" such that: ") + "\\\\ \\\\"
  eqAux = Eq(Mul(Function('M')(x), Function('f')(x)), Derivative(Function('M')(x), x))
  eq1s2 = "$" +  latex(eqAux) + "$" + "\\\\ \\\\"
  h2s2 = latex("Substituting: ") + "\\\\ \\\\"
  eq2s2 = "$" + latex(Eq(Mul(Function('M')(x), functionF), Derivative(Function('M')(x), x))) + "$" + "\\\\ \\\\"
  h3s2 = latex("Which is a 1st order separable diferential equation. Hence solving for ") + "$" + latex(Function('M')(x)) + "$" + "\\\\ \\\\"
  functionM = Pow(E, Integral(functionF, x))
  eq3s2 = "$" + latex(Eq(Mul(Pow(Function('M')(x), Integer(-1)), Symbol('dM(x)')), Mul(functionF, Symbol('(dx)')))) + "$" + "\\\\ \\\\"
  eq4s2 = "$" + latex(Eq(log(Function('M')(x)), Integral(functionF, x))) + "$" + "\\\\ \\\\"
  functionF = expand(functionF)
  exponentM = integrate(expand(functionF), x)
  eq5s2 = "$" + latex(Eq(log(Function('M')(x)), exponentM)) + "$" + "\\\\ \\\\"
  eq6s2 = "$" + latex(Function('M')(x)) + " = " + latex(Pow(E, exponentM))+ "$" + "\\\\ \\\\"

  functionM = functionM.replace(Integral(functionF, x), exponentM)
  functionM = Pow(E, exponentM)
  functionM = simplify(functionM)

  step = []
  step.append(latex("- Calculate integral factor") + "\\\\ \\\\")
  subSteps = []
  subSteps.append(h1s2)
  subSteps.append(eq1s2)
  subSteps.append(h2s2)
  subSteps.append(eq2s2)
  subSteps.append(h3s2)
  subSteps.append(eq3s2)
  subSteps.append(eq4s2)    
  subSteps.append(eq5s2)    
  subSteps.append(eq6s2)    
  step.append(subSteps)
  solveArray.append(step)

  # Step 3 Reduce to 1st order separable ODE

  h1s3 = latex("Multiplying the original equation by ") + "$" + latex(Function('M')(x)) + "$" + latex(" : ") + "\\\\ \\\\"
  equation = Eq(left, right)
  left = Mul(left, functionM)
  right = Add(Mul(Integer(-1), functionF, y(x), functionM), Mul(functionG, functionM))
  equation = Eq(left, right)

  left = Add(left, Mul(functionF, y(x), functionM))
  right = Add(right, Mul(functionF, y(x), functionM))
  equation = Eq(left, right)
  equationaux = Eq(expand(Mul( Function('M')(x), left, pow(functionM, Integer(-1)))), Mul( Function('M')(x), right, pow(functionM, Integer(-1))))

  eq1s3 = "$" + latex(equationaux ) + "$" + "\\\\ \\\\"
  h2s3 = latex("By the definition of ") + "$" + latex(Function('M')(x)) + "$" + latex(" this is equivalent to: ") +  "\\\\ \\\\"
  eq2s3 = "$" + latex(Add(Mul(Derivative(y(x),x), Function('M')(x)),Mul(y(x), Derivative(Function('M')(x), x)))) + " = " + latex(Mul(functionG, Function('M')(x))) +  "$" + "\\\\ \\\\"
  h3s3 = latex("Notice that the left hand side can be reduce by the chain rule to: ") + "\\\\ \\\\"
  eq3s3 = "$" + latex(Add(Mul(Derivative(y(x),x), Function('M')(x)),Mul(y(x), Derivative(Function('M')(x), x)))) + " = " + latex(Derivative(Mul(y(x), Function('M')(x)),x)) +  "$" + "\\\\ \\\\"
  h4s3 = latex("Therefore: ") + "\\\\ \\\\"
  eq4s3 = "$" + latex(Derivative(Mul(y(x), Function('M')(x)),x)) + " = " + latex(Mul(functionG, Function('M')(x))) +  "$" + "\\\\ \\\\"
  h5s3 = latex("Which again is a 1st order separable diferential equation") + "\\\\ \\\\"
  equationaux = Eq(Symbol('dM(x)y(x)'), factor(Mul(Symbol('(dx)'),functionG, Function('M')(x))))
  eq5s3 = "$" + latex(equationaux)+  "$" + "\\\\ \\\\"

  step = []
  step.append(latex("- Reduce to 1st Order Separable ODE") + "\\\\ \\\\")
  subSteps = []
  subSteps.append(h1s3)
  subSteps.append(eq1s3)
  subSteps.append(h2s3)
  subSteps.append(eq2s3)
  subSteps.append(h3s3)
  subSteps.append(eq3s3)  
  subSteps.append(h4s3)
  subSteps.append(eq4s3)
  subSteps.append(h5s3)   
  subSteps.append(eq5s3)
  step.append(subSteps)
  solveArray.append(step)

  # Step 4 Get implicit solve

  left = Derivative(Mul(functionM, y(x)), x)

  equation = Eq(left, right)
  left = Mul(left, Pow(Derivative(Mul(functionM, y(x)), x), Integer(-1)), Symbol('d'), Mul(y(x), functionM))
  right = Mul(right, Symbol('dx'))
  equation = Eq(left, right)
  h6s3 = latex("Integrating the left hand side, and indicating the integral at right hand side: ") + "\\\\ \\\\"
  left = Mul(y(x), functionM)
  right = Mul(right, Pow(Symbol('dx'), Integer(-1)))
  eq6s3 = "$" + latex(Symbol('M(x)y(x)'))+ " = " + latex(Integral(Mul(Mul(right, Pow(functionM, Integer(-1))),Function('M')(x)),x)) + "$" + "\\\\ \\\\"
  h7s3 = latex("Substituting ") + "$" + latex(Function('M')(x)) + " = " + latex(functionM) +"$" + "\\\\ \\\\"
  equationaux = Eq(left, Integral(right,x))
  eq7s3 = "$" + latex(equationaux)+ "$" + "\\\\ \\\\"
  right = expand(right)
  right = integrate(right, x)
  right = Add(right, Symbol('C'))
  equation = Eq(left, right)
  h8s3 = latex("Integrating the right hand side: ") + "\\\\ \\\\"
  eq8s3 = "$" + latex(equation)+ "$" + "\\\\ \\\\"

  step = []
  step.append(latex("- Get implicit solution") + "\\\\ \\\\")
  subSteps = []
  subSteps.append(h6s3)   
  subSteps.append(eq6s3)
  subSteps.append(h7s3) 
  subSteps.append(eq7s3)
  subSteps.append(h8s3) 
  subSteps.append(eq8s3)
  step.append(subSteps)
  solveArray.append(step)

  # Step 5 Solve for y

  left = y(x)
  right = Mul(right, Pow(functionM, Integer(-1)))
  right = simplify(right)
  equation = Eq(left, right)
  h9s3 = latex("Solve for ") + latex(Symbol('y(x)')) + "\\\\ \\\\"
  eq9s3 = "$" + latex(equation)+ "$" + "\\\\ \\\\"

  step = []
  step.append(latex("- Solve for y") + "\\\\ \\\\")
  subSteps = []
  subSteps.append(h9s3) 
  subSteps.append(eq9s3)
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
  return [display_solve(solveArray), solveArray]

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

