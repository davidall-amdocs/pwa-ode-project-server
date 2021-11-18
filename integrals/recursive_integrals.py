# Updated in 29/10/2021 10:52:04

from sympy import *
def build_integrals(symbol):
	dx = Symbol('d' + str(symbol))
	x = Symbol(str(symbol))
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
	HINTS = []

	RECURSIVE_0 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(1, 2)))
	TEXT_0 = "Some text"
	PARTIAL_SOLVE_0 = Mul(Integer(2), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(1, 2)))
	NEW_INTEGRAL_0 = Mul(Symbol('b'), dx, Pow(x, Integer(-1)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(-1, 2)))
	RECURSIVE.append(RECURSIVE_0)
	TEXT.append(TEXT_0)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_0)
	NEW_INTEGRAL.append(NEW_INTEGRAL_0)
	HINT_0 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_0)
	EXCEPTION_0 = []
	EXCEPTIONS.append(EXCEPTION_0)

	RECURSIVE_1 = Mul(dx, Pow(x, Integer(-2)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(1, 2)))
	TEXT_1 = "Some text"
	PARTIAL_SOLVE_1 = Mul(Integer(-1), Pow(x, Integer(-1)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(1, 2)))
	NEW_INTEGRAL_1 = Mul(Rational(1, 2), Symbol('a'), dx, Pow(x, Integer(-1)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(-1, 2)))
	RECURSIVE.append(RECURSIVE_1)
	TEXT.append(TEXT_1)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_1)
	NEW_INTEGRAL.append(NEW_INTEGRAL_1)
	HINT_1 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_1)
	EXCEPTION_1 = []
	EXCEPTIONS.append(EXCEPTION_1)

	RECURSIVE_10 = Mul(dx, Pow(tan(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_10 = "Some text"
	PARTIAL_SOLVE_10 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), Pow(tan(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-1))))
	NEW_INTEGRAL_10 = Mul(Integer(-1), dx, Pow(tan(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_10)
	TEXT.append(TEXT_10)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_10)
	NEW_INTEGRAL.append(NEW_INTEGRAL_10)
	HINT_10 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_10)
	EXCEPTION_10 = []
	EXCEPTIONS.append(EXCEPTION_10)

	RECURSIVE_11 = Mul(dx, Pow(cot(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_11 = "Some text"
	PARTIAL_SOLVE_11 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), Pow(cot(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-1))))
	NEW_INTEGRAL_11 = Mul(Integer(-1), dx, Pow(cot(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_11)
	TEXT.append(TEXT_11)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_11)
	NEW_INTEGRAL.append(NEW_INTEGRAL_11)
	HINT_11 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_11)
	EXCEPTION_11 = []
	EXCEPTIONS.append(EXCEPTION_11)

	RECURSIVE_12 = Mul(dx, Pow(sec(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_12 = "Some text"
	PARTIAL_SOLVE_12 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), tan(Mul(Symbol('a'), x)), Pow(sec(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	NEW_INTEGRAL_12 = Mul(dx, Add(Symbol('n'), Integer(-2)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), Pow(sec(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_12)
	TEXT.append(TEXT_12)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_12)
	NEW_INTEGRAL.append(NEW_INTEGRAL_12)
	HINT_12 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_12)
	EXCEPTION_12 = []
	EXCEPTIONS.append(EXCEPTION_12)

	RECURSIVE_13 = Mul(dx, Pow(csc(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_13 = "Some text"
	PARTIAL_SOLVE_13 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), cot(Mul(Symbol('a'), x)), Pow(csc(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	NEW_INTEGRAL_13 = Mul(dx, Add(Symbol('n'), Integer(-2)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), Pow(csc(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_13)
	TEXT.append(TEXT_13)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_13)
	NEW_INTEGRAL.append(NEW_INTEGRAL_13)
	HINT_13 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_13)
	EXCEPTION_13 = []
	EXCEPTIONS.append(EXCEPTION_13)

	RECURSIVE_14 = Mul(dx, Pow(x, Symbol('n')), asin(Mul(Symbol('a'), x)))
	TEXT_14 = "Some text"
	PARTIAL_SOLVE_14 = Mul(Pow(x, Add(Symbol('n'), Integer(1))), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), asin(Mul(Symbol('a'), x)))
	NEW_INTEGRAL_14 = Mul(Integer(-1), Symbol('a'), dx, Pow(x, Add(Symbol('n'), Integer(1))), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Integer(1)), Rational(-1, 2)))
	RECURSIVE.append(RECURSIVE_14)
	TEXT.append(TEXT_14)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_14)
	NEW_INTEGRAL.append(NEW_INTEGRAL_14)
	HINT_14 = [[{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_14)
	EXCEPTION_14 = []
	EXCEPTIONS.append(EXCEPTION_14)

	RECURSIVE_15 = Mul(dx, Pow(x, Symbol('n')), acos(Mul(Symbol('a'), x)))
	TEXT_15 = "Some text"
	PARTIAL_SOLVE_15 = Mul(Pow(x, Add(Symbol('n'), Integer(1))), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), acos(Mul(Symbol('a'), x)))
	NEW_INTEGRAL_15 = Mul(Symbol('a'), dx, Pow(x, Add(Symbol('n'), Integer(1))), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Integer(1)), Rational(-1, 2)))
	RECURSIVE.append(RECURSIVE_15)
	TEXT.append(TEXT_15)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_15)
	NEW_INTEGRAL.append(NEW_INTEGRAL_15)
	HINT_15 = [[{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_15)
	EXCEPTION_15 = []
	EXCEPTIONS.append(EXCEPTION_15)

	RECURSIVE_16 = Mul(dx, Pow(x, Symbol('n')), atan(Mul(Symbol('a'), x)))
	TEXT_16 = "Some text"
	PARTIAL_SOLVE_16 = Mul(Pow(x, Add(Symbol('n'), Integer(1))), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), atan(Mul(Symbol('a'), x)))
	NEW_INTEGRAL_16 = Mul(Integer(-1), Symbol('a'), dx, Pow(x, Add(Symbol('n'), Integer(1))), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), Pow(Add(Mul(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Integer(1)), Integer(-1)))
	RECURSIVE.append(RECURSIVE_16)
	TEXT.append(TEXT_16)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_16)
	NEW_INTEGRAL.append(NEW_INTEGRAL_16)
	HINT_16 = [[{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_16)
	EXCEPTION_16 = []
	EXCEPTIONS.append(EXCEPTION_16)

	RECURSIVE_17 = Mul(dx, Pow(x, Symbol('n')), exp(Mul(Symbol('a'), x)))
	TEXT_17 = "Some text"
	PARTIAL_SOLVE_17 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(x, Symbol('n')), exp(Mul(Symbol('a'), x)))
	NEW_INTEGRAL_17 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), dx, Symbol('n'), Pow(x, Add(Symbol('n'), Integer(-1))), exp(Mul(Symbol('a'), x)))
	RECURSIVE.append(RECURSIVE_17)
	TEXT.append(TEXT_17)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_17)
	NEW_INTEGRAL.append(NEW_INTEGRAL_17)
	HINT_17 = [[{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_17)
	EXCEPTION_17 = []
	EXCEPTIONS.append(EXCEPTION_17)

	RECURSIVE_18 = Mul(Pow(Symbol('b'), Mul(Symbol('a'), x)), dx, Pow(x, Symbol('n')))
	TEXT_18 = "Some text"
	PARTIAL_SOLVE_18 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Symbol('b'), Mul(Symbol('a'), x)), Pow(x, Symbol('n')), Pow(log(Symbol('b')), Integer(-1)))
	NEW_INTEGRAL_18 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Symbol('b'), Mul(Symbol('a'), x)), dx, Symbol('n'), Pow(x, Add(Symbol('n'), Integer(-1))), Pow(log(Symbol('b')), Integer(-1)))
	RECURSIVE.append(RECURSIVE_18)
	TEXT.append(TEXT_18)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_18)
	NEW_INTEGRAL.append(NEW_INTEGRAL_18)
	HINT_18 = [[{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_18)
	EXCEPTION_18 = []
	EXCEPTIONS.append(EXCEPTION_18)

	RECURSIVE_19 = Mul(dx, Pow(x, Symbol('n')), Pow(log(Mul(Symbol('a'), x)), Symbol('b')))
	TEXT_19 = "Some text"
	PARTIAL_SOLVE_19 = Mul(Pow(x, Add(Symbol('n'), Integer(1))), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), Pow(log(Mul(Symbol('a'), x)), Symbol('b')))
	NEW_INTEGRAL_19 = Mul(Integer(-1), Symbol('b'), dx, Pow(x, Symbol('n')), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), Pow(log(Mul(Symbol('a'), x)), Add(Symbol('b'), Integer(-1))))
	RECURSIVE.append(RECURSIVE_19)
	TEXT.append(TEXT_19)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_19)
	NEW_INTEGRAL.append(NEW_INTEGRAL_19)
	HINT_19 = [[{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('b'), "value":1}],[{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('b'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('b'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('b'), "value":1}]]
	HINTS.append(HINT_19)
	EXCEPTION_19 = []
	EXCEPTIONS.append(EXCEPTION_19)

	RECURSIVE_2 = Mul(dx, Pow(x, Integer(-2)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(-1, 2)))
	TEXT_2 = "Some text"
	PARTIAL_SOLVE_2 = Mul(Integer(-1), Pow(Symbol('b'), Integer(-1)), Pow(x, Integer(-1)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(1, 2)))
	NEW_INTEGRAL_2 = Mul(Integer(-1), Rational(1, 2), Symbol('a'), Pow(Symbol('b'), Integer(-1)), dx, Pow(x, Integer(-1)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(-1, 2)))
	RECURSIVE.append(RECURSIVE_2)
	TEXT.append(TEXT_2)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_2)
	NEW_INTEGRAL.append(NEW_INTEGRAL_2)
	HINT_2 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_2)
	EXCEPTION_2 = []
	EXCEPTIONS.append(EXCEPTION_2)

	RECURSIVE_20 = Mul(dx, Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Mul(Rational(1, 2), Symbol('n'))))
	TEXT_20 = "Some text"
	PARTIAL_SOLVE_20 = Mul(Add(Mul(Integer(-1), Symbol('a')), x), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Mul(Rational(1, 2), Symbol('n'))))
	NEW_INTEGRAL_20 = Mul(Pow(Symbol('a'), Integer(2)), dx, Symbol('n'), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Add(Mul(Rational(1, 2), Symbol('n')), Integer(-1))))
	RECURSIVE.append(RECURSIVE_20)
	TEXT.append(TEXT_20)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_20)
	NEW_INTEGRAL.append(NEW_INTEGRAL_20)
	HINT_20 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_20)
	EXCEPTION_20 = []
	EXCEPTIONS.append(EXCEPTION_20)

	RECURSIVE_21 = Mul(dx, Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Mul(Integer(-1), Rational(1, 2), Symbol('n'))))
	TEXT_21 = "Some text"
	PARTIAL_SOLVE_21 = Mul(Pow(Symbol('a'), Integer(-2)), Add(Mul(Integer(-1), Symbol('a')), x), Pow(Add(Symbol('n'), Integer(-2)), Integer(-1)), Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Add(Integer(1), Mul(Integer(-1), Rational(1, 2), Symbol('n')))))
	NEW_INTEGRAL_21 = Mul(Pow(Symbol('a'), Integer(-2)), dx, Add(Symbol('n'), Integer(-3)), Pow(Add(Symbol('n'), Integer(-2)), Integer(-1)), Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Add(Integer(1), Mul(Integer(-1), Rational(1, 2), Symbol('n')))))
	RECURSIVE.append(RECURSIVE_21)
	TEXT.append(TEXT_21)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_21)
	NEW_INTEGRAL.append(NEW_INTEGRAL_21)
	HINT_21 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_21)
	EXCEPTION_21 = []
	EXCEPTIONS.append(EXCEPTION_21)

	RECURSIVE_22 = Mul(dx, Pow(sinh(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_22 = "Some text"
	PARTIAL_SOLVE_22 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Symbol('n'), Integer(-1)), Pow(sinh(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-1))), cosh(Mul(Symbol('a'), x)))
	NEW_INTEGRAL_22 = Mul(Integer(-1), dx, Pow(Symbol('n'), Integer(-1)), Add(Symbol('n'), Integer(-1)), Pow(sinh(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_22)
	TEXT.append(TEXT_22)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_22)
	NEW_INTEGRAL.append(NEW_INTEGRAL_22)
	HINT_22 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_22)
	EXCEPTION_22 = []
	EXCEPTIONS.append(EXCEPTION_22)

	RECURSIVE_23 = Mul(dx, Pow(cosh(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_23 = "Some text"
	PARTIAL_SOLVE_23 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Symbol('n'), Integer(-1)), sinh(Mul(Symbol('a'), x)), Pow(cosh(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-1))))
	NEW_INTEGRAL_23 = Mul(dx, Pow(Symbol('n'), Integer(-1)), Add(Symbol('n'), Integer(-1)), Pow(cosh(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_23)
	TEXT.append(TEXT_23)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_23)
	NEW_INTEGRAL.append(NEW_INTEGRAL_23)
	HINT_23 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_23)
	EXCEPTION_23 = []
	EXCEPTIONS.append(EXCEPTION_23)

	RECURSIVE_24 = Mul(dx, Pow(x, Symbol('n')), sinh(Mul(Symbol('a'), x)))
	TEXT_24 = "Some text"
	PARTIAL_SOLVE_24 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(x, Symbol('n')), cosh(Mul(Symbol('a'), x)))
	NEW_INTEGRAL_24 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), dx, Symbol('n'), Pow(x, Add(Symbol('n'), Integer(-1))), cosh(Mul(Symbol('a'), x)))
	RECURSIVE.append(RECURSIVE_24)
	TEXT.append(TEXT_24)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_24)
	NEW_INTEGRAL.append(NEW_INTEGRAL_24)
	HINT_24 = [[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}]]
	HINTS.append(HINT_24)
	EXCEPTION_24 = []
	EXCEPTIONS.append(EXCEPTION_24)

	RECURSIVE_25 = Mul(dx, Pow(x, Symbol('n')), cosh(Mul(Symbol('a'), x)))
	TEXT_25 = "Some text"
	PARTIAL_SOLVE_25 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(x, Symbol('n')), sinh(Mul(Symbol('a'), x)))
	NEW_INTEGRAL_25 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), dx, Symbol('n'), Pow(x, Add(Symbol('n'), Integer(-1))), sinh(Mul(Symbol('a'), x)))
	RECURSIVE.append(RECURSIVE_25)
	TEXT.append(TEXT_25)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_25)
	NEW_INTEGRAL.append(NEW_INTEGRAL_25)
	HINT_25 = [[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}]]
	HINTS.append(HINT_25)
	EXCEPTION_25 = []
	EXCEPTIONS.append(EXCEPTION_25)

	RECURSIVE_26 = Mul(dx, Pow(tanh(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_26 = "Some text"
	PARTIAL_SOLVE_26 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), Pow(tanh(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-1))))
	NEW_INTEGRAL_26 = Mul(dx, Pow(tanh(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_26)
	TEXT.append(TEXT_26)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_26)
	NEW_INTEGRAL.append(NEW_INTEGRAL_26)
	HINT_26 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_26)
	EXCEPTION_26 = []
	EXCEPTIONS.append(EXCEPTION_26)

	RECURSIVE_27 = Mul(dx, Pow(coth(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_27 = "Some text"
	PARTIAL_SOLVE_27 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), Pow(coth(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-1))))
	NEW_INTEGRAL_27 = Mul(dx, Pow(coth(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_27)
	TEXT.append(TEXT_27)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_27)
	NEW_INTEGRAL.append(NEW_INTEGRAL_27)
	HINT_27 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_27)
	EXCEPTION_27 = []
	EXCEPTIONS.append(EXCEPTION_27)

	RECURSIVE_28 = Mul(dx, Pow(sech(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_28 = "Some text"
	PARTIAL_SOLVE_28 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), tanh(Mul(Symbol('a'), x)), Pow(sech(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	NEW_INTEGRAL_28 = Mul(dx, Add(Symbol('n'), Integer(-2)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), Pow(sech(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_28)
	TEXT.append(TEXT_28)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_28)
	NEW_INTEGRAL.append(NEW_INTEGRAL_28)
	HINT_28 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_28)
	EXCEPTION_28 = []
	EXCEPTIONS.append(EXCEPTION_28)

	RECURSIVE_29 = Mul(dx, Pow(csch(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_29 = "Some text"
	PARTIAL_SOLVE_29 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), coth(Mul(Symbol('a'), x)), Pow(csch(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	NEW_INTEGRAL_29 = Mul(Integer(-1), dx, Add(Symbol('n'), Integer(-2)), Pow(Add(Symbol('n'), Integer(-1)), Integer(-1)), Pow(csch(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_29)
	TEXT.append(TEXT_29)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_29)
	NEW_INTEGRAL.append(NEW_INTEGRAL_29)
	HINT_29 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_29)
	EXCEPTION_29 = []
	EXCEPTIONS.append(EXCEPTION_29)

	RECURSIVE_3 = Mul(dx, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Mul(Rational(1, 2), Symbol('n'))))
	TEXT_3 = "Some text"
	PARTIAL_SOLVE_3 = Mul(x, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Mul(Rational(1, 2), Symbol('n'))), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)))
	NEW_INTEGRAL_3 = Mul(Integer(-1), Pow(Symbol('a'), Integer(2)), dx, Symbol('n'), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Add(Mul(Rational(1, 2), Symbol('n')), Integer(-1))), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)))
	RECURSIVE.append(RECURSIVE_3)
	TEXT.append(TEXT_3)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_3)
	NEW_INTEGRAL.append(NEW_INTEGRAL_3)
	HINT_3 = [[]]
	HINTS.append(HINT_3)
	EXCEPTION_3 = []
	EXCEPTIONS.append(EXCEPTION_3)

	RECURSIVE_4 = Mul(dx, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Mul(Integer(-1), Rational(1, 2), Symbol('n'))))
	TEXT_4 = "Some text"
	PARTIAL_SOLVE_4 = Mul(Pow(Symbol('a'), Integer(-2)), x, Pow(Add(Integer(2), Mul(Integer(-1), Symbol('n'))), Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Add(Integer(1), Mul(Integer(-1), Rational(1, 2), Symbol('n')))))
	NEW_INTEGRAL_4 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-2)), dx, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Add(Integer(1), Mul(Integer(-1), Rational(1, 2), Symbol('n')))), Add(Symbol('n'), Integer(-3)), Pow(Add(Symbol('n'), Integer(-2)), Integer(-1)))
	RECURSIVE.append(RECURSIVE_4)
	TEXT.append(TEXT_4)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_4)
	NEW_INTEGRAL.append(NEW_INTEGRAL_4)
	HINT_4 = [[]]
	HINTS.append(HINT_4)
	EXCEPTION_4 = []
	EXCEPTIONS.append(EXCEPTION_4)

	RECURSIVE_5 = Mul(dx, Pow(sin(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_5 = "Some text"
	PARTIAL_SOLVE_5 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Symbol('n'), Integer(-1)), Pow(sin(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-1))), cos(Mul(Symbol('a'), x)))
	NEW_INTEGRAL_5 = Mul(dx, Pow(Symbol('n'), Integer(-1)), Add(Symbol('n'), Integer(-1)), Pow(sin(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_5)
	TEXT.append(TEXT_5)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_5)
	NEW_INTEGRAL.append(NEW_INTEGRAL_5)
	HINT_5 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_5)
	EXCEPTION_5 = []
	EXCEPTIONS.append(EXCEPTION_5)

	RECURSIVE_6 = Mul(dx, Pow(cos(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_6 = "Some text"
	PARTIAL_SOLVE_6 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Symbol('n'), Integer(-1)), sin(Mul(Symbol('a'), x)), Pow(cos(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-1))))
	NEW_INTEGRAL_6 = Mul(dx, Pow(Symbol('n'), Integer(-1)), Add(Symbol('n'), Integer(-1)), Pow(cos(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))))
	RECURSIVE.append(RECURSIVE_6)
	TEXT.append(TEXT_6)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_6)
	NEW_INTEGRAL.append(NEW_INTEGRAL_6)
	HINT_6 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_6)
	EXCEPTION_6 = []
	EXCEPTIONS.append(EXCEPTION_6)

	RECURSIVE_7 = Mul(dx, Pow(sin(Mul(Symbol('a'), x)), Symbol('n')), Pow(cos(Mul(Symbol('a'), x)), Symbol('c')))
	TEXT_7 = "Some text"
	PARTIAL_SOLVE_7 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('c'), Symbol('n')), Integer(-1)), Pow(sin(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-1))), Pow(cos(Mul(Symbol('a'), x)), Add(Symbol('c'), Integer(1))))
	NEW_INTEGRAL_7 = Mul(dx, Pow(Add(Symbol('c'), Symbol('n')), Integer(-1)), Add(Symbol('n'), Integer(-1)), Pow(sin(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(-2))), Pow(cos(Mul(Symbol('a'), x)), Symbol('c')))
	RECURSIVE.append(RECURSIVE_7)
	TEXT.append(TEXT_7)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_7)
	NEW_INTEGRAL.append(NEW_INTEGRAL_7)
	HINT_7 = [[{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('c'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('c'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('c'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('c'), "value":1}]]
	HINTS.append(HINT_7)
	EXCEPTION_7 = []
	EXCEPTIONS.append(EXCEPTION_7)

	RECURSIVE_8 = Mul(dx, Pow(x, Symbol('n')), sin(Mul(Symbol('a'), x)))
	TEXT_8 = "Some text"
	PARTIAL_SOLVE_8 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(x, Symbol('n')), cos(Mul(Symbol('a'), x)))
	NEW_INTEGRAL_8 = Mul(Pow(Symbol('a'), Integer(-1)), dx, Symbol('n'), Pow(x, Add(Symbol('n'), Integer(-1))), cos(Mul(Symbol('a'), x)))
	RECURSIVE.append(RECURSIVE_8)
	TEXT.append(TEXT_8)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_8)
	NEW_INTEGRAL.append(NEW_INTEGRAL_8)
	HINT_8 = [[{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_8)
	EXCEPTION_8 = []
	EXCEPTIONS.append(EXCEPTION_8)

	RECURSIVE_9 = Mul(dx, Pow(x, Symbol('n')), cos(Mul(Symbol('a'), x)))
	TEXT_9 = "Some text"
	PARTIAL_SOLVE_9 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(x, Symbol('n')), sin(Mul(Symbol('a'), x)))
	NEW_INTEGRAL_9 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), dx, Symbol('n'), Pow(x, Add(Symbol('n'), Integer(-1))), sin(Mul(Symbol('a'), x)))
	RECURSIVE.append(RECURSIVE_9)
	TEXT.append(TEXT_9)
	PARTIAL_SOLVE.append(PARTIAL_SOLVE_9)
	NEW_INTEGRAL.append(NEW_INTEGRAL_9)
	HINT_9 = [[{"symbol":Symbol('n'), "value":1},{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_9)
	EXCEPTION_9 = []
	EXCEPTIONS.append(EXCEPTION_9)

	index = 0
	for HINT in HINTS:
		for STATE in HINT:
			if len(STATE) > 0:
				new_bas = RECURSIVE[index]
				new_solve = PARTIAL_SOLVE[index]
				new_int = NEW_INTEGRAL[index]
				for CHANGE in STATE:
					new_bas = new_bas.subs(CHANGE['symbol'], CHANGE['value'])
					new_solve = new_solve.subs(CHANGE['symbol'], CHANGE['value'])
					new_int = new_int.subs(CHANGE['symbol'], CHANGE['value'])
				RECURSIVE.append(new_bas)
				PARTIAL_SOLVE.append(new_solve)
				NEW_INTEGRAL.append(new_int)
		index = index + 1
