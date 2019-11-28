import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
        int main(){
            a--!b;
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    