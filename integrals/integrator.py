from utils.constant import ATOMIC_INTEGRAL_DIFFICULTY
from sympy import *

import solvers.controller as controller
import integrals.atomic_integrals as atm

def int_solve(expression, differential):
    '''
    # Params
    * expression (symbolic expression)
    * differential (symbolic expression)

    # Return (symblic expression)
    * integrate of the expression with respect the differential. 
    Uses local and global difficulty control
    '''

    global variable_n
    global variable_a
    global variable_b
    global variable_c

    variable_n = None
    variable_a = None
    variable_b = None
    variable_c = None

    atm.build_integrals(differential)

    global local_difficulty
    local_difficulty = 0

    expression = factor(expression)
    differential_expression = Mul(expression, Symbol('d'+str(differential)))
    print(srepr(differential_expression))

    index = 0
    for integral in atm.BASIC:
        if match_integral(differential_expression, integral):
            local_difficulty = local_difficulty + ATOMIC_INTEGRAL_DIFFICULTY
            controller.global_difficulty = controller.global_difficulty + local_difficulty

            int_solution = atm.SOLVE[index]

            if "Symbol('n')" in srepr(atm.SOLVE[index]):
                int_solution = int_solution.subs(Symbol('n'), variable_n)

            if "Symbol('a')" in srepr(atm.SOLVE[index]):
                int_solution = int_solution.subs(Symbol('a'), variable_a)

            if "Symbol('b')" in srepr(atm.SOLVE[index]):
                int_solution = int_solution.subs(Symbol('b'), variable_b)

            if "Symbol('c')" in srepr(atm.SOLVE[index]):
                int_solution = int_solution.subs(Symbol('c'), variable_c)

            return int_solution
        index = index + 1

    return integrate(expression, differential)

def match_integral(expression, integral):
    if integral == expression:
        return True

    if integral == Symbol('n'):
        if type(expression) is Integer:
            global variable_n
            if variable_n is None:
                variable_n = expression
                return True
            else:
                if variable_n == expression:
                    return True
                else:
                    return False
        else:
            return False

    if integral == Symbol('a'):
        if type(expression) is Integer:
            global variable_a
            if variable_a is None:
                variable_a = expression
                return True
            else:
                if variable_a == expression:
                    return True
                else:
                    return False
        else:
            return False

    if integral == Symbol('b'):
        if type(expression) is Integer:
            global variable_b
            if variable_b is None:
                variable_b = expression
                return True
            else:
                if variable_b == expression:
                    return True
                else:
                    return False
        else:
            return False
    
    if integral == Symbol('c'):
        if type(expression) is Integer:
            global variable_c
            if variable_c is None:
                variable_c = expression
                return True
            else:
                if variable_c == expression:
                    return True
                else:
                    return False
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
        



