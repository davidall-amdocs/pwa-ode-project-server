from sympy import *

dx = Symbol('dx')
x = Symbol('x')
n = Symbol('n')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

BASIC = []
TEXT = []
SOLVE = []

BASIC_001 = dx
TEXT_001 = "Some text"
SOLVE_001 = x
BASIC.append(BASIC_001)
TEXT.append(TEXT_001)
SOLVE.append(SOLVE_001)

BASIC_002 = Mul(Pow(x, n), dx)
TEXT_002 = "Some text"
SOLVE_002 = Mul(Pow(x, Add(n, Integer(1))), Pow(Add(n, Integer(1)), Integer(-1)))
BASIC.append(BASIC_002)
TEXT.append(TEXT_002)
SOLVE.append(SOLVE_002)

BASIC_003 = Mul(Pow(x, Integer(-1)), dx)
TEXT_003 = "Some text"
SOLVE_003 = log(x)
BASIC.append(BASIC_003)
TEXT.append(TEXT_003)
SOLVE.append(SOLVE_003)

BASIC_004 = Mul(Pow(E, x), dx)
TEXT_004 = "Some text"
SOLVE_004 = Pow(E, x)
BASIC.append(BASIC_004)
TEXT.append(TEXT_004)
SOLVE.append(SOLVE_004)

BASIC_005 = Mul(Pow(a, x), dx)
TEXT_005 = "Some text"
SOLVE_005 = Mul(Pow(log(a), Integer(-1)), Pow(a, x))
BASIC.append(BASIC_005)
TEXT.append(TEXT_005)
SOLVE.append(SOLVE_005)

BASIC_006 = Mul(sin(Mul(a, x)), dx)
TEXT_006 = "Some text"
SOLVE_006 = Mul(Integer(-1), Mul(cos(Mul(a, x)), Pow(a, Integer(-1))))
BASIC.append(BASIC_006)
TEXT.append(TEXT_006)
SOLVE.append(SOLVE_006)

BASIC_007 = Mul(cos(Mul(a, x)), dx)
TEXT_007 = "Some text"
SOLVE_007 = Mul(Mul(sin(Mul(a, x)), Pow(a, Integer(-1))))
BASIC.append(BASIC_007)
TEXT.append(TEXT_007)
SOLVE.append(SOLVE_007)

BASIC_008 = Mul(Pow(sec(Mul(a, x)), Integer(2)), dx)
TEXT_008 = "Some text"
SOLVE_008 = Mul(tan(Mul(a, x)), Pow(a, Integer(-1)))
BASIC.append(BASIC_008)
TEXT.append(TEXT_008)
SOLVE.append(SOLVE_008)

BASIC_009 = Mul(Pow(csc(Mul(a, x)), Integer(2)), dx)
TEXT_009 = "Some text"
SOLVE_009 = Mul(Integer(-1), cot(Mul(a, x)), Pow(a, Integer(-1)))
BASIC.append(BASIC_009)
TEXT.append(TEXT_009)
SOLVE.append(SOLVE_009)

BASIC_010 = Mul(sec(Mul(a, x)), tan(Mul(a, x)), dx)
TEXT_010 = "Some text"
SOLVE_010 = Mul(sec(Mul(a, x)), Pow(a, Integer(-1)))
BASIC.append(BASIC_010)
TEXT.append(TEXT_010)
SOLVE.append(SOLVE_010)

BASIC_011 = Mul(csc(Mul(a, x)), cot(Mul(a, x)), dx)
TEXT_011 = "Some text"
SOLVE_011 = Mul(Integer(-1), csc(Mul(a, x)), Pow(a, Integer(-1)))
BASIC.append(BASIC_011)
TEXT.append(TEXT_011)
SOLVE.append(SOLVE_011)

BASIC_012 = Mul(tan(Mul(a, x)), dx)
TEXT_012 = "Some text"
SOLVE_012 = Mul(log(sec(Mul(a, x))), Pow(a, Integer(-1)))
BASIC.append(BASIC_012)
TEXT.append(TEXT_012)
SOLVE.append(SOLVE_012)

BASIC_013 = Mul(cot(Mul(a, x)), dx)
TEXT_013 = "Some text"
SOLVE_013 = Mul(log(sin(Mul(a, x))), Pow(a, Integer(-1)))
BASIC.append(BASIC_013)
TEXT.append(TEXT_013)
SOLVE.append(SOLVE_013)

BASIC_014 = Mul(sinh(Mul(a, x)), dx)
TEXT_014 = "Some text"
SOLVE_014 = Mul(cosh(Mul(a, x)), Pow(a, Integer(-1)))
BASIC.append(BASIC_014)
TEXT.append(TEXT_014)
SOLVE.append(SOLVE_014)

BASIC_015 = Mul(cosh(Mul(a, x)), dx)
TEXT_015 = "Some text"
SOLVE_015 = Mul(sinh(Mul(a, x)), Pow(a, Integer(-1)))
BASIC.append(BASIC_015)
TEXT.append(TEXT_015)
SOLVE.append(SOLVE_015)

BASIC_016 = Mul(dx, Pow(sqrt(Add(Pow(a, Integer(2)), Mul(Integer(-1),Pow(x, Integer(2))))), Integer(-1)))
TEXT_016 = "Some text"
SOLVE_016 = asin(Mul(x, Pow(a, Integer(-1))))
BASIC.append(BASIC_016)
TEXT.append(TEXT_016)
SOLVE.append(SOLVE_016)

BASIC_017 = Mul(dx, Pow(Add(Pow(a, Integer(2)), Pow(x, Integer(2))), Integer(-1)))
TEXT_017 = "Some text"
SOLVE_017 = Mul(atan(Mul(x, Pow(a, Integer(-1)))), Pow(a, Integer(-1)))
BASIC.append(BASIC_017)
TEXT.append(TEXT_017)
SOLVE.append(SOLVE_017)

BASIC_018 = Mul(dx, Pow(Mul(x, sqrt(Add(Pow(x, Integer(2)), Mul(Integer(-1), Pow(a, Integer(2)))))), Integer(-1)))
TEXT_018 = "Some text"
SOLVE_018 = Mul(asec(Mul(x, Pow(a, Integer(-1)))), Pow(a, Integer(-1)))
BASIC.append(BASIC_018)
TEXT.append(TEXT_018)
SOLVE.append(SOLVE_018)

BASIC_019 = Mul(dx, Pow(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Integer(-1)))
TEXT_019 = "Some text"
SOLVE_019 = asinh(Mul(x, Pow(a, Integer(-1))))
BASIC.append(BASIC_019)
TEXT.append(TEXT_019)
SOLVE.append(SOLVE_019)

