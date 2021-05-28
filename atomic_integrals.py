from sympy import *

dx = Symbol('dx')
x = Symbol('x')
n = Symbol('n')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

BASIC_001 = dx
TEXT_001 = "Some text"
SOLVE_001 = x

BASIC_002 = Mul(Pow(x, n), dx)
TEXT_002 = "Some text"
SOLVE_002 = Mul(Pow(x, Add(n, Integer(1))), Pow(Add(n, Integer(1)), Integer(-1)))

BASIC_003 = Mul(Pow(Integer(-1), x), dx)
TEXT_003 = "Some text"
SOLVE_003 = log(x)

BASIC_004 = Mul(Pow(E, x), dx)
TEXT_004 = "Some text"
SOLVE_004 = Pow(E, x)

BASIC_005 = Mul(Pow(n, x), dx)
TEXT_005 = "Some text"
SOLVE_005 = Mul(Pow(log(n), Integer(-1)), Pow(n, x))

BASIC_006 = Mul(sin(Mul(n, x)), dx)
TEXT_006 = "Some text"
SOLVE_006 = Mul(Integer(-1), Mul(cos(Mul(n, x)), Pow(n, Integer(-1))))

BASIC_007 = Mul(cos(Mul(n, x)), dx)
TEXT_007 = "Some text"
SOLVE_007 = Mul(Mul(sin(Mul(n, x)), Pow(n, Integer(-1))))

BASIC_008 = Mul(Pow(sec(Mul(n, x)), Integer(2)), dx)
TEXT_008 = "Some text"
SOLVE_008 = Mul(tan(Mul(n, x)), Pow(n, Integer(-1)))

BASIC_009 = Mul(Pow(csc(Mul(n, x)), Integer(2)), dx)
TEXT_009 = "Some text"
SOLVE_009 = Mul(Integer(-1), cot(Mul(n, x)), Pow(n, Integer(-1)))

BASIC_010 = Mul(sec(Mul(n, x)), tan(Mul(n, x)), dx)
TEXT_010 = "Some text"
SOLVE_010 = Mul(sec(Mul(n, x)), Pow(n, Integer(-1)))

BASIC_011 = Mul(csc(Mul(n, x)), cot(Mul(n, x)), dx)
TEXT_011 = "Some text"
SOLVE_011 = Mul(Integer(-1), csc(Mul(n, x)), Pow(n, Integer(-1)))

BASIC_012 = Mul(tan(Mul(n, x)), dx)
TEXT_012 = "Some text"
SOLVE_012 = Mul(log(sec(Mul(n, x))), Pow(n, Integer(-1)))

BASIC_013 = Mul(cot(Mul(n, x)), dx)
TEXT_013 = "Some text"
SOLVE_013 = Mul(log(sin(Mul(n, x))), Pow(n, Integer(-1)))

BASIC_014 = Mul(sinh(Mul(n, x)), dx)
TEXT_014 = "Some text"
SOLVE_014 = Mul(cosh(Mul(n, x)), Pow(n, Integer(-1)))

BASIC_015 = Mul(cosh(Mul(n, x)), dx)
TEXT_015 = "Some text"
SOLVE_015 = Mul(sinh(Mul(n, x)), Pow(n, Integer(-1)))

BASIC_016 = Mul(dx, Pow(sqrt(Add(Pow(n, Integer(2)), Mul(Integer(-1),Pow(x, Integer(2))))), Integer(-1)))
TEXT_016 = "Some text"
SOLVE_016 = asin(Mul(x, Pow(n, Integer(-1))))

BASIC_017 = Mul(dx, Pow(Add(Pow(n, Integer(2)), Pow(x, Integer(2))), Integer(-1)))
TEXT_017 = "Some text"
SOLVE_017 = Mul(atan(Mul(x, Pow(n, Integer(-1)))), Pow(n, Integer(-1)))

BASIC_018 = Mul(dx, Pow(Mul(x, sqrt(Add(Pow(x, Integer(2)), Mul(Integer(-1), Pow(n, Integer(2)))))), Integer(-1)))
TEXT_018 = "Some text"
SOLVE_018 = Mul(asec(Mul(x, Pow(n, Integer(-1)))), Pow(n, Integer(-1)))

