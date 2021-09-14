from anomalies.completeness_anomaly import CompletenessAnomaly
from sympy import * 
from utils.constant import ALGEBRAIC_STEP_DIFFICULTY, MAX_GLOBAL_DIFFICULTY
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
        raise CompletenessAnomaly(None)
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
        raise CompletenessAnomaly(None)
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
        raise CompletenessAnomaly(None)
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
        raise CompletenessAnomaly(None)
    return Mul(param1, Pow(param2, -1))

