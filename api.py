from flask import Flask, request, jsonify
from sympy import parse_expr, latex
from flask_cors import CORS

from solution.controller import solve
from solution.parsing.parse_sympy import parseSympy

app = Flask(__name__)
CORS(app)

@app.route("/solve", methods = ["POST", "GET"])
def getSolve():
    # Check inputs
    jsonInput = request.get_json()
    if (jsonInput == None) :
        return jsonify({ "status": "error on json" })
    inputString = jsonInput["equation"]
    if (inputString == None) :
        return jsonify({ "status": "error on string" })

    # Call function
    try: 
        solution = solve(inputString)
        latexSolve = latex(solution.args[1])
    except Exception as e:
        return jsonify({ "status": e.args[0] })

    # return value
    return jsonify({ "status": "ok", "solution": "y(x) = " + str(latexSolve) })
    

@app.route("/parse/latex", methods = ["POST", "GET"])
def parseToLatex():
    # Check inputs
    jsonInput = request.get_json()
    if (jsonInput == None) :
        return jsonify({ "status": "error on json" })
    inputString = jsonInput["equation"]
    if (inputString == None) :
        return jsonify({ "status": "error on string" })

    # Call function
    try:
        equation = parseSympy(inputString)
        equationLatex = latex(equation)
    except Exception as e:
        return jsonify({ "status": e.args[0] })
    
    response = jsonify({ "equation": equationLatex + " = 0", "status": "ok" })
    # return value
    return response

if __name__ == "__main__":
    app.run(debug = True, port = 4000)  