BASIC_019 = Mul(dx, Pow(sqrt(Add(Pow(n, Integer(2)), Pow(x, Integer(2)))), Integer(-1)))
TEXT_019 = "Some text"
SOLVE_019 = asinh(Mul(x, Pow(n, Integer(-1))))

BASIC_020 = Mul(dx, Pow(sqrt(Add(Pow(x, Integer(2)), Mul(Integer(-1), Pow(n, Integer(2))))), Integer(-1)))
TEXT_020 = "Some text"
SOLVE_020 = acosh(Mul(x, Pow(n, Integer(-1))))

BASIC_021 = Mul(Pow(Add(Mul(a, x), b), n), dx)
TEXT_021 = "Some text"
SOLVE_021 = Mul(Pow(Add(Mul(a, x), b), Add(n, Integer(1))), Pow(Mul(a, Add(n, Integer(1))), Integer(-1)))

BASIC_022 = Mul(x, Pow(Add(Mul(a, x), b), n), dx)
TEXT_022 = "Some text"
SOLVE_022 = Mul(Mul(Pow(Add(Mul(a, x), b), Add(n, Integer(1))), Pow(Pow(a, 2), Integer(-1))), Add(Mul(Add(Mul(a, x), b), Pow(Add(n, Integer(2)), Integer(-1))), Mul(Mul(b, Pow(Add(n, Integer(1)), Integer(-1))), Integer(-1))))

BASIC_023 = Mul(Pow(Add(Mul(a, x), b), Integer(-1)), dx)
TEXT_023 = "Some text"
SOLVE_023 = Mul(log(Add(Mul(a, x), b)), Pow(a, Integer(-1)))

BASIC_024 = Mul(x, Pow(Add(Mul(a, x), b), Integer(-1)), dx)
TEXT_024 = "Some text"
SOLVE_024 = Add(Mul(x, Pow(a, Integer(-1))), Mul(Mul(Mul(b, Pow(Pow(a, Integer(2)), Integer(-1))), log(Add(Mul(a, x), b))), Integer(-1)))

BASIC_025 = Mul(x, Pow(Pow(Add(Mul(a, x), b), Integer(2)), Integer(-1)), dx)
TEXT_025 = "Some text"
SOLVE_025 = Mul(Pow(Pow(a, Integer(2)), Integer(-1)), Add(log(Add(Mul(a, x), b)), Mul(b, Pow(Add(Mul(a, x), b), Integer(-1)))))

BASIC_026 = Mul(Pow(Mul(x, Add(Mul(a, x), b)), Integer(-1)), dx)
TEXT_026 = "Some text"
SOLVE_026 = Mul(log(Mul(x, Pow(Add(Mul(a, x), b), Integer(-1)))), Pow(b, Integer(-1)))

BASIC_027 = Mul(Pow(sqrt(Add(Mul(a, x), b)), n), dx)
TEXT_027 = "Some text"
SOLVE_027 = Mul(Mul(Integer(2), Pow(a, Integer(-1))), Mul(Pow(sqrt(Add(Mul(a, x), b)), Add(n, Integer(2))), Pow(Add(n, Integer(2)), Integer(-1))))

BASIC_028 = Mul(Pow(Mul(x, sqrt(Add(Mul(a, x), b))), Integer(-1)), dx)
TEXT_028 = "Some text"
SOLVE_028 = Mul(Pow(sqrt(b), Integer(-1)), log(Mul(Add(sqrt(Add(Mul(a, x), b)), Mul(sqrt(b), Integer(-1))), Pow(Add(sqrt(Add(Mul(a, x), b)), sqrt(b)), Integer(-1)))))

BASIC_029 = Mul(Pow(Mul(x, sqrt(Add(Mul(a, x), Mul(b, Integer(-1))))), Integer(-1)), dx)
TEXT_029 = "Some text"
SOLVE_029 = Mul(Mul(Integer(2), Pow(sqrt(b), Integer(-1))), atan(sqrt(Mul(Add(Mul(a, x), Mul(b, Integer(-1))), Pow(b, Integer(-1))))))