BASIC_020 = Mul(dx, Pow(sqrt(Add(Pow(x, Integer(2)), Mul(Integer(-1), Pow(a, Integer(2))))), Integer(-1)))
TEXT_020 = "Some text"
SOLVE_020 = acosh(Mul(x, Pow(a, Integer(-1))))
BASIC.append(BASIC_020)
TEXT.append(TEXT_020)
SOLVE.append(SOLVE_020)

BASIC_021 = Mul(Pow(Add(Mul(a, x), b), n), dx)
TEXT_021 = "Some text"
SOLVE_021 = Mul(Pow(Add(Mul(a, x), b), Add(n, Integer(1))), Pow(Mul(a, Add(n, Integer(1))), Integer(-1)))
BASIC.append(BASIC_021)
TEXT.append(TEXT_021)
SOLVE.append(SOLVE_021)

BASIC_022 = Mul(x, Pow(Add(Mul(a, x), b), n), dx)
TEXT_022 = "Some text"
SOLVE_022 = Mul(Mul(Pow(Add(Mul(a, x), b), Add(n, Integer(1))), Pow(Pow(a, 2), Integer(-1))), Add(Mul(Add(Mul(a, x), b), Pow(Add(n, Integer(2)), Integer(-1))), Mul(Mul(b, Pow(Add(n, Integer(1)), Integer(-1))), Integer(-1))))
BASIC.append(BASIC_022)
TEXT.append(TEXT_022)
SOLVE.append(SOLVE_022)

BASIC_023 = Mul(Pow(Add(Mul(a, x), b), Integer(-1)), dx)
TEXT_023 = "Some text"
SOLVE_023 = Mul(log(Add(Mul(a, x), b)), Pow(a, Integer(-1)))
BASIC.append(BASIC_023)
TEXT.append(TEXT_023)
SOLVE.append(SOLVE_023)

BASIC_024 = Mul(x, Pow(Add(Mul(a, x), b), Integer(-1)), dx)
TEXT_024 = "Some text"
SOLVE_024 = Add(Mul(x, Pow(a, Integer(-1))), Mul(Mul(Mul(b, Pow(Pow(a, Integer(2)), Integer(-1))), log(Add(Mul(a, x), b))), Integer(-1)))
BASIC.append(BASIC_024)
TEXT.append(TEXT_024)
SOLVE.append(SOLVE_024)

BASIC_025 = Mul(x, Pow(Pow(Add(Mul(a, x), b), Integer(2)), Integer(-1)), dx)
TEXT_025 = "Some text"
SOLVE_025 = Mul(Pow(Pow(a, Integer(2)), Integer(-1)), Add(log(Add(Mul(a, x), b)), Mul(b, Pow(Add(Mul(a, x), b), Integer(-1)))))
BASIC.append(BASIC_025)
TEXT.append(TEXT_025)
SOLVE.append(SOLVE_025)

BASIC_026 = Mul(Pow(Mul(x, Add(Mul(a, x), b)), Integer(-1)), dx)
TEXT_026 = "Some text"
SOLVE_026 = Mul(log(Mul(x, Pow(Add(Mul(a, x), b), Integer(-1)))), Pow(b, Integer(-1)))
BASIC.append(BASIC_026)
TEXT.append(TEXT_026)
SOLVE.append(SOLVE_026)

BASIC_027 = Mul(Pow(sqrt(Add(Mul(a, x), b)), n), dx)
TEXT_027 = "Some text"
SOLVE_027 = Mul(Mul(Integer(2), Pow(a, Integer(-1))), Mul(Pow(sqrt(Add(Mul(a, x), b)), Add(n, Integer(2))), Pow(Add(n, Integer(2)), Integer(-1))))
BASIC.append(BASIC_027)
TEXT.append(TEXT_027)
SOLVE.append(SOLVE_027)

BASIC_028 = Mul(Pow(Mul(x, sqrt(Add(Mul(a, x), b))), Integer(-1)), dx)
TEXT_028 = "Some text"
SOLVE_028 = Mul(Pow(sqrt(b), Integer(-1)), log(Mul(Add(sqrt(Add(Mul(a, x), b)), Mul(sqrt(b), Integer(-1))), Pow(Add(sqrt(Add(Mul(a, x), b)), sqrt(b)), Integer(-1)))))
BASIC.append(BASIC_028)
TEXT.append(TEXT_028)
SOLVE.append(SOLVE_028)

BASIC_029 = Mul(Pow(Mul(x, sqrt(Add(Mul(a, x), Mul(b, Integer(-1))))), Integer(-1)), dx)
TEXT_029 = "Some text"
SOLVE_029 = Mul(Mul(Integer(2), Pow(sqrt(b), Integer(-1))), atan(sqrt(Mul(Add(Mul(a, x), Mul(b, Integer(-1))), Pow(b, Integer(-1))))))
BASIC.append(BASIC_029)
TEXT.append(TEXT_029)
SOLVE.append(SOLVE_029)

BASIC_030 = Mul(Pow(Pow(Add(Pow(a, Integer(2)), Pow(x, Integer(2))), Integer(2)), Integer(-1)), dx)
TEXT_030 = "Some text"
SOLVE_030 = Add(Mul(x, Pow(Mul(Integer(2), Pow(a, Integer(2)), Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Integer(-1))), Mul(atan(Mul(x, Pow(a, Integer(-1)))), Pow(Mul(Integer(2), Pow(a, Integer(3))), Integer(-1))))
BASIC.append(BASIC_030)
TEXT.append(TEXT_030)
SOLVE.append(SOLVE_030)

BASIC_031 = Mul(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), dx)
TEXT_031 = "Some text"
SOLVE_031 = Add(Mul(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(Integer(2), Integer(-1))), Mul(Pow(a, Integer(2)), log(Add(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))))), Pow(Integer(2), Integer(-1))))
BASIC.append(BASIC_031)
TEXT.append(TEXT_031)
SOLVE.append(SOLVE_031)

BASIC_032 = Mul(Pow(x, Integer(2)), sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), dx) 
TEXT_032 = "Some text"
SOLVE_032 = Add(Mul(x, Add(Pow(a, Integer(2)), Mul(Integer(2), Pow(x, Integer(2)))), sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(Integer(8), Integer(-1))), Mul(Mul(Pow(a, Integer(4)), log(Add(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))))), Pow(Integer(8), Integer(-1))), Integer(-1)))
BASIC.append(BASIC_032)
TEXT.append(TEXT_032)
SOLVE.append(SOLVE_032)

