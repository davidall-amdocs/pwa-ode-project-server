from timers.custom_threads import PropagatingThread
from sympy import *
from algebraics.operations import *
from utils.constant import \
ATOMIC_INTEGRAL_DIFFICULTY, \
RECURSIVE_INTEGRAL_DIFFICULTY, \
MAX_GLOBAL_DIFFICULTY, \
MAX_INTEGRAL_LEVEL, \
MAX_NODE_DIFFICULTY, \
SYMPY_INTEGRAL

import solvers.controller as controller
import integrals.atomic_integrals as atm
import integrals.recursive_integrals as rec

def int_atm_solve(expression, differential):
    # Variables of global scope in integrator module
    global variables
    variables = [
        {"symbol": Symbol('n'), "value": None}, 
        {"symbol": Symbol('a'), "value": None}, 
        {"symbol": Symbol('b'), "value": None}, 
        {"symbol": Symbol('c'), "value": None}
    ]

    # Create list of atm integrals using the appropriate differential
    atm.build_integrals(differential)

    # Factor expression for atm integral checking
    expression = alg_factor(expression)
    differential_expression = Mul(expression, Symbol('d'+str(differential)))

    # Iterate all along the list of atomic integrals and use the match function to 
    # verify for a possible match
    index = 0
    for integral in atm.BASIC:
        if match_integral(differential_expression, integral):
            int_solution = atm.SOLVE[index]

            # Replace variables in integral solution
            for variable in variables:
                if srepr(variable['symbol']) in srepr(atm.SOLVE[index]):
                    int_solution = int_solution.subs(variable['symbol'], variable['value'])    

            # Return symbolic expression and difficulty
            return {"symbol": int_solution, "difficulty": ATOMIC_INTEGRAL_DIFFICULTY}

        index = index + 1

    # If there's no match, then retun None
    return None

def int_rec_solve(expression, differential):

    # Variables of global scope in integrator module
    global variables
    variables = [
        {"symbol": Symbol('n'), "value": None}, 
        {"symbol": Symbol('a'), "value": None}, 
        {"symbol": Symbol('b'), "value": None}, 
        {"symbol": Symbol('c'), "value": None}
    ]

    # Create list of atm integrals using the appropriate differential
    rec.build_integrals(differential)

    # Factor expression for atm integral checking
    expression = alg_factor(expression)
    differential_expression = Mul(expression, Symbol('d'+str(differential)))

    # Iterate all along the list of atomic integrals and use the match function to 
    # verify for a possible match
    index = 0
    for integral in rec.RECURSIVE:
        if match_integral(differential_expression, integral):
            int_partial_solution = rec.PARTIAL_SOLVE[index]
            int_new_int = rec.NEW_INTEGRAL[index]

            # Replace variables in integral solution
            for variable in variables:
                if srepr(variable['symbol']) in srepr(rec.PARTIAL_SOLVE[index]):
                    int_partial_solution = int_partial_solution.subs(variable['symbol'], variable['value'])
                    int_new_int = int_new_int.subs(variable['symbol'], variable['value'])

            # Return symbolic expression and difficulty
            return {"partial_symbol": int_partial_solution, "new_int_symbol": int_new_int, "difficulty": RECURSIVE_INTEGRAL_DIFFICULTY}

        index = index + 1

    # If there's no match, then retun None
    return None

def integrate_timeout(exp, dif):
    global aux_int_sympy
    aux_int_sympy = integrate(exp, dif)