BASIC_030 = Mul(Pow(Pow(Add(Pow(a, Integer(2)), Pow(x, Integer(2))), Integer(2)), Integer(-1)), dx)
TEXT_030 = "Some text"
SOLVE_030 = Add(Mul(x, Pow(Mul(Integer(2), Pow(a, Integer(2)), Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Integer(-1))), Mul(atan(Mul(x, Pow(a, Integer(-1)))), Pow(Mul(Integer(2), Pow(a, Integer(3))), Integer(-1))))

BASIC_031 = Mul(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), dx)
TEXT_031 = "Some text"
SOLVE_031 = Add(Mul(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(Integer(2), Integer(-1))), Mul(Pow(a, Integer(2)), log(Add(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))))), Pow(Integer(2), Integer(-1))))

BASIC_032 = Mul(Pow(x, Integer(2)), sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), dx) 
TEXT_032 = "Some text"
SOLVE_032 = Add(Mul(x, Add(Pow(a, Integer(2)), Mul(Integer(2), Pow(x, Integer(2)))), sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(Integer(8), Integer(-1))), Mul(Mul(Pow(a, Integer(4)), log(Add(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))))), Pow(Integer(8), Integer(-1))), Integer(-1)))

BASIC_033 = Mul(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(x, Integer(-1)), dx)
TEXT_033 = "Some text"
SOLVE_033 = Add(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Mul(Mul(a, log(Mul(Add(a, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2))))), Pow(x, Integer(-1))))), Integer(-1)))

BASIC_034 = Mul(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(Pow(x, Integer(2)), Integer(-1)), dx) 
TEXT_034 = "Some text"
SOLVE_034 = Add(log(Add(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))))), Mul(Mul(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(x, Integer(-1))), Integer(-1)))

BASIC_035 = Mul(Pow(x, Integer(2)), Pow(sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Integer(-1)), dx) 
TEXT_035 = "Some text"
SOLVE_035 = Add(Mul(Integer(-1), Pow(a, Integer(2)), log(Add(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))))), Pow(Integer(2), Integer(-1))), Mul(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))), Pow(Integer(2), Integer(-1))))

BASIC_036 = Mul(Pow(Mul(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2))))), Integer(-1)), dx)
TEXT_036 = "Some text"
SOLVE_036 = Mul(Integer(-1), Pow(a, Integer(-1)), log(Mul(Add(a, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2))))), Pow(x, Integer(-1)))))

BASIC_036 = Mul(Pow(Mul(x, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2))))), Integer(-1)), dx)
TEXT_036 = "Some text"
SOLVE_036 = Mul(Integer(-1), Pow(a, Integer(-1)), log(Mul(Add(a, sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2))))), Pow(x, Integer(-1)))))

BASIC_037 = Mul(Pow(Mul(Pow(x, Integer(2)), sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2))))), Integer(-1)), dx)
TEXT_037 = "Some text"
SOLVE_037 = Mul(Integer(-1), Pow(Mul(Pow(a, Integer(2)), x), Integer(-1)), sqrt(Add(Pow(a, Integer(2)), Pow(x, Integer(2)))))

BASIC_038 = Mul(Pow(Add(Pow(a, Integer(2)), Mul(Pow(x, Integer(2)), Integer(-1))), Integer(-1)), dx)
TEXT_038 = "Some text"
SOLVE_038 = Mul(Pow(Mul(Integer(2), a), Integer(-1)), log(Mul(Add(x, a), Pow(Add(x, Mul(a, Integer(-1))), Integer(-1)))))

BASIC_039 = Mul( dx, Pow( Pow( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ), Integer(2) ), Integer(-1) ) )
TEXT_039 = "Some text"
SOLVE_039 = Add( Mul( x, Pow( Mul( Integer(2), Pow( a, Integer(2) ), Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Integer(-1) ) ), Mul( log( Mul( Add( x, a ), Pow( Add( x, Mul( a, Integer(-1) ) ), Integer(-1) ) ) ), Pow( Mul( Integer(4), Pow( a, Integer(3) ) ), Integer(-1) ) ) )

BASIC_040 = Mul( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), dx ) 
TEXT_040 = "Some text" 
SOLVE_040 = Add( Mul( x, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( Integer(2), Integer(-1) ) ), Mul( Pow( a, Integer(2) ), asin( Mul( x, Pow( a, Integer(-1) ) ) ), Pow( Integer(2), Integer(-1) ) ) )

