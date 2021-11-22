# PWA for ODE (Server side)
Processing of the equations requested by the user in the [client](https://github.com/buronsuave/pwa-ode-project-client) by means of the parsing of strings and the handling of symbolic expressions with SymPy. The algorithms described for the solution of each type of differential equation as well as its corresponding classification were developed by the original authors of the project: [David López](https://github.com/buronsuave), [Andrés Huerta](https://github.com/AndresHv07) and [Daniel Tejeda](https://github.com/FGauss)

```pyhton
def solve(inputString, user_type):
    # Parse Latex expression 
    try:
        equation = parseLatex(inputString)
    except Exception as e:
        raise e

    # Trying to catch a completeness anomaly 
    try:
        # Classify ODE. Could raise a Classification Anomaly
        odeType = classify(str(equation) + "= 0")
        if odeType == "seperable":
            # Solver serable is called
        elif odeType == "exact":
            # Solver exact is called
        # ...
```