def tree_solve(expression, differential, level):
    global integral_solve_array
    global aux_int_sympy

    # Check level limit. If is too deep, then use integrate from sympy
    if level >= MAX_INTEGRAL_LEVEL:
        try:
            process = PropagatingThread(target=integrate_timeout, args=(expression, differential))
            process.start()
            process.join(timeout=10)
            # aux_int_sympy = integrate(expression, differential)

            integral_solve_array.append({"left": expression, 
            "right": aux_int, 
            "level": level, 
            "difficulty": SYMPY_INTEGRAL, 
            "type": "SymPy Integral",
            "symbol": "$\int{" + latex(expression) + "} d" + str(differential) + " = "+ latex(aux_int_sympy) +"$", 
            "text": latex("Using DSolve (backup system): ")})

            return {"symbol": aux_int, "difficulty": SYMPY_INTEGRAL}
        except:
            raise CompletenessAnomaly([["", []]])

    # Check if the expression is a number
    if expression.is_number:
        atomic_int = int_atm_solve(Integer(1), differential)
        right_side = alg_mul(expression, atomic_int["symbol"])

        integral_solve_array.append({"left": expression, 
        "right": right_side, 
        "level": level, 
        "difficulty": atomic_int["difficulty"], 
        "type": "Constant integral k", 
        "symbol": "$\int{" + latex(expression) + "} d" + str(differential) + "=" +
            latex(right_side) +"$", 
        "text": latex("It is known that the solution is: ")})

        return {"symbol": right_side, "difficulty": atomic_int["difficulty"] }

    # Check if the expression has the form k*f(x) with
    # k a constant number. Try to solve the new integral
    if type(expression) is Mul and expression.args[0].is_number:
        try:
            new_int = alg_div(expression, expression.args[0])
            prev_expression = "$\int{" + latex(expression) + "} d" + str(differential) + "=" + latex(expression.args[0]) + "\int{" + latex(new_int) + "} d" + str(differential) +"$"

            integral_solve_array.append({"left": Integer(0), 
            "right": Integer(0), 
            "level": level, 
            "difficulty": 0, 
            "type": "Symbol", 
            "symbol": prev_expression, 
            "text": latex("Taking the constant ") + "$" + latex(expression.args[0]) + "$" + latex(" out of the integral: ")})

            aux_int = tree_solve(new_int, differential, level+1)
            integral_solve_array.append({"left": expression, 
            "right": aux_int["symbol"], 
            "level": level, 
            "difficulty": aux_int["difficulty"], 
            "type": "Constant integral kf(x)", 
            "symbol": "$\int{" + latex(expression) + "} d" + str(differential) + "=" +
            latex(Mul(aux_int["symbol"], expression.args[0]))+"$", 
            "text": latex("Multiplying back the constant ") + "$" + latex(expression.args[0]) + "$" + latex(" we have: ")})

            return { "symbol": alg_mul(expression.args[0], aux_int["symbol"]), 
            "difficulty": aux_int["difficulty"] }
        
        except CompletenessAnomaly as ca:
            raise ca

    # Check if the expression is atomic
    atomic_int = int_atm_solve(expression, differential)
    if atomic_int is not None:
        integral_solve_array.append({"left": expression, 
        "right": atomic_int["symbol"], 
        "level": level, 
        "difficulty": atomic_int["difficulty"], 
        "type": "Atomic", 
        "symbol": "$\int{" + latex(expression) + "} d" + str(differential) + "=" +
            latex(atomic_int["symbol"]) + "$", 
        "text": latex("It is known that the solution is: ")})

        return atomic_int

    node_difficulty = 0

    # Check if the expression is recursive one to one
    # (from the list)
    recursive_int = int_rec_solve(expression, differential)
    if recursive_int is not None:
        node_difficulty = recursive_int["difficulty"]
        try:
            prev_expression = "$\int{" + latex(expression) + "} d" + str(differential) + "=" + latex(recursive_int["partial_symbol"]) + "+" + "\int{" + latex(recursive_int["new_int_symbol"].subs(Symbol('d' + str(differential)), 1)) + "} d" + str(differential) + "$"

            integral_solve_array.append({"left": Integer(0), 
            "right": Integer(0), 
            "level": level, 
            "difficulty": 0, 
            "type": "Symbol", 
            "symbol": prev_expression, 
            "text": latex("Using integration by parts, we rewrite the integral: ")})

            solution_new_int = tree_solve(recursive_int["new_int_symbol"].subs(Symbol('d' + str(differential)), 1), differential, level+1)
            node_difficulty = node_difficulty + solution_new_int["difficulty"]
            if node_difficulty >= MAX_NODE_DIFFICULTY:
                raise CompletenessAnomaly([["", []]])

            right_side = alg_add(recursive_int["partial_symbol"], solution_new_int["symbol"])
            integral_solve_array.append({"left": expression, 
            "right": right_side, 
            "level": level, 
            "difficulty": node_difficulty, 
            "type": "Recursive (list)", 
            "symbol": "$\int{" + latex(expression) + "} d" + str(differential) + "=" +
                latex(right_side) +"$", 
            "text": latex("Adding with the additional part of integration by parts: ")})

            return { "symbol": right_side, "difficulty": node_difficulty }
        except CompletenessAnomaly as ca:
            raise ca

    # Expand expression to do the addition distribution and try to solve each
    # sub integral
    expression = alg_expand(expression)
    int_solution = Integer(0)
    if type(expression) is Add:
        prev_expression = "$\int{" + latex(expression) + "} d" + str(differential) + "="
        for item in expression.args:
            partial_symbol = "\int{" + latex(item) + "} d" + str(differential) + "+"
            prev_expression = prev_expression + partial_symbol
        prev_expression = prev_expression[:-1]
        prev_expression = prev_expression + "$"
        integral_solve_array.append({"left": Integer(0), 
        "right": Integer(0), 
        "level": level, 
        "difficulty": 0, 
        "type": "Symbol", 
        "symbol": prev_expression, 
        "text": latex("We separate the integral into sums of integrals and solve each of them: ")})

        for item in expression.args:
            try:
                aux_int = tree_solve(item, differential, level+1)
                int_solution = alg_add(int_solution, aux_int["symbol"])
                node_difficulty = node_difficulty + aux_int["difficulty"]
                if node_difficulty >= MAX_NODE_DIFFICULTY:
                    raise CompletenessAnomaly([["", []]])
            
            except CompletenessAnomaly as ca:
                raise ca

    if int_solution != Integer(0):
        integral_solve_array.append({"left": expression, 
        "right": int_solution, 
        "level": level, 
        "difficulty": node_difficulty, 
        "type": "Addition of integrals", 
        "symbol": "$\int{" + latex(expression) + "} d" + str(differential) + "=" +
            latex(int_solution) +"$", 
        "text": latex("Adding the results of the integrals: ")
            })

        return {"symbol": int_solution, "difficulty": node_difficulty}

