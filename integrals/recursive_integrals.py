from sympy import *

# TODO: Rebuild integrals using special constants cases (n = 1, ...)

def build_integrals(symbol):
    dx = Symbol('d' + str(symbol))
    x = Symbol(str(symbol))
    n = Symbol('n')
    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')

    global RECURSIVE
    global TEXT
    global PARTIAL_SOLVE
    global NEW_INTEGRAL
    global EXCEPTIONS

    RECURSIVE = []
    TEXT = []
    PARTIAL_SOLVE = []
    NEW_INTEGRAL = []
    EXCEPTIONS = []

    # Hints for building integral variations
    HINTS = []

    RECURSIVE_001 = Mul(sqrt(Add(Mul(a, x), b)), Pow(x, -1), dx)
    TEXT_001 = "Some text"
    PARTIAL_SOLVE_001 = Mul(2, sqrt(Add(Mul(a, x), b)))
    NEW_INTEGRAL_001 = Mul(dx, b, Pow(Mul(x, sqrt(Add(Mul(a, x), b))), -1))
    RECURSIVE.append(RECURSIVE_001)
    TEXT.append(TEXT_001)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_001)
    NEW_INTEGRAL.append(NEW_INTEGRAL_001)

    HINT_001 = [[{"symbol": a, "value": 1}]]
    HINTS.append(HINT_001)

    RECURSIVE_002 = Mul(sqrt(Add(Mul(a, x), b)), Pow(x, -2), dx)
    TEXT_002 = "Some text"
    PARTIAL_SOLVE_002 = Mul(-1, sqrt(Add(Mul(a, x), b)), Pow(x, -1))
    NEW_INTEGRAL_002 = Mul(dx, Mul(a, Rational(1, 2)), Pow(Mul(x, sqrt(Add(Mul(a, x), b))), -1))
    RECURSIVE.append(RECURSIVE_002)
    TEXT.append(TEXT_002)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_002)
    NEW_INTEGRAL.append(NEW_INTEGRAL_002)

    HINT_002 = [[{"symbol": a, "value": 1}]]
    HINTS.append(HINT_002)

    RECURSIVE_003 = Mul(Pow(sqrt(Add(Mul(a, x), b)), -1), Pow(x, -2), dx)
    TEXT_003 = "Some text"
    PARTIAL_SOLVE_003 = Mul(-1, sqrt(Add(Mul(a, x), b)), Pow(Mul(x, b), -1))
    NEW_INTEGRAL_003 = Mul(dx, Mul(a, Rational(-1, 2)), Pow(Mul(b, x, sqrt(Add(Mul(a, x), b))), -1))
    RECURSIVE.append(RECURSIVE_003)
    TEXT.append(TEXT_003)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_003)
    NEW_INTEGRAL.append(NEW_INTEGRAL_003)

    HINT_003 = [[{"symbol": a, "value": 1}]]
    HINTS.append(HINT_003)

    RECURSIVE_004 = Mul(Pow(sqrt(Add(Pow(x, 2), Mul(-1, Pow(a, 2)))), n), dx)
    TEXT_004 = "Some text"
    PARTIAL_SOLVE_004 = Mul(x, Pow(sqrt(Add(Pow(x, 2), Mul(-1, Pow(a, 2)))), n), Pow(Add(n, 1), -1))
    NEW_INTEGRAL_004 = Mul(dx, Pow(a, 2), n, Pow(Add(n, 1), -1), -1, Pow(sqrt(Add(Pow(x, 2), Mul(-1, Pow(a, 2)))), Add(n, Mul(-1, 2))))
    RECURSIVE.append(RECURSIVE_004)
    TEXT.append(TEXT_004)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_004)
    NEW_INTEGRAL.append(NEW_INTEGRAL_004)

    HINT_004 = [[]]
    HINTS.append(HINT_004)

    RECURSIVE_005 = Mul(Pow(sqrt(Add(Pow(x, 2), Mul(-1, Pow(a, 2)))), Mul(-1, n)), dx)
    TEXT_005 = "Some text"
    PARTIAL_SOLVE_005 = Mul(x, Pow(sqrt(Add(Pow(x, 2), Mul(-1, Pow(a, 2)))), Add(2, Mul(-1, n))), Pow(Mul(Add(2, Mul(-1, n)), Pow(a, 2)), -1))
    NEW_INTEGRAL_005 = Mul(dx, Pow(a, -2), Add(n, -3), Pow(Add(n, -2), -1), -1, Pow(sqrt(Add(Pow(x, 2), Mul(-1, Pow(a, 2)))), Add(Mul(-1, n), 2)))
    RECURSIVE.append(RECURSIVE_005)
    TEXT.append(TEXT_005)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_005)
    NEW_INTEGRAL.append(NEW_INTEGRAL_005)

    HINT_005 = [[]]
    HINTS.append(HINT_005)

    RECURSIVE_006 = Mul(Pow(sin(Mul(a, x)), n), dx)
    TEXT_006 = "Some text"
    PARTIAL_SOLVE_006 = Mul(-1, Pow(Mul(a, n), -1), Pow(sin(Mul(a, x)), Add(n, -1)), cos(Mul(a, x)))
    NEW_INTEGRAL_006 = Mul(dx, Pow(n, -1), Add(n, -1), Pow(sin(Mul(a, x)), Add(n, -2)))
    RECURSIVE.append(RECURSIVE_006)
    TEXT.append(TEXT_006)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_006)
    NEW_INTEGRAL.append(NEW_INTEGRAL_006)

    HINT_006 = [[{"symbol": a, "value": 1}]]
    HINTS.append(HINT_006)

    RECURSIVE_007 = Mul(Pow(cos(Mul(a, x)), n), dx)
    TEXT_007 = "Some text"
    PARTIAL_SOLVE_007 = Mul(Pow(Mul(a, n), -1), Pow(cos(Mul(a, x)), Add(n, -1)), sin(Mul(a, x)))
    NEW_INTEGRAL_007 = Mul(dx, Pow(n, -1), Add(n, -1), Pow(cos(Mul(a, x)), Add(n, -2)))
    RECURSIVE.append(RECURSIVE_007)
    TEXT.append(TEXT_007)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_007)
    NEW_INTEGRAL.append(NEW_INTEGRAL_007)

    HINT_007 = [[{"symbol": a, "value": 1}]]
    HINTS.append(HINT_007)

    RECURSIVE_008 = Mul(Pow(cos(Mul(a, x)), c), Pow(sin(Mul(a, x)), n), dx)
    TEXT_008 = "Some text"
    PARTIAL_SOLVE_008 = Mul(-1, Pow(Mul(a, Add(n, c)), -1), Pow(cos(Mul(a, x)), Add(c, 1)), Pow(sin(Mul(a, x)), Add(n, -1)))
    NEW_INTEGRAL_008 = Mul(dx, Pow(Add(c, n), -1), Add(n, -1), Pow(sin(Mul(a, x)), Add(n, -2)), Pow(cos(Mul(a, x)), c))
    RECURSIVE.append(RECURSIVE_008)
    TEXT.append(TEXT_008)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_008)
    NEW_INTEGRAL.append(NEW_INTEGRAL_008)

    HINT_008 = [[{"symbol": a, "value": 1}], [{"symbol": a, "value": 1}, {"symbol": c, "value": 1}], 
    [{"symbol": a, "value": 1}, {"symbol": n, "value": 1}], [{"symbol": c, "value": 1}], [{"symbol": n, "value": 1}]]
    HINTS.append(HINT_008)

    RECURSIVE_010 = Mul(Pow(x, n), sin(Mul(a, x)), dx)
    TEXT_010 = "Some text"
    PARTIAL_SOLVE_010 = Mul(-1, Pow(a, -1), Pow(x, n), cos(Mul(a, x)))
    NEW_INTEGRAL_010 = Mul(dx, n, Pow(a, -1), Pow(x, Add(n, -1)), cos(Mul(a, x)))
    RECURSIVE.append(RECURSIVE_010)
    TEXT.append(TEXT_010)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_010)
    NEW_INTEGRAL.append(NEW_INTEGRAL_010)

    RECURSIVE_011 = Mul(Pow(x, n), cos(Mul(a, x)), dx)
    TEXT_011 = "Some text"
    PARTIAL_SOLVE_011 = Mul(Pow(a, -1), Pow(x, n), sin(Mul(a, x)))
    NEW_INTEGRAL_011 = Mul(dx, -1, n, Pow(a, -1), Pow(x, Add(n, -1)), sin(Mul(a, x)))
    RECURSIVE.append(RECURSIVE_011)
    TEXT.append(TEXT_011)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_011)
    NEW_INTEGRAL.append(NEW_INTEGRAL_011)

    RECURSIVE_012 = Mul(Pow(tan(Mul(a, x)), n), dx)
    TEXT_012 = "Some text"
    PARTIAL_SOLVE_012 = Mul(Pow(Mul(a, Add(n, -1)), -1), Pow(tan(Mul(a, x)), Add(n, -1)))
    NEW_INTEGRAL_012 = Mul(dx, -1, Pow(tan(Mul(a, x)), Add(n, -2)))
    RECURSIVE.append(RECURSIVE_012)
    TEXT.append(TEXT_012)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_012)
    NEW_INTEGRAL.append(NEW_INTEGRAL_012)

    RECURSIVE_013 = Mul(Pow(cot(Mul(a, x)), n), dx)
    TEXT_013 = "Some text"
    PARTIAL_SOLVE_013 = Mul(-1, Pow(Mul(a, Add(n, -1)), -1), Pow(cot(Mul(a, x)), Add(n, -1)))
    NEW_INTEGRAL_013 = Mul(dx, -1, Pow(cot(Mul(a, x)), Add(n, -2)))
    RECURSIVE.append(RECURSIVE_013)
    TEXT.append(TEXT_013)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_013)
    NEW_INTEGRAL.append(NEW_INTEGRAL_013)

    RECURSIVE_014 = Mul(Pow(sec(Mul(a, x)), n), dx)
    TEXT_014 = "Some text"
    PARTIAL_SOLVE_014 = Mul(Pow(Mul(a, Add(n, -1)), -1), Pow(sec(Mul(a, x)), Add(n, -2)), tan(Mul(a, x)))
    NEW_INTEGRAL_014 = Mul(dx, Pow(sec(Mul(a, x)), Add(n, -2)), Add(n, -2), Pow(Add(n, -1), -1))
    RECURSIVE.append(RECURSIVE_014)
    TEXT.append(TEXT_014)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_014)
    NEW_INTEGRAL.append(NEW_INTEGRAL_014)

    RECURSIVE_015 = Mul(Pow(csc(Mul(a, x)), n), dx)
    TEXT_015 = "Some text"
    PARTIAL_SOLVE_015 = Mul(-1, Pow(Mul(a, Add(n, -1)), -1), Pow(csc(Mul(a, x)), Add(n, -2)), cot(Mul(a, x)))
    NEW_INTEGRAL_015 = Mul(dx, Pow(csc(Mul(a, x)), Add(n, -2)), Add(n, -2), Pow(Add(n, -1), -1))
    RECURSIVE.append(RECURSIVE_015)
    TEXT.append(TEXT_015)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_015)
    NEW_INTEGRAL.append(NEW_INTEGRAL_015)

    RECURSIVE_016 = Mul(Pow(x, n), asin(Mul(a, x)),  dx)
    TEXT_016 = "Some text"
    PARTIAL_SOLVE_016 = Mul(Pow(x, Add(n, 1)), Pow(Add(n, 1), -1), asin(Mul(a, x)))
    NEW_INTEGRAL_016 = Mul(dx, -1, a, Pow(Add(n, 1), -1), Pow(x, Add(n+1)), Pow(sqrt(Add(1, Mul(-1, Pow(Mul(a, x), 2)))), -1))
    RECURSIVE.append(RECURSIVE_016)
    TEXT.append(TEXT_016)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_016)
    NEW_INTEGRAL.append(NEW_INTEGRAL_016)

    RECURSIVE_017 = Mul(Pow(x, n), acos(Mul(a, x)),  dx)
    TEXT_017 = "Some text"
    PARTIAL_SOLVE_017 = Mul(Pow(x, Add(n, 1)), Pow(Add(n, 1), -1), acos(Mul(a, x)))
    NEW_INTEGRAL_017 = Mul(dx, a, Pow(Add(n, 1), -1), Pow(x, Add(n+1)), Pow(sqrt(Add(1, Mul(-1, Pow(Mul(a, x), 2)))), -1))
    RECURSIVE.append(RECURSIVE_017)
    TEXT.append(TEXT_017)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_017)
    NEW_INTEGRAL.append(NEW_INTEGRAL_017)

    RECURSIVE_017 = Mul(Pow(x, n), acos(Mul(a, x)),  dx)
    TEXT_017 = "Some text"
    PARTIAL_SOLVE_017 = Mul(Pow(x, Add(n, 1)), Pow(Add(n, 1), -1), acos(Mul(a, x)))
    NEW_INTEGRAL_017 = Mul(dx, a, Pow(Add(n, 1), -1), Pow(x, Add(n+1)), Pow(sqrt(Add(1, Mul(-1, Pow(Mul(a, x), 2)))), -1))
    RECURSIVE.append(RECURSIVE_017)
    TEXT.append(TEXT_017)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_017)
    NEW_INTEGRAL.append(NEW_INTEGRAL_017)

    RECURSIVE_018 = Mul(Pow(x, n), atan(Mul(a, x)),  dx)
    TEXT_018 = "Some text"
    PARTIAL_SOLVE_018 = Mul(Pow(x, Add(n, 1)), Pow(Add(n, 1), -1), atan(Mul(a, x)))
    NEW_INTEGRAL_018 = Mul(dx, a, -1, Pow(Add(n, 1), -1), Pow(x, Add(n+1)), Pow(Add(1, Pow(Mul(a, x), 2)), -1))
    RECURSIVE.append(RECURSIVE_018)
    TEXT.append(TEXT_018)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_018)
    NEW_INTEGRAL.append(NEW_INTEGRAL_018)

    RECURSIVE_019 = Mul(Pow(x, n), Pow(E, Mul(a, x)),  dx)
    TEXT_019 = "Some text"
    PARTIAL_SOLVE_019 = Mul(Pow(a, -1), Pow(x, n), Pow(E, Mul(a, x)))
    NEW_INTEGRAL_019 = Mul(dx, -1, n, Pow(a, -1), Pow(x, Add(n, -1)), Pow(E, Mul(a, x)))
    RECURSIVE.append(RECURSIVE_019)
    TEXT.append(TEXT_019)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_019)
    NEW_INTEGRAL.append(NEW_INTEGRAL_019)

    RECURSIVE_020 = Mul(Pow(x, n), Pow(b, Mul(a, x)),  dx)
    TEXT_020 = "Some text"
    PARTIAL_SOLVE_020 = Mul(Pow(Mul(a, ln(b)), -1), Pow(x, n), Pow(b, Mul(a, x)))
    NEW_INTEGRAL_020 = Mul(dx, -1, n, Pow(Mul(a, ln(b)), -1), Pow(x, Add(n, -1)), Pow(b, Mul(a, x)))
    RECURSIVE.append(RECURSIVE_020)
    TEXT.append(TEXT_020)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_020)
    NEW_INTEGRAL.append(NEW_INTEGRAL_020)

    RECURSIVE_021 = Mul(Pow(x, n), Pow(ln(Mul(a, x)), b),  dx)
    TEXT_021 = "Some text"
    PARTIAL_SOLVE_021 = Mul(Pow(x, Add(n, 1)), Pow(Add(n, 1), -1), Pow(ln(Mul(a, x)), b))
    NEW_INTEGRAL_021 = Mul(dx, -1, b, Pow(Add(n+1), -1), Pow(x, n), Pow(ln(Mul(a, x)), Add(b, -1)))
    RECURSIVE.append(RECURSIVE_021)
    TEXT.append(TEXT_021)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_021)
    NEW_INTEGRAL.append(NEW_INTEGRAL_021)

    RECURSIVE_022 = Mul(Pow(sqrt(Add(Mul(2, a, x), Mul(-1, Pow(x, 2)))), n), dx)
    TEXT_022 = "Some text"
    PARTIAL_SOLVE_022 = Mul(Pow(Add(n, 1), -1), Add(x, Mul(-1, a)), Pow(sqrt(Add(Mul(2, a, x), Mul(-1, Pow(x, 2)))), n))
    NEW_INTEGRAL_022 = Mul(dx, n, Pow(a, 2), Pow(Add(n, 1), -1), Pow(sqrt(Add(Mul(2, a, x), Mul(-1, Pow(x, 2)))), Add(n, -2)))
    RECURSIVE.append(RECURSIVE_022)
    TEXT.append(TEXT_022)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_022)
    NEW_INTEGRAL.append(NEW_INTEGRAL_022)

    RECURSIVE_023 = Mul(Pow(sqrt(Add(Mul(2, a, x), Mul(-1, Pow(x, 2)))), Mul(n, -1)), dx)
    TEXT_023 = "Some text"
    PARTIAL_SOLVE_023 = Mul(Pow(Mul(Add(n, -2), Pow(a, 2)), -1), Add(x, Mul(-1, a)), Pow(sqrt(Add(Mul(2, a, x), Mul(-1, Pow(x, 2)))), Add(2, Mul(-1, n))))
    NEW_INTEGRAL_023 = Mul(dx, Add(n, -3), Pow(a, -2), Pow(Add(n, -2), -1), Pow(sqrt(Add(Mul(2, a, x), Mul(-1, Pow(x, 2)))), Add(2, Mul(n, -1))))
    RECURSIVE.append(RECURSIVE_023)
    TEXT.append(TEXT_023)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_023)
    NEW_INTEGRAL.append(NEW_INTEGRAL_023)

    RECURSIVE_024 = Mul(Pow(sinh(Mul(a, x)), n), dx)
    TEXT_024 = "Some text"
    PARTIAL_SOLVE_024 = Mul(Pow(Mul(n, a), -1), Pow(sinh(Mul(a, x)), Add(n, -1)), cosh(Mul(a, x)))
    NEW_INTEGRAL_024 = Mul(dx, -1, Pow(sinh(Mul(a, x)), Add(n, -2)), Add(n, -1), Pow(n, -1))
    RECURSIVE.append(RECURSIVE_024)
    TEXT.append(TEXT_024)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_024)
    NEW_INTEGRAL.append(NEW_INTEGRAL_024)

    RECURSIVE_025 = Mul(Pow(cosh(Mul(a, x)), n), dx)
    TEXT_025 = "Some text"
    PARTIAL_SOLVE_025 = Mul(Pow(Mul(n, a), -1), Pow(cosh(Mul(a, x)), Add(n, -1)), sinh(Mul(a, x)))
    NEW_INTEGRAL_025 = Mul(dx, Pow(cosh(Mul(a, x)), Add(n, -2)), Add(n, -1), Pow(n, -1))
    RECURSIVE.append(RECURSIVE_025)
    TEXT.append(TEXT_025)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_025)
    NEW_INTEGRAL.append(NEW_INTEGRAL_025)

    RECURSIVE_026 = Mul(dx, Pow(x, n), sinh(Mul(a, x)))
    TEXT_026 = "Some text"
    PARTIAL_SOLVE_026 = Mul(Pow(x, n), Pow(a, -1), cosh(Mul(a, x)))
    NEW_INTEGRAL_026 = Mul(dx, -1, n, Pow(a, -1), Pow(x, Add(n, -1)), cosh(Mul(a, x)))
    RECURSIVE.append(RECURSIVE_026)
    TEXT.append(TEXT_026)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_026)
    NEW_INTEGRAL.append(NEW_INTEGRAL_026)

    RECURSIVE_027 = Mul(dx, Pow(x, n), cosh(Mul(a, x)))
    TEXT_027 = "Some text"
    PARTIAL_SOLVE_027 = Mul(Pow(x, n), Pow(a, -1), sinh(Mul(a, x)))
    NEW_INTEGRAL_027 = Mul(dx, -1, n, Pow(a, -1), Pow(x, Add(n, -1)), sinh(Mul(a, x)))
    RECURSIVE.append(RECURSIVE_027)
    TEXT.append(TEXT_027)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_027)
    NEW_INTEGRAL.append(NEW_INTEGRAL_027)

    RECURSIVE_028 = Mul(dx, Pow(tanh(Mul(a, x)), n) )
    TEXT_028 = "Some text"
    PARTIAL_SOLVE_028 = Mul(Pow(Mul(a, n-1), -1), Pow(tanh(Mul(a, x)), n-1), -1)
    NEW_INTEGRAL_028 = Mul(dx, Pow(tanh(Mul(a, x)), n-2))
    RECURSIVE.append(RECURSIVE_028)
    TEXT.append(TEXT_028)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_028)
    NEW_INTEGRAL.append(NEW_INTEGRAL_028)

    RECURSIVE_029 = Mul(dx, Pow(coth(Mul(a, x)), n) )
    TEXT_029 = "Some text"
    PARTIAL_SOLVE_029 = Mul(Pow(Mul(a, n-1), -1), Pow(coth(Mul(a, x)), n-1), -1)
    NEW_INTEGRAL_029 = Mul(dx, Pow(coth(Mul(a, x)), n-2))
    RECURSIVE.append(RECURSIVE_029)
    TEXT.append(TEXT_029)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_029)
    NEW_INTEGRAL.append(NEW_INTEGRAL_029)

    RECURSIVE_030 = Mul(dx, Pow(sech(Mul(a, x)), n) )
    TEXT_030 = "Some text"
    PARTIAL_SOLVE_030 = Mul(Pow(Mul(a, n-1), -1), Pow(sech(Mul(a, x)), n-2), tanh(Mul(a, x)) )
    NEW_INTEGRAL_030 = Mul(dx, Pow(sech(Mul(a, x)), n-2), n-2, Pow(n-1, -1))
    RECURSIVE.append(RECURSIVE_030)
    TEXT.append(TEXT_030)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_030)
    NEW_INTEGRAL.append(NEW_INTEGRAL_030)

    RECURSIVE_031 = Mul(dx, Pow(csch(Mul(a, x)), n) )
    TEXT_031 = "Some text"
    PARTIAL_SOLVE_031 = Mul(Pow(Mul(a, n-1), -1), Pow(csch(Mul(a, x)), n-2), coth(Mul(a, x)), -1 )
    NEW_INTEGRAL_031 = Mul(dx, Pow(csch(Mul(a, x)), n-2), n-2, Pow(n-1, -1), -1)
    RECURSIVE.append(RECURSIVE_031)
    TEXT.append(TEXT_031)
    PARTIAL_SOLVE.append(PARTIAL_SOLVE_031)
    NEW_INTEGRAL.append(NEW_INTEGRAL_031)

    index = 0
    for HINT in HINTS:
        for STATE in HINT:
            if len(STATE) > 0:
                new_rec = RECURSIVE[index]
                new_partial = PARTIAL_SOLVE[index]
                new_int = NEW_INTEGRAL[index]
                for CHANGE in STATE:
                    new_rec = new_rec.subs(CHANGE["symbol"], CHANGE["value"])
                    new_partial = new_partial.subs(CHANGE["symbol"], CHANGE["value"])
                    new_int = new_int.subs(CHANGE["symbol"], CHANGE["value"])
                RECURSIVE.append(new_rec)
                PARTIAL_SOLVE.append(new_partial)
                NEW_INTEGRAL.append(new_int)
        index = index + 1






















