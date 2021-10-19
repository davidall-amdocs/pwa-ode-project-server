from anomalies.classification_anomaly import ClassificationAnomaly
from anomalies.completeness_anomaly import CompletenessAnomaly
from flask import Flask, request, jsonify, after_this_request
from flask_cors import CORS

from sympy import parse_expr, latex
from compiler.textopdf import text_to_pdf

from solvers.controller import solve
from parsers.parse_sympy import parseSympy, parseLatex
from vision.text_detection import detectText

app = Flask(__name__)
CORS(app)

@app.route("/solve", methods = ["POST", "GET"])
def getSolve():
    # Check inputs
    jsonInput = request.get_json()  
    if (jsonInput == None) :
        return jsonify({ "status": "error on json" })

    inputString = jsonInput["equation"]
    user_type = jsonInput["type"]

    if (inputString == None or user_type == None) :
        return jsonify({ "status": "error on string" })

    try: 
        solution = solve(inputString, user_type)
        # No anomaly in solve call
        return jsonify({ "status": "ok", "solution": str(solution)})

    # Classification error in solve call
    except ClassificationAnomaly as clsa:
        return jsonify({ "exception": "classification", "status": clsa.args[0], "solution": str(clsa.final_solve) })

    # Completeness error in solve call
    except CompletenessAnomaly as ca:
        return jsonify({ "exception": "completeness", "status": ca.args[0], "solution": str(ca.partial_solution) })

    # Unexpected error during execution of solve method
    except Exception as e:
        return jsonify({ "exception": "generic", "status": e.args[0] })

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

@app.route("/image/text", methods = ["POST"])
def getTextFromImage():

    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    # Check inputs
    jsonInput = request.get_json()
    if (jsonInput == None):
        return jsonify({ "status": "error on json" })
    inputString = jsonInput["image"]
    if (inputString == None):
        return jsonify({ "status": "error on string" })
    
    # Call function
    try:
        text = detectText(inputString)
    except Exception as e:
        print(e.args[0])
        return jsonify({ "status": e.args[0] })
    
    response = jsonify({ "text": text , "status": "ok" })
    return response

@app.route("/pdf", methods = ["POST"])
def getPDFFromLatex():
    # Check inputs
    jsonInput = request.get_json()
    if (jsonInput == None):
        return jsonify({ "status": "error on json" })
    inputString = jsonInput["latex"]
    if (inputString == None):
        return jsonify({ "status": "error on string" })
    
    # Call function
    try:
        text = text_to_pdf(inputString)
    except Exception as e:
        print(e)
        return jsonify({ "status": e.args[0] })
    
    response = jsonify({ "text": text , "status": "ok" })
    return response

if __name__ == "__main__":
    app.run(debug = True, port = 4000, host='26.142.66.43')  