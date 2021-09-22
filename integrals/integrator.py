from utils.constant import ATOMIC_INTEGRAL_DIFFICULTY, MAX_GLOBAL_DIFFICULTY, MAX_INTEGRAL_LEVEL, MAX_NODE_DIFFICULTY, SYMPY_INTEGRAL
from sympy import *
from algebraics.operations import *

import solvers.controller as controller
import integrals.atomic_integrals as atm

def int_atm_solve(expression, differential):
    '''
    # Params
    * expression (symbolic expression)
    * differential (symbolic expression)

    # Return (symblic expression)
    * integrate of the expression with respect the differential. 
    Uses local and global difficulty control
    '''

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

def tree_solve(expression, differential, level):

    # Check level limit. If is too deep, then use integrate from sympy
    if level >= MAX_INTEGRAL_LEVEL:
        try:
            print("Expression: " + str(expression))
            print("Level: " + str(level))
            print("Difficulty: " + str(SYMPY_INTEGRAL))
            print()
            return {"symbol": integrate(expression, differential), "difficulty": SYMPY_INTEGRAL}
        except:
            raise CompletenessAnomaly([["", []]])

    # Check if the expression is a number
    if expression.is_number:
        atomic_int = int_atm_solve(Integer(1), differential)
        print("Expression: " + str(expression))
        print("Level: " + str(level))
        print("Difficulty: " + str(atomic_int["difficulty"]))
        print()
        return {"symbol": alg_mul(expression, atomic_int["symbol"]), 
        "difficulty": atomic_int["difficulty"] }

    # Check if the expression is atomic
    atomic_int = int_atm_solve(expression, differential)
    if atomic_int is not None:
        print("Expression: " + str(expression))
        print("Level: " + str(level))
        print("Difficulty: " + str(atomic_int["difficulty"]))
        print()
        return atomic_int

    # Check if the expression has the form k*f(x) with
    # k a constant number. Try to solve the new integral
    if type(expression) is Mul and expression.args[0].is_number:
        try:
            aux_int = tree_solve(expression.args[1], differential, level+1)
            print("Expression: " + str(expression))
            print("Level: " + str(level))
            print("Difficulty: " + str(aux_int["difficulty"]))
            print()
            return { "symbol": alg_mul(expression.args[0], aux_int["symbol"]), 
            "difficulty": aux_int["difficulty"] }
        
        except CompletenessAnomaly as ca:
            raise ca
    
    node_difficulty = 0

    # Expand expression to do the addition distribution and try to solve each
    # sub integral
    expression = alg_expand(expression)
    int_solution = Integer(0)
    if type(expression) is Add:
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
        print("Expression: " + str(expression))
        print("Level: " + str(level))
        print("Difficulty: " + str(node_difficulty))
        print()
        return {"symbol": int_solution, "difficulty": node_difficulty}

def int_solve(expression, differential):
    '''
    # Params
    * expression (symbolic expression)
    * differential (symbolic expression)

    # Return (symblic expression)
    * integrate of the expression with respect the differential. 
    Uses branch and global difficulty control
    '''

    try:
        solution = tree_solve(expression, differential, 0)
        controller.global_difficulty = controller.global_difficulty + solution["difficulty"]
        if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
            raise CompletenessAnomaly([["", []]])
        return solution["symbol"]

    except CompletenessAnomaly:
        print("Integral solved with sympy")
        print()
        controller.global_difficulty = controller.global_difficulty + MAX_NODE_DIFFICULTY

        if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
            raise CompletenessAnomaly([["", []]])
        return integrate(expression, differential)

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
        return True
    else:
        return False
        



