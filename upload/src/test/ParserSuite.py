import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """void main() {foo();}"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestParser.checkParser(input,expect,400))


    def test_diff_numofparam_stmt(self):
        input = """
        void main () {
            foo(a);
            putIntLn();
        }
        int foo(){}
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestParser.checkParser(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """void main () {
            putIntLn(getInt(4));
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestParser.checkParser(input,expect,402))
    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            CallExpr(Id("foo"),[])]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestParser.checkParser(input,expect,403))
    def test_undeclared(self):
        
        input ="""
                    void main(){
                        b;
                    }
                    int b;

        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestParser.checkParser(input,expect,404))
    def test_return(self):
        """Simple program: int main() {} """
        input ="""
                    string i;
                    void main(){
                        int i;
                        boolean b;
                        boolean a;
                        if(a&&b)
                            {   
                                
                                return b;{
                                    return a && b;
                                }
                            }
                        {
                        return a;                          
                        }
                    }
                

        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestParser.checkParser(input,expect,405))
    def test_hard_return(self):
        """Simple program: int main() {} """
        input ="""  
                    string a;
                  
                    void main(){   
                        int a;
                        int b;
                        float d;
                        boolean c;
                        for(b;c;b+1){
                            for(b;c;b+1){
                                {
                                    return d = a;
                                }
                            }
                        }     
                    }
                   
                    
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(=,Id(d),Id(a)))"
        self.assertTrue(TestParser.checkParser(input,expect,406))
    def test_simplereturn(self):
        """Simple program: int main() {} """
        input ="""  
                    
                  
                    void main(){   
                        int a;
                        int b;
                        boolean c;
                        return c;
                      }           
                                            
                    
                   
                    
        """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestParser.checkParser(input,expect,407))
    def test_complex_return(self):
        """Simple program: int main() {} """
        input ="""  
                    
                  
                    void main(){
                    int  a ;
                    boolean b;
                    do {
                        a = a*2;
                        return a;
                        {
                            {
                                return a;
                            }
                        }
                    }
                    while a < 10; 
                    return b;
                }
                                        
                    
                   
                    
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestParser.checkParser(input,expect,408))
    def test_return_binary(self):
        """Simple program: int main() {} """
        input ="""  
                    
                  
                    void main(){
                    float  a ;
                    int b;
                    do {
                       if(a==b){
                           return a / 1;
                       }
                    }
                    while a < 10; 
                    return b;
                }
                                        
                    
                   
                    
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestParser.checkParser(input,expect,409)) 
    def test_hard_returnBinary(self):
        """Simple program: int main() {} """
        input ="""  
                    
                  
                void main(int a,int b){
                    foo(a,b);
                    do {
                        if(a==b){
                           return a &&1;
                       }
                    }
                    while a < 10; 
                    return b;
                }
                int foo(int a,int b);{}             
                    
                   
                    
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(&&,Id(a),IntLiteral(1)))"
        self.assertTrue(TestParser.checkParser(input,expect,414))    
    def test_noentry(self):
        """Simple program: int main() {} """
        input =""" int main(int a,int b){
                    boolean c;
                    if(true){
                          continue;
                    }
                    
                    for(a;c;b){
                        return a;
                      
                    }
                    return a;
                    
                    }
                    
                   
                    
        """
        expect = "No entry point"
        self.assertTrue(TestParser.checkParser(input,expect,410))           
    def test_returnID(self):
        """Simple program: int main() {} """
        input =""" void main(int a,int b){
                    boolean c;
                    if(true){
                             
                    }
                    
                    for(a;c;b){
                        return a;
                   
                    }
                    break;
                    return a;
                    }
                   
                   
                    
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestParser.checkParser(input,expect,411))        
    def test_simpleReturnId(self):
        """Simple program: int main() {} """
        input ="""  void main(int a,int b){
                    boolean c;
                    return c ;
                    }
                   
                   
                    
        """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestParser.checkParser(input,expect,412))    
    def test_unreached(self):
        """Simple program: int main() {} """
        input ="""  void main(int a,int b){
                    foo(a);
                    
                    return ;
                    }
                    int foo(int a){
                        return a;
                    }
                    int foo2(int b){
                        return b;
                    }
                   
                   
                    
        """
        expect = "Unreachable function: foo2"
        self.assertTrue(TestParser.checkParser(input,expect,413))   
    def test_redeclared_ID(self):
        input ="""  void main(){
                     int i;
                     int a;
                     return;
                    }
                    int i;
                    int foo(){
                        return i;
                    }
                    int i;
                    
                   
                   
                    
        """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestParser.checkParser(input,expect,415))     
    def test_redeclared_ID__more_simple(self):
        input =""" 
        void main(){
            int i;
            int i
            return;
        }
        """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestParser.checkParser(input,expect,416))   
    def test_redeclared_ID__more_complex(self):
        input =""" 
        void main(){
            int i;
            int i;
            foo();
            return;
        }
        int i ;
        int foo(int i){
            int i; int i;
        }
        """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestParser.checkParser(input,expect,417))     
    def test_redeclared_function(self):
        input =""" 
        void main(){
            int i;
            foo();
            return;
        }
        int main(){
            int i;
        }
        
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestParser.checkParser(input,expect,418)) 
    def test_redeclared_function_more_simple(self):
        input =""" 
        void main(){
            int i;
            foo();
            return;
        }
        int foo(){}
        int main(){};
        
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestParser.checkParser(input,expect,419))     
    def test_redeclared_function_more_complex(self):
        input =""" 
        void main(){
            boolean a;
            do break;
            while a < 10;
        return a ;
        }
        int main(){};
        
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestParser.checkParser(input,expect,420))         
    def test_redeclared_function_more_simple(self):
        input =""" 
        int main(){
            int a;
            return a;
        }
        int main(){}
        
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestParser.checkParser(input,expect,421))   
    def test_redeclared_Para(self):
        input =""" 
        void main(int a,int a){
            int a;
            return;
        }
       
        
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestParser.checkParser(input,expect,422))       
    def test_redeclared_Para_and_ID(self):
        input =""" 
        void main(int a,int a){
            int a;
            return;
        }
       
        
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestParser.checkParser(input,expect,423))
    def test_redeclared_Para_more_simple(self):
        input =""" 
        void main(int a){
            return;
            foo(a,a);
        }
        int foo(int a,int a){}
       
        
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestParser.checkParser(input,expect,424)) 
    def test_Undecl_para(self):
        input =""" 
        void main(int a){
            return;
            foo(b,b);
        }
        int foo(int a,int a){}
       
        
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestParser.checkParser(input,expect,425)) 
    def test_Undecl_para_hard(self):
        input =""" 
        void main(int a){
            return;
            int b;
            foo(b,b);
            return;
        }
        int foo(int a,int b){
            return c;
        }
       
        
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestParser.checkParser(input,expect,426))                             
    def test_Undecl_para_complex1(self):
        input =""" 
        void main(int a){
            return;
            int b;
            foo(b,b);
            return;
        }
        int foo(int a,int b){
            return b + b;
            if(c) return b;
        }
       
        
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestParser.checkParser(input,expect,427))              
    def test_Undecl_para_simple(self):
        input =""" 
        void main(int a){
            return;
            b;
            return;
        }
        
       
        
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestParser.checkParser(input,expect,428))
    def test_Undecl_function(self):
        input =""" 
        void main(int a){
            return;
            foo();
            return;
        }
        
       
        
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestParser.checkParser(input,expect,429))  
    def test_Undecl_function_hard(self):
        input =""" 
        int a;
        void main(int b){
            putInt(a);
            return;
            k();
        } 
        void k(){
            putInt(b);
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestParser.checkParser(input,expect,430))                  
    def test__Call(self):
        input =""" 
        void main(int a){
            putInt(getInt());
            return;
        } 
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putInt),[CallExpr(Id(getInt),[])])"
        self.assertTrue(TestParser.checkParser(input,expect,431))     
    def test_Undecl_para_complex(self):
        input =""" 
        void main(int b){
            
            return;
            k(a);
        } 
        
        void k(int a){
            int b;
            putInt(b);
        }
      
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestParser.checkParser(input,expect,432))                
    def test_mismatch_in_stmt_if(self):
        input = """
        int[] foo(int i[]){int b[5]; return b;}
        void main(){
            int b[5];
            b[5] = 2;
            int a;
            foo(b);
            return;
        }"""
        expect = ""
        self.assertTrue(TestParser.checkParser(input, expect, 433))
    def test_Undecl_Para_sophiticated12(self):
        input =""" 
        void main(int b){
            {{{{
                a;
            }}}}
            return;
            k(a);
        } 
        
        void k(int a){
            int b;
            putInt(b);
        }
      
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestParser.checkParser(input,expect,434))      
    def test_Undecl_function_sophisticated1(self):
        input =""" 
        int a;
        void main(int b){
            putInt(a);
            return;
            k();
        } 
        void k(){
            int i;
            {{
                foo2();
            }}
            putInt(b);
        }
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestParser.checkParser(input,expect,435))    
    def test_complex_Undecl(self):
        input =""" 
        int a;
        void main(int b){
            putInt(a);
            foo2();
            return ;
            k();
        } 
        void k(){
            int i;
            putInt(b);
        }
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestParser.checkParser(input,expect,436))    
    def test_typeMISSMATCHIF(self):
        input =""" 
        int a;
        void main(int b){
            putInt(a);
            if(a+b){
                return;
            }
            else{
                return b;
            }
            return ;
            k();
        } 
        void k(int b){
            int i;
            putInt(b);
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),Id(b)),Block([Return()]),Block([Return(Id(b))]))"
        self.assertTrue(TestParser.checkParser(input,expect,437))   
    def test_typeMISSMATCHIF_complex(self):
        input =""" 
        int a;
        void main(int b){
            putInt(a);
            if(a!=b && a <= b && b >= a ){
                return;
            }
            else{
                return ;
            }
            return ;
            k(a);
        } 
        void k(int b){
            int i;
            putInt(b);
            return ;
        }
        """
        expect = ""
        self.assertTrue(TestParser.checkParser(input,expect,438)) 
    def test_typeMISSMATCHIF_hard(self):
        input =""" 
        int a;
        void main(int b){
            putInt(a);
            if(a!=b && a <= b && b >= a ){
                if(a==b){
                    a + b;
                  if (a +b){
                      return;
                  }
                }
            }
            else{
                return ;
            }

            return ;
            k(a);
        } 
        void k(int b){
            int i;
            putInt(b);
            return ;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),Id(b)),Block([Return()]))"
        self.assertTrue(TestParser.checkParser(input,expect,439))           
    def test_typeMISSMATCHIF_sophiticated(self):
        input =""" 
        int a;
        void main(int b){
            putInt(a);
            return ;
            k(a);
        } 
        void k(int b){
            if(a==b){
                if(a>b){
                    if(a>=b){
                        if(a *b)
                    }
                    else{
                        return;
                    }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(*,Id(a),Id(b)),None)"
        self.assertTrue(TestParser.checkParser(input,expect,440))  
    def test_typeMISSMATCHIF_HARD(self):
        input =""" 
        int a;
        void main(int b){
            putInt(a);
            return ;
            k(a);
        } 
        void k(int b){
            if(a==b){
                if(a/b){
                    if(a>=b){
                        a + b;
                    }
                    else{
                        return;
                    }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(/,Id(a),Id(b)),Block([If(BinaryOp(>=,Id(a),Id(b)),Block([BinaryOp(+,Id(a),Id(b))]),Block([Return()]))]))"
        self.assertTrue(TestParser.checkParser(input,expect,441))  
    def test_typeMISSMATCHFOR(self):
        input =""" 
        int a;
        void main(int b){
            for(a;a;b){
                return;
            }
        } 
       
        }
        """
        expect = "Type Mismatch In Statement: For(Id(a);Id(a);Id(b);Block([Return()]))"
        self.assertTrue(TestParser.checkParser(input,expect,442))  
    def test_typeMISSMATCHFORIF(self):
        input =""" 
        int a;
        void main(int b,boolean c){
            for(a;c;b){
                if(a == b){
                    for (a;c;c){
                        a + b
                    }
                }
            }
        } 
       
        
        """
        expect = "Type Mismatch In Statement: For(Id(a);Id(c);Id(c);Block([BinaryOp(+,Id(a),Id(b))]))"
        self.assertTrue(TestParser.checkParser(input,expect,443))      
    def test_typeMISSMATCHIFFOR(self):
        input =""" 
        int a;
        void main(int b,boolean c){
            if(a==b){
                if(a>b){
                    for (a;c;c){
                        return;
                    }
                }
                else{
                    return;
                }
            }
        } 
       
        
        """
        expect = "Type Mismatch In Statement: For(Id(a);Id(c);Id(c);Block([Return()]))"
        self.assertTrue(TestParser.checkParser(input,expect,444))    
    def test_typeMISSMATCHIFFOR_complex(self):
        input =""" 
        int a;
        void main(int b,boolean c){
            if(a==b){
                if(a>b){
                    for (a;c;b;){
                        for(a;c;c){}
                    }
                }
                else{
                    return;
                }
        }}
        
       
        
        """
        expect = "Type Mismatch In Statement: For(Id(a);Id(c);Id(c);Block([]))"
        self.assertTrue(TestParser.checkParser(input,expect,445))           