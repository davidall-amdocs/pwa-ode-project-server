# PWA for ODE (Server side)
Processing of the equations requested by the user in the [client](https://github.com/buronsuave/pwa-ode-project-client) by means of the parsing of strings and the handling of symbolic expressions with SymPy. The algorithms described for the solution of each type of differential equation as well as its corresponding classification were developed by the original authors of the project: [David López](https://github.com/buronsuave), [Andrés Huerta](https://github.com/AndresHv07) and [Daniel Tejeda](https://github.com/FGauss)

```python
def classify(odeString):    
    # Check if the equation is separable
    try:
        if checkSeparable(odeString, "y"):
            return "separable"
    except:
        print("Non Separable")
    # Check if the equation is 1st order linear
    try:
        if checkLinear(odeString, "y"):
            return "linear"
    except:
        print("Non Linear")
    # ...
```