BASIC_033 = Mul(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(x, Integer(-1)), dx)
TEXT_033 = "Some text"
SOLVE_033 = Add(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Mul(Mul(a, log(Mul(Add(a, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2))))), Pow(x, Integer(-1))))), Integer(-1)))
BASIC.append(BASIC_033)
TEXT.append(TEXT_033)
SOLVE.append(SOLVE_033)

BASIC_034 = Mul(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(Pow(x, Integer(2)), Integer(-1)), dx) 
TEXT_034 = "Some text"
SOLVE_034 = Add(log(Add(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))))), Mul(Mul(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(x, Integer(-1))), Integer(-1)))
BASIC.append(BASIC_034)
TEXT.append(TEXT_034)
SOLVE.append(SOLVE_034)

BASIC_035 = Mul(Pow(x, Integer(2)), Pow(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Integer(-1)), dx) 
TEXT_035 = "Some text"
SOLVE_035 = Add(Mul(Integer(-1), Pow(a, Integer(2)), log(Add(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))))), Pow(Integer(2), Integer(-1))), Mul(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(Integer(2), Integer(-1))))
BASIC.append(BASIC_035)
TEXT.append(TEXT_035)
SOLVE.append(SOLVE_035)

BASIC_036 = Mul(Pow(Mul(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2))))), Integer(-1)), dx)
TEXT_036 = "Some text"
SOLVE_036 = Mul(Integer(-1), Pow(a, Integer(-1)), log(Mul(Add(a, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2))))), Pow(x, Integer(-1)))))
BASIC.append(BASIC_036)
TEXT.append(TEXT_036)
SOLVE.append(SOLVE_036)

BASIC_037 = Mul(Pow(Mul(Pow(x, Integer(2)), sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2))))), Integer(-1)), dx)
TEXT_037 = "Some text"
SOLVE_037 = Mul(Integer(-1), Pow(Mul(Pow(a, Integer(2)), x), Integer(-1)), sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))))
BASIC.append(BASIC_037)
TEXT.append(TEXT_037)
SOLVE.append(SOLVE_037)

BASIC_038 = Mul(Pow(Add(Pow(a, Integer(2)), Mul(Pow(x, Integer(2)), Integer(-1))), Integer(-1)), dx)
TEXT_038 = "Some text"
SOLVE_038 = Mul(Pow(Mul(Integer(2), a), Integer(-1)), log(Mul(Add(x, a), Pow(Add(x, Mul(a, Integer(-1))), Integer(-1)))))
BASIC.append(BASIC_038)
TEXT.append(TEXT_038)
SOLVE.append(SOLVE_038)

BASIC_039 = Mul( dx, Pow( Pow( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ), Integer(2) ), Integer(-1) ) )
TEXT_039 = "Some text"
SOLVE_039 = Add( Mul( x, Pow( Mul( Integer(2), Pow( a, Integer(2) ), Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Integer(-1) ) ), Mul( log( Mul( Add( x, a ), Pow( Add( x, Mul( a, Integer(-1) ) ), Integer(-1) ) ) ), Pow( Mul( Integer(4), Pow( a, Integer(3) ) ), Integer(-1) ) ) )
BASIC.append(BASIC_039)
TEXT.append(TEXT_039)
SOLVE.append(SOLVE_039)

BASIC_040 = Mul( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), dx ) 
TEXT_040 = "Some text" 
SOLVE_040 = Add( Mul( x, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( Integer(2), Integer(-1) ) ), Mul( Pow( a, Integer(2) ), asin( Mul( x, Pow( a, Integer(-1) ) ) ), Pow( Integer(2), Integer(-1) ) ) )
BASIC.append(BASIC_040)
TEXT.append(TEXT_040)
SOLVE.append(SOLVE_040)

BASIC_041 = Mul( Pow( x, Integer(2) ), sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), dx ) 
TEXT_041 = "Some text" 
SOLVE_041 = Add( Mul( Pow( a, Integer(4) ), asin( Mul( x, Pow( a, Integer(-1) ) ) ), Pow( Integer(8), Integer(-1) ) ), Mul( Mul( x, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Add( Pow( a, Integer(2) ), Mul( Mul( Integer(2), Pow( x, Integer(2) ) ), Integer(-1) ) ), Pow( Integer(8), Integer(-1) ) ), Integer(-1) ) )
BASIC.append(BASIC_041)
TEXT.append(TEXT_041)
SOLVE.append(SOLVE_041)

BASIC_042 = Mul( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( x, Integer(-1) ), dx ) 
TEXT_042 = "Some text" 
SOLVE_042 = Add( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Mul( Mul( a, log( Mul( Add( a, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ) ), Pow( x, Integer(-1) ) ) ) ), Integer(-1) ) )
BASIC.append(BASIC_042)
TEXT.append(TEXT_042)
SOLVE.append(SOLVE_042)

BASIC_043 = Mul( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( Pow( x, Integer(2) ), Integer(-1) ), dx ) 
TEXT_043 = "Some text" 
SOLVE_043 = Add( Mul( asin( Mul( x, Pow( a, Integer(-1) ) ) ), Integer(-1) ), Mul( Mul( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( x, Integer(-1) ) ), Integer(-1) ) )
BASIC.append(BASIC_043)
TEXT.append(TEXT_043)
SOLVE.append(SOLVE_043)

BASIC_044 = Mul( Pow( x, Integer(2) ), Pow( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Integer(-1) ), dx ) 
TEXT_044 = "Some text" 
SOLVE_044 = Add( Mul( Pow( a, Integer(2) ), Pow( Integer(2), Integer(-1) ), asin( Mul( x, Pow( a, Integer(-1) ) ) ) ), Mul( Mul( x, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( Integer(2), Integer(-1) ) ), Integer(-1) ) )
BASIC.append(BASIC_044)
TEXT.append(TEXT_044)
SOLVE.append(SOLVE_044)

BASIC_045 = Mul( Pow( Mul( x, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ), dx ) 
TEXT_045 = "Some text" 
SOLVE_045 = Mul( log( Mul( Add( a, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ) ), Pow( x, Integer(-1) ) ) ), Pow( a, Integer(-1) ), Integer(-1) )
BASIC.append(BASIC_045)
TEXT.append(TEXT_045)
SOLVE.append(SOLVE_045)

