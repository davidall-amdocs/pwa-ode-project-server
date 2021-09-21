from anomalies.completeness_anomaly import CompletenessAnomaly
from sympy import * 
from utils.constant import \
ALGEBRAIC_STEP_DIFFICULTY, \
EXPAND_STEP_DIFFICULTY, \
FACTOR_STEP_DIFFICULTY, \
MAX_GLOBAL_DIFFICULTY, \
SIMPLIFY_STEP_DIFFICULTY, \
SOLVE_STEP_DIFFICULTY, \
SUBSTITUTION_STEP_DIFFICULTY

import solvers.controller as controller

def alg_add(param1, param2):
    '''
    ## Params
    * param1 (symbolic expression)
    * param2 (symbolic expression)

    ## Return (symbolic expression)
    * param1 + param2 and adds the amount of difficulty to the global count
    '''

    controller.global_difficulty = controller.global_difficulty + ALGEBRAIC_STEP_DIFFICULTY
    if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
        raise CompletenessAnomaly([["", []]])
    return Add(param1, param2)

def alg_subs(param1, param2):
    '''
    ## Params
    * param1 (symbolic expression)
    * param2 (symbolic expression)

    ## Return (symbolic expression)
    * param1 - param2 and adds the amount of difficulty to the global count
    '''
    controller.global_difficulty = controller.global_difficulty + ALGEBRAIC_STEP_DIFFICULTY
    if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
        raise CompletenessAnomaly([["", []]])
    return Add(param1, Mul(param2, -1))

def alg_mul(param1, param2):
    '''
    ## Params
    * param1 (symbolic expression)
    * param2 (symbolic expression)

    ## Return (symbolic expression)
    * param1 * param2 and adds the amount of difficulty to the global count
    '''

    controller.global_difficulty = controller.global_difficulty + ALGEBRAIC_STEP_DIFFICULTY
    if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
        raise CompletenessAnomaly([["", []]])
    return Mul(param1, param2)

def alg_div(param1, param2):
    '''
    ## Params
    * param1 (symbolic expression)
    * param2 (symbolic expression)

    ## Return (symbolic expression)
    * param1 / param2 and adds the amount of difficulty to the global count
    '''

    controller.global_difficulty = controller.global_difficulty + ALGEBRAIC_STEP_DIFFICULTY
    if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
        raise CompletenessAnomaly([["", []]])
    return Mul(param1, Pow(param2, -1))

def alg_solve(equation, variable):
    '''
    ## Params
    * equation (symbolic expression)
    * variable (symbolic expression)

    ## Return (symbolic expression)
    * solve variable as a function of the given equation
    '''

    controller.global_difficulty = controller.global_difficulty + SOLVE_STEP_DIFFICULTY
    try:
        if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
            raise CompletenessAnomaly([["", []]])
        return solve(equation, variable)
    except:
        print("Couldn't make the solve for the equation")
        raise CompletenessAnomaly([["", []]])

def alg_simplify(param1):
    '''
    ## Params
    * param1 (symbolic expression)

    ## Return (symbolic expression)
    * simplified expression of param1
    '''

    controller.global_difficulty = controller.global_difficulty + SIMPLIFY_STEP_DIFFICULTY
    if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
        raise CompletenessAnomaly([["", []]])
    return simplify(param1)

def alg_expand(param1):
    '''
    ## Params
    * param1 (symbolic expression)

    ## Return (symbolic expression)
    * expanded expression of param1
    '''

    controller.global_difficulty = controller.global_difficulty + EXPAND_STEP_DIFFICULTY
    if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
        raise CompletenessAnomaly([["", []]])
    return param1.expand(force = True)

def alg_factor(param1):
    '''
    ## Params
    * param1 (symbolic expression)

    ## Return (symbolic expression)
    * factored expression of param1
    '''

    controller.global_difficulty = controller.global_difficulty + FACTOR_STEP_DIFFICULTY
    if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
        raise CompletenessAnomaly([["", []]])
    return factor(param1)

def alg_mul_inv(param1):
    '''
    ## Params
    * param1 (symbolic expression)

    ## Return (symbolic expression)
    * mul inverse of param1
    '''

    controller.global_difficulty = controller.global_difficulty + ALGEBRAIC_STEP_DIFFICULTY
    if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
        raise CompletenessAnomaly([["", []]])
    return Pow(param1, Integer(-1))

def alg_substitution(expression, old_variable, new_variable):
    '''
    ## Params
    * expression (symbolic expression)
    * old_variable (symbolic expression)
    * new_variable (symbolic expression)

    ## Return (symbolic expression)
    * substitutes in the expression the old_variable with the new_variable and returns the 
    new expression
    '''

    controller.global_difficulty = controller.global_difficulty + SUBSTITUTION_STEP_DIFFICULTY
    if controller.global_difficulty >= MAX_GLOBAL_DIFFICULTY:
        raise CompletenessAnomaly([["", []]])
    return expression.subs(old_variable, new_variable)