BASIC_041 = Mul( Pow( x, Integer(2) ), sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), dx ) 
TEXT_041 = "Some text" 
SOLVE_041 = Add( Mul( Pow( a, Integer(4) ), asin( Mul( x, Pow( a, Integer(-1) ) ) ), Pow( Integer(8), Integer(-1) ) ), Mul( Mul( x, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Add( Pow( a, Integer(2) ), Mul( Mul( Integer(2), Pow( x, Integer(2) ) ), Integer(-1) ) ), Pow( Integer(8), Integer(-1) ) ), Integer(-1) ) )

BASIC_042 = Mul( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( x, Integer(-1) ), dx ) 
TEXT_042 = "Some text" 
SOLVE_042 = Add( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Mul( Mul( a, log( Mul( Add( a, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ) ), Pow( x, Integer(-1) ) ) ) ), Integer(-1) ) )

BASIC_043 = Mul( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( Pow( x, Integer(2) ), Integer(-1) ), dx ) 
TEXT_043 = "Some text" 
SOLVE_043 = Add( Mul( asin( Mul( x, Pow( a, Integer(-1) ) ) ), Integer(-1) ), Mul( Mul( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( x, Integer(-1) ) ), Integer(-1) ) )

BASIC_044 = Mul( Pow( x, Integer(2) ), Pow( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Integer(-1) ), dx ) 
TEXT_044 = "Some text" 
SOLVE_044 = Add( Mul( Pow( a, Integer(2) ), Pow( Integer(2), Integer(-1) ), asin( Mul( x, Pow( a, Integer(-1) ) ) ) ), Mul( Mul( x, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( Integer(2), Integer(-1) ) ), Integer(-1) ) )

BASIC_045 = Mul( Pow( Mul( x, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ), dx ) 
TEXT_045 = "Some text" 
SOLVE_045 = Mul( log( Mul( Add( a, sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ) ), Pow( x, Integer(-1) ) ) ), Pow( a, Integer(-1) ), Integer(-1) )

BASIC_046 = Mul( dx, Pow( Mul( Pow( x, Integer(2) ), sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ) ) 
TEXT_046 = "Some text" 
SOLVE_046 = Mul( Mul( sqrt( Add( Pow( a, Integer(2) ), Mul( Pow( x, Integer(2) ), Integer(-1) ) ) ), Pow( Mul( Pow( a, Integer(2) ), x ), Integer(-1) ) ), Integer(-1) )

BASIC_047 = Mul( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), dx ) 
TEXT_047 = "Some text" 
SOLVE_047 = Add( Mul( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( Integer(2), Integer(-1) ) ), Mul( Pow( a, Integer(2) ), log( Add( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ) ), Pow( Integer(2), Integer(-1) ), Integer(-1) ) )

BASIC_048 = Mul( x, Pow( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), n ), dx ) 
TEXT_048 = "Some text" 
SOLVE_048 = Mul( Pow( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Add( n, Integer(2) ) ), Pow( Add( n, Integer(2) ), Integer(-1) ) )

