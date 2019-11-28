import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("aA?sVN","aA,Error Token ?",103))       
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123a23","123,a23,<EOF>",104))
    def test_float_point(self) :    
        self.assertTrue(TestLexer.checkLexeme("1.2e02","1.2e02,<EOF>",105))
    def test_float_point1(self) :   
        self.assertTrue(TestLexer.checkLexeme("1.","1.,<EOF>",106))
    def test_variable_decl_1(self):
        self.assertTrue(TestLexer.checkLexeme("""_="this is a string" ""","_,=,this is a string,<EOF>",41))  
    def test_float_point3(self) :       
        self.assertTrue(TestLexer.checkLexeme("2e02","2e02,<EOF>",108))
    def test_float_point4(self) :       
        self.assertTrue(TestLexer.checkLexeme("1e3.202","1e3,.202,<EOF>",109))
    def test_float_point5(self) :       
        self.assertTrue(TestLexer.checkLexeme("13.e22","13.e22,<EOF>",110))
    def test_id(self):
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",111))
    def test_string(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""",112))
    def test_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","""123,Illegal Escape In String: 123a\\m""",113))
    def test_double_slash(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\\\123" ""","""123,123a\\\\123,<EOF>""",114))
    def test_unclose_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123 ""","""Unclosed String: 123a\\n123 """,115))
    def test_upper_id2(self):
        self.assertTrue(TestLexer.checkLexeme("AB","AB,<EOF>",116))
    def test_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("ABVC$","ABVC,Error Token $",117))
    def test_dash_id(self):
        self.assertTrue(TestLexer.checkLexeme("_abc$","_abc,Error Token $",118))
    def test_dash_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("_ABC","_ABC,<EOF>",119))
    def test_dash_upper_lower_id(self):
        self.assertTrue(TestLexer.checkLexeme("_aBbcDE","_aBbcDE,<EOF>",120))
    def test_dash_many_id(self):
        self.assertTrue(TestLexer.checkLexeme("abc ade ABR","abc,ade,ABR,<EOF>",121)) 
    def test_dash_many_id2(self):
        self.assertTrue(TestLexer.checkLexeme("abc_ ade ABR","abc_,ade,ABR,<EOF>",122))
    def test_dash_many_id3(self):
        self.assertTrue(TestLexer.checkLexeme("abc/ AND","abc,/,AND,<EOF>",123))
    def test_dash_many_id4(self):
        self.assertTrue(TestLexer.checkLexeme("tranhung123 123 ","tranhung123,123,<EOF>",124)) 
    def test_dash_many_id5(self):
        self.assertTrue(TestLexer.checkLexeme("_acf45asd","_acf45asd,<EOF>",125))  
    def test_dash_many_id6(self):
        self.assertTrue(TestLexer.checkLexeme("_457:","_457,Error Token :",126))  
    def test_dash_many_id6(self):
        self.assertTrue(TestLexer.checkLexeme("_457:","_457,Error Token :",126))      
    def test_dash_many_id7(self):
        self.assertTrue(TestLexer.checkLexeme("_0410ABCD Lan_Vy:","_0410ABCD,Lan_Vy,Error Token :",127))
    def test_id_int(self):
        self.assertTrue(TestLexer.checkLexeme("a123_ 123_123a","a123_,123,_123a,<EOF>",133))      
    def test_int(self):
        self.assertTrue(TestLexer.checkLexeme("123","123,<EOF>",128))
    def test_int2(self):
        self.assertTrue(TestLexer.checkLexeme("123?","123,Error Token ?",129))  
    def test_int_id(self):
        self.assertTrue(TestLexer.checkLexeme("123 456a589 90","123,456,a589,90,<EOF>",130))  
    def test_int_id1(self):
        self.assertTrue(TestLexer.checkLexeme("890_bde _123 123asd","890,_bde,_123,123,asd,<EOF>",131))
    def test_int_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("123Ab_c","123,Ab_c,<EOF>",132))
    def test_int_upper_id2(self):
        self.assertTrue(TestLexer.checkLexeme("ABc123_ 123ABC123","ABc123_,123,ABC123,<EOF>",134))
    def test_all_1(self):
        self.assertTrue(TestLexer.checkLexeme("int main(){if(x>3) printf(\"Tran Manh Hung\");}","int,main,(,),{,if,(,x,>,3,),printf,(,Tran Manh Hung,),;,},<EOF>",135))
    def test_all_2(self):
        self.assertTrue(TestLexer.checkLexeme("int main(){int x = 0 ; for(int i =0 ; i<10;i++){x=x+i;}}","int,main,(,),{,int,x,=,0,;,for,(,int,i,=,0,;,i,<,10,;,i,+,+,),{,x,=,x,+,i,;,},},<EOF>",136))
    def test_all_3(self):
        self.assertTrue(TestLexer.checkLexeme("int main(){do foo(x,y=x*x); while x<=10;}","int,main,(,),{,do,foo,(,x,,,y,=,x,*,x,),;,while,x,<=,10,;,},<EOF>",137))
    def test_all_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" string str="This is stirng ""","string,str,=,Unclosed String: This is stirng ",138))   
    def test_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("+-*/*-/-*+++++6123++++","+,-,*,/,*,-,/,-,*,+,+,+,+,+,6123,+,+,+,+,<EOF>",139))   
    def test_operator_1(self):
        self.assertTrue(TestLexer.checkLexeme("+*95+*/6+**+%%6123","+,*,95,+,*,/,6,+,*,*,+,%,%,6123,<EOF>",140))    
    def test_operator(self):
        self.assertTrue(TestLexer.checkLexeme("+-*/*-/-*4123","+,-,*,/,*,-,/,-,*,4123,<EOF>",141))   
    def test_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("exp[2]+3+4+5+980%4%4//123","exp,[,2,],+,3,+,4,+,5,+,980,%,4,%,4,<EOF>",142))
    def test_variable_decl_5(self):
        self.assertTrue(TestLexer.checkLexeme("int a = 9; int b = 10 ; a + b = 19;","int,a,=,9,;,int,b,=,10,;,a,+,b,=,19,;,<EOF>",143))
    def test_exp(self):
        self.assertTrue(TestLexer.checkLexeme("a=b+10;","a,=,b,+,10,;,<EOF>",144))                     
    def test_exp1(self):
        self.assertTrue(TestLexer.checkLexeme("a = b *b ; b = b*2 ;","a,=,b,*,b,;,b,=,b,*,2,;,<EOF>",145)) 
    def test_exp2(self):
        self.assertTrue(TestLexer.checkLexeme("a[] = 7/2 +1 ","a,[,],=,7,/,2,+,1,<EOF>",146)) 
    def test_exp3(self):
        self.assertTrue(TestLexer.checkLexeme("int id = 110 ; id = id *2 ","int,id,=,110,;,id,=,id,*,2,<EOF>",147))     
    def test_all_5(self):
        self.assertTrue(TestLexer.checkLexeme("void main() {int a;int b; a+b=10} ","void,main,(,),{,int,a,;,int,b,;,a,+,b,=,10,},<EOF>",148))     
    def test_all_6(self):
        self.assertTrue(TestLexer.checkLexeme("int main() {} ","int,main,(,),{,},<EOF>",149))
    def test_all_7(self):
        self.assertTrue(TestLexer.checkLexeme("void main() {} ","void,main,(,),{,},<EOF>",150))      
    def test_float_point6(self):    
        self.assertTrue(TestLexer.checkLexeme("1.2E-2","1.2E-2,<EOF>",151))
    def test_float_point7(self):    
        self.assertTrue(TestLexer.checkLexeme("1.E-2","1.E-2,<EOF>",152))    
    def test_float_point8(self):    
        self.assertTrue(TestLexer.checkLexeme(".341",".341,<EOF>",153))
    def test_float_point9(self):    
        self.assertTrue(TestLexer.checkLexeme(".1E2",".1E2,<EOF>",154))        
    def test_float_point10(self):    
        self.assertTrue(TestLexer.checkLexeme("1.","1.,<EOF>",155))
    def test_float_point11(self):    
        self.assertTrue(TestLexer.checkLexeme("1.2E+2","1.2,E,+,2,<EOF>",156))    
    def test_float_point12(self):    
        self.assertTrue(TestLexer.checkLexeme("1.+2","1.,+,2,<EOF>",157))
    def test_float_point13(self):    
        self.assertTrue(TestLexer.checkLexeme("123.e.6e3.789.234e-2E","123.,e,.6e3,.789,.234e-2,E,<EOF>",158))
    def test_float_point14(self):    
        self.assertTrue(TestLexer.checkLexeme("e123.abv123E2.1234","e123,Error Token .",159))
    def test_float_point15(self):    
        self.assertTrue(TestLexer.checkLexeme("e123E.1.123","e123E,.1,.123,<EOF>",160))    
    def test_float_point16(self):    
        self.assertTrue(TestLexer.checkLexeme("abcd.2","abcd,.2,<EOF>",161))
    def test_float_point17(self):    
        self.assertTrue(TestLexer.checkLexeme("123.e2.E.3.2","123.e2,Error Token .",162))
    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "tran hung" ""","""tran hung,<EOF>""",163))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "tran\nhung" ""","""Unclosed String: tran""",164)) 
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "tran\thung" ""","""Unclosed String: tran""",165))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "tran\bhung" ""","""Unclosed String: tran""",166))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "tran\\hung" ""","""Illegal Escape In String: tran\\h""",167))          
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "tran\rhung" ""","""Unclosed String: tran""",168))     
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "tran\fhung" ""","""Unclosed String: tran""",169))
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\\t12345" "tranhung" ""","""abcd\\t12345,tranhung,<EOF>""",170))        
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\\t12345" "tranhung\\tHung" ""","""abcd\\t12345,tranhung\\tHung,<EOF>""",171))     
    def test_string10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\\t12345" "tranhung\tHung" ""","""abcd\\t12345,Unclosed String: tranhung""",172))
    def test_string11(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\\t12345" "Tran Manh Hung" ""","""abcd\\t12345,Tran Manh Hung,<EOF>""",173))
    def test_string12(self):
        self.assertTrue(TestLexer.checkLexeme(""" _abcd "abcd\\t12345" "tranhung\\tHung" ""","""_abcd,abcd\\t12345,tranhung\\tHung,<EOF>""",174))
    def test_string13(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123abcde"abcd\\t12345" "tranhung\\tHung" ""","""123,abcde,abcd\\t12345,tranhung\\tHung,<EOF>""",175))
    def test_string14(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1.2e-3.2E4"abcd\\b12345" "tranhung\\bHung" ""","""1.2e-3,.2E4,abcd\\b12345,tranhung\\bHung,<EOF>""",176))
    def test_string15(self):
        self.assertTrue(TestLexer.checkLexeme(""" "%$%^&" ""","""%$%^&,<EOF>""",177))
    def test_string16(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Tran Hung 12u%^$#" ""","""Tran Hung 12u%^$#,<EOF>""",178))
    def test_string17(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123"" ""","""123,,<EOF>""",179))
    def test_string18(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """,""",<EOF>""",180)) 
    def test_string19(self):
        self.assertTrue(TestLexer.checkLexeme(""" abcd"" ""","""abcd,,<EOF>""",181))     
    def test_string20(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1234.E2abcd"" ""","""1234.E2,abcd,,<EOF>""",182))
    def test_string21(self):
        self.assertTrue(TestLexer.checkLexeme(""" abcd"tran\\mHUng" ""","""abcd,Illegal Escape In String: tran\\m""",183))       
    def test_string22(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Tran\\tHung" "Tran\\tHung" ""","""Tran\\tHung,Tran\\tHung,<EOF>""",184)) 
    def test_string23(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "Tran\\tHung  ""","""123,Unclosed String: Tran\\tHung  """,185))                         
    def test_string24(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "1e.245"  ""","""123,1e.245,<EOF>""",186))                         
    def test_string25(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "1e.245""$%##" _abcd ""","""123,1e.245,$%##,_abcd,<EOF>""",187))  
    def test_string26(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "1e.245\\\\"  ""","""123,1e.245\\\\,<EOF>""",188))    
    def test_string27(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "1e.245""","""123,Unclosed String: 1e.245""",189))
    def test_string28(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "1e.245??" 123.  ""","""123,1e.245??,123.,<EOF>""",190))
    def test_string29(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "1e.245??" 123?  ""","""123,1e.245??,123,Error Token ?""",191))    
    def test_string30(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "1e.245??" 123.E23_abcde ""","""123,1e.245??,123.E23,_abcde,<EOF>""",192))
    def test_string31(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Tran\\tManh||Hung\\fTran\\\\Tran???\\tHung"  ""","""Tran\\tManh||Hung\\fTran\\\\Tran???\\tHung,<EOF>""",193))    
    def test_string32(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Tran\\bManh||Hung\\bTran\\mTran???\\tHung"  ""","""Illegal Escape In String: Tran\\bManh||Hung\\bTran\\m""",194))    
    def test_string33(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Tran\\bManh||Hung\\bTran\\\\mTran???\\tHung"  ""","""Tran\\bManh||Hung\\bTran\\\\mTran???\\tHung,<EOF>""",195))    
    def test_string34(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Tran\\tHung" "Tran\\0Hung" ""","""Tran\\tHung,Illegal Escape In String: Tran\\0""",196))   
    def test_id_6(self):
        self.assertTrue(TestLexer.checkLexeme("id1\tid2_","id1,id2_,<EOF>",197))
    def test_variable_decl_2(self):
        self.assertTrue(TestLexer.checkLexeme("float a[3];","float,a,[,3,],;,<EOF>",198))
    def test_variable_decl_3(self):
        self.assertTrue(TestLexer.checkLexeme("int x,y[10]; float a,b,c[10] ","int,x,,,y,[,10,],;,float,a,,,b,,,c,[,10,],<EOF>",199))
    def test_string39(self):
        self.assertTrue(TestLexer.checkLexeme(""" "true false"true false"truefalse" ""","""true false,true,false,truefalse,<EOF>""", 200))



