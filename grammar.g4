/*
 * options
 */

grammar latex;

options {
    lenguage = Python3;
}

/*
 * skip tokens
 */

WHITESACE: [ \t\r\n ]+ -> skip;
THINSPACE: ('\\,' | '\\thinspace') -> skip;
MEDSPACE: ('\\:' | '\\medspace') -> skip;
QUAD: '\\quad' -> skip;
QQUAD: '\\qquad' -> skip;
NEGTHINSPACE: ('\\!' | '\\negthinspace') -> skip;
NEGMEDSPACE: '\\negmedspace' -> skip;
NEGTHICKSPACE: '\\negthickspace' -> skip;
CMD_LEFT: '\\left' -> skip;
CMD_RIGHT: '\\right' -> skip;

IGNORE: (
      '\\vrule'
    | '\\vcenter'
	| '\\vbox'
	| '\\vskip'
	| '\\vspace'
	| '\\hfil'
	| '\\*'
	| '\\-'
	| '\\.'
	| '\\/'
	| '\\"'
	| '\\('
	| '\\='
) -> skip;

/*
 * arithm tokens
 */

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

/*
 * group tokens
 */

L_PAREN: '(';
R_PAREN: ')';
L_BRACE: '{';
R_BRACE: '}';
L_BRACE_LITERAL: '\\{';
R_BRACE_LITERAL: '\\}';
L_BRACKET: '[';
R_BRACKET: ']';

/*
 * basic functions
 */

FUNC_EXP: '\\exp';
FUNC_LOG: '\\log';
FUNC_LN: '\\ln';
FUNC_SIN: '\\sin';
FUNC_COS: '\\cos';
FUNC_TAN: '\\tan';
FUNC_CSC: '\\csc';
FUNC_SEC: '\\sec';
FUNC_COT: '\\cot';
FUNC_SQRT: '\\sqrt';

/*
 * hard functions
 */

FUNC_ARCSIN: '\\arcsin';
FUNC_ARCCOS: '\\arccos';
FUNC_ARCTAN: '\\arctan';
FUNC_ARCCSC: '\\arccsc';
FUNC_ARCSEC: '\\arcsec';
FUNC_ARCCOT: '\\arccot';

FUNC_SINH: '\\sinh';
FUNC_COSH: '\\cosh';
FUNC_TANH: '\\tanh';
FUNC_ARSINH: '\\arsinh';
FUNC_ARCOSH: '\\arcosh';
FUNC_ARTANH: '\\artanh';

/* 
 * 
 */