BASIC_049 = Mul( Pow( x, Integer(2) ), sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ) 
TEXT_049 = "Some text" 
SOLVE_049 = Add( Mul( x, Add( Mul( Integer(2), Pow( x, Integer(2) ) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ), sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( Integer(8), Integer(-1) ) ), Mul( Mul( Pow( a, Integer(4) ), log( Add( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ) ), Pow( Integer(8), Integer(-1) ) ), Integer(-1) ) )

BASIC_050 = Mul( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( x, Integer(-1) ), dx ) 
TEXT_050 = "Some text" 
SOLVE_050 = Add( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Mul( Mul( a, asec( Mul( x, Pow( a, Integer(-1) ) ) ) ), Integer(-1) ) )

BASIC_051 = Mul( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( Pow( x, Integer(2) ), Integer(-1) ), dx ) 
TEXT_051 = "Some text" 
SOLVE_051 = Add( log( Add( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ) ), Mul( Mul( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( x, Integer(-1) ) ), Integer(-1) ) )

BASIC_052 = Mul( Pow( x, Integer(2) ), Pow( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Integer(-1) ), dx ) 
TEXT_052 = "Some text" 
SOLVE_052 = Add( Mul( Pow( a, Integer(2) ), log( Add( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ) ), Pow( Integer(2), Integer(-1) ) ), Mul( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( Integer(2), Integer(-1) ) ) )

BASIC_053 = Mul( Pow( Mul( x, sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ), dx ) 
TEXT_053 = "Some text" 
SOLVE_053 = Mul( asec( Mul( x, Pow( a, Integer(-1) ) ) ), Pow( a, Integer(-1) ) )

BASIC_054 = Mul( Pow( Mul( Pow( x, Integer(2) ), sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ), dx ) 
TEXT_054 = "Some text" 
SOLVE_054 = Mul( sqrt( Add( Pow( x, Integer(2) ), Mul( Pow( a, Integer(2) ), Integer(-1) ) ) ), Pow( Mul( Pow( a, Integer(2) ), x ), Integer(-1) ) )

BASIC_055 = Mul( Pow( sin( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_055 = "Some text" 
SOLVE_055 = Add( Mul( x, Pow( Integer(2), Integer(-1) ) ), Mul( Mul( sin( Mul( Integer(2), a, x ) ), Pow( Mul( Integer(4), a ), Integer(-1) ) ), Integer(-1) ) )

BASIC_056 = Mul( Pow( cos( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_056 = "Some text" 
SOLVE_056 = Add( Mul( x, Pow( Integer(2), Integer(-1) ) ), Mul( sin( Mul( Integer(2), a, x ) ), Pow( Mul( Integer(4), a ), Integer(-1) ) ) )

BASIC_057 = Mul( sin( Mul( a, x ) ), cos( Mul( b, x ) ), dx ) 
TEXT_057 = "Some text" 
SOLVE_057 = Add( Mul( Mul( Mul( cos( Add( a, b ) ), x ), Pow( Mul( Integer(2), Add( a, b ) ), Integer(-1) ) ), Integer(-1) ), Mul( Mul( Mul( cos( Add( a, Mul( b, Integer(-1) ) ) ), x ), Pow( Mul( Integer(2), Add( a, Mul( b, Integer(-1) ) ) ), Integer(-1) ) ), Integer(-1) ) )

BASIC_058 = Mul( sin( Mul( a, x ) ), sin( Mul( b, x ) ), dx ) 
TEXT_058 = "Some text" 
SOLVE_058 = Add( Mul( Mul( sin( Add( a, Mul( b, Integer(-1) ) ) ), x ), Pow( Mul( Integer(2), Add( a, Mul( b, Integer(-1) ) ) ), Integer(-1) ) ), Mul( Mul( Mul( sin( Add( a, b ) ), x ), Pow( Mul( Integer(2), Add( a, b ) ), Integer(-1) ) ), Integer(-1) ) )

BASIC_059 = Mul( cos( Mul( a, x ) ), cos( Mul( b, x ) ), dx ) 
TEXT_059 = "Some text" 
SOLVE_059 = Add( Mul( Mul( sin( Add( a, Mul( b, Integer(-1) ) ) ), x ), Pow( Mul( Integer(2), Add( a, Mul( b, Integer(-1) ) ) ), Integer(-1) ) ), Mul( Mul( sin( Add( a, b ) ), x ), Pow( Mul( Integer(2), Add( a, b ) ), Integer(-1) ) ) )

BASIC_060 = Mul( Pow( sin( Mul( a, x ) ), n ), cos( Mul( a, x ) ), dx ) 
TEXT_060 = "Some text" 
SOLVE_060 = Mul( Pow( sin( Mul( a, x ) ), Add( n, Integer(1) ) ), Pow( Mul( a, Add( n, Integer(1) ) ), Integer(-1) ) )

BASIC_061 = Mul( Pow( cos( Mul( a, x ) ), n ), sin( Mul( a, x ) ), dx ) 
TEXT_061 = "Some text" 
SOLVE_061 = Mul( Mul( Pow( cos( Mul( a, x ) ), Add( n, Integer(1) ) ), Pow( Mul( a, Add( n, Integer(1) ) ), Integer(-1) ) ), Integer(-1) )

BASIC_062 = Mul( sin( Mul( a, x ) ), Pow( cos( Mul( a, x ) ), Integer(-1) ), dx ) 
TEXT_062 = "Some text" 
SOLVE_062 = Mul( log( sec( Mul( a, x ) ) ), Pow( a, Integer(-1) ) )

BASIC_063 = Mul( cos( Mul( a, x ) ), Pow( sin( Mul( a, x ) ), Integer(-1) ), dx ) 
TEXT_063 = "Some text" 
SOLVE_063 = Mul( log( sin( Mul( a, x ) ) ), Pow( a, Integer(-1) ) )

BASIC_064 = Mul( Pow( Add( b, Mul( c, sin( Mul( a, x ) ) ) ), Integer(-1) ), dx ) 
TEXT_064 = "Some text" 
SOLVE_064 = Mul( Integer(-1), Integer(2), atan( Mul( sqrt( Mul( Add( b, Mul( c, Integer(-1) ) ), Pow( Add( b, c ), Integer(-1) ) ) ), tan( Add( Mul( pi, Pow( Integer(4), Integer(-1) ) ), Mul( Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ), Integer(-1) ) ) ) ) ), Pow( Mul( a, sqrt( Add( Pow( b, Integer(2) ), Mul( Pow( c, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ) )

BASIC_065 = Mul(Pow(Add(b, Mul(c, sin(Mul(a, x)))), Integer(-1)), dx)
TEXT_065 = "Some text" 
SOLVE_065 = Mul(Integer(-1), Pow(Mul(a, sqrt(Add(Pow(c, Integer(2)), Mul(Integer(-1), Pow(b, Integer(2)))))), Integer(-1)), log(Mul(Add(c, Mul(b, sin(Mul(a, x))), Mul(sqrt(Add(Pow(c, Integer(2)), Mul(Integer(-1), Pow(b, Integer(2))))), cos(Mul(a, x)))), Pow(Add(b, Mul(c, sin(Mul(a, x)))), Integer(-1)))))

BASIC_066 = Mul( Pow( Add( Integer(1), sin( Mul( a, x ) ) ), Integer(-1) ), dx ) 
TEXT_066 = "Some text" 
SOLVE_066 = Mul( Integer(-1), tan( Add( Mul( pi, Pow( Integer(4), Integer(-1) ) ), Mul( Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ), Integer(-1) ) ) ), Pow( a, Integer(-1) ) )

BASIC_067 = Mul( Pow( Add( Integer(1), Mul( sin( Mul( a, x ) ), Integer(-1) ) ), Integer(-1) ), dx ) 
TEXT_067 = "Some text" 
SOLVE_067 = Mul( tan( Add( Mul( pi, Pow( Integer(4), Integer(-1) ) ), Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ) ) ), Pow( a, Integer(-1) ) )

BASIC_069 = Mul( dx, Pow( Add( b, Mul( c, cos( Mul( a, x ) ) ) ), Integer(-1) ) ) 
TEXT_069 = "Some text" 
SOLVE_069 = Mul( Integer(2), cot( Mul( sqrt( Mul( Add( b, Mul( c, Integer(-1) ) ), Pow( Add( b, c ), Integer(-1) ) ) ), tan( Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ) ) ) ), Pow( Mul( a, sqrt( Add( Pow( b, Integer(2) ), Mul( Pow( c, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ) )

BASIC_070 = Mul( dx, Pow( Add( b, Mul( c, cos( Mul( a, x ) ) ) ), Integer(-1) ) ) 
TEXT_070 = "Some text" 
SOLVE_070 = Mul( log( Mul( Add( c, Mul( b, cos( Mul( a, x ) ) ), Mul( sqrt( Add( Pow( c, Integer(2) ), Mul( Pow( b, Integer(2) ), Integer(-1) ) ) ), sin( Mul( a, x ) ) ) ), Pow( Add( b, Mul( c, cos( Mul( a, x ) ) ) ), Integer(-1) ) ) ), Pow( Mul( a, sqrt( Add( Pow( c, Integer(2) ), Mul( Pow( b, Integer(2) ), Integer(-1) ) ) ) ), Integer(-1) ) )

BASIC_071 = Mul( dx, Pow( Add( Integer(1), Mul( c, cos( Mul( a, x ) ) ) ), Integer(-1) ) ) 
TEXT_071 = "Some text" 
SOLVE_071 = Mul( tan( Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ) ), Pow( a, Integer(-1) ) )

BASIC_072 = Mul( dx, Pow( Add( Integer(1), Mul( c, cos( Mul( a, x ) ) ) ), Integer(-1) ) ) 
TEXT_072 = "Some text" 
SOLVE_072 = Mul( cot( Mul( Mul( a, x ), Pow( Integer(2), Integer(-1) ) ) ), Pow( a, Integer(-1) ) )

BASIC_073 = Mul( x, sin( Mul( a, x ) ), dx ) 
TEXT_073 = "Some text" 
SOLVE_073 = Mul( Add( Mul( sin( Mul( a, x ) ), Pow( Pow( a, Integer(2) ), Integer(-1) ) ), Mul( Mul( x, cos( Mul( a, x ) ), Pow( a, Integer(-1) ) ), Integer(-1) ) ) )

BASIC_074 = Mul( x, cos( Mul( a, x ) ), dx )
TEXT_074 = "Some text" 
SOLVE_074 = Mul( Add( Mul( cos( Mul( a, x ) ), Pow( Pow( a, Integer(2) ), Integer(-1) ) ), Mul( Mul( x, sin( Mul( a, x ) ), Pow( a, Integer(-1) ) ), Integer(-1) ) ) )

BASIC_075 = Mul( tan( Mul( a, x ) ), dx ) 
TEXT_075 = "Some text" 
SOLVE_075 = Mul( log( sec( Mul( a, x ) ) ), Pow( a, Integer(-1) ) )

BASIC_076 = Mul( cot( Mul( a, x ) ), dx )
TEXT_076 = "Some text" 
SOLVE_076 = Mul( log( sin( Mul( a, x ) ) ), Pow( a, Integer(-1) ) )

BASIC_077 = Mul( Pow( tan( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_077 = "Some text" 
SOLVE_077 = Add( Mul( tan( Mul(a, x) ), Pow( a, Integer(-1) ) ), Mul( x, Integer(-1) ) )

BASIC_078 = Mul( Pow( cot( Mul( a, x ) ), Integer(2) ), dx ) 
TEXT_078 = "Some text" 
SOLVE_078 = Add( Mul( Mul( cot( Mul( a, x ) ), Pow( a, Integer(-1) ) ), Integer(-1) ), Mul( x, Integer(-1) ) )

BASIC_079 = Mul( sec( Mul( a, x ) ), dx ) 
TEXT_079 = "Some text" 
SOLVE_079 = Mul( log( Add( sec( Mul( a, x ) ), tan( Mul( a, x ) ) ) ), Pow( a, Integer(-1) ) )

BASIC_080 = Mul(csc(Mul(a, x)), dx)
TEXT_080 = "Some text"
SOLVE_080 = Mul(Integer(-1), Pow(a, Integer(-1)), log(Add(csc(Mul(a, x)), cot(Mul(a, x)))))

BASIC_081 = Mul(Pow(sec(Mul(a, x)), Integer(2)), dx)
TEXT_081 = "Some text"
SOLVE_081 = Mul(Pow(a, Integer(-1)), tan(Mul(a, x)))

BASIC_082 = Mul(Pow(csc(Mul(a, x)), Integer(2)), dx)
TEXT_082 = "Some text"
SOLVE_082 = Mul(Integer(-1), Pow(a, Integer(-1)), cot(Mul(a, x)))

BASIC_083 = Mul(Pow(sec(Mul(a, x)), n), tan(Mul(a, x)), dx)
TEXT_083 = "Some text"
SOLVE_083 = Mul(Pow(sec(Mul(a,x)), Integer(2)), Pow(Mul(n, a), Integer(-1)))

BASIC_084 = Mul(Pow(csc(Mul(a, x)), n), cot(Mul(a, x)), dx)
TEXT_084 = "Some text"
SOLVE_084 = Mul(Integer(-1), Pow(csc(Mul(a,x)), Integer(2)), Pow(Mul(n, a), Integer(-1)))

BASIC_085 = Mul(asin(Mul(a, x)), dx)
TEXT_085 = "Some text"
SOLVE_085 = Add(Mul(x, asin(Mul(a, x))), Mul(Pow(a, Integer(-1)), sqrt(Add(Integer(1), Mul(Integer(-1), Pow(a, Integer(2)), Pow(x, Integer(2)))))))

BASIC_086 = Mul(acos(Mul(a, x)), dx)
TEXT_086 = "Some text"
SOLVE_086 = Add(Mul(x, acos(Mul(a, x))), Mul(Integer(-1), Pow(a, Integer(-1)), sqrt(Add(Integer(1), Mul(Integer(-1), Pow(a, Integer(2)), Pow(x, Integer(2)))))))

BASIC_087 = Mul(atan(Mul(a, x)), dx)
TEXT_087 = "Some text"
SOLVE_087 = Add(Mul(x, atan(Mul(a, x))), Mul(Pow(Mul(a, Integer(2)), Integer(-1)), ln(Add(Integer(1), Mul(Pow(a, Integer(2)), Pow(x, Integer(2)))))))

BASIC_088 = Mul(Pow(E, Mul(a, x)), dx)
TEXT_088 = "Some text"
SOLVE_088 = Mul(Pow(a, Integer(-1)), Pow(E, Mul(a, x)))

BASIC_089 = Mul(Pow(b, Mul(a, x)), dx)
TEXT_089 = "Some text"
SOLVE_089 = Mul(Pow(a, Integer(-1)), Pow(b, Mul(a, x)), Pow(log(b), Integer(-1)))

BASIC_090 = Mul(x, Pow(E, Mul(a, x)), dx)
TEXT_090 = "Some text"
SOLVE_090 = Mul(Pow(a, Integer(-2)), Pow(E, Mul(a, x)), Add(Mul(a, x), Mul(Integer(-1), 1)))

BASIC_091 = Mul(sin(Mul(b, x)), Pow(E, Mul(a, x)), dx)
TEXT_091 = "Some text"
SOLVE_091 = Mul(Pow(Add(Pow(a, Integer(2)), Pow(b, Integer(2))), Integer(-1)), Pow(E, Mul(a, x)), Add(Mul(a, sin(Mul(b, x))), Mul(Integer(-1), b, cos(Mul(b, x)))))

BASIC_092 = Mul(cos(Mul(b, x)), Pow(E, Mul(a, x)), dx)
TEXT_092 = "Some text"
SOLVE_092 = Mul(Pow(Add(Pow(a, Integer(2)), Pow(b, Integer(2))), Integer(-1)), Pow(E, Mul(a, x)), Add(Mul(a, cos(Mul(b, x))), Mul(b, sin(Mul(b, x)))))

BASIC_093 = Mul(log(Mul(a, x)), dx)
TEXT_093 = "Some text"
SOLVE_093 = Add(Mul(x, log(Mul(a, x))), Mul(Integer(-1), x)) 

BASIC_094 = Mul(Pow(x, Integer(-1)), Pow(log(Mul(a, x)), n), dx)
TEXT_094 = "Some text"
SOLVE_094 = Mul(Pow(Add(n, Integer(1)), Integer(-1)), Pow(ln(Mul(a, x)), Add(n, Integer(1))))

BASIC_095 = Mul(Pow(Mul(x, log(Mul(a, x))), Integer(-1)), dx)
TEXT_095 = "Some text"
SOLVE_095 = log(log(Mul(a, x)))

BASIC_096 = Mul(Pow(sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))), Integer(-1)), dx)
TEXT_096 = "Some text"
SOLVE_096 = asin(Mul(Pow(a, Integer(-1)), Add(x, Mul(Integer(-1), a))))

BASIC_097 = Mul(sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))) , dx)
TEXT_097 = "Some text"
SOLVE_097 = Add(Mul(Add(x,Mul(Integer(-1),a)),Pow(Integer(2),Integer(-1)),sqrt(Add(Mul(Integer(2),a,x),Mul(Integer(-1),Pow(x,Integer(2)))))),Mul(Pow(a,Integer(2)),Pow(Integer(2),Integer(-1)),asin(Mul(Add(x,Mul(Integer(-1),a)),Pow(a,Integer(-1))))))

BASIC_098 = Mul(x, sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))) , dx)
TEXT_098 = "Some text"
SOLVE_098 = asin(Mul(Pow(a, Integer(-1)), Add(x, Mul(Integer(-1), a))))

BASIC_099 = Mul(Pow(x, Integer(-1)), sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))) , dx)
TEXT_099 = "Some text"
SOLVE_099 = Add(sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))), asin(Mul(Add(x, Mul(Integer(-1), a)), Pow(a, Integer(-1)))))

BASIC_100 = Mul(Pow(x, Integer(-2)), sqrt(Add(Mul(Integer(2), a, x), Mul(Integer(-1), Pow(x, Integer(2))))) , dx)
TEXT_100 = "Some text"
SOLVE_100 = Add(Mul(Integer(-2), sqrt(Mul(Add(Mul(Integer(2), a), Mul(Integer(-1), x)), Pow(x, Integer(-1))))), Mul(Integer(-1), asin(Mul(Add(x, Mul(Integer(-1), a)), Pow(a, Integer(-1))))))