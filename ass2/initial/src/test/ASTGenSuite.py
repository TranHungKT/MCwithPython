 unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):    
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_more_complex_program(self):
        """More complex program"""
        input = """
                int a,b;
                }"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main() {a+1;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("+",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_1(self):
        input = """int main(){
        for(i = 0; i < 4; i = i + 1){
        int a;
        a = i * i;
        }
        return a;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(4)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),BinaryOp('*',Id('i'),Id('i')))])),Return(Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))
    def test_2(self):
        input = """void main() {
                    float b ;
                      if(c) b = 5 ;
                    }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("b",FloatType()),If(Id("c"),BinaryOp("=",Id("b"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_3(self):
        input = """void main() {    
                     getInt();
                        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("getInt"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))    
    def test_4(self):
        input = """void main() {    
                     putInt(4);
                        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("putInt"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_5(self):
        input = """void main() {    
                     getFloat();
                        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("getFloat"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))               
    def test_34(self):
        input = """void main() {    
                     putFloat(4.0);
                        }"""
        expect =str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("putFloat"),[FloatLiteral(4.0)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))        
    def test_33(self):
        input = """void main() {    
                     putFloatLn(4.0);
                        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("putFloatLn"),[FloatLiteral(4.0)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_6(self):
        input = """void main() {    
                     putBool(true);
                        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("putBool"),[BooleanLiteral("true")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))               
    def test_7(self):
        input = """void main() {    
                     putBoolLn(false);
                        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('putBoolLn'),[BooleanLiteral('false')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_8(self):
        input = """void main() {    
                     putString("tran");
                        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("putString"),[StringLiteral("tran")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))               
    def test_9(self):
        input = """void main() {    
                     putStringLn("tran");
                        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("putStringLn"),[StringLiteral("tran")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))               
    def test_10(self):
        input = """void main() {
                      int i;
                      for( a = 0 ; a < 10 ; a + 1 ) {
                         if(a == 1) break;
                        }
                      } """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("+",Id("a"),IntLiteral(1)),Block([If(BinaryOp("==",Id("a"),IntLiteral(1)),Break())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))               
    def test_more_super_complex_program2(self):
        """More complex program"""
        input = """int i ;
                   int f ( ) {
                         return 200;
                             } 
                    void main () {
                        int main ;
                        main = f ( ) ;
                        putIntLn ( main ) ;
                        {
                        int i ;
                        int main ;
                        int f ;
                        main = f = i = 100;
                        putIntLn ( i ) ;
                        putIntLn ( main ) ;
                        putIntLn ( f ) ;
                        }
                        putIntLn ( main ) ;
                    }
                    
                """
        expect = str(Program([VarDecl("i",IntType()),FuncDecl(Id("f"),[],IntType(),Block([Return(IntLiteral(200))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("main",IntType()),BinaryOp("=",Id("main"),CallExpr(Id("f"),[])),CallExpr(Id("putIntLn"),[Id("main")]),Block([VarDecl("i",IntType()),VarDecl("main",IntType()),VarDecl("f",IntType()),BinaryOp("=",Id("main"),BinaryOp("=",Id("f"),BinaryOp("=",Id("i"),IntLiteral(100)))),CallExpr(Id("putIntLn"),[Id("i")]),CallExpr(Id("putIntLn"),[Id("main")]),CallExpr(Id("putIntLn"),[Id("f")])]),CallExpr(Id("putIntLn"),[Id("main")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))                        
    def test_11(self):
        input = """int a; float b; """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",FloatType())])) 
        self.assertTrue(TestAST.checkASTGen(input,expect,317)) 
    def test_12(self):
        input = """int a; float b;
                    void main(){} """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",FloatType()),FuncDecl(Id("main"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_13(self):
        input = """int a; float b;
                    void main(){
                    putIntLn(20,40,50);
                    } """
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',FloatType()),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('putIntLn'),[IntLiteral(20),IntLiteral(40),IntLiteral(50)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
   
    def test_14(self):
        input = """int a; float b;
                    void main(){
                    putIntLn(20,40,50);
                    getInt();
                    getString(tran);
                    } """
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',FloatType()),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('putIntLn'),[IntLiteral(20),IntLiteral(40),IntLiteral(50)]),CallExpr(Id('getInt'),[]),CallExpr(Id('getString'),[Id('tran')])]))]))    
        self.assertTrue(TestAST.checkASTGen(input,expect,320))      

    def test_15(self):
        input = """ void main(){
                    foo( a,abc[50],b);
                    putIntLn ( 30 ) ;
                   } """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[Id('a'),ArrayCell(Id('abc'),IntLiteral(50)),Id('b')]),CallExpr(Id('putIntLn'),[IntLiteral(30)])]))]))    
        self.assertTrue(TestAST.checkASTGen(input,expect,321))   
    def test_32(self):
        input = """ void main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([]))]))   
        self.assertTrue(TestAST.checkASTGen(input,expect,322))   
    def test_16(self):
        input = """int main(){
        if(a == b) return c;
        else return b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),Id("b")),Return(Id("c")),Return(Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_assignment_statement_4(self):
        input = """int main(){
        int a;
        a = a;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))
    def test_18(self):
        input = """ int main(){
             int i ;
             for(i = 0;i<10;i+1)
             {
                  i = i + 1 ;
                  if(i == 9 ) i = i * 2;
             }
          }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("+",Id("i"),IntLiteral(1)),Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",Id("i"),IntLiteral(9)),BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),IntLiteral(2))))]))]))]))    
        self.assertTrue(TestAST.checkASTGen(input,expect,325))   
    def test_19(self):
        input = """ int main(){
            int i,k ;
            int k;
            for(i = 0;i<10;i+1)
            {
                i = i * 2;
            }
            if(k>i) k = i;
          }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('i',IntType()),VarDecl('k',IntType()),VarDecl('k',IntType()),For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),Block([BinaryOp('=',Id('i'),BinaryOp('*',Id('i'),IntLiteral(2)))])),If(BinaryOp('>',Id('k'),Id('i')),BinaryOp('=',Id('k'),Id('i')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_20(self):
        input = """int foo(int a, int b , float c){

        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',FloatType())],IntType(),Block([]))]))   
        self.assertTrue(TestAST.checkASTGen(input,expect,327))   
    def test_21(self):
        input = """int foo(int a, int b , float c){
                   if(1) a = 2 ;
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',FloatType())],IntType(),Block([If(IntLiteral(1),BinaryOp('=',Id('a'),IntLiteral(2)))]))]))   
        self.assertTrue(TestAST.checkASTGen(input,expect,328)) 
    def test_22(self):
        input = """boolean foo(int a, int b , float c){
                     int a;
                     if(a==1) break;
                     else continue;
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',FloatType())],BoolType(),Block([VarDecl('a',IntType()),If(BinaryOp('==',Id('a'),IntLiteral(1)),Break(),Continue())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))  
    def test_23(self):
        input = """boolean b(int a) {
               do{
                 a + 1;
               }while(a<100);
               }"""
        expect = str(Program([FuncDecl(Id('b'),[VarDecl('a',IntType())],BoolType(),Block([Dowhile([Block([BinaryOp('+',Id('a'),IntLiteral(1))])],BinaryOp('<',Id('a'),IntLiteral(100)))]))]))     
        self.assertTrue(TestAST.checkASTGen(input,expect,230))  
    def test_24(self):
        input = """int foo(boolean a, boolean b){
                        if(b == true) return a = b;
                        else return a = true;
                    }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',BoolType()),VarDecl('b',BoolType())],IntType(),Block([If(BinaryOp('==',Id('b'),BooleanLiteral('true')),Return(BinaryOp('=',Id('a'),Id('b'))),Return(BinaryOp('=',Id('a'),BooleanLiteral('true'))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_25(self):
        input = """void main(){
                        int a;
                        if(a == 0) a = 2;
                        else if(a == 3) a = 1;
                        else a = 3;
                    }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),If(BinaryOp('==',Id('a'),IntLiteral(0)),BinaryOp('=',Id('a'),IntLiteral(2)),If(BinaryOp('==',Id('a'),IntLiteral(3)),BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('=',Id('a'),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_26(self):
        input = """int main(){
                    for(i;y;z ){
                        a = 0;
                        a = a + 1;     
                        }
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),Block([BinaryOp('=',Id('a'),IntLiteral(0)),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))]))]))]))

        self.assertTrue(TestAST.checkASTGen(input, expect, 333))                                                 
    def test_27(self):
        input = """int main(){
        for(i = 0; i < 10; i = i + 1)
        if(i > 3) i = i * 2;
        return 0;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),If(BinaryOp('>',Id('i'),IntLiteral(3)),BinaryOp('=',Id('i'),BinaryOp('*',Id('i'),IntLiteral(2))))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))                                                
    def test_28(self):
        input = """int main(){
        int foo[2];
        foo[0] = 2;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('foo',ArrayType(2,IntType())),BinaryOp('=',ArrayCell(Id('foo'),IntLiteral(0)),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))
    def test_29(self):
        input = """void main(){
        string abc ;
        float a ; 
        a = 4.0 ; 
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('abc',StringType()),VarDecl('a',FloatType()),BinaryOp('=',Id('a'),FloatLiteral(4.0))]))]))   
        self.assertTrue(TestAST.checkASTGen(input,expect,336))    
    def test_30(self):
        input = """int main(){
        a + 1 + 2 = 10 ;
        b + 2 + 4 / 10 = 1 ;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',BinaryOp('+',BinaryOp('+',Id('a'),IntLiteral(1)),IntLiteral(2)),IntLiteral(10)),BinaryOp('=',BinaryOp('+',BinaryOp('+',Id('b'),IntLiteral(2)),BinaryOp('/',IntLiteral(4),IntLiteral(10))),IntLiteral(1))]))]))    
        self.assertTrue(TestAST.checkASTGen(input,expect,337))    
    def test_31(self):
        input = """int main(){
        a + 1 + 2 = 10 ;
        b = b + 2 + 4 / 10;
        if(a==b){
         return a = b +10;
        } 
        }        
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',BinaryOp('+',BinaryOp('+',Id('a'),IntLiteral(1)),IntLiteral(2)),IntLiteral(10)),BinaryOp('=',Id('b'),BinaryOp('+',BinaryOp('+',Id('b'),IntLiteral(2)),BinaryOp('/',IntLiteral(4),IntLiteral(10)))),If(BinaryOp('==',Id('a'),Id('b')),Block([Return(BinaryOp('=',Id('a'),BinaryOp('+',Id('b'),IntLiteral(10))))]))]))]))    
        self.assertTrue(TestAST.checkASTGen(input,expect,338))    
    def test_35(self):
        input = """int foo(int a, int b, int c){
        if(a == 0) b = c;
        else if(a == 1) c = b;
        else a = c;
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType())],IntType(),Block([If(BinaryOp('==',Id('a'),IntLiteral(0)),BinaryOp('=',Id('b'),Id('c')),If(BinaryOp('==',Id('a'),IntLiteral(1)),BinaryOp('=',Id('c'),Id('b')),BinaryOp('=',Id('a'),Id('c'))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))    
    def test_36(self):
        input = """int foo(int a, int b, int c){
        if(a == 0) b = c;
        else if(a == 1) c = b;
        else a = c;
        for(a;a<10;a + 1)
        {
         a + 1;
        }
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType())],IntType(),Block([If(BinaryOp('==',Id('a'),IntLiteral(0)),BinaryOp('=',Id('b'),Id('c')),If(BinaryOp('==',Id('a'),IntLiteral(1)),BinaryOp('=',Id('c'),Id('b')),BinaryOp('=',Id('a'),Id('c')))),For(Id('a'),BinaryOp('<',Id('a'),IntLiteral(10)),BinaryOp('+',Id('a'),IntLiteral(1)),Block([BinaryOp('+',Id('a'),IntLiteral(1))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))    
    def test_37(self):
        input = """int foo(int a, int b, int c){
        for(a;a<10;a + 1)
        {
         getInt();
         putIntLn(4);
        }
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType())],IntType(),Block([For(Id('a'),BinaryOp('<',Id('a'),IntLiteral(10)),BinaryOp('+',Id('a'),IntLiteral(1)),Block([CallExpr(Id('getInt'),[]),CallExpr(Id('putIntLn'),[IntLiteral(4)])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))
    def test_38(self):
        input = """int foo(int a, int b, int c){
        if(a == 0) b = c;
        else a = c;
        for(a;a<10;a + 1)
        {
         putString(tran) ; 
         putBool(false);
         putBool(true);
        }
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType())],IntType(),Block([If(BinaryOp('==',Id('a'),IntLiteral(0)),BinaryOp('=',Id('b'),Id('c')),BinaryOp('=',Id('a'),Id('c'))),For(Id('a'),BinaryOp('<',Id('a'),IntLiteral(10)),BinaryOp('+',Id('a'),IntLiteral(1)),Block([CallExpr(Id('putString'),[Id('tran')]),CallExpr(Id('putBool'),[BooleanLiteral('false')]),CallExpr(Id('putBool'),[BooleanLiteral('true')])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))   
    def test_39(self):
        input = """void main( ){ if (a) if (b) if (c) a; else a; else a; }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([If(Id('a'),If(Id('b'),If(Id('c'),Id('a'),Id('a')),Id('a')))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))       
    def test_40(self):
        input = """int main(){
                break ;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))
    def test_41(self):
        input = """boolean a ; """
        expect = str(Program([VarDecl('a',BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))               
    def test_42(self):
        input = """void foo(){
            putIntLn(3);
            getInt(3);
            putString(tran);
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[],VoidType(),Block([CallExpr(Id('putIntLn'),[IntLiteral(3)]),CallExpr(Id('getInt'),[IntLiteral(3)]),CallExpr(Id('putString'),[Id('tran')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))          
    def test_43(self):
        input = """void main(){
                    int a;
                    if(a == 0) a = 2;
                    else if(a == 3) a = 1;
                    else a;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),If(BinaryOp('==',Id('a'),IntLiteral(0)),BinaryOp('=',Id('a'),IntLiteral(2)),If(BinaryOp('==',Id('a'),IntLiteral(3)),BinaryOp('=',Id('a'),IntLiteral(1)),Id('a')))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))          
    def test_44(self):
        input = """boolean main(){
                        int a;
                        do a + 1 = 0 ;
                        while (true);
                    }"""
        expect = str(Program([FuncDecl(Id('main'),[],BoolType(),Block([VarDecl('a',IntType()),Dowhile([BinaryOp('=',BinaryOp('+',Id('a'),IntLiteral(1)),IntLiteral(0))],BooleanLiteral('true'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))            
    def test_45(self):
        input = """int main(){
                        int a;
                        do break ;
                        while a > 0;
                    }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),Dowhile([Break()],BinaryOp('>',Id('a'),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 349)) 
    def test_46(self):
        input = """int main(){
                    int a;
                    return ;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))
    def test_47(self):
        input = """int main(){
                    int a;
                    continue ;
                }"""
        expect =str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))    
    def test_48(self):
        input = """int main(){
        int a;
        for(a = 0; a<10;a+ 1)
        {
          continue;
        }
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),For(BinaryOp('=',Id('a'),IntLiteral(0)),BinaryOp('<',Id('a'),IntLiteral(10)),BinaryOp('+',Id('a'),IntLiteral(1)),Block([Continue()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))
    def test_49(self):
        input = """int main(){
        int a;
        for(a = 0; a<10;a+ 1)
        {
          if(a==9) break;
        }
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),For(BinaryOp('=',Id('a'),IntLiteral(0)),BinaryOp('<',Id('a'),IntLiteral(10)),BinaryOp('+',Id('a'),IntLiteral(1)),Block([If(BinaryOp('==',Id('a'),IntLiteral(9)),Break())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))   
    def test_64(self):
        input = """int main(){
        int a; boolean b;
        for(a = 0; a<10;a+ 1)
        { 
          putIntLn(5) ;
          if(a==9) getInt();
        }
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),VarDecl('b',BoolType()),For(BinaryOp('=',Id('a'),IntLiteral(0)),BinaryOp('<',Id('a'),IntLiteral(10)),BinaryOp('+',Id('a'),IntLiteral(1)),Block([CallExpr(Id('putIntLn'),[IntLiteral(5)]),If(BinaryOp('==',Id('a'),IntLiteral(9)),CallExpr(Id('getInt'),[]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))         
    def test_50(self):
        input = """void main(){
        int a;
        do a = a*a;
        while a < 3;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),Dowhile([BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('a')))],BinaryOp('<',Id('a'),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))
    def test_51(self):
        input = """void main(){
        float a ;
        do a = a*2;
        while a < 10;
        return a ;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',FloatType()),Dowhile([BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),IntLiteral(2)))],BinaryOp('<',Id('a'),IntLiteral(10))),Return(Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))            
    def test_52(self):
        input = """void main(){
        int a;
        do a = a*2;
        while a < 10;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),Dowhile([BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),IntLiteral(2)))],BinaryOp('<',Id('a'),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))    
    def test_53(self):
        input = """void main(){
        int a;
        do a = a*2;
        while(a>2); 
        }"""
        expect =str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),Dowhile([BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),IntLiteral(2)))],BinaryOp('>',Id('a'),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))    
    def test_54(self):
        input = """void main(){
        int a;
        do{
          if(a<10) a + 1;
          else break;
        } 
        while(a<10); 
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),Dowhile([Block([If(BinaryOp('<',Id('a'),IntLiteral(10)),BinaryOp('+',Id('a'),IntLiteral(1)),Break())])],BinaryOp('<',Id('a'),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))        
    def test_55(self):
        input = """int main(){
        int a;
        a = d(foo);
        }
        float e;
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),CallExpr(Id('d'),[Id('foo')]))])),VarDecl('e',FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))
          
    def test_56(self):
        input = """void main(){
        int a;
        for(a;a;a){
            break;
        }
        
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),For(Id('a'),Id('a'),Id('a'),Block([Break()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))     
    def test_57(self):
        input = """int main(){
        int a;
        for(a = 1;a<10;a){
         a = 10 ;
        }
        
        }  """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),For(BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('<',Id('a'),IntLiteral(10)),Id('a'),Block([BinaryOp('=',Id('a'),IntLiteral(10))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))   
    def test_58(self):
        input = """void main(){
        int a;
        for(a<10;a;a){
          continue;
        }
        
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),For(BinaryOp('<',Id('a'),IntLiteral(10)),Id('a'),Id('a'),Block([Continue()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))                     
    def test_59(self):
        input = """void main(){
        int a;
        do{
        a = a*2;
        if(a > 6) break;
        }
        while a < 12;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),Dowhile([Block([BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),IntLiteral(2))),If(BinaryOp('>',Id('a'),IntLiteral(6)),Break())])],BinaryOp('<',Id('a'),IntLiteral(12)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 264))    
    def test_60(self):
        input = """void main(){
        int a;
        do{
        a = a*2;      
        if(a > 6) continue;
        }
        while a < 12;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),Dowhile([Block([BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),IntLiteral(2))),If(BinaryOp('>',Id('a'),IntLiteral(6)),Continue())])],BinaryOp('<',Id('a'),IntLiteral(12)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 265))     
    def test_61(self):
        input = """void main(){
        boolean a;
        do break;
        while a < 10;
        return a ;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',BoolType()),Dowhile([Break()],BinaryOp('<',Id('a'),IntLiteral(10))),Return(Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))     
    def test_62(self):
        input = """
        int foo(int a){
        float a ;
        do a = a*2;
        while (a < 10);
        return a ;}
        """
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType())],IntType(),Block([VarDecl('a',FloatType()),Dowhile([BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),IntLiteral(2)))],BinaryOp('<',Id('a'),IntLiteral(10))),Return(Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))           
    def test_63(self):
        input = """int main(){
        int foo[10];
        foo[0] = 3;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('foo',ArrayType(10,IntType())),BinaryOp('=',ArrayCell(Id('foo'),IntLiteral(0)),IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))       
    def test_65(self):
        input = """
            int a ;
            float foo(){
            float b;
            a != b ; 
            a = b +1 ;
            return a/2;
            }
            """
        expect = str(Program([VarDecl('a',IntType()),FuncDecl(Id('foo'),[],FloatType(),Block([VarDecl('b',FloatType()),BinaryOp('!=',Id('a'),Id('b')),BinaryOp('=',Id('a'),BinaryOp('+',Id('b'),IntLiteral(1))),Return(BinaryOp('/',Id('a'),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))     
    def test_66(self):
        input = """
            int a ;
            float foo(){
            float b;
            if(a != b)  
            return a = b +1 ;
            else return a = b - 1;
            }"""
        expect = str(Program([VarDecl('a',IntType()),FuncDecl(Id('foo'),[],FloatType(),Block([VarDecl('b',FloatType()),If(BinaryOp('!=',Id('a'),Id('b')),Return(BinaryOp('=',Id('a'),BinaryOp('+',Id('b'),IntLiteral(1)))),Return(BinaryOp('=',Id('a'),BinaryOp('-',Id('b'),IntLiteral(1)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))
    def test_67(self):
        input = """
            int a ;
            int foo(){
            float b;
            if(a != b)  
            break ;
            else continue;
            return;}
            """
        expect = str(Program([VarDecl('a',IntType()),FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('b',FloatType()),If(BinaryOp('!=',Id('a'),Id('b')),Break(),Continue()),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))  
    def test_68(self):
        input = """
            int a ;
            int foo(){
            float b;
            if(a != b)  
            a = b +1 ;
            else a = b - 1;
            a[100];
            100;
            b;
            return b;}
            """
        expect = str(Program([VarDecl('a',IntType()),FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('b',FloatType()),If(BinaryOp('!=',Id('a'),Id('b')),BinaryOp('=',Id('a'),BinaryOp('+',Id('b'),IntLiteral(1))),BinaryOp('=',Id('a'),BinaryOp('-',Id('b'),IntLiteral(1)))),ArrayCell(Id('a'),IntLiteral(100)),IntLiteral(100),Id('b'),Return(Id('b'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))  
    def test_69(self):
        input = """
            int foo(){
            float b;
            a[100];
            100;
            b;
            return b;}
            """
        expect = str(Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('b',FloatType()),ArrayCell(Id('a'),IntLiteral(100)),IntLiteral(100),Id('b'),Return(Id('b'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))       
    def test_70(self):
        input = """
           void tran(){
           int a ; 
           foo(1.,2.3,4);
           }
            """
        expect = str(Program([FuncDecl(Id('tran'),[],VoidType(),Block([VarDecl('a',IntType()),CallExpr(Id('foo'),[FloatLiteral(1.0),FloatLiteral(2.3),IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))          
    def test_71(self):
        input = """int foo(int a, int b){
        if(a == 0) return b = c;
        else if(a == 1) return c = b;
        else return a = 10;

        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',IntType())],IntType(),Block([If(BinaryOp('==',Id('a'),IntLiteral(0)),Return(BinaryOp('=',Id('b'),Id('c'))),If(BinaryOp('==',Id('a'),IntLiteral(1)),Return(BinaryOp('=',Id('c'),Id('b'))),Return(BinaryOp('=',Id('a'),IntLiteral(10)))))]))]))

        self.assertTrue(TestAST.checkASTGen(input, expect, 375))
    def test_72(self):
        input = """
        int main() {
        int a;
        if(a==10) {a + 1 = 11;} 
        else break;
        } 
            """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),If(BinaryOp('==',Id('a'),IntLiteral(10)),Block([BinaryOp('=',BinaryOp('+',Id('a'),IntLiteral(1)),IntLiteral(11))]),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))              
    def test_73(self):
        input = """
           int main() {
           int a;
           if(a==10) a + 1 = 11 ; else a + 1 = 12  ;
        }  
            """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),If(BinaryOp('==',Id('a'),IntLiteral(10)),BinaryOp('=',BinaryOp('+',Id('a'),IntLiteral(1)),IntLiteral(11)),BinaryOp('=',BinaryOp('+',Id('a'),IntLiteral(1)),IntLiteral(12)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))          
    def test_74(self):
        input = """int main(){
        foo(1.1);
        int a;
        doo(a);
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('foo'),[FloatLiteral(1.1)]),VarDecl('a',IntType()),CallExpr(Id('doo'),[Id('a')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))
    def test_75(self):
        input = """int main(){
        foo(1);
        int a;
        doo(a);
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('foo'),[IntLiteral(1)]),VarDecl('a',IntType()),CallExpr(Id('doo'),[Id('a')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))
    def test_76(self):
        input = """int main(){
        int a;
        doo(a);
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),CallExpr(Id('doo'),[Id('a')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))
    def test_77(self):
        input = """int main(){
        int a;
        doo(a);
        float b;
        a = b/10;
        a = a +10;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),CallExpr(Id('doo'),[Id('a')]),VarDecl('b',FloatType()),BinaryOp('=',Id('a'),BinaryOp('/',Id('b'),IntLiteral(10))),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))                           
    def test_78(self):
        input = """int main(){
        int a;
        a = b/10;
        a = a +10;
        putIntLn(a);
        return a;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),BinaryOp('/',Id('b'),IntLiteral(10))),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(10))),CallExpr(Id('putIntLn'),[Id('a')]),Return(Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))        
    def test_79(self):
        input = """int main(){
        int a;
        doo(a);
        float b;
        string c ; 
        putString(c) ;
        putStringLn(c);
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),CallExpr(Id('doo'),[Id('a')]),VarDecl('b',FloatType()),VarDecl('c',StringType()),CallExpr(Id('putString'),[Id('c')]),CallExpr(Id('putStringLn'),[Id('c')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))          
    def test_80(self):
        input = """
        int c;
        int doo(int a){
        float b;
        a = b/10;
        a = a +10;
        return a;
        }
        """
        expect = str(Program([VarDecl('c',IntType()),FuncDecl(Id('doo'),[VarDecl('a',IntType())],IntType(),Block([VarDecl('b',FloatType()),BinaryOp('=',Id('a'),BinaryOp('/',Id('b'),IntLiteral(10))),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(10))),Return(Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))    
    def test_81(self):
        input = """void main(){
        int a,b;
        do{ 
        a = a*b;
        if(a > b) break;
        }
        while a < 10;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),Dowhile([Block([BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('b'))),If(BinaryOp('>',Id('a'),Id('b')),Break())])],BinaryOp('<',Id('a'),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))         
    def test_if_statement_5(self):
        input = """int foo(int a){
        if(a != 10){
        int b;
        b = a;
        return b*2;
        }
        else{
        int c;
        c = a*2*2*2-1;
        }
        return a*2;
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType())],IntType(),Block([If(BinaryOp('!=',Id('a'),IntLiteral(10)),Block([VarDecl('b',IntType()),BinaryOp('=',Id('b'),Id('a')),Return(BinaryOp('*',Id('b'),IntLiteral(2)))]),Block([VarDecl('c',IntType()),BinaryOp('=',Id('c'),BinaryOp('-',BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('a'),IntLiteral(2)),IntLiteral(2)),IntLiteral(2)),IntLiteral(1)))])),Return(BinaryOp('*',Id('a'),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))  
    def test_83(self):
        input = """
                int a(int b){
                do{ 
                a = a*b;
                if(a > b) break;
                }
                while (a < 10);
                }"""
        expect = str(Program([FuncDecl(Id('a'),[VarDecl('b',IntType())],IntType(),Block([Dowhile([Block([BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),Id('b'))),If(BinaryOp('>',Id('a'),Id('b')),Break())])],BinaryOp('<',Id('a'),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))    
    def test_90(self):
        input = """void main(){
        int a,b;
        a = b + 2;
        if(a>b) return;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),BinaryOp('=',Id('a'),BinaryOp('+',Id('b'),IntLiteral(2))),If(BinaryOp('>',Id('a'),Id('b')),Return())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))          
    def test_89(self):
        input = """
        int a(){
        putBoolLn(true);
        putInt();
        putIntLn(5);
        }"""
        expect = str(Program([FuncDecl(Id('a'),[],IntType(),Block([CallExpr(Id('putBoolLn'),[BooleanLiteral('true')]),CallExpr(Id('putInt'),[]),CallExpr(Id('putIntLn'),[IntLiteral(5)])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))
    def test_84(self):
        input = """void main(){
        int a,b;
        if(a>b) continue;
        return ;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),If(BinaryOp('>',Id('a'),Id('b')),Continue()),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390)) 
    def test_85(self):
        input = """int foo(int a, int b){
        if(a > b) return a;
        return b;
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',IntType())],IntType(),Block([If(BinaryOp('>',Id('a'),Id('b')),Return(Id('a'))),Return(Id('b'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))                   
    def test_86(self):
        input = """int foo(int a, int b,float c){
        if(a > b) return a;
        else break;
        return b;
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',FloatType())],IntType(),Block([If(BinaryOp('>',Id('a'),Id('b')),Return(Id('a')),Break()),Return(Id('b'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))
    def test_87(self):
        input = """
        int foo(int a){
            for(i = 0;i < 10;i=i+1)
            if(i > a) a = i*2;
            return a;
        }
        void main(){
            int b,c;
            c = foo(7);
            b = foo(8);
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType())],IntType(),Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),If(BinaryOp('>',Id('i'),Id('a')),BinaryOp('=',Id('a'),BinaryOp('*',Id('i'),IntLiteral(2))))),Return(Id('a'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('b',IntType()),VarDecl('c',IntType()),BinaryOp('=',Id('c'),CallExpr(Id('foo'),[IntLiteral(7)])),BinaryOp('=',Id('b'),CallExpr(Id('foo'),[IntLiteral(8)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))    
    def test_88(self):
        input = """
        int foo(int a){
            do a + 1 ;
            while a<10;
            return a;
        }
        void main(){
            int b,c;
            do b = b * c;
            while b <100;
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType())],IntType(),Block([Dowhile([BinaryOp('+',Id('a'),IntLiteral(1))],BinaryOp('<',Id('a'),IntLiteral(10))),Return(Id('a'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('b',IntType()),VarDecl('c',IntType()),Dowhile([BinaryOp('=',Id('b'),BinaryOp('*',Id('b'),Id('c')))],BinaryOp('<',Id('b'),IntLiteral(100)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))    
    def test_91(self):
        input = """
        int a,b,c;
        int foo(){
            do a + 1 ;
            while a<10;
            return a;
        }
        void main(){
            do b = b * c;
            while b <100;
        }
        """
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType()),FuncDecl(Id('foo'),[],IntType(),Block([Dowhile([BinaryOp('+',Id('a'),IntLiteral(1))],BinaryOp('<',Id('a'),IntLiteral(10))),Return(Id('a'))])),FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([BinaryOp('=',Id('b'),BinaryOp('*',Id('b'),Id('c')))],BinaryOp('<',Id('b'),IntLiteral(100)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))   
    def test_92(self):
        input = """
        int a,b,c;
        int foo(int a){
            putIntLn(a);
        }
        void main(){
            putIntLn(b);
        }
        """
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType()),FuncDecl(Id('foo'),[VarDecl('a',IntType())],IntType(),Block([CallExpr(Id('putIntLn'),[Id('a')])])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('putIntLn'),[Id('b')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))     
    def test_93(self):
        input = """
            int a,b,c;
            int foo(int a){
                putIntLn(a);
            }
            void main(){
                putIntLn(b);
            }
            void main(){
                do b = b * c;
                while b <100;
            }
        """
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType()),FuncDecl(Id('foo'),[VarDecl('a',IntType())],IntType(),Block([CallExpr(Id('putIntLn'),[Id('a')])])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('putIntLn'),[Id('b')])])),FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([BinaryOp('=',Id('b'),BinaryOp('*',Id('b'),Id('c')))],BinaryOp('<',Id('b'),IntLiteral(100)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))    
    def test_94(self):
        input = """
        int a,b,c;
        int foo(int a){
            putIntLn(a);
            if(a==10) 
              for(b = 1;b<a ;b +1 )
                b +1;
            else break;    
        }
        void main(){
            putIntLn(b);
        }
        """
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType()),FuncDecl(Id('foo'),[VarDecl('a',IntType())],IntType(),Block([CallExpr(Id('putIntLn'),[Id('a')]),If(BinaryOp('==',Id('a'),IntLiteral(10)),For(BinaryOp('=',Id('b'),IntLiteral(1)),BinaryOp('<',Id('b'),Id('a')),BinaryOp('+',Id('b'),IntLiteral(1)),BinaryOp('+',Id('b'),IntLiteral(1))),Break())])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('putIntLn'),[Id('b')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))   
    def test_95(self):
        input = """
        int foo(int x,int a, int b, int c){
            return ;
        }
        int main(){
            return foo(3,4,2,1);
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('x',IntType()),VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType())],IntType(),Block([Return()])),FuncDecl(Id('main'),[],IntType(),Block([Return(CallExpr(Id('foo'),[IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(1)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))   
    def test_program_96(self):
        input = """
        int foo(int x,int a, int b, int c){
            x*a*b*c/a/b/c;
        }
        int main(){
            break ;
        }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('x',IntType()),VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType())],IntType(),Block([BinaryOp('/',BinaryOp('/',BinaryOp('/',BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('x'),Id('a')),Id('b')),Id('c')),Id('a')),Id('b')),Id('c'))])),FuncDecl(Id('main'),[],IntType(),Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))         
             import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""