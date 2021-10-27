from sympy import *
def build_integrals(symbol):
	dx = Symbol('d' + str(symbol))
	x = Symbol(str(symbol))
	global BASIC
	global TEXT
	global SOLVE
	global EXCEPTIONS
	BASIC = []
	TEXT = []
	SOLVE = []
	EXCEPTIONS = []
	HINTS = []

	BASIC_0 = dx
	TEXT_0 = "Some text"
	SOLVE_0 = x
	BASIC.append(BASIC_0)
	TEXT.append(TEXT_0)
	SOLVE.append(SOLVE_0)
	HINT_0 = [[]]
	HINTS.append(HINT_0)
	EXCEPTION_0 = []
	EXCEPTIONS.append(EXCEPTION_0)

	BASIC_1 = Mul(dx, Pow(x, Symbol('n')))
	TEXT_1 = "Some text"
	SOLVE_1 = Mul(Pow(x, Add(Symbol('n'), Integer(1))), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)))
	BASIC.append(BASIC_1)
	TEXT.append(TEXT_1)
	SOLVE.append(SOLVE_1)
	HINT_1 = [[{"symbol":Symbol('n'), "value":1}]]
	HINTS.append(HINT_1)
	EXCEPTION_1 = [{"symbol":Symbol('n'), "value":Integer(-1), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_1)

	BASIC_10 = Mul(dx, cot(Mul(Symbol('a'), x)), csc(Mul(Symbol('a'), x)))
	TEXT_10 = "Some text"
	SOLVE_10 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), csc(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_10)
	TEXT.append(TEXT_10)
	SOLVE.append(SOLVE_10)
	HINT_10 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_10)
	EXCEPTION_10 = []
	EXCEPTIONS.append(EXCEPTION_10)

	BASIC_100 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(-1, 2)))
	TEXT_100 = "Some text"
	SOLVE_100 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Mul(Pow(x, Integer(-1)), Add(Mul(Integer(2), Symbol('a')), Mul(Integer(-1), x))), Rational(1, 2)))
	BASIC.append(BASIC_100)
	TEXT.append(TEXT_100)
	SOLVE.append(SOLVE_100)
	HINT_100 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_100)
	EXCEPTION_100 = [{"symbol":Symbol('a'), "value":Integer(0), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_100)

	BASIC_101 = Mul(dx, sinh(Mul(Symbol('a'), x)))
	TEXT_101 = "Some text"
	SOLVE_101 = Mul(Pow(Symbol('a'), Integer(-1)), cosh(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_101)
	TEXT.append(TEXT_101)
	SOLVE.append(SOLVE_101)
	HINT_101 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_101)
	EXCEPTION_101 = []
	EXCEPTIONS.append(EXCEPTION_101)

	BASIC_102 = Mul(dx, cosh(Mul(Symbol('a'), x)))
	TEXT_102 = "Some text"
	SOLVE_102 = Mul(Pow(Symbol('a'), Integer(-1)), sinh(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_102)
	TEXT.append(TEXT_102)
	SOLVE.append(SOLVE_102)
	HINT_102 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_102)
	EXCEPTION_102 = []
	EXCEPTIONS.append(EXCEPTION_102)

	BASIC_103 = Mul(dx, Pow(sinh(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_103 = "Some text"
	SOLVE_103 = Add(Mul(Integer(-1), Rational(1, 2), x), Mul(Rational(1, 4), Pow(Symbol('a'), Integer(-1)), sinh(Mul(Integer(2), Symbol('a'), x))))
	BASIC.append(BASIC_103)
	TEXT.append(TEXT_103)
	SOLVE.append(SOLVE_103)
	HINT_103 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_103)
	EXCEPTION_103 = []
	EXCEPTIONS.append(EXCEPTION_103)

	BASIC_104 = Mul(dx, Pow(cosh(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_104 = "Some text"
	SOLVE_104 = Add(Mul(Rational(1, 2), x), Mul(Rational(1, 4), Pow(Symbol('a'), Integer(-1)), sinh(Mul(Integer(2), Symbol('a'), x))))
	BASIC.append(BASIC_104)
	TEXT.append(TEXT_104)
	SOLVE.append(SOLVE_104)
	HINT_104 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_104)
	EXCEPTION_104 = []
	EXCEPTIONS.append(EXCEPTION_104)

	BASIC_105 = Mul(dx, x, sinh(Mul(Symbol('a'), x)))
	TEXT_105 = "Some text"
	SOLVE_105 = Add(Mul(Pow(Symbol('a'), Integer(-1)), cosh(Mul(Symbol('a'), x))), Mul(Integer(-1), Pow(Symbol('a'), Integer(-2)), sinh(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_105)
	TEXT.append(TEXT_105)
	SOLVE.append(SOLVE_105)
	HINT_105 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_105)
	EXCEPTION_105 = []
	EXCEPTIONS.append(EXCEPTION_105)

	BASIC_106 = Mul(dx, x, cosh(Mul(Symbol('a'), x)))
	TEXT_106 = "Some text"
	SOLVE_106 = Add(Mul(Pow(Symbol('a'), Integer(-1)), sinh(Mul(Symbol('a'), x))), Mul(Integer(-1), Pow(Symbol('a'), Integer(-2)), cosh(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_106)
	TEXT.append(TEXT_106)
	SOLVE.append(SOLVE_106)
	HINT_106 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_106)
	EXCEPTION_106 = []
	EXCEPTIONS.append(EXCEPTION_106)

	BASIC_107 = Mul(dx, tanh(Mul(Symbol('a'), x)))
	TEXT_107 = "Some text"
	SOLVE_107 = Mul(Pow(Symbol('a'), Integer(-1)), log(cosh(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_107)
	TEXT.append(TEXT_107)
	SOLVE.append(SOLVE_107)
	HINT_107 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_107)
	EXCEPTION_107 = []
	EXCEPTIONS.append(EXCEPTION_107)

	BASIC_108 = Mul(dx, coth(Mul(Symbol('a'), x)))
	TEXT_108 = "Some text"
	SOLVE_108 = Mul(Pow(Symbol('a'), Integer(-1)), log(sinh(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_108)
	TEXT.append(TEXT_108)
	SOLVE.append(SOLVE_108)
	HINT_108 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_108)
	EXCEPTION_108 = []
	EXCEPTIONS.append(EXCEPTION_108)

	BASIC_109 = Mul(dx, Pow(tanh(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_109 = "Some text"
	SOLVE_109 = Add(x, Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), tanh(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_109)
	TEXT.append(TEXT_109)
	SOLVE.append(SOLVE_109)
	HINT_109 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_109)
	EXCEPTION_109 = []
	EXCEPTIONS.append(EXCEPTION_109)

	BASIC_11 = Mul(dx, tan(Mul(Symbol('a'), x)))
	TEXT_11 = "Some text"
	SOLVE_11 = Mul(Pow(Symbol('a'), Integer(-1)), log(sec(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_11)
	TEXT.append(TEXT_11)
	SOLVE.append(SOLVE_11)
	HINT_11 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_11)
	EXCEPTION_11 = []
	EXCEPTIONS.append(EXCEPTION_11)

	BASIC_110 = Mul(dx, Pow(coth(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_110 = "Some text"
	SOLVE_110 = Add(x, Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), coth(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_110)
	TEXT.append(TEXT_110)
	SOLVE.append(SOLVE_110)
	HINT_110 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_110)
	EXCEPTION_110 = []
	EXCEPTIONS.append(EXCEPTION_110)

	BASIC_111 = Mul(dx, sech(Mul(Symbol('a'), x)))
	TEXT_111 = "Some text"
	SOLVE_111 = Mul(Pow(Symbol('a'), Integer(-1)), asin(tanh(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_111)
	TEXT.append(TEXT_111)
	SOLVE.append(SOLVE_111)
	HINT_111 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_111)
	EXCEPTION_111 = []
	EXCEPTIONS.append(EXCEPTION_111)

	BASIC_112 = Mul(dx, csch(Mul(Symbol('a'), x)))
	TEXT_112 = "Some text"
	SOLVE_112 = Mul(Pow(Symbol('a'), Integer(-1)), log(tanh(Mul(Rational(1, 2), Symbol('a'), x))))
	BASIC.append(BASIC_112)
	TEXT.append(TEXT_112)
	SOLVE.append(SOLVE_112)
	HINT_112 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_112)
	EXCEPTION_112 = []
	EXCEPTIONS.append(EXCEPTION_112)

	BASIC_113 = Mul(dx, Pow(sech(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_113 = "Some text"
	SOLVE_113 = Mul(Pow(Symbol('a'), Integer(-1)), tanh(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_113)
	TEXT.append(TEXT_113)
	SOLVE.append(SOLVE_113)
	HINT_113 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_113)
	EXCEPTION_113 = []
	EXCEPTIONS.append(EXCEPTION_113)

	BASIC_114 = Mul(dx, Pow(csch(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_114 = "Some text"
	SOLVE_114 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), coth(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_114)
	TEXT.append(TEXT_114)
	SOLVE.append(SOLVE_114)
	HINT_114 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_114)
	EXCEPTION_114 = []
	EXCEPTIONS.append(EXCEPTION_114)

	BASIC_115 = Mul(dx, tanh(Mul(Symbol('a'), x)), Pow(sech(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_115 = "Some text"
	SOLVE_115 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Symbol('n'), Integer(-1)), Pow(sech(Mul(Symbol('a'), x)), Symbol('n')))
	BASIC.append(BASIC_115)
	TEXT.append(TEXT_115)
	SOLVE.append(SOLVE_115)
	HINT_115 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('n'), "value":1}]]
	HINTS.append(HINT_115)
	EXCEPTION_115 = []
	EXCEPTIONS.append(EXCEPTION_115)

	BASIC_116 = Mul(dx, cot(Mul(Symbol('a'), x)), Pow(csch(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_116 = "Some text"
	SOLVE_116 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Symbol('n'), Integer(-1)), Pow(csch(Mul(Symbol('a'), x)), Symbol('n')))
	BASIC.append(BASIC_116)
	TEXT.append(TEXT_116)
	SOLVE.append(SOLVE_116)
	HINT_116 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('n'), "value":1}]]
	HINTS.append(HINT_116)
	EXCEPTION_116 = []
	EXCEPTIONS.append(EXCEPTION_116)

	BASIC_117 = Mul(dx, exp(Mul(Symbol('a'), x)), sinh(Mul(Symbol('b'), x)))
	TEXT_117 = "Some text"
	SOLVE_117 = Mul(Rational(1, 2), Add(Mul(Pow(Add(Symbol('a'), Symbol('b')), Integer(-1)), exp(Mul(Symbol('b'), x))), Mul(Integer(-1), Pow(Add(Symbol('a'), Mul(Integer(-1), Symbol('b'))), Integer(-1)), exp(Mul(Integer(-1), Symbol('b'), x)))), exp(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_117)
	TEXT.append(TEXT_117)
	SOLVE.append(SOLVE_117)
	HINT_117 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('b'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('b'), "value":1}]]
	HINTS.append(HINT_117)
	EXCEPTION_117 = [{"symbol":Pow(Symbol('b'), Integer(2)), "value":Pow(Symbol('a'), Integer(2)), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_117)

	BASIC_118 = Mul(dx, exp(Mul(Symbol('a'), x)), cosh(Mul(Symbol('b'), x)))
	TEXT_118 = "Some text"
	SOLVE_118 = Mul(Rational(1, 2), Add(Mul(Pow(Add(Symbol('a'), Symbol('b')), Integer(-1)), exp(Mul(Symbol('b'), x))), Mul(Pow(Add(Symbol('a'), Mul(Integer(-1), Symbol('b'))), Integer(-1)), exp(Mul(Integer(-1), Symbol('b'), x)))), exp(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_118)
	TEXT.append(TEXT_118)
	SOLVE.append(SOLVE_118)
	HINT_118 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('b'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('b'), "value":1}]]
	HINTS.append(HINT_118)
	EXCEPTION_118 = [{"symbol":Pow(Symbol('b'), Integer(2)), "value":Pow(Symbol('a'), Integer(2)), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_118)

	BASIC_119 = Mul(dx, sin(Mul(Symbol('a'), x)), cos(Mul(Symbol('a'), x)))
	TEXT_119 = "Some text"
	SOLVE_119 = Mul(Integer(-1), Rational(1, 4), Pow(Symbol('a'), Integer(-1)), cos(Mul(Integer(2), Symbol('a'), x)))
	BASIC.append(BASIC_119)
	TEXT.append(TEXT_119)
	SOLVE.append(SOLVE_119)
	HINT_119 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_119)
	EXCEPTION_119 = []
	EXCEPTIONS.append(EXCEPTION_119)

	BASIC_12 = Mul(dx, cot(Mul(Symbol('a'), x)))
	TEXT_12 = "Some text"
	SOLVE_12 = Mul(Pow(Symbol('a'), Integer(-1)), log(sin(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_12)
	TEXT.append(TEXT_12)
	SOLVE.append(SOLVE_12)
	HINT_12 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_12)
	EXCEPTION_12 = []
	EXCEPTIONS.append(EXCEPTION_12)

	BASIC_13 = Mul(dx, sinh(Mul(Symbol('a'), x)))
	TEXT_13 = "Some text"
	SOLVE_13 = Mul(Pow(Symbol('a'), Integer(-1)), cosh(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_13)
	TEXT.append(TEXT_13)
	SOLVE.append(SOLVE_13)
	HINT_13 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_13)
	EXCEPTION_13 = []
	EXCEPTIONS.append(EXCEPTION_13)

	BASIC_14 = Mul(dx, cosh(Mul(Symbol('a'), x)))
	TEXT_14 = "Some text"
	SOLVE_14 = Mul(Pow(Symbol('a'), Integer(-1)), sinh(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_14)
	TEXT.append(TEXT_14)
	SOLVE.append(SOLVE_14)
	HINT_14 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_14)
	EXCEPTION_14 = []
	EXCEPTIONS.append(EXCEPTION_14)

	BASIC_15 = Mul(dx, Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(-1, 2)))
	TEXT_15 = "Some text"
	SOLVE_15 = asin(Mul(Pow(Symbol('a'), Integer(-1)), x))
	BASIC.append(BASIC_15)
	TEXT.append(TEXT_15)
	SOLVE.append(SOLVE_15)
	HINT_15 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_15)
	EXCEPTION_15 = []
	EXCEPTIONS.append(EXCEPTION_15)

	BASIC_16 = Mul(dx, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Integer(-1)))
	TEXT_16 = "Some text"
	SOLVE_16 = Mul(Pow(Symbol('a'), Integer(-1)), atan(Mul(Pow(Symbol('a'), Integer(-1)), x)))
	BASIC.append(BASIC_16)
	TEXT.append(TEXT_16)
	SOLVE.append(SOLVE_16)
	HINT_16 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_16)
	EXCEPTION_16 = []
	EXCEPTIONS.append(EXCEPTION_16)

	BASIC_17 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(-1, 2)))
	TEXT_17 = "Some text"
	SOLVE_17 = Mul(Pow(Symbol('a'), Integer(-1)), asec(Mul(Pow(Symbol('a'), Integer(-1)), x)))
	BASIC.append(BASIC_17)
	TEXT.append(TEXT_17)
	SOLVE.append(SOLVE_17)
	HINT_17 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_17)
	EXCEPTION_17 = []
	EXCEPTIONS.append(EXCEPTION_17)

	BASIC_18 = Mul(dx, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(-1, 2)))
	TEXT_18 = "Some text"
	SOLVE_18 = asinh(Mul(Pow(Symbol('a'), Integer(-1)), x))
	BASIC.append(BASIC_18)
	TEXT.append(TEXT_18)
	SOLVE.append(SOLVE_18)
	HINT_18 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_18)
	EXCEPTION_18 = []
	EXCEPTIONS.append(EXCEPTION_18)

	BASIC_19 = Mul(dx, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(-1, 2)))
	TEXT_19 = "Some text"
	SOLVE_19 = acosh(Mul(Pow(Symbol('a'), Integer(-1)), x))
	BASIC.append(BASIC_19)
	TEXT.append(TEXT_19)
	SOLVE.append(SOLVE_19)
	HINT_19 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_19)
	EXCEPTION_19 = [{"symbol":Symbol('a'), "value":Integer(0), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_19)

	BASIC_2 = Mul(dx, Pow(x, Integer(-1)))
	TEXT_2 = "Some text"
	SOLVE_2 = log(x)
	BASIC.append(BASIC_2)
	TEXT.append(TEXT_2)
	SOLVE.append(SOLVE_2)
	HINT_2 = [[]]
	HINTS.append(HINT_2)
	EXCEPTION_2 = []
	EXCEPTIONS.append(EXCEPTION_2)

	BASIC_20 = Mul(dx, Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Symbol('n')))
	TEXT_20 = "Some text"
	SOLVE_20 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Add(Symbol('n'), Integer(1))))
	BASIC.append(BASIC_20)
	TEXT.append(TEXT_20)
	SOLVE.append(SOLVE_20)
	HINT_20 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_20)
	EXCEPTION_20 = [{"symbol":Symbol('n'), "value":Integer(-1), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_20)

	BASIC_21 = Mul(dx, x, Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Symbol('n')))
	TEXT_21 = "Some text"
	SOLVE_21 = Mul(Pow(Symbol('a'), Integer(-2)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Add(Symbol('n'), Integer(1))), Add(Mul(Integer(-1), Symbol('b'), Pow(Add(Symbol('n'), Integer(1)), Integer(-1))), Mul(Pow(Add(Symbol('n'), Integer(2)), Integer(-1)), Add(Mul(Symbol('a'), x), Symbol('b')))))
	BASIC.append(BASIC_21)
	TEXT.append(TEXT_21)
	SOLVE.append(SOLVE_21)
	HINT_21 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_21)
	EXCEPTION_21 = [{"symbol":Symbol('n'), "value":Integer(-1), "type":"neq"},{"symbol":Symbol('n'), "value":Integer(-2), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_21)

	BASIC_22 = Mul(dx, Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Integer(-1)))
	TEXT_22 = "Some text"
	SOLVE_22 = Mul(Pow(Symbol('a'), Integer(-1)), log(Add(Mul(Symbol('a'), x), Symbol('b'))))
	BASIC.append(BASIC_22)
	TEXT.append(TEXT_22)
	SOLVE.append(SOLVE_22)
	HINT_22 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_22)
	EXCEPTION_22 = []
	EXCEPTIONS.append(EXCEPTION_22)

	BASIC_23 = Mul(dx, x, Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Integer(-1)))
	TEXT_23 = "Some text"
	SOLVE_23 = Add(Mul(Pow(Symbol('a'), Integer(-1)), x), Mul(Integer(-1), Pow(Symbol('a'), Integer(-2)), Symbol('b'), log(Add(Mul(Symbol('a'), x), Symbol('b')))))
	BASIC.append(BASIC_23)
	TEXT.append(TEXT_23)
	SOLVE.append(SOLVE_23)
	HINT_23 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_23)
	EXCEPTION_23 = []
	EXCEPTIONS.append(EXCEPTION_23)

	BASIC_24 = Mul(dx, x, Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Integer(-2)))
	TEXT_24 = "Some text"
	SOLVE_24 = Mul(Pow(Symbol('a'), Integer(-2)), Add(Mul(Symbol('b'), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Integer(-1))), log(Add(Mul(Symbol('a'), x), Symbol('b')))))
	BASIC.append(BASIC_24)
	TEXT.append(TEXT_24)
	SOLVE.append(SOLVE_24)
	HINT_24 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_24)
	EXCEPTION_24 = []
	EXCEPTIONS.append(EXCEPTION_24)

	BASIC_25 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Integer(-1)))
	TEXT_25 = "Some text"
	SOLVE_25 = Mul(Pow(Symbol('b'), Integer(-1)), log(Mul(x, Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Integer(-1)))))
	BASIC.append(BASIC_25)
	TEXT.append(TEXT_25)
	SOLVE.append(SOLVE_25)
	HINT_25 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_25)
	EXCEPTION_25 = []
	EXCEPTIONS.append(EXCEPTION_25)

	BASIC_26 = Mul(dx, Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Mul(Rational(1, 2), Symbol('n'))))
	TEXT_26 = "Some text"
	SOLVE_26 = Mul(Integer(2), Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(2)), Integer(-1)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Add(Mul(Rational(1, 2), Symbol('n')), Integer(1))))
	BASIC.append(BASIC_26)
	TEXT.append(TEXT_26)
	SOLVE.append(SOLVE_26)
	HINT_26 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_26)
	EXCEPTION_26 = [{"symbol":Symbol('n'), "value":Integer(-2), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_26)

	BASIC_27 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(-1, 2)))
	TEXT_27 = "Some text"
	SOLVE_27 = Mul(Pow(Symbol('b'), Rational(-1, 2)), log(Mul(Add(Mul(Integer(-1), Pow(Symbol('b'), Rational(1, 2))), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(1, 2))), Pow(Add(Pow(Symbol('b'), Rational(1, 2)), Pow(Add(Mul(Symbol('a'), x), Symbol('b')), Rational(1, 2))), Integer(-1)))))
	BASIC.append(BASIC_27)
	TEXT.append(TEXT_27)
	SOLVE.append(SOLVE_27)
	HINT_27 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_27)
	EXCEPTION_27 = []
	EXCEPTIONS.append(EXCEPTION_27)

	BASIC_28 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Mul(Symbol('a'), x), Mul(Integer(-1), Symbol('b'))), Rational(-1, 2)))
	TEXT_28 = "Some text"
	SOLVE_28 = Mul(Integer(2), Pow(Symbol('b'), Rational(-1, 2)), atan(Pow(Mul(Pow(Symbol('b'), Integer(-1)), Add(Mul(Symbol('a'), x), Mul(Integer(-1), Symbol('b')))), Rational(1, 2))))
	BASIC.append(BASIC_28)
	TEXT.append(TEXT_28)
	SOLVE.append(SOLVE_28)
	HINT_28 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_28)
	EXCEPTION_28 = []
	EXCEPTIONS.append(EXCEPTION_28)

	BASIC_29 = Mul(dx, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Integer(-2)))
	TEXT_29 = "Some text"
	SOLVE_29 = Add(Mul(Rational(1, 2), Pow(Symbol('a'), Integer(-2)), x, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Integer(-1))), Mul(Rational(1, 2), Pow(Symbol('a'), Integer(-3)), atan(Mul(Pow(Symbol('a'), Integer(-1)), x))))
	BASIC.append(BASIC_29)
	TEXT.append(TEXT_29)
	SOLVE.append(SOLVE_29)
	HINT_29 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_29)
	EXCEPTION_29 = []
	EXCEPTIONS.append(EXCEPTION_29)

	BASIC_3 = Mul(dx, exp(x))
	TEXT_3 = "Some text"
	SOLVE_3 = exp(x)
	BASIC.append(BASIC_3)
	TEXT.append(TEXT_3)
	SOLVE.append(SOLVE_3)
	HINT_3 = [[]]
	HINTS.append(HINT_3)
	EXCEPTION_3 = []
	EXCEPTIONS.append(EXCEPTION_3)

	BASIC_30 = Mul(dx, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2)))
	TEXT_30 = "Some text"
	SOLVE_30 = Add(Mul(Rational(1, 2), Pow(Symbol('a'), Integer(2)), log(Add(x, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2))))), Mul(Rational(1, 2), x, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2))))
	BASIC.append(BASIC_30)
	TEXT.append(TEXT_30)
	SOLVE.append(SOLVE_30)
	HINT_30 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_30)
	EXCEPTION_30 = []
	EXCEPTIONS.append(EXCEPTION_30)

	BASIC_31 = Mul(dx, Pow(x, Integer(2)), Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2)))
	TEXT_31 = "Some text"
	SOLVE_31 = Add(Mul(Integer(-1), Rational(1, 8), Pow(Symbol('a'), Integer(4)), log(Add(x, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2))))), Mul(Rational(1, 8), x, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2)), Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(2), Pow(x, Integer(2))))))
	BASIC.append(BASIC_31)
	TEXT.append(TEXT_31)
	SOLVE.append(SOLVE_31)
	HINT_31 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_31)
	EXCEPTION_31 = []
	EXCEPTIONS.append(EXCEPTION_31)

	BASIC_32 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2)))
	TEXT_32 = "Some text"
	SOLVE_32 = Add(Mul(Integer(-1), Symbol('a'), log(Mul(Pow(x, Integer(-1)), Add(Symbol('a'), Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2)))))), Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2)))
	BASIC.append(BASIC_32)
	TEXT.append(TEXT_32)
	SOLVE.append(SOLVE_32)
	HINT_32 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_32)
	EXCEPTION_32 = []
	EXCEPTIONS.append(EXCEPTION_32)

	BASIC_33 = Mul(dx, Pow(x, Integer(-2)), Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2)))
	TEXT_33 = "Some text"
	SOLVE_33 = Add(log(Add(x, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2)))), Mul(Integer(-1), Pow(x, Integer(-1)), Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2))))
	BASIC.append(BASIC_33)
	TEXT.append(TEXT_33)
	SOLVE.append(SOLVE_33)
	HINT_33 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_33)
	EXCEPTION_33 = []
	EXCEPTIONS.append(EXCEPTION_33)

	BASIC_34 = Mul(dx, Pow(x, Integer(2)), Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(-1, 2)))
	TEXT_34 = "Some text"
	SOLVE_34 = Add(Mul(Integer(-1), Rational(1, 2), Pow(Symbol('a'), Integer(2)), log(Add(x, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2))))), Mul(Rational(1, 2), x, Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2))))
	BASIC.append(BASIC_34)
	TEXT.append(TEXT_34)
	SOLVE.append(SOLVE_34)
	HINT_34 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_34)
	EXCEPTION_34 = []
	EXCEPTIONS.append(EXCEPTION_34)

	BASIC_35 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(-1, 2)))
	TEXT_35 = "Some text"
	SOLVE_35 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), log(Mul(Pow(x, Integer(-1)), Add(Symbol('a'), Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2))))))
	BASIC.append(BASIC_35)
	TEXT.append(TEXT_35)
	SOLVE.append(SOLVE_35)
	HINT_35 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_35)
	EXCEPTION_35 = []
	EXCEPTIONS.append(EXCEPTION_35)

	BASIC_36 = Mul(dx, Pow(x, Integer(-2)), Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(-1, 2)))
	TEXT_36 = "Some text"
	SOLVE_36 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-2)), Pow(x, Integer(-1)), Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Rational(1, 2)))
	BASIC.append(BASIC_36)
	TEXT.append(TEXT_36)
	SOLVE.append(SOLVE_36)
	HINT_36 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_36)
	EXCEPTION_36 = []
	EXCEPTIONS.append(EXCEPTION_36)

	BASIC_37 = Mul(dx, Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Integer(-1)))
	TEXT_37 = "Some text"
	SOLVE_37 = Mul(Rational(1, 2), Pow(Symbol('a'), Integer(-1)), log(Mul(Pow(Add(Mul(Integer(-1), Symbol('a')), x), Integer(-1)), Add(Symbol('a'), x))))
	BASIC.append(BASIC_37)
	TEXT.append(TEXT_37)
	SOLVE.append(SOLVE_37)
	HINT_37 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_37)
	EXCEPTION_37 = []
	EXCEPTIONS.append(EXCEPTION_37)

	BASIC_38 = Mul(dx, Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Integer(-2)))
	TEXT_38 = "Some text"
	SOLVE_38 = Add(Mul(Rational(1, 2), Pow(Symbol('a'), Integer(-2)), x, Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Integer(-1))), Mul(Rational(1, 4), Pow(Symbol('a'), Integer(-3)), log(Mul(Pow(Add(Mul(Integer(-1), Symbol('a')), x), Integer(-1)), Add(Symbol('a'), x)))))
	BASIC.append(BASIC_38)
	TEXT.append(TEXT_38)
	SOLVE.append(SOLVE_38)
	HINT_38 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_38)
	EXCEPTION_38 = []
	EXCEPTIONS.append(EXCEPTION_38)

	BASIC_39 = Mul(dx, Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)))
	TEXT_39 = "Some text"
	SOLVE_39 = Add(Mul(Rational(1, 2), Pow(Symbol('a'), Integer(2)), asin(Mul(Pow(Symbol('a'), Integer(-1)), x))), Mul(Rational(1, 2), x, Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2))))
	BASIC.append(BASIC_39)
	TEXT.append(TEXT_39)
	SOLVE.append(SOLVE_39)
	HINT_39 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_39)
	EXCEPTION_39 = []
	EXCEPTIONS.append(EXCEPTION_39)

	BASIC_4 = Mul(Pow(Symbol('a'), x), dx)
	TEXT_4 = "Some text"
	SOLVE_4 = Mul(Pow(Symbol('a'), x), Pow(log(Symbol('a')), Integer(-1)))
	BASIC.append(BASIC_4)
	TEXT.append(TEXT_4)
	SOLVE.append(SOLVE_4)
	HINT_4 = [[]]
	HINTS.append(HINT_4)
	EXCEPTION_4 = [{"symbol":Symbol('a'), "value":Integer(1), "type":"neq"},{"symbol":Symbol('a'), "value":Integer(0), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_4)

	BASIC_40 = Mul(dx, Pow(x, Integer(2)), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)))
	TEXT_40 = "Some text"
	SOLVE_40 = Add(Mul(Rational(1, 8), Pow(Symbol('a'), Integer(4)), asin(Mul(Pow(Symbol('a'), Integer(-1)), x))), Mul(Integer(-1), Rational(1, 8), x, Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Pow(x, Integer(2)))), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2))))
	BASIC.append(BASIC_40)
	TEXT.append(TEXT_40)
	SOLVE.append(SOLVE_40)
	HINT_40 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_40)
	EXCEPTION_40 = []
	EXCEPTIONS.append(EXCEPTION_40)

	BASIC_41 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)))
	TEXT_41 = "Some text"
	SOLVE_41 = Add(Mul(Integer(-1), Symbol('a'), log(Mul(Pow(x, Integer(-1)), Add(Symbol('a'), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)))))), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)))
	BASIC.append(BASIC_41)
	TEXT.append(TEXT_41)
	SOLVE.append(SOLVE_41)
	HINT_41 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_41)
	EXCEPTION_41 = []
	EXCEPTIONS.append(EXCEPTION_41)

	BASIC_42 = Mul(dx, Pow(x, Integer(-2)), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)))
	TEXT_42 = "Some text"
	SOLVE_42 = Add(Mul(Integer(-1), asin(Mul(Pow(Symbol('a'), Integer(-1)), x))), Mul(Integer(-1), Pow(x, Integer(-1)), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2))))
	BASIC.append(BASIC_42)
	TEXT.append(TEXT_42)
	SOLVE.append(SOLVE_42)
	HINT_42 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_42)
	EXCEPTION_42 = []
	EXCEPTIONS.append(EXCEPTION_42)

	BASIC_43 = Mul(dx, Pow(x, Integer(2)), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(-1, 2)))
	TEXT_43 = "Some text"
	SOLVE_43 = Add(Mul(Rational(1, 2), Pow(Symbol('a'), Integer(2)), asin(Mul(Pow(Symbol('a'), Integer(-1)), x))), Mul(Integer(-1), Rational(1, 2), x, Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2))))
	BASIC.append(BASIC_43)
	TEXT.append(TEXT_43)
	SOLVE.append(SOLVE_43)
	HINT_43 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_43)
	EXCEPTION_43 = []
	EXCEPTIONS.append(EXCEPTION_43)

	BASIC_44 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(-1, 2)))
	TEXT_44 = "Some text"
	SOLVE_44 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), log(Mul(Pow(x, Integer(-1)), Add(Symbol('a'), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2))))))
	BASIC.append(BASIC_44)
	TEXT.append(TEXT_44)
	SOLVE.append(SOLVE_44)
	HINT_44 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_44)
	EXCEPTION_44 = []
	EXCEPTIONS.append(EXCEPTION_44)

	BASIC_45 = Mul(dx, Pow(x, Integer(-2)), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(-1, 2)))
	TEXT_45 = "Some text"
	SOLVE_45 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-2)), Pow(x, Integer(-1)), Pow(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)))
	BASIC.append(BASIC_45)
	TEXT.append(TEXT_45)
	SOLVE.append(SOLVE_45)
	HINT_45 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_45)
	EXCEPTION_45 = []
	EXCEPTIONS.append(EXCEPTION_45)

	BASIC_46 = Mul(dx, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2)))
	TEXT_46 = "Some text"
	SOLVE_46 = Add(Mul(Integer(-1), Rational(1, 2), Pow(Symbol('a'), Integer(2)), log(Add(x, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2))))), Mul(Rational(1, 2), x, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2))))
	BASIC.append(BASIC_46)
	TEXT.append(TEXT_46)
	SOLVE.append(SOLVE_46)
	HINT_46 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_46)
	EXCEPTION_46 = []
	EXCEPTIONS.append(EXCEPTION_46)

	BASIC_47 = Mul(dx, x, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Mul(Rational(1, 2), Symbol('n'))))
	TEXT_47 = "Some text"
	SOLVE_47 = Mul(Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Add(Mul(Rational(1, 2), Symbol('n')), Integer(1))), Pow(Add(Symbol('n'), Integer(2)), Integer(-1)))
	BASIC.append(BASIC_47)
	TEXT.append(TEXT_47)
	SOLVE.append(SOLVE_47)
	HINT_47 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_47)
	EXCEPTION_47 = []
	EXCEPTIONS.append(EXCEPTION_47)

	BASIC_48 = Mul(dx, Pow(x, Integer(2)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2)))
	TEXT_48 = "Some text"
	SOLVE_48 = Add(Mul(Integer(-1), Rational(1, 8), Pow(Symbol('a'), Integer(4)), log(Add(x, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2))))), Mul(Rational(1, 8), x, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2)), Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Integer(2), Pow(x, Integer(2))))))
	BASIC.append(BASIC_48)
	TEXT.append(TEXT_48)
	SOLVE.append(SOLVE_48)
	HINT_48 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_48)
	EXCEPTION_48 = []
	EXCEPTIONS.append(EXCEPTION_48)

	BASIC_49 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2)))
	TEXT_49 = "Some text"
	SOLVE_49 = Add(Mul(Integer(-1), Symbol('a'), asec(Mul(Pow(Symbol('a'), Integer(-1)), x))), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2)))
	BASIC.append(BASIC_49)
	TEXT.append(TEXT_49)
	SOLVE.append(SOLVE_49)
	HINT_49 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_49)
	EXCEPTION_49 = []
	EXCEPTIONS.append(EXCEPTION_49)

	BASIC_5 = Mul(dx, sin(Mul(Symbol('a'), x)))
	TEXT_5 = "Some text"
	SOLVE_5 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), cos(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_5)
	TEXT.append(TEXT_5)
	SOLVE.append(SOLVE_5)
	HINT_5 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_5)
	EXCEPTION_5 = []
	EXCEPTIONS.append(EXCEPTION_5)

	BASIC_50 = Mul(dx, Pow(x, Integer(-2)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2)))
	TEXT_50 = "Some text"
	SOLVE_50 = Add(log(Add(x, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2)))), Mul(Integer(-1), Pow(x, Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2))))
	BASIC.append(BASIC_50)
	TEXT.append(TEXT_50)
	SOLVE.append(SOLVE_50)
	HINT_50 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_50)
	EXCEPTION_50 = []
	EXCEPTIONS.append(EXCEPTION_50)

	BASIC_51 = Mul(dx, Pow(x, Integer(2)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(-1, 2)))
	TEXT_51 = "Some text"
	SOLVE_51 = Add(Mul(Rational(1, 2), Pow(Symbol('a'), Integer(2)), log(Add(x, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2))))), Mul(Rational(1, 2), x, Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2))))
	BASIC.append(BASIC_51)
	TEXT.append(TEXT_51)
	SOLVE.append(SOLVE_51)
	HINT_51 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_51)
	EXCEPTION_51 = []
	EXCEPTIONS.append(EXCEPTION_51)

	BASIC_52 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(-1, 2)))
	TEXT_52 = "Some text"
	SOLVE_52 = Mul(Pow(Symbol('a'), Integer(-1)), asec(Mul(Pow(Symbol('a'), Integer(-1)), x)))
	BASIC.append(BASIC_52)
	TEXT.append(TEXT_52)
	SOLVE.append(SOLVE_52)
	HINT_52 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_52)
	EXCEPTION_52 = []
	EXCEPTIONS.append(EXCEPTION_52)

	BASIC_53 = Mul(dx, Pow(x, Integer(-2)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(-1, 2)))
	TEXT_53 = "Some text"
	SOLVE_53 = Mul(Pow(Symbol('a'), Integer(-2)), Pow(x, Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Pow(x, Integer(2))), Rational(1, 2)))
	BASIC.append(BASIC_53)
	TEXT.append(TEXT_53)
	SOLVE.append(SOLVE_53)
	HINT_53 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_53)
	EXCEPTION_53 = []
	EXCEPTIONS.append(EXCEPTION_53)

	BASIC_54 = Mul(dx, Pow(sin(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_54 = "Some text"
	SOLVE_54 = Add(Mul(Rational(1, 2), x), Mul(Integer(-1), Rational(1, 4), Pow(Symbol('a'), Integer(-1)), sin(Mul(Integer(2), Symbol('a'), x))))
	BASIC.append(BASIC_54)
	TEXT.append(TEXT_54)
	SOLVE.append(SOLVE_54)
	HINT_54 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_54)
	EXCEPTION_54 = []
	EXCEPTIONS.append(EXCEPTION_54)

	BASIC_55 = Mul(dx, Pow(cos(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_55 = "Some text"
	SOLVE_55 = Add(Mul(Rational(1, 2), x), Mul(Rational(1, 4), Pow(Symbol('a'), Integer(-1)), sin(Mul(Integer(2), Symbol('a'), x))))
	BASIC.append(BASIC_55)
	TEXT.append(TEXT_55)
	SOLVE.append(SOLVE_55)
	HINT_55 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_55)
	EXCEPTION_55 = []
	EXCEPTIONS.append(EXCEPTION_55)

	BASIC_56 = Mul(dx, sin(Mul(Symbol('a'), x)), cos(Mul(Symbol('b'), x)))
	TEXT_56 = "Some text"
	SOLVE_56 = Add(Mul(Integer(-1), x, Pow(Add(Mul(Integer(2), Symbol('a')), Mul(Integer(2), Symbol('b'))), Integer(-1)), cos(Add(Symbol('a'), Symbol('b')))), Mul(Integer(-1), x, Pow(Add(Mul(Integer(2), Symbol('a')), Mul(Integer(-1), Integer(2), Symbol('b'))), Integer(-1)), cos(Add(Symbol('a'), Mul(Integer(-1), Symbol('b'))))))
	BASIC.append(BASIC_56)
	TEXT.append(TEXT_56)
	SOLVE.append(SOLVE_56)
	HINT_56 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_56)
	EXCEPTION_56 = [{"symbol":Pow(Symbol('b'), Integer(2)), "value":Pow(Symbol('a'), Integer(2)), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_56)

	BASIC_57 = Mul(dx, sin(Mul(Symbol('a'), x)), sin(Mul(Symbol('b'), x)))
	TEXT_57 = "Some text"
	SOLVE_57 = Add(Mul(Integer(-1), x, Pow(Add(Mul(Integer(2), Symbol('a')), Mul(Integer(2), Symbol('b'))), Integer(-1)), sin(Add(Symbol('a'), Symbol('b')))), Mul(x, Pow(Add(Mul(Integer(2), Symbol('a')), Mul(Integer(-1), Integer(2), Symbol('b'))), Integer(-1)), sin(Add(Symbol('a'), Mul(Integer(-1), Symbol('b'))))))
	BASIC.append(BASIC_57)
	TEXT.append(TEXT_57)
	SOLVE.append(SOLVE_57)
	HINT_57 = [[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('b'), "value":1}],[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('b'), "value":1}]]
	HINTS.append(HINT_57)
	EXCEPTION_57 = [{"symbol":Pow(Symbol('b'), Integer(2)), "value":Pow(Symbol('a'), Integer(2)), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_57)

	BASIC_58 = Mul(dx, cos(Mul(Symbol('a'), x)), cos(Mul(Symbol('b'), x)))
	TEXT_58 = "Some text"
	SOLVE_58 = Add(Mul(x, Pow(Add(Mul(Integer(2), Symbol('a')), Mul(Integer(2), Symbol('b'))), Integer(-1)), sin(Add(Symbol('a'), Symbol('b')))), Mul(x, Pow(Add(Mul(Integer(2), Symbol('a')), Mul(Integer(-1), Integer(2), Symbol('b'))), Integer(-1)), sin(Add(Symbol('a'), Mul(Integer(-1), Symbol('b'))))))
	BASIC.append(BASIC_58)
	TEXT.append(TEXT_58)
	SOLVE.append(SOLVE_58)
	HINT_58 = [[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('b'), "value":1}],[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('b'), "value":1}]]
	HINTS.append(HINT_58)
	EXCEPTION_58 = [{"symbol":Pow(Symbol('b'), Integer(2)), "value":Pow(Symbol('a'), Integer(2)), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_58)

	BASIC_59 = Mul(dx, Pow(sin(Mul(Symbol('a'), x)), Symbol('n')), cos(Mul(Symbol('a'), x)))
	TEXT_59 = "Some text"
	SOLVE_59 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), Pow(sin(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(1))))
	BASIC.append(BASIC_59)
	TEXT.append(TEXT_59)
	SOLVE.append(SOLVE_59)
	HINT_59 = [[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_59)
	EXCEPTION_59 = [{"symbol":Pow(Symbol('b'), Integer(2)), "value":Pow(Symbol('a'), Integer(2)), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_59)

	BASIC_6 = Mul(dx, cos(Mul(Symbol('a'), x)))
	TEXT_6 = "Some text"
	SOLVE_6 = Mul(Pow(Symbol('a'), Integer(-1)), sin(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_6)
	TEXT.append(TEXT_6)
	SOLVE.append(SOLVE_6)
	HINT_6 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_6)
	EXCEPTION_6 = []
	EXCEPTIONS.append(EXCEPTION_6)

	BASIC_60 = Mul(dx, sin(Mul(Symbol('a'), x)), Pow(cos(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_60 = "Some text"
	SOLVE_60 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), Pow(cos(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(1))))
	BASIC.append(BASIC_60)
	TEXT.append(TEXT_60)
	SOLVE.append(SOLVE_60)
	HINT_60 = [[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_60)
	EXCEPTION_60 = [{"symbol":Pow(Symbol('b'), Integer(2)), "value":Pow(Symbol('a'), Integer(2)), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_60)

	BASIC_61 = Mul(dx, sin(Mul(Symbol('a'), x)), Pow(cos(Mul(Symbol('a'), x)), Integer(-1)))
	TEXT_61 = "Some text"
	SOLVE_61 = Mul(Pow(Symbol('a'), Integer(-1)), log(sec(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_61)
	TEXT.append(TEXT_61)
	SOLVE.append(SOLVE_61)
	HINT_61 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_61)
	EXCEPTION_61 = []
	EXCEPTIONS.append(EXCEPTION_61)

	BASIC_62 = Mul(dx, Pow(sin(Mul(Symbol('a'), x)), Integer(-1)), cos(Mul(Symbol('a'), x)))
	TEXT_62 = "Some text"
	SOLVE_62 = Mul(Pow(Symbol('a'), Integer(-1)), log(sin(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_62)
	TEXT.append(TEXT_62)
	SOLVE.append(SOLVE_62)
	HINT_62 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_62)
	EXCEPTION_62 = []
	EXCEPTIONS.append(EXCEPTION_62)

	BASIC_63 = Mul(dx, Pow(Add(Symbol('b'), Mul(Symbol('c'), sin(Mul(Symbol('a'), x)))), Integer(-1)))
	TEXT_63 = "Some text"
	SOLVE_63 = Mul(Integer(-1), Integer(2), Pow(Symbol('a'), Integer(-1)), Pow(Add(Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Pow(Symbol('c'), Integer(2)))), Rational(-1, 2)), atan(Mul(Pow(Mul(Add(Symbol('b'), Mul(Integer(-1), Symbol('c'))), Pow(Add(Symbol('b'), Symbol('c')), Integer(-1))), Rational(1, 2)), cot(Add(Mul(Rational(1, 2), Symbol('a'), x), Mul(Rational(1, 4), pi))))))
	BASIC.append(BASIC_63)
	TEXT.append(TEXT_63)
	SOLVE.append(SOLVE_63)
	HINT_63 = [[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('c'), "value":1}],[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('c'), "value":1}]]
	HINTS.append(HINT_63)
	EXCEPTION_63 = [{"symbol":Pow(Symbol('b'), Integer(2)), "value":Pow(Symbol('c'), Integer(2)), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_63)

	BASIC_64 = Mul(dx, Pow(Add(Symbol('b'), Mul(Symbol('c'), sin(Mul(Symbol('a'), x)))), Integer(-1)))
	TEXT_64 = "Some text"
	SOLVE_64 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(2))), Pow(Symbol('c'), Integer(2))), Rational(-1, 2)), log(Mul(Pow(Add(Symbol('b'), Mul(Symbol('c'), sin(Mul(Symbol('a'), x)))), Integer(-1)), Add(Mul(Symbol('b'), sin(Mul(Symbol('a'), x))), Symbol('c'), Mul(Pow(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(2))), Pow(Symbol('c'), Integer(2))), Rational(1, 2)), cos(Mul(Symbol('a'), x)))))))
	BASIC.append(BASIC_64)
	TEXT.append(TEXT_64)
	SOLVE.append(SOLVE_64)
	HINT_64 = [[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('c'), "value":1}],[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('c'), "value":1}]]
	HINTS.append(HINT_64)
	EXCEPTION_64 = [{"symbol":Pow(Symbol('c'), Integer(2)), "value":Pow(Symbol('b'), Integer(2)), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_64)

	BASIC_65 = Mul(dx, Pow(Add(sin(Mul(Symbol('a'), x)), Integer(1)), Integer(-1)))
	TEXT_65 = "Some text"
	SOLVE_65 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), cot(Add(Mul(Rational(1, 2), Symbol('a'), x), Mul(Rational(1, 4), pi))))
	BASIC.append(BASIC_65)
	TEXT.append(TEXT_65)
	SOLVE.append(SOLVE_65)
	HINT_65 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_65)
	EXCEPTION_65 = []
	EXCEPTIONS.append(EXCEPTION_65)

	BASIC_66 = Mul(dx, Pow(Add(Integer(1), Mul(Integer(-1), sin(Mul(Symbol('a'), x)))), Integer(-1)))
	TEXT_66 = "Some text"
	SOLVE_66 = Mul(Pow(Symbol('a'), Integer(-1)), tan(Add(Mul(Rational(1, 2), Symbol('a'), x), Mul(Rational(1, 4), pi))))
	BASIC.append(BASIC_66)
	TEXT.append(TEXT_66)
	SOLVE.append(SOLVE_66)
	HINT_66 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_66)
	EXCEPTION_66 = []
	EXCEPTIONS.append(EXCEPTION_66)

	BASIC_67 = Mul(dx, Pow(Add(Symbol('b'), Mul(Symbol('c'), cos(Mul(Symbol('a'), x)))), Integer(-1)))
	TEXT_67 = "Some text"
	SOLVE_67 = Mul(Integer(2), Pow(Symbol('a'), Integer(-1)), Pow(Add(Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Pow(Symbol('c'), Integer(2)))), Rational(-1, 2)), cot(Mul(Pow(Mul(Add(Symbol('b'), Mul(Integer(-1), Symbol('c'))), Pow(Add(Symbol('b'), Symbol('c')), Integer(-1))), Rational(1, 2)), tan(Mul(Rational(1, 2), Symbol('a'), x)))))
	BASIC.append(BASIC_67)
	TEXT.append(TEXT_67)
	SOLVE.append(SOLVE_67)
	HINT_67 = [[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('c'), "value":1}],[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('c'), "value":1}]]
	HINTS.append(HINT_67)
	EXCEPTION_67 = [{"symbol":Pow(Symbol('b'), Integer(2)), "value":Pow(Symbol('c'), Integer(2)), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_67)

	BASIC_68 = Mul(dx, Pow(Add(Symbol('b'), Mul(Symbol('c'), cos(Mul(Symbol('a'), x)))), Integer(-1)))
	TEXT_68 = "Some text"
	SOLVE_68 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(2))), Pow(Symbol('c'), Integer(2))), Rational(-1, 2)), log(Mul(Pow(Add(Symbol('b'), Mul(Symbol('c'), cos(Mul(Symbol('a'), x)))), Integer(-1)), Add(Mul(Symbol('b'), cos(Mul(Symbol('a'), x))), Symbol('c'), Mul(Pow(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(2))), Pow(Symbol('c'), Integer(2))), Rational(1, 2)), sin(Mul(Symbol('a'), x)))))))
	BASIC.append(BASIC_68)
	TEXT.append(TEXT_68)
	SOLVE.append(SOLVE_68)
	HINT_68 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('c'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('c'), "value":1}]]
	HINTS.append(HINT_68)
	EXCEPTION_68 = [{"symbol":Pow(Symbol('c'), Integer(2)), "value":Pow(Symbol('b'), Integer(2)), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_68)

	BASIC_69 = Mul(dx, Pow(Add(Mul(Symbol('c'), cos(Mul(Symbol('a'), x))), Integer(1)), Integer(-1)))
	TEXT_69 = "Some text"
	SOLVE_69 = Mul(Pow(Symbol('a'), Integer(-1)), tan(Mul(Rational(1, 2), Symbol('a'), x)))
	BASIC.append(BASIC_69)
	TEXT.append(TEXT_69)
	SOLVE.append(SOLVE_69)
	HINT_69 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('c'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('c'), "value":1}]]
	HINTS.append(HINT_69)
	EXCEPTION_69 = []
	EXCEPTIONS.append(EXCEPTION_69)

	BASIC_7 = Mul(dx, Pow(sec(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_7 = "Some text"
	SOLVE_7 = Mul(Pow(Symbol('a'), Integer(-1)), tan(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_7)
	TEXT.append(TEXT_7)
	SOLVE.append(SOLVE_7)
	HINT_7 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_7)
	EXCEPTION_7 = []
	EXCEPTIONS.append(EXCEPTION_7)

	BASIC_70 = Mul(dx, Pow(Add(Mul(Symbol('c'), cos(Mul(Symbol('a'), x))), Integer(1)), Integer(-1)))
	TEXT_70 = "Some text"
	SOLVE_70 = Mul(Pow(Symbol('a'), Integer(-1)), cot(Mul(Rational(1, 2), Symbol('a'), x)))
	BASIC.append(BASIC_70)
	TEXT.append(TEXT_70)
	SOLVE.append(SOLVE_70)
	HINT_70 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('c'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('c'), "value":1}]]
	HINTS.append(HINT_70)
	EXCEPTION_70 = []
	EXCEPTIONS.append(EXCEPTION_70)

	BASIC_71 = Mul(dx, x, sin(Mul(Symbol('a'), x)))
	TEXT_71 = "Some text"
	SOLVE_71 = Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), x, cos(Mul(Symbol('a'), x))), Mul(Pow(Symbol('a'), Integer(-2)), sin(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_71)
	TEXT.append(TEXT_71)
	SOLVE.append(SOLVE_71)
	HINT_71 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_71)
	EXCEPTION_71 = []
	EXCEPTIONS.append(EXCEPTION_71)

	BASIC_72 = Mul(dx, x, cos(Mul(Symbol('a'), x)))
	TEXT_72 = "Some text"
	SOLVE_72 = Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), x, sin(Mul(Symbol('a'), x))), Mul(Pow(Symbol('a'), Integer(-2)), cos(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_72)
	TEXT.append(TEXT_72)
	SOLVE.append(SOLVE_72)
	HINT_72 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_72)
	EXCEPTION_72 = []
	EXCEPTIONS.append(EXCEPTION_72)

	BASIC_73 = Mul(dx, tan(Mul(Symbol('a'), x)))
	TEXT_73 = "Some text"
	SOLVE_73 = Mul(Pow(Symbol('a'), Integer(-1)), log(sec(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_73)
	TEXT.append(TEXT_73)
	SOLVE.append(SOLVE_73)
	HINT_73 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_73)
	EXCEPTION_73 = []
	EXCEPTIONS.append(EXCEPTION_73)

	BASIC_74 = Mul(dx, cot(Mul(Symbol('a'), x)))
	TEXT_74 = "Some text"
	SOLVE_74 = Mul(Pow(Symbol('a'), Integer(-1)), log(sin(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_74)
	TEXT.append(TEXT_74)
	SOLVE.append(SOLVE_74)
	HINT_74 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_74)
	EXCEPTION_74 = []
	EXCEPTIONS.append(EXCEPTION_74)

	BASIC_75 = Mul(dx, Pow(tan(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_75 = "Some text"
	SOLVE_75 = Add(Mul(Integer(-1), x), Mul(Pow(Symbol('a'), Integer(-1)), tan(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_75)
	TEXT.append(TEXT_75)
	SOLVE.append(SOLVE_75)
	HINT_75 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_75)
	EXCEPTION_75 = []
	EXCEPTIONS.append(EXCEPTION_75)

	BASIC_76 = Mul(dx, Pow(cot(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_76 = "Some text"
	SOLVE_76 = Add(Mul(Integer(-1), x), Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), cot(Mul(Symbol('a'), x))))
	BASIC.append(BASIC_76)
	TEXT.append(TEXT_76)
	SOLVE.append(SOLVE_76)
	HINT_76 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_76)
	EXCEPTION_76 = []
	EXCEPTIONS.append(EXCEPTION_76)

	BASIC_77 = Mul(dx, sec(Mul(Symbol('a'), x)))
	TEXT_77 = "Some text"
	SOLVE_77 = Mul(Pow(Symbol('a'), Integer(-1)), log(Add(tan(Mul(Symbol('a'), x)), sec(Mul(Symbol('a'), x)))))
	BASIC.append(BASIC_77)
	TEXT.append(TEXT_77)
	SOLVE.append(SOLVE_77)
	HINT_77 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_77)
	EXCEPTION_77 = []
	EXCEPTIONS.append(EXCEPTION_77)

	BASIC_78 = Mul(dx, csc(Mul(Symbol('a'), x)))
	TEXT_78 = "Some text"
	SOLVE_78 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), log(Add(cot(Mul(Symbol('a'), x)), csc(Mul(Symbol('a'), x)))))
	BASIC.append(BASIC_78)
	TEXT.append(TEXT_78)
	SOLVE.append(SOLVE_78)
	HINT_78 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_78)
	EXCEPTION_78 = []
	EXCEPTIONS.append(EXCEPTION_78)

	BASIC_79 = Mul(dx, Pow(sec(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_79 = "Some text"
	SOLVE_79 = Mul(Pow(Symbol('a'), Integer(-1)), tan(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_79)
	TEXT.append(TEXT_79)
	SOLVE.append(SOLVE_79)
	HINT_79 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_79)
	EXCEPTION_79 = []
	EXCEPTIONS.append(EXCEPTION_79)

	BASIC_8 = Mul(dx, Pow(csc(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_8 = "Some text"
	SOLVE_8 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), cot(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_8)
	TEXT.append(TEXT_8)
	SOLVE.append(SOLVE_8)
	HINT_8 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_8)
	EXCEPTION_8 = []
	EXCEPTIONS.append(EXCEPTION_8)

	BASIC_80 = Mul(dx, Pow(csc(Mul(Symbol('a'), x)), Integer(2)))
	TEXT_80 = "Some text"
	SOLVE_80 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), cot(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_80)
	TEXT.append(TEXT_80)
	SOLVE.append(SOLVE_80)
	HINT_80 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_80)
	EXCEPTION_80 = []
	EXCEPTIONS.append(EXCEPTION_80)

	BASIC_81 = Mul(dx, tan(Mul(Symbol('a'), x)), Pow(sec(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_81 = "Some text"
	SOLVE_81 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Symbol('n'), Integer(-1)), Pow(sec(Mul(Symbol('a'), x)), Integer(2)))
	BASIC.append(BASIC_81)
	TEXT.append(TEXT_81)
	SOLVE.append(SOLVE_81)
	HINT_81 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_81)
	EXCEPTION_81 = []
	EXCEPTIONS.append(EXCEPTION_81)

	BASIC_82 = Mul(dx, cot(Mul(Symbol('a'), x)), Pow(csc(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_82 = "Some text"
	SOLVE_82 = Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Symbol('n'), Integer(-1)), Pow(csc(Mul(Symbol('a'), x)), Integer(2)))
	BASIC.append(BASIC_82)
	TEXT.append(TEXT_82)
	SOLVE.append(SOLVE_82)
	HINT_82 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('n'), "value":1}]]
	HINTS.append(HINT_82)
	EXCEPTION_82 = []
	EXCEPTIONS.append(EXCEPTION_82)

	BASIC_83 = Mul(dx, asin(Mul(Symbol('a'), x)))
	TEXT_83 = "Some text"
	SOLVE_83 = Add(Mul(x, asin(Mul(Symbol('a'), x))), Mul(Pow(Symbol('a'), Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Integer(1)), Rational(1, 2))))
	BASIC.append(BASIC_83)
	TEXT.append(TEXT_83)
	SOLVE.append(SOLVE_83)
	HINT_83 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_83)
	EXCEPTION_83 = []
	EXCEPTIONS.append(EXCEPTION_83)

	BASIC_84 = Mul(dx, acos(Mul(Symbol('a'), x)))
	TEXT_84 = "Some text"
	SOLVE_84 = Add(Mul(x, acos(Mul(Symbol('a'), x))), Mul(Integer(-1), Pow(Symbol('a'), Integer(-1)), Pow(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Integer(1)), Rational(1, 2))))
	BASIC.append(BASIC_84)
	TEXT.append(TEXT_84)
	SOLVE.append(SOLVE_84)
	HINT_84 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_84)
	EXCEPTION_84 = []
	EXCEPTIONS.append(EXCEPTION_84)

	BASIC_85 = Mul(dx, atan(Mul(Symbol('a'), x)))
	TEXT_85 = "Some text"
	SOLVE_85 = Add(Mul(x, atan(Mul(Symbol('a'), x))), Mul(Rational(1, 2), Pow(Symbol('a'), Integer(-1)), log(Add(Mul(Pow(Symbol('a'), Integer(2)), Pow(x, Integer(2))), Integer(1)))))
	BASIC.append(BASIC_85)
	TEXT.append(TEXT_85)
	SOLVE.append(SOLVE_85)
	HINT_85 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_85)
	EXCEPTION_85 = []
	EXCEPTIONS.append(EXCEPTION_85)

	BASIC_86 = Mul(dx, exp(Mul(Symbol('a'), x)))
	TEXT_86 = "Some text"
	SOLVE_86 = Mul(Pow(Symbol('a'), Integer(-1)), exp(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_86)
	TEXT.append(TEXT_86)
	SOLVE.append(SOLVE_86)
	HINT_86 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_86)
	EXCEPTION_86 = []
	EXCEPTIONS.append(EXCEPTION_86)

	BASIC_87 = Mul(Pow(Symbol('b'), Mul(Symbol('a'), x)), dx)
	TEXT_87 = "Some text"
	SOLVE_87 = Mul(Pow(Symbol('a'), Integer(-1)), Pow(Symbol('b'), Mul(Symbol('a'), x)), Pow(log(Symbol('b')), Integer(-1)))
	BASIC.append(BASIC_87)
	TEXT.append(TEXT_87)
	SOLVE.append(SOLVE_87)
	HINT_87 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('b'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('b'), "value":1}]]
	HINTS.append(HINT_87)
	EXCEPTION_87 = []
	EXCEPTIONS.append(EXCEPTION_87)

	BASIC_88 = Mul(dx, x, exp(Mul(Symbol('a'), x)))
	TEXT_88 = "Some text"
	SOLVE_88 = Mul(Pow(Symbol('a'), Integer(-2)), Add(Mul(Symbol('a'), x), Integer(-1)), exp(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_88)
	TEXT.append(TEXT_88)
	SOLVE.append(SOLVE_88)
	HINT_88 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_88)
	EXCEPTION_88 = []
	EXCEPTIONS.append(EXCEPTION_88)

	BASIC_89 = Mul(dx, exp(Mul(Symbol('a'), x)), sin(Mul(Symbol('b'), x)))
	TEXT_89 = "Some text"
	SOLVE_89 = Mul(Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Integer(-1)), Add(Mul(Symbol('a'), sin(Mul(Symbol('b'), x))), Mul(Integer(-1), Symbol('b'), cos(Mul(Symbol('b'), x)))), exp(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_89)
	TEXT.append(TEXT_89)
	SOLVE.append(SOLVE_89)
	HINT_89 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('b'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('b'), "value":1}]]
	HINTS.append(HINT_89)
	EXCEPTION_89 = []
	EXCEPTIONS.append(EXCEPTION_89)

	BASIC_9 = Mul(dx, tan(Mul(Symbol('a'), x)), sec(Mul(Symbol('a'), x)))
	TEXT_9 = "Some text"
	SOLVE_9 = Mul(Pow(Symbol('a'), Integer(-1)), sec(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_9)
	TEXT.append(TEXT_9)
	SOLVE.append(SOLVE_9)
	HINT_9 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_9)
	EXCEPTION_9 = []
	EXCEPTIONS.append(EXCEPTION_9)

	BASIC_90 = Mul(dx, exp(Mul(Symbol('a'), x)), cos(Mul(Symbol('b'), x)))
	TEXT_90 = "Some text"
	SOLVE_90 = Mul(Pow(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Integer(-1)), Add(Mul(Symbol('a'), cos(Mul(Symbol('b'), x))), Mul(Symbol('b'), sin(Mul(Symbol('b'), x)))), exp(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_90)
	TEXT.append(TEXT_90)
	SOLVE.append(SOLVE_90)
	HINT_90 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('b'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('b'), "value":1}]]
	HINTS.append(HINT_90)
	EXCEPTION_90 = []
	EXCEPTIONS.append(EXCEPTION_90)

	BASIC_91 = Mul(dx, log(Mul(Symbol('a'), x)))
	TEXT_91 = "Some text"
	SOLVE_91 = Add(Mul(x, log(Mul(Symbol('a'), x))), Mul(Integer(-1), x))
	BASIC.append(BASIC_91)
	TEXT.append(TEXT_91)
	SOLVE.append(SOLVE_91)
	HINT_91 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_91)
	EXCEPTION_91 = []
	EXCEPTIONS.append(EXCEPTION_91)

	BASIC_92 = Mul(dx, Pow(x, Integer(-1)), Pow(log(Mul(Symbol('a'), x)), Symbol('n')))
	TEXT_92 = "Some text"
	SOLVE_92 = Mul(Pow(Add(Symbol('n'), Integer(1)), Integer(-1)), Pow(log(Mul(Symbol('a'), x)), Add(Symbol('n'), Integer(1))))
	BASIC.append(BASIC_92)
	TEXT.append(TEXT_92)
	SOLVE.append(SOLVE_92)
	HINT_92 = [[{"symbol":Symbol('a'), "value":1}],[{"symbol":Symbol('n'), "value":1}],[{"symbol":Symbol('a'), "value":1},{"symbol":Symbol('n'), "value":1}]]
	HINTS.append(HINT_92)
	EXCEPTION_92 = [{"symbol":Symbol('n'), "value":Integer(-1), "type":"neq"}]
	EXCEPTIONS.append(EXCEPTION_92)

	BASIC_93 = Mul(dx, Pow(x, Integer(-1)), Pow(log(Mul(Symbol('a'), x)), Integer(-1)))
	TEXT_93 = "Some text"
	SOLVE_93 = log(log(Mul(Symbol('a'), x)))
	BASIC.append(BASIC_93)
	TEXT.append(TEXT_93)
	SOLVE.append(SOLVE_93)
	HINT_93 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_93)
	EXCEPTION_93 = []
	EXCEPTIONS.append(EXCEPTION_93)

	BASIC_94 = Mul(dx, Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(-1, 2)))
	TEXT_94 = "Some text"
	SOLVE_94 = asin(Mul(Pow(Symbol('a'), Integer(-1)), Add(Mul(Integer(-1), Symbol('a')), x)))
	BASIC.append(BASIC_94)
	TEXT.append(TEXT_94)
	SOLVE.append(SOLVE_94)
	HINT_94 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_94)
	EXCEPTION_94 = [{"symbol":Symbol('a'), "value":Integer(0), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_94)

	BASIC_95 = Mul(dx, Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)))
	TEXT_95 = "Some text"
	SOLVE_95 = Add(Mul(Rational(1, 2), Pow(Symbol('a'), Integer(2)), asin(Mul(Pow(Symbol('a'), Integer(-1)), Add(Mul(Integer(-1), Symbol('a')), x)))), Mul(Rational(1, 2), Add(Mul(Integer(-1), Symbol('a')), x), Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2))))
	BASIC.append(BASIC_95)
	TEXT.append(TEXT_95)
	SOLVE.append(SOLVE_95)
	HINT_95 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_95)
	EXCEPTION_95 = [{"symbol":Symbol('a'), "value":Integer(0), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_95)

	BASIC_96 = Mul(dx, x, Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)))
	TEXT_96 = "Some text"
	SOLVE_96 = asin(Mul(Pow(Symbol('a'), Integer(-1)), Add(Mul(Integer(-1), Symbol('a')), x)))
	BASIC.append(BASIC_96)
	TEXT.append(TEXT_96)
	SOLVE.append(SOLVE_96)
	HINT_96 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_96)
	EXCEPTION_96 = [{"symbol":Symbol('a'), "value":Integer(0), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_96)

	BASIC_97 = Mul(dx, Pow(x, Integer(-1)), Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)))
	TEXT_97 = "Some text"
	SOLVE_97 = Add(Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)), asin(Mul(Pow(Symbol('a'), Integer(-1)), Add(Mul(Integer(-1), Symbol('a')), x))))
	BASIC.append(BASIC_97)
	TEXT.append(TEXT_97)
	SOLVE.append(SOLVE_97)
	HINT_97 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_97)
	EXCEPTION_97 = [{"symbol":Symbol('a'), "value":Integer(0), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_97)

	BASIC_98 = Mul(dx, Pow(x, Integer(-2)), Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2)))
	TEXT_98 = "Some text"
	SOLVE_98 = Add(Mul(Integer(-1), Integer(2), Pow(Mul(Pow(x, Integer(-1)), Add(Mul(Integer(2), Symbol('a')), Mul(Integer(-1), x))), Rational(1, 2))), Mul(Integer(-1), asin(Mul(Pow(Symbol('a'), Integer(-1)), Add(Mul(Integer(-1), Symbol('a')), x)))))
	BASIC.append(BASIC_98)
	TEXT.append(TEXT_98)
	SOLVE.append(SOLVE_98)
	HINT_98 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_98)
	EXCEPTION_98 = [{"symbol":Symbol('a'), "value":Integer(0), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_98)

	BASIC_99 = Mul(dx, x, Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(-1, 2)))
	TEXT_99 = "Some text"
	SOLVE_99 = Add(Mul(Symbol('a'), asin(Mul(Pow(Symbol('a'), Integer(-1)), Add(Mul(Integer(-1), Symbol('a')), x)))), Mul(Integer(-1), Pow(Add(Mul(Integer(2), Symbol('a'), x), Mul(Integer(-1), Pow(x, Integer(2)))), Rational(1, 2))))
	BASIC.append(BASIC_99)
	TEXT.append(TEXT_99)
	SOLVE.append(SOLVE_99)
	HINT_99 = [[{"symbol":Symbol('a'), "value":1}]]
	HINTS.append(HINT_99)
	EXCEPTION_99 = [{"symbol":Symbol('a'), "value":Integer(0), "type":"g"}]
	EXCEPTIONS.append(EXCEPTION_99)

	index = 0
	for HINT in HINTS:
		for STATE in HINT:
			if len(STATE) > 0:
				new_bas = BASIC[index]
				new_solve = SOLVE[index]
				for CHANGE in STATE:
					new_bas = new_bas.subs(CHANGE['symbol'], CHANGE['value'])
					new_solve = new_solve.subs(CHANGE['symbol'], CHANGE['value'])
				BASIC.append(new_bas)
				SOLVE.append(new_solve)
		index = index + 1