def int_solve(expression, differential):
    global integral_solve_array
    global aux_int_sympy

    integral_solve_array = []

    try:
        solution = tree_solve(expression, differential, 0)
        controller.global_difficulty = controller.global_difficulty + solution["difficulty"]
        if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
            raise CompletenessAnomaly([["", []]])
        print_solution()
        return {"solution": solution["symbol"], "steps": integral_solve_array}

    except CompletenessAnomaly:
        controller.global_difficulty = controller.global_difficulty + MAX_NODE_DIFFICULTY
        if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
            raise CompletenessAnomaly([["", []]])
        try:
            print("I'm here")

            process = PropagatingThread(target=integrate_timeout, args=(expression, differential))
            process.start()
            process.join(timeout = 10)

            print("Integral solved with sympy")
            print()
            print_solution()

            integral_solve_array.append({"left": expression, 
            "right": aux_int_sympy, 
            "level": 0, 
            "difficulty": SYMPY_INTEGRAL, 
            "type": "SymPy Integral",
            "symbol": "$\int{" + latex(expression) + "} d" + str(differential) + " = "+ latex(aux_int_sympy) +"$", 
            "text": latex("Using DSolve (backup system): ")})
            return {"solution": aux_int_sympy, "steps": integral_solve_array}
        except Exception as e:
            print(e)
            raise CompletenessAnomaly([["partial integral", integral_solve_array]])

def match_integral(expression, integral):
    if integral == expression:
        return True

    global variables
    for variable in variables:
        if integral == variable['symbol']:
            if expression.is_number:
                if variable['value'] is None:
                    variable['value'] = expression
                    return True
                else:
                    return variable['value'] == expression
            else:
                return False

    if type(expression) is type(integral):
        item_index = 0
        for item in integral.args:
            try:
                if match_integral(expression.args[item_index], item):
                    item_index = item_index + 1
                else:
                    return False
            except:
                return False
        return len(integral.args) == len(expression.args)
    else:
        return False

def print_solution():
    global integral_solve_array
    for step in integral_solve_array:
        print("Left: " + str(step["left"]))
        print("Right: " + str(step["right"]))
        print("Level: " + str(step["level"]))
        print("Difficulty: " + str(step["difficulty"]))
        print("Type: " + step["type"])
        print()
        
