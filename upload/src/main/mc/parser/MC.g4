//1711646 - Trần Mạnh Hưng 

grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
  language=Python3;
}

program  : (vardecl|fun_decl)+ EOF ;

vardecl : pritype var (CM var)* SEMI ;

var : ID (LS INTLIT RS)?;
 
pritype : BOOLEAN | FLOAT | INTTYPE | STRING   ;

 //Function decleration 
fun_decl : type_ ID LB paraList RB block_state  ;

type_ : pritype | array_pointer | VOID ;

paraList : para (CM para)* | ;
para : pritype ID(LS RS)? ;    



WS : ('\n'|'\t'|'\r'|' ')+ -> skip ; 
COMMENT
    :   '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;

INTLIT: [0-9]+;

Exponent : [eE] (SUB)?[0-9]+ ;
//FLOATLIT : Exponent '.' INTLIT| INTLIT '.' Exponent | Exponent | INTLIT '.' INTLIT ;
FLOATLIT : INTLIT'.'? Exponent | INTLIT?  '.' INTLIT Exponent? | INTLIT'.' Exponent?  ;

STRINGLIT : '"' ( '\\' [btnfr"'\\] | ~[\r\n\f\b\t\\"] )* '"'{self.text = self.text[1:-1]} ;

//Types and Values


array : pritype ID LS INTLIT RS ;

array_pointer : pritype ID LS  RS | pritype LS RS  ;  
//Phần 6
PLUS : '+' ;

SUB : '-' ;

MUL : '*' ;

NOT : '!' ;

OR : '||' ;

DIF : '!=' ;

LESS : '<' ;

LESS_EQUAL : '<=' ;

ASSIGN : '=' ;

DIV : '/' ;

MOD : '%' ;

AND : '&&' ;

EQUAL : '==' ;

GREATER : '>' ;

GREATER_EQUAL : '>=' ;

BOOLEAN : 'boolean' ;

BREAK : 'break' ;

CONTINUE : 'continue' ;

ELSE : 'else' ;

FOR : 'for' ;

FLOAT : 'float' ;

IF : 'if' ;



RETURN : 'return' ;

INTTYPE : 'int' ;

VOID : 'void' ;

DO :'do' ;

WHILE : 'while' ;

TRUE : 'true' ;

FALSE : 'false' ;

STRING : 'string' ;




LS : '[' ;

RS : ']' ;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

CM : ',' ;


//variables

//Expression

exp : exp1 | exp1 ASSIGN exp ;

exp1 : exp2 | exp1 OR exp2 ;

exp2 : exp3 | exp2 AND exp3 ;

exp3 : exp4 | exp4 EQUAL exp4 | exp4 DIF exp4 ;

exp4 : exp5 
       | exp5 GREATER exp5
       | exp5 GREATER_EQUAL  exp5 
       | exp5 LESS exp5 
       | exp5 LESS_EQUAL exp5 
       ;

exp5 : exp6  
       |exp5 PLUS exp6 
       | exp5 SUB exp6
      ;

exp6 : exp7 
       | exp6 DIV exp7
       | exp6 MUL exp7 
       | exp6 MOD exp7 
      ;

exp7 : exp8 | SUB exp7 | NOT exp7 ;

exp8 : operands | operands LS exp RS ;

operands :  INTLIT | STRINGLIT | bool_lit | ID | FLOATLIT |  LB  exp  RB | func_call;

bool_lit : TRUE|FALSE ; 

//Type Coercions
 
//Index Expression 
index_op : exp LS exp RS ;

//Invocation Expression 
func_call : ID LB listexp RB ;

listexp :(exp (CM exp)* | ) ;


//Evaluation Order 

//Statements and control flow 




statement : if_state 
          | for_state 
          | do_while_state 
          | exp_statement 
          | block_state 
          | return_statement
          | break_state
          | continue_state 
          ;
//if statement
if_state : IF LB exp RB statement (ELSE  (statement) )? ;
//do while Statementsnt 
do_while_state:DO statementList WHILE exp SEMI ;

statementList : statement+ ;

for_state : FOR LB exp SEMI exp SEMI  exp RB statement ;

break_state : BREAK SEMI ; 

continue_state : CONTINUE SEMI ;

return_statement : RETURN exp? SEMI ;

exp_statement :exp SEMI ;

block_state : LP var_stmtList RP ;
var_stmtList : (vardecl|statement)* ;



ID: [_a-zA-Z][_a-zA-Z0-9]*;
//keywords

//int getInt() 



ERROR_CHAR: .;
UNCLOSE_STRING: '"' ( '\\' [btnfr"'\\] | ~[\b\t\f\r\n\\"] )* ;
ILLEGAL_ESCAPE:    ('"' (( '\\' [btnfr"\\] | ~[\r\\"\b\f\t] )*)) '\\' ~[btnfr"'\\];