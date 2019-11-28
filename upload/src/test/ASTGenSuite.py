import unittest
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