BASIC_046 = Mul( dx, Pow( Mul( Pow( x, Integer(2) ), sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ) ) 
TEXT_046 = "Some text" 
SOLVE_046 = Mul( Mul( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( Mul( Pow( a, Integer(2) ), x ), Integer(-1) ) ), Integer(-1) )
BASIC.append(BASIC_046)
TEXT.append(TEXT_046)
SOLVE.append(SOLVE_046)

BASIC_047 = Mul( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), dx ) 
TEXT_047 = "Some text" 
SOLVE_047 = Add( Mul( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( Integer(2), Integer(-1) ) ), Mul( Pow( a, Integer(2) ), log( Add( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ) ), Pow( Integer(2), Integer(-1) ), Integer(-1) ) )
BASIC.append(BASIC_047)
TEXT.append(TEXT_047)
SOLVE.append(SOLVE_047)

BASIC_048 = Mul( x, Pow( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), n ), dx ) 
TEXT_048 = "Some text" 
SOLVE_048 = Mul( Pow( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Add( n, Integer(2) ) ), Pow( Add( n, Integer(2) ), Integer(-1) ) )
BASIC.append(BASIC_048)
TEXT.append(TEXT_048)
SOLVE.append(SOLVE_048)

BASIC_049 = Mul( Pow( x, Integer(2) ), sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ) 
TEXT_049 = "Some text" 
SOLVE_049 = Add( Mul( x, Add( Mul( Integer(2), Pow( x, Integer(2) ) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ), sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( Integer(8), Integer(-1) ) ), Mul( Mul( Pow( a, Integer(4) ), log( Add( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ) ), Pow( Integer(8), Integer(-1) ) ), Integer(-1) ) )
BASIC.append(BASIC_049)
TEXT.append(TEXT_049)
SOLVE.append(SOLVE_049)

BASIC_050 = Mul( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( x, Integer(-1) ), dx ) 
TEXT_050 = "Some text" 
SOLVE_050 = Add( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Mul( Mul( a, asec( Mul( x, Pow( a, Integer(-1) ) ) ) ), Integer(-1) ) )
BASIC.append(BASIC_050)
TEXT.append(TEXT_050)
SOLVE.append(SOLVE_050)

BASIC_051 = Mul( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( Pow( x, Integer(2) ), Integer(-1) ), dx ) 
TEXT_051 = "Some text" 
SOLVE_051 = Add( log( Add( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ) ), Mul( Mul( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( x, Integer(-1) ) ), Integer(-1) ) )
BASIC.append(BASIC_051)
TEXT.append(TEXT_051)
SOLVE.append(SOLVE_051)

BASIC_052 = Mul( Pow( x, Integer(2) ), Pow( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Integer(-1) ), dx ) 
TEXT_052 = "Some text" 
SOLVE_052 = Add( Mul( Pow( a, Integer(2) ), log( Add( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ) ), Pow( Integer(2), Integer(-1) ) ), Mul( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( Integer(2), Integer(-1) ) ) )
BASIC.append(BASIC_052)
TEXT.append(TEXT_052)
SOLVE.append(SOLVE_052)

BASIC_053 = Mul( Pow( Mul( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ), dx ) 
TEXT_053 = "Some text" 
SOLVE_053 = Mul( asec( Mul( x, Pow( a, Integer(-1) ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_053)
TEXT.append(TEXT_053)
SOLVE.append(SOLVE_053)

BASIC_054 = Mul( Pow( Mul( Pow( x, Integer(2) ), sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ), dx ) 
TEXT_054 = "Some text" 
SOLVE_054 = Mul( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( Mul( Pow( a, Integer(2) ), x ), Integer(-1) ) )
BASIC.append(BASIC_054)
TEXT.append(TEXT_054)
SOLVE.append(SOLVE_054)

BASIC_055 = Mul( Pow( sin( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_055 = "Some text" 
SOLVE_055 = Add( Mul( x, Pow( Integer(2), Integer(-1) ) ), Mul( Mul( sin( Mul( Integer(2), a, x ) ), Pow( Mul( Integer(4), a ), Integer(-1) ) ), Integer(-1) ) )
BASIC.append(BASIC_055)
TEXT.append(TEXT_055)
SOLVE.append(SOLVE_055)

BASIC_056 = Mul( Pow( cos( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_056 = "Some text" 
SOLVE_056 = Add( Mul( x, Pow( Integer(2), Integer(-1) ) ), Mul( sin( Mul( Integer(2), a, x ) ), Pow( Mul( Integer(4), a ), Integer(-1) ) ) )
BASIC.append(BASIC_056)
TEXT.append(TEXT_056)
SOLVE.append(SOLVE_056)

BASIC_057 = Mul( sin( Mul( a, x ) ), cos( Mul( b, x ) ), dx ) 
TEXT_057 = "Some text" 
SOLVE_057 = Add( Mul( Mul( Mul( cos( Add( a, b ) ), x ), Pow( Mul( Integer(2), Add( a, b ) ), Integer(-1) ) ), Integer(-1) ), Mul( Mul( Mul( cos( Add( a, Mul( b, Integer(-1) ) ) ), x ), Pow( Mul( Integer(2), Add( a, Mul( b, Integer(-1) ) ) ), Integer(-1) ) ), Integer(-1) ) )
BASIC.append(BASIC_057)
TEXT.append(TEXT_057)
SOLVE.append(SOLVE_057)

BASIC_058 = Mul( sin( Mul( a, x ) ), sin( Mul( b, x ) ), dx ) 
TEXT_058 = "Some text" 
SOLVE_058 = Add( Mul( Mul( sin( Add( a, Mul( b, Integer(-1) ) ) ), x ), Pow( Mul( Integer(2), Add( a, Mul( b, Integer(-1) ) ) ), Integer(-1) ) ), Mul( Mul( Mul( sin( Add( a, b ) ), x ), Pow( Mul( Integer(2), Add( a, b ) ), Integer(-1) ) ), Integer(-1) ) )
BASIC.append(BASIC_058)
TEXT.append(TEXT_058)
SOLVE.append(SOLVE_058)

BASIC_059 = Mul( cos( Mul( a, x ) ), cos( Mul( b, x ) ), dx ) 
TEXT_059 = "Some text" 
SOLVE_059 = Add( Mul( Mul( sin( Add( a, Mul( b, Integer(-1) ) ) ), x ), Pow( Mul( Integer(2), Add( a, Mul( b, Integer(-1) ) ) ), Integer(-1) ) ), Mul( Mul( sin( Add( a, b ) ), x ), Pow( Mul( Integer(2), Add( a, b ) ), Integer(-1) ) ) )
BASIC.append(BASIC_059)
TEXT.append(TEXT_059)
SOLVE.append(SOLVE_059)

BASIC_060 = Mul( Pow( sin( Mul( a, x ) ), n ), cos( Mul( a, x ) ), dx ) 
TEXT_060 = "Some text" 
SOLVE_060 = Mul( Pow( sin( Mul( a, x ) ), Add( n, Integer(1) ) ), Pow( Mul( a, Add( n, Integer(1) ) ), Integer(-1) ) )
BASIC.append(BASIC_060)
TEXT.append(TEXT_060)
SOLVE.append(SOLVE_060)

BASIC_061 = Mul( Pow( cos( Mul( a, x ) ), n ), sin( Mul( a, x ) ), dx ) 
TEXT_061 = "Some text" 
SOLVE_061 = Mul( Mul( Pow( cos( Mul( a, x ) ), Add( n, Integer(1) ) ), Pow( Mul( a, Add( n, Integer(1) ) ), Integer(-1) ) ), Integer(-1) )
BASIC.append(BASIC_061)
TEXT.append(TEXT_061)
SOLVE.append(SOLVE_061)

BASIC_062 = Mul( sin( Mul( a, x ) ), Pow( cos( Mul( a, x ) ), Integer(-1) ), dx ) 
TEXT_062 = "Some text" 
SOLVE_062 = Mul( log( sec( Mul( a, x ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_062)
TEXT.append(TEXT_062)
SOLVE.append(SOLVE_062)

BASIC_063 = Mul( cos( Mul( a, x ) ), Pow( sin( Mul( a, x ) ), Integer(-1) ), dx ) 
TEXT_063 = "Some text" 
SOLVE_063 = Mul( log( sin( Mul( a, x ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_063)
TEXT.append(TEXT_063)
SOLVE.append(SOLVE_063)

BASIC_064 = Mul( Pow( Add( b, Mul( c, sin( Mul( a, x ) ) ) ), Integer(-1) ), dx ) 
TEXT_064 = "Some text" 
SOLVE_064 = Mul( Integer(-1), Integer(2), atan( Mul( sqrt( Mul( Add( b, Mul( c, Integer(-1) ) ), Pow( Add( b, c ), Integer(-1) ) ) ), tan( Add( Mul( pi, Pow( Integer(4), Integer(-1) ) ), Mul( Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ), Integer(-1) ) ) ) ) ), Pow( Mul( a, sqrt( Add( Pow( b, Integer(2) ), Mul( Pow( c, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ) )
BASIC.append(BASIC_064)
TEXT.append(TEXT_064)
SOLVE.append(SOLVE_064)

BASIC_065 = Mul(Pow(Add(b, Mul(c, sin(Mul(a, x)))), Integer(-1)), dx)
TEXT_065 = "Some text" 
SOLVE_065 = Mul(Integer(-1), Pow(Mul(a, sqrt(Add(Pow(c, Integer(2)), Mul(Integer(-1), Pow(b, Integer(2)))))), Integer(-1)), log(Mul(Add(c, Mul(b, sin(Mul(a, x))), Mul(sqrt(Add(Pow(c, Integer(2)), Mul(Integer(-1), Pow(b, Integer(2))))), cos(Mul(a, x)))), Pow(Add(b, Mul(c, sin(Mul(a, x)))), Integer(-1)))))
BASIC.append(BASIC_065)
TEXT.append(TEXT_065)
SOLVE.append(SOLVE_065)

BASIC_066 = Mul( Pow( Add( Integer(1), sin( Mul( a, x ) ) ), Integer(-1) ), dx ) 
TEXT_066 = "Some text" 
SOLVE_066 = Mul( Integer(-1), tan( Add( Mul( pi, Pow( Integer(4), Integer(-1) ) ), Mul( Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ), Integer(-1) ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_066)
TEXT.append(TEXT_066)
SOLVE.append(SOLVE_066)

BASIC_067 = Mul( Pow( Add( Integer(1), Mul( sin( Mul( a, x ) ), Integer(-1) ) ), Integer(-1) ), dx ) 
TEXT_067 = "Some text" 
SOLVE_067 = Mul( tan( Add( Mul( pi, Pow( Integer(4), Integer(-1) ) ), Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_067)
TEXT.append(TEXT_067)
SOLVE.append(SOLVE_067)

BASIC_069 = Mul( dx, Pow( Add( b, Mul( c, cos( Mul( a, x ) ) ) ), Integer(-1) ) ) 
TEXT_069 = "Some text" 
SOLVE_069 = Mul( Integer(2), cot( Mul( sqrt( Mul( Add( b, Mul( c, Integer(-1) ) ), Pow( Add( b, c ), Integer(-1) ) ) ), tan( Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ) ) ) ), Pow( Mul( a, sqrt( Add( Pow( b, Integer(2) ), Mul( Pow( c, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ) )
BASIC.append(BASIC_069)
TEXT.append(TEXT_069)
SOLVE.append(SOLVE_069)

BASIC_070 = Mul( dx, Pow( Add( b, Mul( c, cos( Mul( a, x ) ) ) ), Integer(-1) ) ) 
TEXT_070 = "Some text" 
SOLVE_070 = Mul( log( Mul( Add( c, Mul( b, cos( Mul( a, x ) ) ), Mul( sqrt( Add( Pow( c, Integer(2) ), Mul( Pow( b, Integer(2) ), Integer(-1) ) ) ), sin( Mul( a, x ) ) ) ), Pow( Add( b, Mul( c, cos( Mul( a, x ) ) ) ), Integer(-1) ) ) ), Pow( Mul( a, sqrt( Add( Pow( c, Integer(2) ), Mul( Pow( b, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ) )
BASIC.append(BASIC_070)
TEXT.append(TEXT_070)
SOLVE.append(SOLVE_070)

BASIC_071 = Mul( dx, Pow( Add( Integer(1), Mul( c, cos( Mul( a, x ) ) ) ), Integer(-1) ) ) 
TEXT_071 = "Some text" 
SOLVE_071 = Mul( tan( Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_071)
TEXT.append(TEXT_071)
SOLVE.append(SOLVE_071)

BASIC_072 = Mul( dx, Pow( Add( Integer(1), Mul( c, cos( Mul( a, x ) ) ) ), Integer(-1) ) ) 
TEXT_072 = "Some text" 
SOLVE_072 = Mul( cot( Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_072)
TEXT.append(TEXT_072)
SOLVE.append(SOLVE_072)

BASIC_073 = Mul( x, sin( Mul( a, x ) ), dx ) 
TEXT_073 = "Some text" 
SOLVE_073 = Mul( Add( Mul( sin( Mul( a, x ) ), Pow( Pow( a, Integer(2) ), Integer(-1) ) ), Mul( Mul( x, cos( Mul( a, x ) ), Pow( a, Integer(-1) ) ), Integer(-1) ) ) )
BASIC.append(BASIC_073)
TEXT.append(TEXT_073)
SOLVE.append(SOLVE_073)

BASIC_074 = Mul( x, cos( Mul( a, x ) ), dx )
TEXT_074 = "Some text" 
SOLVE_074 = Mul( Add( Mul( cos( Mul( a, x ) ), Pow( Pow( a, Integer(2) ), Integer(-1) ) ), Mul( Mul( x, sin( Mul( a, x ) ), Pow( a, Integer(-1) ) ), Integer(-1) ) ) )
BASIC.append(BASIC_074)
TEXT.append(TEXT_074)
SOLVE.append(SOLVE_074)

BASIC_075 = Mul( tan( Mul( a, x ) ), dx ) 
TEXT_075 = "Some text" 
SOLVE_075 = Mul( log( sec( Mul( a, x ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_075)
TEXT.append(TEXT_075)
SOLVE.append(SOLVE_075)

BASIC_076 = Mul( cot( Mul( a, x ) ), dx )
TEXT_076 = "Some text" 
SOLVE_076 = Mul( log( sin( Mul( a, x ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_076)
TEXT.append(TEXT_076)
SOLVE.append(SOLVE_076)

BASIC_077 = Mul( Pow( tan( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_077 = "Some text" 
SOLVE_077 = Add( Mul( tan( Mul(a, x) ), Pow( a, Integer(-1) ) ), Mul( x, Integer(-1) ) )
BASIC.append(BASIC_077)
TEXT.append(TEXT_077)
SOLVE.append(SOLVE_077)

BASIC_078 = Mul( Pow( cot( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_078 = "Some text" 
SOLVE_078 = Add( Mul( Mul( cot( Mul( a, x ) ), Pow( a, Integer(-1) ) ), Integer(-1) ), Mul( x, Integer(-1) ) )
BASIC.append(BASIC_078)
TEXT.append(TEXT_078)
SOLVE.append(SOLVE_078)

BASIC_079 = Mul( sec( Mul( a, x ) ), dx ) 
TEXT_079 = "Some text" 
SOLVE_079 = Mul( log( Add( sec( Mul( a, x ) ), tan( Mul( a, x ) ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_079)
TEXT.append(TEXT_079)
SOLVE.append(SOLVE_079)

BASIC_080 = Mul(csc(Mul(a, x)), dx)
TEXT_080 = "Some text"
SOLVE_080 = Mul(Integer(-1), Pow(a, Integer(-1)), log(Add(csc(Mul(a, x)), cot(Mul(a, x)))))
BASIC.append(BASIC_080)
TEXT.append(TEXT_080)
SOLVE.append(SOLVE_080)

BASIC_081 = Mul(Pow(sec(Mul(a, x)), Integer(2)), dx)
TEXT_081 = "Some text"
SOLVE_081 = Mul(Pow(a, Integer(-1)), tan(Mul(a, x)))
BASIC.append(BASIC_081)
TEXT.append(TEXT_081)
SOLVE.append(SOLVE_081)

BASIC_082 = Mul(Pow(csc(Mul(a, x)), Integer(2)), dx)
TEXT_082 = "Some text"
SOLVE_082 = Mul(Integer(-1), Pow(a, Integer(-1)), cot(Mul(a, x)))
BASIC.append(BASIC_082)
TEXT.append(TEXT_082)
SOLVE.append(SOLVE_082)

BASIC_083 = Mul(Pow(sec(Mul(a, x)), n), tan(Mul(a, x)), dx)
TEXT_083 = "Some text"
SOLVE_083 = Mul(Pow(sec(Mul(a,x)), Integer(2)), Pow(Mul(n, a), Integer(-1)))
BASIC.append(BASIC_083)
TEXT.append(TEXT_083)
SOLVE.append(SOLVE_083)

BASIC_084 = Mul(Pow(csc(Mul(a, x)), n), cot(Mul(a, x)), dx)
TEXT_084 = "Some text"
SOLVE_084 = Mul(Integer(-1), Pow(csc(Mul(a,x)), Integer(2)), Pow(Mul(n, a), Integer(-1)))
BASIC.append(BASIC_084)
TEXT.append(TEXT_084)
SOLVE.append(SOLVE_084)

BASIC_085 = Mul(asin(Mul(a, x)), dx)
TEXT_085 = "Some text"
SOLVE_085 = Add(Mul(x, asin(Mul(a, x))), Mul(Pow(a, Integer(-1)), sqrt(Add(Integer(1), Mul(Integer(-1), Pow(a, Integer(2)), Pow(x, Integer(2)))))))
BASIC.append(BASIC_085)
TEXT.append(TEXT_085)
SOLVE.append(SOLVE_085)

BASIC_086 = Mul(acos(Mul(a, x)), dx)
TEXT_086 = "Some text"
SOLVE_086 = Add(Mul(x, acos(Mul(a, x))), Mul(Integer(-1), Pow(a, Integer(-1)), sqrt(Add(Integer(1), Mul(Integer(-1), Pow(a, Integer(2)), Pow(x, Integer(2)))))))
BASIC.append(BASIC_086)
TEXT.append(TEXT_086)
SOLVE.append(SOLVE_086)

BASIC_087 = Mul(atan(Mul(a, x)), dx)
TEXT_087 = "Some text"
SOLVE_087 = Add(Mul(x, atan(Mul(a, x))), Mul(Pow(Mul(a, Integer(2)), Integer(-1)), ln(Add(Integer(1), Mul(Pow(a, Integer(2)), Pow(x, Integer(2)))))))
BASIC.append(BASIC_087)
TEXT.append(TEXT_087)
SOLVE.append(SOLVE_087)

BASIC_088 = Mul(Pow(E, Mul(a, x)), dx)
TEXT_088 = "Some text"
SOLVE_088 = Mul(Pow(a, Integer(-1)), Pow(E, Mul(a, x)))
BASIC.append(BASIC_088)
TEXT.append(TEXT_088)
SOLVE.append(SOLVE_088)

BASIC_089 = Mul(Pow(b, Mul(a, x)), dx)
TEXT_089 = "Some text"
SOLVE_089 = Mul(Pow(a, Integer(-1)), Pow(b, Mul(a, x)), Pow(log(b), Integer(-1)))
BASIC.append(BASIC_089)
TEXT.append(TEXT_089)
SOLVE.append(SOLVE_089)

BASIC_090 = Mul(x, Pow(E, Mul(a, x)), dx)
TEXT_090 = "Some text"
SOLVE_090 = Mul(Pow(a, Integer(-2)), Pow(E, Mul(a, x)), Add(Mul(a, x), Mul(Integer(-1), 1)))
BASIC.append(BASIC_090)
TEXT.append(TEXT_090)
SOLVE.append(SOLVE_090)

BASIC_091 = Mul(sin(Mul(b, x)), Pow(E, Mul(a, x)), dx)
TEXT_091 = "Some text"
SOLVE_091 = Mul(Pow(Add(Pow(a, Integer(2)), Pow(b, Integer(2))), Integer(-1)), Pow(E, Mul(a, x)), Add(Mul(a, sin(Mul(b, x))), Mul(Integer(-1), b, cos(Mul(b, x)))))
BASIC.append(BASIC_091)
TEXT.append(TEXT_091)
SOLVE.append(SOLVE_091)

BASIC_092 = Mul(cos(Mul(b, x)), Pow(E, Mul(a, x)), dx)
TEXT_092 = "Some text"
SOLVE_092 = Mul(Pow(Add(Pow(a, Integer(2)), Pow(b, Integer(2))), Integer(-1)), Pow(E, Mul(a, x)), Add(Mul(a, cos(Mul(b, x))), Mul(b, sin(Mul(b, x)))))
BASIC.append(BASIC_092)
TEXT.append(TEXT_092)
SOLVE.append(SOLVE_092)

BASIC_093 = Mul(log(Mul(a, x)), dx)
TEXT_093 = "Some text"
SOLVE_093 = Add(Mul(x, log(Mul(a, x))), Mul(Integer(-1), x)) 
BASIC.append(BASIC_093)
TEXT.append(TEXT_093)
SOLVE.append(SOLVE_093)

BASIC_094 = Mul(Pow(x, Integer(-1)), Pow(log(Mul(a, x)), n), dx)
TEXT_094 = "Some text"
SOLVE_094 = Mul(Pow(Add(n, Integer(1)), Integer(-1)), Pow(ln(Mul(a, x)), Add(n, Integer(1))))
BASIC.append(BASIC_094)
TEXT.append(TEXT_094)
SOLVE.append(SOLVE_094)

BASIC_095 = Mul(Pow(Mul(x, log(Mul(a, x))), Integer(-1)), dx)
TEXT_095 = "Some text"
SOLVE_095 = log(log(Mul(a, x)))
BASIC.append(BASIC_095)
TEXT.append(TEXT_095)
SOLVE.append(SOLVE_095)

BASIC_096 = Mul(Pow(sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))), Integer(-1)), dx)
TEXT_096 = "Some text"
SOLVE_096 = asin(Mul(Pow(a, Integer(-1)), Add(x, Mul(Integer(-1), a))))
BASIC.append(BASIC_096)
TEXT.append(TEXT_096)
SOLVE.append(SOLVE_096)

BASIC_097 = Mul(sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))) , dx)
TEXT_097 = "Some text"
SOLVE_097 = Add(Mul(Add(x,Mul(Integer(-1),a)),Pow(Integer(2),Integer(-1)),sqrt(Add(Mul(Integer(2),a,x),Mul(Integer(-1),Pow(x,Integer(2)))))),Mul(Pow(a,Integer(2)),Pow(Integer(2),Integer(-1)),asin(Mul(Add(x,Mul(Integer(-1),a)),Pow(a,Integer(-1))))))
BASIC.append(BASIC_097)
TEXT.append(TEXT_097)
SOLVE.append(SOLVE_097)

BASIC_098 = Mul(x, sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))) , dx)
TEXT_098 = "Some text"
SOLVE_098 = asin(Mul(Pow(a, Integer(-1)), Add(x, Mul(Integer(-1), a))))
BASIC.append(BASIC_098)
TEXT.append(TEXT_098)
SOLVE.append(SOLVE_098)

BASIC_099 = Mul(Pow(x, Integer(-1)), sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))) , dx)
TEXT_099 = "Some text"
SOLVE_099 = Add(sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))), asin(Mul(Add(x, Mul(Integer(-1), a)), Pow(a, Integer(-1)))))
BASIC.append(BASIC_099)
TEXT.append(TEXT_099)
SOLVE.append(SOLVE_099)

BASIC_100 = Mul(Pow(x, Integer(-2)), sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))) , dx)
TEXT_100 = "Some text"
SOLVE_100 = Add(Mul(Integer(-2), sqrt(Mul(Add(Mul(Integer(2), a), Mul(Integer(-1), x)), Pow(x, Integer(-1))))), Mul(Integer(-1), asin(Mul(Add(x, Mul(Integer(-1), a)), Pow(a, Integer(-1))))))
BASIC.append(BASIC_100)
TEXT.append(TEXT_100)
SOLVE.append(SOLVE_100)

BASIC_101 = Mul( x, dx, Pow( sqrt( Add( Mul( Integer(2), a, x ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Integer(-1) ) ) 
TEXT_101 = "Some text" 
SOLVE_101 = Add( Mul( a, asin( Mul( Add( x, Mul( a, Integer(-1) ) ), Pow( a, Integer(-1) ) ) ) ), Mul( sqrt( Add( Mul( Integer(2), a, x ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Integer(-1) ) )
BASIC.append(BASIC_101)
TEXT.append(TEXT_101)
SOLVE.append(SOLVE_101)

BASIC_102 = Mul( dx, Pow( Mul( x, sqrt( Add( Mul( Integer(2), a, x ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ) ) 
TEXT_102 = "Some text" 
SOLVE_102 = Mul( Integer(-1), sqrt( Mul( Add( Mul( Integer(2), a ), Mul( x, Integer(-1) ) ), Pow( x, Integer(-1) ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_102)
TEXT.append(TEXT_102)
SOLVE.append(SOLVE_102)

BASIC_103 = Mul( sinh( Mul( a, x ) ), dx ) 
TEXT_103 = "Some text" 
SOLVE_103 = Mul( cosh( Mul( a, x ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_103)
TEXT.append(TEXT_103)
SOLVE.append(SOLVE_103)

BASIC_104 = Mul( cosh( Mul( a, x ) ), dx ) 
TEXT_104 = "Some text" 
SOLVE_104 = Mul( sinh( Mul( a, x ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_104)
TEXT.append(TEXT_104)
SOLVE.append(SOLVE_104)

BASIC_105 = Mul( Pow( sinh( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_105 = "Some text" 
SOLVE_105 = Add( Mul( sinh( Mul( Integer(2), a, x ) ), Pow( Mul( Integer(4), a ), Integer(-1) ) ), Mul( Mul( x, Pow( Integer(2), Integer(-1) ) ), Integer(-1) ) )
BASIC.append(BASIC_105)
TEXT.append(TEXT_105)
SOLVE.append(SOLVE_105)

BASIC_106 = Mul( Pow( cosh( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_106 = "Some text" 
SOLVE_106 = Add( Mul( sinh( Mul( Integer(2), a, x ) ), Pow( Mul( Integer(4), a ), Integer(-1) ) ), Mul( x, Pow( Integer(2), Integer(-1) ) ) )
BASIC.append(BASIC_106)
TEXT.append(TEXT_106)
SOLVE.append(SOLVE_106)

BASIC_107 = Mul( x, sinh( Mul( a, x ) ), dx ) 
TEXT_107 = "Some text" 
SOLVE_107 = Add( Mul( cosh( Mul( a, x ) ), Pow( a, Integer(-1) ) ), Mul( Mul( sinh( Mul( a, x ) ), Pow( a, Integer(-2) ) ), Integer(-1) ) )
BASIC.append(BASIC_107)
TEXT.append(TEXT_107)
SOLVE.append(SOLVE_107)

BASIC_108 = Mul( x, cosh( Mul( a, x ) ), dx ) 
TEXT_108 = "Some text" 
SOLVE_108 = Add( Mul( sinh( Mul( a, x ) ), Pow( a, Integer(-1) ) ), Mul( Mul( cosh( Mul( a, x ) ), Pow( a, Integer(-2) ) ), Integer(-1) ) )
BASIC.append(BASIC_108)
TEXT.append(TEXT_108)
SOLVE.append(SOLVE_108)

BASIC_109 = Mul( tanh( Mul( a, x ) ), dx ) 
TEXT_109 = "Some text" 
SOLVE_109 = Mul( log( cosh( Mul( a, x ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_109)
TEXT.append(TEXT_109)
SOLVE.append(SOLVE_109)

BASIC_110 = Mul( coth( Mul( a, x ) ), dx ) 
TEXT_110 = "Some text" 
SOLVE_110 = Mul( log( sinh( Mul( a, x ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_110)
TEXT.append(TEXT_110)
SOLVE.append(SOLVE_110)

BASIC_111 = Mul( Pow( tanh( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_111 = "Some text" 
SOLVE_111 = Add( x, Mul( Mul( tanh( Mul( a, x ) ), Pow( a, Integer(-1) ) ), Integer(-1) ) )
BASIC.append(BASIC_111)
TEXT.append(TEXT_111)
SOLVE.append(SOLVE_111)

BASIC_112 = Mul( Pow( coth( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_112 = "Some text" 
SOLVE_112 = Add( x, Mul( Mul( coth( Mul( a, x ) ), Pow( a, Integer(-1) ) ), Integer(-1) ) )
BASIC.append(BASIC_112)
TEXT.append(TEXT_112)
SOLVE.append(SOLVE_112)

BASIC_113 = Mul( sech( Mul( a, x ) ), dx ) 
TEXT_113 = "Some text" 
SOLVE_113 = Mul( asin( tanh( Mul( a, x ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_113)
TEXT.append(TEXT_113)
SOLVE.append(SOLVE_113)

BASIC_114 = Mul( csch( Mul( a, x ) ), dx ) 
TEXT_114 = "Some text" 
SOLVE_114 = Mul( log( tanh( Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ) ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_114)
TEXT.append(TEXT_114)
SOLVE.append(SOLVE_114)

BASIC_115 = Mul( Pow( sech( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_115 = "Some text" 
SOLVE_115 = Mul( tanh( Mul( a, x ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_115)
TEXT.append(TEXT_115)
SOLVE.append(SOLVE_115)

BASIC_116 = Mul( Pow( csch( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_116 = "Some text" 
SOLVE_116 = Mul( Integer(-1), coth( Mul( a, x ) ), Pow( a, Integer(-1) ) )
BASIC.append(BASIC_116)
TEXT.append(TEXT_116)
SOLVE.append(SOLVE_116)

BASIC_117 = Mul( Pow( sech( Mul( a, x ) ), n ), tanh( Mul( a, x ) ), dx ) 
TEXT_117 = "Some text" 
SOLVE_117 = Mul( Integer(-1), Pow( sech( Mul( a, x ) ), n ), Pow( Mul( n, a ), Integer(-1) ) )
BASIC.append(BASIC_117)
TEXT.append(TEXT_117)
SOLVE.append(SOLVE_117)

BASIC_118 = Mul( Pow( csch( Mul( a, x ) ), n ), cot( Mul( a, x ) ), dx ) 
TEXT_118 = "Some text" 
SOLVE_118 = Mul( Integer(-1), Pow( csch( Mul( a, x ) ), n ), Pow( Mul( n, a ), Integer(-1) ) )
BASIC.append(BASIC_118)
TEXT.append(TEXT_118)
SOLVE.append(SOLVE_118)

BASIC_119 = Mul( Pow( E, Mul( a, x ) ), sinh( Mul( b, x ) ), dx ) 
TEXT_119 = "Some text" 
SOLVE_119 = Mul( Mul( Pow( E, Mul( a, x ) ), Pow( Integer(2), Integer(-1) ) ), Add( Mul( Pow( E, Mul( b, x ) ), Pow( Add( a, b ), Integer(-1) ) ), Mul( Mul( Pow( E, Mul( Integer(-1), b, x ) ), Pow( Add( a, Mul( b, Integer(-1) ) ), Integer(-1) ) ), Integer(-1) ) ) )
BASIC.append(BASIC_119)
TEXT.append(TEXT_119)
SOLVE.append(SOLVE_119)

BASIC_120 = Mul( Pow( E, Mul( a, x ) ), cosh( Mul( b, x ) ), dx ) 
TEXT_120 = "Some text" 
SOLVE_120 = Mul( Mul( Pow( E, Mul( a, x ) ), Pow( Integer(2), Integer(-1) ) ), Add( Mul( Pow( E, Mul( b, x ) ), Pow( Add( a, b ), Integer(-1) ) ), Mul( Pow( E, Mul( Integer(-1), b, x ) ), Pow( Add( a, Mul( b, Integer(-1) ) ), Integer(-1) ) ) ) )
BASIC.append(BASIC_120)
TEXT.append(TEXT_120)
SOLVE.append(SOLVE_120)
