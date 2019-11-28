import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: void main() {} """
        input = """
        void main() {
            foo();
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """
        int a;
        /*float b(int a,float b){
            return b;
        }*/
        void main () {
            putIntLn(12e-1);
            //b(2,1.5);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[FloatLiteral(1.2)])"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_diff_numofparam_stmt_with_some_decl(self):
        """More complex program"""
        input = """
        int a;
        float c[2];
        float b(int a,float b){
            int mam;
            float coi;
            {
                int c;
                float d;
            }
        }
        void main () {
            //putIntLn();
        }"""
        expect = "Function b Not Return "
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """void main () {
            putIntLn(getInt(4));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_undeclared_function_use_ast(self):
        """Simple program: void main() {} """
        input = Program(
            [FuncDecl(Id("main"),[],IntType(),
            Block([
                CallExpr(Id("foo"),[])
            ]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([
                    CallExpr(Id("putIntLn"),[
                        CallExpr(Id("getInt"),[IntLiteral(4)])
                        ])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_diff_numofparam_stmt_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([
                    CallExpr(Id("putIntLn"),[])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_undeclared_function_with_some_decl_function(self):
        """Simple program: void main() {} """
        input = """
        float foo1(int a, float b, boolean c){
            return a;
        }
        void main() {
            foo();
            return;
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_var_reDecl(self):
        input = """
        int a;
        int b;
        int a;
        void main(){
            z;
            return;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_func_reDecl(self):
        input ="""
        int a(float b,boolean c){
            return b;
        }
        float a(boolean c,int d){
            return c;
        }
        void main(){

        }
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_var_and_func_reDecl(self):
        input = """
        int a;
        void main(){
            return;
        }
        int a(float a){
            return a;
        }
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_param_Redecl(self):
        input ="""
        float foo(int a,float a){
            return 0;
        }
        void main(){

        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_param_Redecl(self):
        input ="""
        float foo(int a,float a){
            return 0;
        }
        void main(){

        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redecl_param(self):
        input ="""
        float foo(int a,float b){

            int a;
            return 0;
        }
        void main(){

        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_redecl_block_in_blokc_stmt(self):
        input ="""
        int haha(float b,boolean c){
            boolean d;
            {
                string e;
                {
                    string e;
                    int e;
                }
                return 0;
            }
        }
        void main(){

        }
        """
        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclare_id(self):
        input ="""
        int foo;
        void main(){
            a;
            return;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_undeclare_call_exp(self):
        input ="""
        int foo;
        void main(){
            a();
            return;
        }
        """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclare_id_in_call_exp(self):
        input ="""
        int a(int b){
            return b;
        }
        void main(){
            a(b);
            return;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclare_if_statement_with_undeclare(self):
        input ="""
        boolean b;
        int a(int b){
            return b;
        }
        void main(){

            if (a) b;
            return;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclare_if_statement_with_not_boolean(self):
        input ="""
        float b;
        int a(int b){
            return b;
        }
        void main(){

            if (b) {
                int a;
            }
            return;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(b),Block([VarDecl(a,IntType)]))"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclare_if_statement_redeclare_in_ThenStmt(self):
        input ="""
        boolean b;
        int a(int b){
            return b;
        }
        void main(){

            if (b) {
                int a;
                float a;
            }
            return;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclare_if_statement_redeclare_in_elseStmt(self):
        input ="""
        boolean b;
        int a(int b){
            return b;
        }
        void main(){

            if (b) {
                int a;
                float c;
            }
            else{
                string foo;
                boolean foo;
            }
            return;
        }
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_mismatch_for_in_expr1_and_expr3(self):
        input ="""
        float a,b;
        boolean c;
        void main(){
            for (a;c;b){

            }
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(Id(a);Id(c);Id(b);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_mismatch_for_in_expr2(self):
        input ="""
        int a,b,c;
        void main(){
            for (a;b;c){

            }
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(Id(a);Id(b);Id(c);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_unandredeclare_in_loop(self):
        input ="""
        int a,c;
        boolean b;
        void main(){
            for (a;b;c){
                int d;
                c();
            }
            return;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(c),[])"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_mismatch_do_with(self):
        input ="""
        int b;
        void main(){
            do {

            }while(b);
            return;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(b))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_unandredeclare_in_dowhile(self):
        input ="""
        boolean b;
        void main(){
            do {
                int b;
                int a;
                float a;
            }while(b);
            return;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_if_with_local_varDecl(self):
        input ="""
        boolean test;
        void main(){
            {
                {
                    {
                        int test;
                        int c[5];
                        if (test) return;
                    }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(Id(test),Return())"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_return_primate_type_in_voidTypeFunction(self):
        input ="""
        int test;
        void main(boolean test){
            {
                int a;
                float b;
                if (test) return b;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_return_in_boolTypeFunction_(self):
        input ="""
        int a[5];
        boolean test;
        int[] foo(int b){
            return b;
        }
        void main(){
            {
                int a;
                float b;
                if (test) return;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_redecl_block_stmt(self):
        input ="""
        int haha(float b,boolean c){
            boolean d;
            {
                string b;
            }
        }
        void main(){

        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_arrayCell(self):
        input ="""
        void main(){
            boolean b[3];
            if (b[0]) {
                a;
            }
            else {
                return;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_assignment(self):
        input ="""
        int[] foo(){
            int a[2];
            return a;
        }
        void main(){
            int a,b;
            boolean c;
            foo[a];
        }
        """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_funcall(self):
        input ="""
        int foo(){
            return 0;
        }
        void main(){
            foo();
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_if_stmlt_multi_exp(self):
        input ="""
        void main(){
            int a,b;
            if (a != b && a == b && b){
               return;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,BinaryOp(&&,BinaryOp(!=,Id(a),Id(b)),BinaryOp(==,Id(a),Id(b))),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_for_in_if_with_local_decl(self):
        input ="""
        void main(){
            float a,b;
            if (a > b || a == b){
                for(a; a < 10;a = a +1){
                    float foo;
                }
            }else{
                getInt();
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_do_while_stmt_with_wrong_return(self):
        input ="""
        int test(int ba[]){
            do{
                return ba;
            }while ba[2] == 2;
        }
        void main(){
            int a[3];
            test(a);
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(ba))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_if_manybinop_wronginUnaryOp(self):
        input ="""
        void main(){
            int a,b;
            if (a == b || -a < b && !a) a;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_multi_if_stml(self):
        input ="""
        void main(){
            int a,b;
            boolean c;
            if (a == b){
                if ( a  > b){
                    if (a < b ){
                        if (a != b ){
                            if (-a >= b){
                                if (a <= -b){
                                    if ( a + b  > 0){
                                        if (a - b < 0){
                                            if (!c)
                                                 return c;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

        }
        """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_multi_if_stml_2(self):
        input ="""
        void main(){
            int a,b;
            boolean c;
            if (a == b){
                if ( a  > b){
                    if (a < b ){
                        if (a != b ){
                            if (-a >= b){
                                if (a <= -b){
                                    if ( a + b  > 0){
                                        if (a - b < 0){
                                            if (!c)
                                                 return;
                                        }else{
                                            float d;
                                        }
                                    }else{
                                        string e;
                                    }
                                }else{
                                    boolean d;
                                }
                            }else{
                                int e;
                            }
                        }else{
                            float a,b;
                        }
                    }else{
                        boolean a,b,c,d,e;
                    }
                }else{
                    string f;
                }
            }else{
                if (f){
                    return;
                }
            }
        }
        """
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_scope_when_return(self):
        input ="""
        int foo(int b,int a){
            int f;
            if (a  < b ){
                boolean f;
                if (f){
                    return 2;
                }
            }else {
                return f;
            }
        }
        void main(){
            int a,b;
            foo(a,b);
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_multi_block_stmt(self):
        input ="""
        void main(){
            int a,b;
            {
                float a,b;
                {
                    boolean a,b;
                    {
                        if (a && b)
                            return a;
                    }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_local_var(self):
        input ="""
        void main(){
            boolean a;
            if (a){
                int b,c;
            }
            else{
                if (b > c)
                    return;
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_coerce_in_callExpr(self):
        input ="""
        int foo(float c){
            int b;
            return b;
        }
        void main(){
            boolean a;
            if (a){
                int c;
                foo(c);
            }
            else{
                float d;
                foo(d);
                return 0;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_multi_callExpr(self):
        input ="""
        int foo(boolean c){
            if (c) return 0;
            else return 1;
        }
        void main(){
            int a;
            boolean d;
            if (foo(d) > a){
                putFloatLn(getInt());
                return 1;
            }

        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_callExpr_in_condition_exp(self):
        input ="""
        float foo(int a,float b,boolean c){
            if (a > b || c){
                return 12E-1;
            }
            else {
                if (!c) return 0;
                else return 1;
            }
        }
        void main(){
            int a,b;
            boolean c;
            if (foo(a,b,c) == a) return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,CallExpr(Id(foo),[Id(a),Id(b),Id(c)]),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_NoEntryPoint(self):
        input ="""
        int test(float a,string b[]){
            return 0;
        }
        void foo(){

        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_UnReachableFunction_with_many_function(self):
        input ="""
        int[] a(){
            int a[3],b[2];
            if (a[2] > a[3] || test(a[0],a[1]) || b[0] > foo())
                return a;
            else return b;
        }
        float foo(){
            return 12e-12;
        }

        boolean test(int a,int b){
            return true;
        }
        void main(){
        }
        """
        expect = "Unreachable Function: a"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_UnReachableFunction_with_logicFunction(self):
        input ="""
        int[] a(boolean iu, boolean lov){
            int a[3],b[2];
            if (a[2] > a[3] || test(a[0],a[1]) ||  foo(b[0],b[2])){
                if (iu == lov)
                    return a;
                else
                    return b;
            }
            else {
                if (foo(a[0],a[1]) || test(b[0],b[1]) || foo(a[1],a[2]))
                    return a;
                else {
                    int c[10];
                    c[0] = 5;
                    return c;
                }

            }
        }
        boolean foo(int a, float b){
            if (a  > b)
                return true;
            else
                return false;
        }

        boolean test(int a,int b){
            if (a != b || -a == b || a + b != 0)
                return false;
            else
                return true;
        }
        void main(){
        }
        """
        expect = "Unreachable Function: a"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_reDecl_param_in_function(self):
        input ="""
        int b;
        int foo(float b, int c){
            if (b > c)
                return c;
            else
                return 0;
        }

        float fail(int wr,boolean wr[]){

        }
        void main(){
            boolean wr[3];
            foo(2.3,5);
            fail(2,wr);
        }
        """
        expect = "Redeclared Parameter: wr"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_reDecl_varialbe_with_paraDecl(self):
        input ="""
        int[] iloveU(boolean iu, boolean lov){
            int a[3],b[2];
            if (a[2] > a[3] || IDo(a[0],a[1]) ||  IDo(b[0],b[2])){
                if (iu == lov)
                    return a;
                else
                    return b;
            }
            else {
                if (IDo(a[0],a[1]) || IRealyDo(b[0],b[1]) || IDo(a[1],a[2]))
                    return a;
                else {
                    int c[10];
                    c[0] = 5;
                    return c;
                }

            }
            int iu;
        }
        boolean IDo(int a, float b){
            if (a  > b)
                return true;
            else
                return false;
        }

        boolean IRealyDo(int a,int b){
            if (a != b || -a == b || a + b != 0)
                return false;
            else
                return true;
        }
        void main(){
            iloveU(true,true);
        }
        """
        expect = "Redeclared Variable: iu"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_WrongReturnType_in_boolFunction(self):
        input ="""
        boolean ilovU(string i,boolean lov, string u){
            boolean tuesday;
            tuesday = false;

            string anhiuem;
            anhiuem= "";
            string iiuu;
            iiuu = "justkidding";
            if (yes(lov) == 1 && no(tuesday) == 1)
                return anhiuem;
            else
                return lov;
        }
        int yes(boolean ans){
            if (ans)
                return 1;
            else
                return 1;
        }
        int no (boolean ans){
            if (ans)
                return 1;
            else
                return 1;
        }
        void main(){
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(anhiuem))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_wrongCondition_in_Ifstmlt(self):
        input ="""
        boolean checker(int a, int b){
            int term;
            if (a > b){
                int c;
                c = 10;
                if (a < c){
                    float d;
                    d = 12e-12;
                    if (a + d  == c)
                        return true;
                    else
                        return false;
                }else
                    return false;
            }else
                return false;
        }
        void main(){
            int a,b;
            a = 10;
            b = 20;
            checker(a,b);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,BinaryOp(+,Id(a),Id(d)),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_wrongExpr_inForStmts(self):
        input ="""
        boolean test(int e,int f){
            int a,b;
            a = e;
            b = f;
            for(a;a<10;a = a + b){
                int a,b,c;
                for(a;a<c;a = a + b){
                    int a,c;
                    float b;
                    for(a;a<c;a = a + b){
                        return true;
                    }
                }
            }
            return false;
        }

        void main(){
            test(10,100);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_wrongCondition_in_DoWhileStmts_(self):
        input ="""
        int main(int arg){
            do
            {
                int b;
                float c;
                do{
                    int b;
                    float c;
                    do{
                        if (b > c)
                            return 0;
                        else return 1;
                    }while(b/c != 0);
                }while(b/c >= 0);
            }while (arg == 1);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,BinaryOp(/,Id(b),Id(c)),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_return_wrong_inVoidType_insofar(self):
        input ="""
        void main(){
            int a,b,c;
            for (a;a<b;c){
                if (a == c){
                    do{
                        {
                            {
                                float a;
                                return a;
                            }
                        }
                    }while(a + b != c);
                }else {
                    {
                        return;
                    }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_return_type_notmatch(self):
        input ="""
        boolean main(int arg, float x){
            if (x+arg < 12.0e-12){
                boolean k;
                for (arg; x < arg;arg = arg - 1){
                    do{
                        int k;
                        k = 1;
                        return k;
                    }while (k);
                }
            }else{
                return false;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(k))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_return_coerce(self):
        input ="""
        float main(int fe, boolean c){
            c = true;
            if (c){
                for (fe;c;fe = fe+1){
                    if (fe > 10){
                        c = false;
                        return fe;
                    }
                    else{
                        boolean k;
                        k = false;
                        return k;
                    }
                }
            }else{
                return fe;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(k))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_return_unDeclare(self):
        input ="""
        string main(int a,float b[]){
            if (a < b[1]){
                for (a;a < b[2]; a = a +1){
                    do{
                        return test;
                    }while (b[3] > 0);
                }
            }else{
                string k;
                k = "phu dep trai";
                return k;
            }

        }
        """
        expect = "Undeclared Identifier: test"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_return_arrayPointer_fail(self):
        input ="""
        string[] foo(int a,string b[]){
            //b = "Phu Yeu PPL";
            if (a < 10){
                if (a > 5){
                    if (a < 7){
                        return b;
                    }else{
                        int b[3];
                        return b;
                    }
                }
            }
        }
        void main(){
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_binop_asssign(self):
        input ="""
        void main(int b){
            string c;
            c = b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_ContinueNotinForStmts(self):
        input ="""
        void main(int test,float fe){
            if (test == 0) {
                int a,b,c;
                for (a;a<b;c=c+1){
                    if (fe > a)
                        continue;
                    else
                        return;
                }
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_ContinueNotinDoWhileStmts(self):
        input ="""
        void main(int a,float b,boolean c){
            do {
                do{
                    if (c){
                        do{
                            continue;
                            return;
                        }while(a+b > 0);
                    }else{
                        return;
                    }
                    continue;
                }while(-a != 10);
                continue;
            }while (b - 10 < 10);
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_break_NotIn_ForSTtms(self):
        input ="""
        boolean main(string str,int index,int a[]){
            boolean bool;
            bool = false;
            if (!bool){
                for(index;index < a[index];index=index + 1){
                    int b,bool;
                    boolean c;
                    for (b;c;bool + 1){
                        break;
                    }
                    if (!c) return c;
                    break;
                }
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_Break_notIn_DoWhileStmts(self):
        input ="""
        float main(string str, int arg, boolean bool, float fl){
            do {
                if (arg + 1 < fl){
                    do{
                        break;
                    }while(bool || fl - 10 > 0);
                    return fl;
                }else{
                    do{
                        break;
                    }while(arg<10);
                }
                break;
            }while(!bool);
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_Block_withReDecl_Var(self):
        input ="""
        void main(){
            int a;
            {
                int a;
                {
                    int a;
                    {
                        int a;
                        {
                            int a;
                            if (a < 10){
                                for (a; a < 10 ; a = a + 1){
                                    do{
                                        continue;
                                        return;
                                    }while(a != 0);
                                }
                            }else{
                                do{
                                    break;
                                    return;
                                }while(-a!=0);
                            }
                            int a;
                        }
                    }
                }
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_AssignOp_iswrongType(self):
        input ="""
        int[] a(int arg){
            int arr[4],b[2];
            if (arg > 10)
                return arr;
            else
                return b;
        }
        void main(string str){
            boolean bool;
            bool = true;
            if (bool){
                a(10) = str;
            }
        }
        """
        expect = "Not Left Value: CallExpr(Id(a),[IntLiteral(10)])"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_AssignOp_Nothave_ValueLeft(self):
        input ="""
        boolean StaticChecker(){
            boolean bool;
            if (bool)
                return true;
            else{
                if (!bool)
                    return false;
            }
        }
        void main(){
                int i ;
                int main ;
                StaticChecker() = main;

        }
        """
        expect = "Not Left Value: CallExpr(Id(StaticChecker),[])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_Another_NotValueLeft(self):
        input ="""
        void main(){
            int a[3],b,value;
            value = 5;
            putInt(getInt()) = value;
        }
        """
        expect = "Not Left Value: CallExpr(Id(putInt),[CallExpr(Id(getInt),[])])"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_AssignOp_notMatchType(self):
        input ="""
        void main(){
            string str;
            boolean c;
            str = c;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(str),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_AssignOp_IntTypeLHS_notMatchRHS(self):
        input ="""
        void main(){
            int a;
            float b;
            if (a = b) {
                return;
            }else{
                a  = 2;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_AssignOp_notCoerce(self):
        input ="""
        float foo1(int foo, float fl){
            if (foo > fl){
                string str;
                fl = str;
            }else{
                fl = foo;
            }
            return fl;
        }
        void main(int a,float b){
            foo1(a,b);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(fl),Id(str))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_CoerceOp_NotMatchType(self):
        input ="""
        int foo(int a,boolean c){
            if (a + 10 == 0){
                if (a /c  >= 5)
                    return 0;
                else return a;
            }else {
                return a;
            }
        }
        void main(int a,boolean c){
            foo(a,c);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_another_coerceOp_wrongType(self):
        input ="""
        int foo(float a,string c){
            if (a * c == 0)
                return 1;
            else return 0;
        }
        void main(float a,string c){
            foo(a,c);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_equalOp_NotMatchType(self):
        input ="""
        void main(int a,boolean bool,float fl){
            if (a == fl)
                return;
            else{
                //do no thing
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(fl))"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_equanlOp_MatchType_butLHS_isNot_RHS(self):
        input ="""
        int main(int a,boolean bool){
            if (a != bool)
                return a;
            else{
                return 0;
            }
            return 1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(a),Id(bool))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_return_fail_with_hardcode(self):
        input ="""
        string i;
        void main(){
            int i;
            boolean b;
            boolean a;
            if(a&&b)
                {

                    return c;
                    {
                        return a && b;
                    }
                }
            {
            return a;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_reDecl_withCompl_Program(self):
        input ="""
        int z;
        void main(){
            doo();
            return;
        }
        int z;
        float doo(){
            float b;
            b = 4.0;
            if(b<5){

            }
            else{
                int a; boolean b;
                float c;
                for(a;b;a){
                    return c;
                }
            }
            return b ;
        }
        """
        expect = "Redeclared Variable: z"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_equalOp_isNotIntType(self):
        input ="""
        void main(int a){
            float b;
            if (true)
                foo(a,b);
        }
        int foo(int a,float b){
            return (a % b);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_logicOp_isNotBoolType(self):
        input ="""
        void main(boolean a){
            string c;
            if (true)
                LovChecker(a,c);
        }
        boolean LovChecker(boolean a,string b){
            if (a || b)
                return true;
            else return false;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_logicOp_mutilCheck(self):
        input ="""
        void main(){
          Checker();
        }
        boolean Checker(){
            if (true || false && true == false){
                int a,b;
                float c,d;
                string e;
                boolean f;
                if (a < b || c >= d || e)
                    return f;
            }else
                return true;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,BinaryOp(||,BinaryOp(<,Id(a),Id(b)),BinaryOp(>=,Id(c),Id(d))),Id(e))"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_UnaryOp_NotMatch_Type(self):
        input = """
        void main(){
             checkUnary();
        }
        float checkUnary(){
            int a,b;
            float c,d;
            string e,f;
            boolean g,h;
            if (!g || -a+c-d*b < 0 && h){
                for (a;h;b){
                    if (!e)
                        return c;
                    else
                        return d;
                }
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(e))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_Multi_UnaryOp(self):
        input = """
        void main(){
            CheckMultiUnaryOp();
        }
        string CheckMultiUnaryOp(){
            float fl,fh;
            int index,_t;
            boolean bool,ean;
            string str,ing;
            ing = "thay Phung dep trai vo dich vu tru";
            if (-fl < -fh || -index + fl * (fh / _t) && str = ing)
                return ing;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,BinaryOp(+,UnaryOp(-,Id(index)),BinaryOp(*,Id(fl),BinaryOp(/,Id(fh),Id(_t)))),Id(str))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_ArrayCell_Index_isnotIntType(self):
        input = """
        void main(int a[]){
            float x;
            if (a[10] == 10)
                a[x];
            else 
                return;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_ArrayCell_Arr_isNotMatchType(self):
        input = """
        void main(float a[]){
            float b[5];
            checker(b);
        }
        float[] checker(float a[]){
            int index;
            float fl[10];
            if (true){
                int fl;
                fl[index] = 0;
            }
            return a;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(fl),Id(index))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_CallExpr_UnDeclThatFunc(self):
        input = """
        void main(){
            foo(2);
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_CallExpr_UndeclThatFunc_ButDeclthatName(self):
        input = """
        int test;
        void main(){
            int a,b;
            float c,d;
            string e,f;
            boolean k,h;
            test(10);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(test),[IntLiteral(10)])"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_CallExpr_ButwrongParamSize(self):
        input = """
        void main(){
            int index,t;
            float e,d;
            string str,ing;
            boolean bool,ena;
            foo(t,e);
        }

        int foo(int a,float b,string c,boolean d){
            return 1;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(t),Id(e)])"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_CallExpr_samelenParam_but_notMatchLHStoRHS(self):
        input = """
        void main(){
            string e;
            int f;
            checker(e,f);
        }
        float checker(string e,int f[]){
            return 12e12;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(checker),[Id(e),Id(f)])"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_CallExpr_samelenParam_but_coerce_failwithIntType(self):
        input = """
        void main(){
            boolean bool;
            int t;
            checker(t,bool);
        }
        int checker(int a,int b){
            return 1;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(checker),[Id(t),Id(bool)])"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_CallExpr_samelenParam_but_coerce_failwithFloatType(self):
        input = """
        void main(){
            int a,b;
            float e,f;
            string g,h;
            checker(a,b);
            coere(e,g);
        }
        int checker(float a,float b){
            return 1;
        }
        int coere(float c,float d){
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(coere),[Id(e),Id(g)])"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_IdUndecleare(self):
        input = """
        int test;
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
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_complexprogram_withUndeclFunction(self):
        input = """
        int main()
        {
            int n, i, flag;
            flag = 0;
            printf("Enter a positive integer: ");
            scanf("%d", n);
            for(i = 2; i <= n/2; i=i+1)
            {
                // condition for i to be a prime number
                if (checkPrime(i) == 1)
                {
                    // condition for n-i to be a prime number
                    if (checkPrime(n-i) == 1)
                    {
                        // n = primeNumber1 + primeNumber2
                        printf("%d = %d + %d\\n", n, i, n - i);
                        flag = 1;
                    }
                }
            }
            if (flag == 0)
                printf("%d cannot be expressed as the sum of two prime numbers.", n);
            return 0;
        }
        """
        expect = "Undeclared Function: printf"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_anotherveryComplexprogram_withwrong_EqualOp(self):
        input = """
        int main()
        {
            string line[30];
            int i, vowels, consonants, digits, spaces;
            vowels =  consonants = digits = spaces = 0;
            for(i=0; line[i]!=""; i=i+1)
            {
                if(line[i]=="a" || line[i]=="e" || line[i]=="i" ||
                line[i]=="o" || line[i]=="u" || line[i]=="A" ||
                line[i]=="E" || line[i]=="I" || line[i]=="O" ||
                line[i]=="U")
                {
                    vowels=vowels+1;
                }
                else if((line[i]>="a"&& line[i]<="z") || (line[i]>="A"&& line[i]<="Z"))
                {
                    consonants=consonants + 1;
                }
                else if(line[i]>="0" && line[i]<="9")
                {
                    digits=digits+1;
                }
                else if (line[i]==" ")
                {
                    spaces=spaces+1;
                }
            }
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,ArrayCell(Id(line),Id(i)),StringLiteral())"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_function_Nothave_EntryPoint(self):
        input = """
        int checkPrime(int n)
        {
            int i, isPrime;
            isPrime=1;
            for(i = 2; i <= n/2; i=i+1)
            {
                if(n % i == 0)
                {
                    isPrime = 0;
                    break;
                }  
            }
            return isPrime;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_complexProgram_wrongReturn(self):
        input = """
        int main()
        {
            int low, high, i, flag;
          do
            {
                flag = 0;
                for(i = 2; i <= low/2; i=i+1)
                {
                    if((low % i) == 0)
                    {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0)
                low= low + 1;
            }while (low < high);
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_ModOp(self):
        input = """
        void main(){
            int a,b;
            if (a % b == 0)
                return true;
        }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_UnDeclFunction_insilde_CallExpr(self):
        input = """
        int convertBinarytoOctal(int binaryNumber)
        {
            int octalNumber, decimailNumber, i;
            octalNumber = 0;decimailNumber = 0;i = 0;
            do
            {
                decimailNumber = decimailNumber+(binaryNumber%10)*pow(2,i);
                i=i+1;
                binaryNumber= binaryNumber/10;
            }while(binaryNumber != 0);
            i = 1;
            do
            {
                octalNumber = octalNumber + (decimailNumber % 8) * i;
                decimailNumber = decimailNumber/ 8;
                i = i* 10;
            }while(decimailNumber != 0);
            return octalNumber;
        }
        int main()
        {
            int binaryNumber;
            convertBinarytoOctal(binaryNumber);
            return 0;
        }
        """
        expect = "Undeclared Function: pow"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_ReDeclFunction_inVoidType(self):
        input = """
    void reverseSentence(){

    }
    int main()
    {
        reverseSentence();
        return 0;
    }
    void reverseSentence()
    {
        string c;
        if( c != "")
        {
            reverseSentence();
        }
    }
        """
        expect = "Redeclared Function: reverseSentence"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_UnDecl_hardVariable_inside_function(self):
        input = """
    float calculateSD(float data[])
    {
        float sum , mean, standardDeviation;
        int i;
        for(i=0; i<10; i=i+1)
        {
            sum = sum + data[i];
        }
        mean = sum/10;
        for(i=0; i<10; i= i + 1)
            standardDeviation = standardDiviation + pow(data[i] - mean, 2);
        return sqrt(standardDeviation/10);
    }
    int main()
    {
        int i;
        float data[10];
        
        calculateSD(data);
        return 0;
    }
        """
        expect = "Undeclared Identifier: standardDiviation"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_simple_program(self):
        input = """
        void main(){
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input, expect, 499))
