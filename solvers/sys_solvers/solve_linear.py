from sympy import * 
from sympy.abc import x 
from sympy.parsing import parse_expr 
from sympy.parsing.latex import parse_latex

def solveLinear(odeString, functionName):
  odeLeftString = odeString.split("=")[0]
  odeRightString = odeString.split("=")[1]

  odeLeftSym = parse_expr(odeLeftString)
  odeRightSym = parse_expr(odeRightString)

  y = Function(functionName)
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
    if functionName in str(term):
      functionF = Add(functionF, Mul(term, Pow(y(x), Integer(-1))))
    else:
      functionG = Add(functionG, term)

  functionF = Mul(functionF, Integer(-1))
  functionF = simplify(functionF)
  functionG = simplify(functionG)

  right = Add(functionG, Mul(Integer(-1), functionF, y(x)))

  # Step 1 Identify the linear equation

  h0 = "With algebra, transform the expression: " + "\\\\ \\\\"
  eq0 = "$" + latex(Eq(odeLeftSym, odeRightSym)) + "$" + "\\\\ \\\\"
  h1 = "into the equation: " + "\\\\ \\\\"
  eq1 = "$" + latex(Derivative(y(x), x)) + " = " + latex(exp) + "$" + "\\\\ \\\\"
  h2 = "wich has the form: " + "\\\\ \\\\"
  eq2 = "$" + latex(Derivative(y(x), x)) + " = " + latex(Add(Function('g')(x), Mul(Function('f')(x), Integer(-1), y(x)))) + "$" + "\\\\ \\\\"
  h3 = "where: " + "\\\\ \\\\"
  eq3 = "$g{\\left(x \\right)} = " + latex(functionG) + "$ \\\\ \\\\"
  eq4 = "$f{\\left(x \\right)} = " + latex(functionF) + "$ \\\\ \\\\"
  h4 = "So, it is 1st order linear" + "\\\\ \\\\"

  step = []
  step.append("- Identify the linear equation and its parts" + "\\\\ \\\\")
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

  h1s2 = "Lets propose a function M(x) such that: " + "\\\\ \\\\"
  eqAux = Eq(Mul(Function('M')(x), Function('f')(x)), Derivative(Function('M')(x), x))
  eq1s2 = "$" +  latex(eqAux) + "$" + "\\\\ \\\\"
  h2s2 = "Substituting: " + "\\\\ \\\\"
  eq2s2 = "$" + latex(Eq(Mul(Function('M')(x), functionF), Derivative(Function('M')(x), x))) + "$" + "\\\\ \\\\"
  h3s2 = "Which is a 1st order separable diferential equation. Hence solving for M(x)" + "\\\\ \\\\"
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
  step.append("- Calculate integral factor" + "\\\\ \\\\")
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

  h1s3 = "Multiplying the original equation by M(x):" + "\\\\ \\\\"
  equation = Eq(left, right)
  left = Mul(left, functionM)
  right = Add(Mul(Integer(-1), functionF, y(x), functionM), Mul(functionG, functionM))
  equation = Eq(left, right)

  left = Add(left, Mul(functionF, y(x), functionM))
  right = Add(right, Mul(functionF, y(x), functionM))
  equation = Eq(left, right)
  equationaux = Eq(expand(Mul( Function('M')(x), left, pow(functionM, Integer(-1)))), Mul( Function('M')(x), right, pow(functionM, Integer(-1))))

  eq1s3 = "$" + latex(equationaux) + "$" + "\\\\ \\\\"
  h2s3 = "By the definition of M(x) this is equivalent to: " +  "\\\\ \\\\"
  eq2s3 = "$" + latex(Add(Mul(Derivative(y(x),x), Function('M')(x)),Mul(y(x), Derivative(Function('M')(x), x)))) + " = " + latex(Mul(functionG, Function('M')(x))) +  "$" + "\\\\ \\\\"
  h3s3 = "Notice that the left hand side can be reduce by the chain rule to: " + "\\\\ \\\\"
  eq3s3 = "$" + latex(Add(Mul(Derivative(y(x),x), Function('M')(x)),Mul(y(x), Derivative(Function('M')(x), x)))) + " = " + latex(Derivative(Mul(y(x), Function('M')(x)),x)) +  "$" + "\\\\ \\\\"
  h4s3 = "Therefore: " + "\\\\ \\\\"
  eq4s3 = "$" + latex(Derivative(Mul(y(x), Function('M')(x)),x)) + " = " + latex(Mul(functionG, Function('M')(x))) +  "$" + "\\\\ \\\\"
  h5s3 = "Which again is a 1st order separable diferential equation" + "\\\\ \\\\"
  equationaux = Eq(Symbol('dM(x)'+functionName+'(x)'), factor(Mul(Symbol('(dx)'),functionG, Function('M')(x))))
  eq5s3 = "$" + latex(equationaux)+  "$" + "\\\\ \\\\"

  step = []
  step.append("- Reduce to 1st Order Separable ODE" + "\\\\ \\\\")
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
  h6s3 = "Integrating the left hand side, and indicating the integral at right hand side: " + "\\\\ \\\\"
  left = Mul(y(x), functionM)
  right = Mul(right, Pow(Symbol('dx'), Integer(-1)))
  eq6s3 = "$" + latex(Symbol('M(x)'+functionName+'(x)'))+ " = " + latex(Integral(Mul(Mul(right, Pow(functionM, Integer(-1))),Function('M')(x)),x)) + "$" + "\\\\ \\\\"
  h7s3 = "Substituting M(x) = " + "\\\\ \\\\"
  eqAux1 = "$" + latex(functionM) + "$" +  "\\\\ \\\\"
  equationaux = Eq(left, Integral(right,x))
  eq7s3 = "$" + latex(equationaux)+ "$" + "\\\\ \\\\"
  right = expand(right)
  right = integrate(right, x)
  right = Add(right, Symbol('C'))
  equation = Eq(left, right)
  h8s3 = "Integrating the right hand side: " + "\\\\ \\\\"
  eq8s3 = "$" + latex(equation)+ "$" + "\\\\ \\\\"

  step = []
  step.append("- Get implicit solution" + "\\\\ \\\\")
  subSteps = []
  subSteps.append(h6s3)   
  subSteps.append(eq6s3)
  subSteps.append(h7s3)
  subSteps.append(eqAux1) 
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
  h9s3 = "Solve for " + "\\\\ \\\\"
  eqAux = latex(Symbol(functionName+'(x)')) + + "\\\\ \\\\"
  eq9s3 = "$" + latex(equation)+ "$" + "\\\\ \\\\"

  step = []
  step.append("- Solve for " + functionName + "\\\\ \\\\")
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