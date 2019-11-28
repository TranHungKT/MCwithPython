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
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_1(self):
        input = """int main() {
                        int a,b[5] ;
                        float b;
                        int d(int c){
                          if(c==1) b + 1 = 5 ;
                          else b + 2 = 10  ;
                        }
                        }"""
        expect = "Error on line 4 col 29: ("
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_2(self):
        input = """void main() {
                    float b ;
                    float d(boolean c){
                      if(c) b = 5 ;
                    }
                    }"""
        expect = "Error on line 3 col 27: ("
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_3(self):
        input = """void main() {    
                     getInt();
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))    
    def test_4(self):
        input = """void main() {    
                     putInt(4);
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_5(self):
        input = """void main() {    
                     getFloat();
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))               
    def test_34(self):
        input = """void main() {    
                     putFloat(4.0);
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))        
    def test_33(self):
        input = """void main() {    
                     putFloatLn(4.0);
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_6(self):
        input = """void main() {    
                     putBool(true);
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))               
    def test_7(self):
        input = """void main() {    
                     putBoolLn(false);
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_8(self):
        input = """void main() {    
                     putString("tran");
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))               
    def test_9(self):
        input = """void main() {    
                     putStringLn("tran");
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))               
    def test_10(self):
        input = """void main() {
                      int i(){
                      for( a = 0 ; a < 10 ; a + 1 ) {
                         if(a == 1) break;
                      }}} """
        expect = "Error on line 2 col 27: ("
        self.assertTrue(TestParser.checkParser(input,expect,215))               
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))                        
    def test_11(self):
        input = """int a; float b; """
        expect = "successful" 
        self.assertTrue(TestParser.checkParser(input,expect,217)) 
    def test_12(self):
        input = """int a; float b;
                    void main(){} """
        expect = "successful"     
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_13(self):
        input = """int a; float b;
                    void main(){
                    putIntLn(20,40,50);
                    } """
        expect = "successful"     
        self.assertTrue(TestParser.checkParser(input,expect,219))
   
    def test_14(self):
        input = """int a; float b;
                    void main(){
                    putIntLn(20,40,50);
                    getInt();
                    getString(tran);
                    } """
        expect = "successful"     
        self.assertTrue(TestParser.checkParser(input,expect,220))      

    def test_15(self):
        input = """ void main(){
                    foo( a,abc[50],b);
                    putIntLn ( 30 ) ;
                   } """
        expect = "successful"     
        self.assertTrue(TestParser.checkParser(input,expect,221))   
    def test_32(self):
        input = """ void main("""
        expect = "Error on line 1 col 11: <EOF>"     
        self.assertTrue(TestParser.checkParser(input,expect,222))   
    def test_16(self):
        input = """ int a = 10;
                   } """
        expect = "Error on line 1 col 7: ="      
        self.assertTrue(TestParser.checkParser(input,expect,223))   
    def test_17(self):
        input = """ int a; float b[10] ; int b = 10 ;
                   } """
        expect = "Error on line 1 col 28: ="     
        self.assertTrue(TestParser.checkParser(input,expect,224))   
    def test_18(self):
        input = """ int main(){
          int c(){
             int i ;
             for(i = 0;i<10;i+1)
             {
                   i ++ ;
             }
          }
        } """
        expect = "Error on line 2 col 15: ("     
        self.assertTrue(TestParser.checkParser(input,expect,225))   
    def test_19(self):
        input = """ int main(){
          int c(){
             int i ;
             for(i = 0;i<10;i+1)
             {
                   i + 10 ;
             }
          }
        } """
        expect = "Error on line 2 col 15: ("     
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_20(self):
        input = """int foo(int a, int b , float c){

        }"""
        expect = "successful"     
        self.assertTrue(TestParser.checkParser(input,expect,227))   
    def test_21(self):
        input = """int foo(int a, int b , float c){
                   if(1) a = 2 ;
        }"""
        expect = "successful"     
        self.assertTrue(TestParser.checkParser(input,expect,228)) 
    def test_22(self):
        input = """boolean foo(int a, int b , float c){
                    int boo(){
                     float doo(){

                     }
                    }   
        }"""
        expect = "Error on line 2 col 27: ("     
        self.assertTrue(TestParser.checkParser(input,expect,229))  
    def test_23(self):
        input = """boolean b( }"""
        expect = "Error on line 1 col 11: }"     
        self.assertTrue(TestParser.checkParser(input,expect,230))  
    def test_24(self):
        input = """float a = 10;"""
        expect = "Error on line 1 col 8: ="     
        self.assertTrue(TestParser.checkParser(input,expect,231))  
    def test_25(self):
        input = """float a ; float b ; float a + b;"""
        expect = "Error on line 1 col 28: +"     
        self.assertTrue(TestParser.checkParser(input,expect,232))  
    def test_26(self):
        input = """float a ; float b ; float a """
        expect = "Error on line 1 col 28: <EOF>"     
        self.assertTrue(TestParser.checkParser(input,expect,233))                                                     
    def test_27(self):
        input = """int main(){
        int a;
        int b[10];
        a = b[0];
        }"""
        expect = "successful"     
        self.assertTrue(TestParser.checkParser(input,expect,234))                                                     
    def test_28(self):
        input = """float main(){
        int a;
        int b[10];
        a = b[0] + b[1] + b[2];
        }"""
        expect = "successful"     
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_29(self):
        input = """void main(){
        string abc ;
        float a ; 
        a = 4.0 ; 
        }"""
        expect = "successful"     
        self.assertTrue(TestParser.checkParser(input,expect,236))    
    def test_30(self):
        input = """int main(){
        a + 1 + 2 = 10 ;
        b + 2 + 4 / 10 = 1 ;
        }"""
        expect = "successful"     
        self.assertTrue(TestParser.checkParser(input,expect,237))    
    def test_31(self):
        input = """int main(){
        a + 1 + 2 = 10 ;
        b + 2 + 4 / 10 = 1
        """
        expect = "Error on line 4 col 8: <EOF>"     
        self.assertTrue(TestParser.checkParser(input,expect,238))    
    def test_35(self):
        input = """int foo(int a, int b, int c){
        if(a == 0) b = c;
        else if(a == 1) c = b;
        else a = c;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))    
    def test_37(self):
        input = """int foo(int a, int b, int c){
        for(a;a<10;a + 1)
        {
         getInt();
         putIntLn(4);
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))   
    def test_39(self):
        input = """void main( ){ if (a) if (b) if (c) a; else a; else }"""
        expect = "Error on line 1 col 51: }"
        self.assertTrue(TestParser.checkParser(input, expect, 243))       
    def test_40(self):
        input = """int main(){
                break ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))
    def test_41(self):
        input = """boolean a ; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))               
    def test_42(self):
        input = """bool a ;; """
        expect = "Error on line 1 col 0: bool"
        self.assertTrue(TestParser.checkParser(input, expect, 246))               
    def test_43(self):
        input = """void main(){
        int a;
        if(a == 0) a = 2;
        else if(a == 3) a = 1;
        else
        }"""
        expect = "Error on line 6 col 8: }"
        self.assertTrue(TestParser.checkParser(input, expect, 247))          
    def test_44(self):
        input = """boolean main(){
        int a;
        do a + 1 = 0 ;
        while (true)
        }"""
        expect = "Error on line 5 col 8: }"
        self.assertTrue(TestParser.checkParser(input, expect, 248))            
    def test_45(self):
        input = """int main(){
        int a;
        do break ;
        while a > 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249)) 
    def test_46(self):
        input = """int main(){
        int a;
        return ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))
    def test_47(self):
        input = """int main(){
        int a;
        continue ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))    
    def test_48(self):
        input = """int main(){
        int a;
        for(a = 0; a<10;a+ 1)
        {
          continue;
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))
    def test_49(self):
        input = """int main(){
        int a;
        for(a = 0; a<10;a+ 1)
        {
          if(a==9) break;
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))   
    def test_64(self):
        input = """int main(){
        int a; boolean b;
        for(a = 0; a<10;a+ 1)
        { 
          putIntLn(5) ;
          if(a==9) getInt();
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))         
    def test_50(self):
        input = """void main(){
        int a;
        do a = a*a;
        while a < 3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))
    def test_51(self):
        input = """void main(){
        float a ;
        do a = a*2;
        while a < 10;
        return a ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))            
    def test_52(self):
        input = """void main(){
        int a
        do a = a*2;
        while a < 10;
        }"""
        expect = "Error on line 3 col 8: do"
        self.assertTrue(TestParser.checkParser(input, expect, 257))    
    def test_53(self):
        input = """void main(){
        int a;
        do a = a*2;
        while 
        }"""
        expect = "Error on line 5 col 8: }"
        self.assertTrue(TestParser.checkParser(input, expect, 258))    
    def test_54(self):
        input = """void main(){
        int a;
        do 
        while 
        }"""
        expect = "Error on line 4 col 8: while"
        self.assertTrue(TestParser.checkParser(input, expect, 259))        
    def test_55(self):
        input = """void main(){
        int a;
        do a = a*2;
        
        }"""
        expect = "Error on line 5 col 8: }"
        self.assertTrue(TestParser.checkParser(input, expect, 260))        
    def test_56(self):
        input = """void main(){
        int a;
        for(){

        }
        
        }"""
        expect = "Error on line 3 col 12: )"
        self.assertTrue(TestParser.checkParser(input, expect, 261))     
    def test_57(self):
        input = """int main(){
        int a;
        for(a = 1;a<10;){
         a = 10 ;
        }
        
        }"""
        expect = "Error on line 3 col 23: )"
        self.assertTrue(TestParser.checkParser(input, expect, 262))   
    def test_58(self):
        input = """void main(){
        int a;
        for(a<10){
          a = 10;
        }
        
        }"""
        expect = "Error on line 3 col 16: )"
        self.assertTrue(TestParser.checkParser(input, expect, 263))                     
    def test_59(self):
        input = """void main(){
        int a;
        do{
        a = a*2;
        if(a > 6) break;
        }
        while a < 12;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))    
    def test_60(self):
        input = """void main(){
        int a;
        do{
        a = a*2;
        if(a > 6) continue;
        }
        while a < 12;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))     
    def test_61(self):
        input = """void main(){
        boolean a;
        do break;
        while a < 10;
        return a ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))     
    def test_62(self):
        input = """
        float a ;
        do a = a*2;
        while a < 10;
        return a ;
        """
        expect = "Error on line 3 col 8: do"
        self.assertTrue(TestParser.checkParser(input, expect, 267))           
    def test_63(self):
        input = """
        }"""
        expect = "Error on line 2 col 8: }"
        self.assertTrue(TestParser.checkParser(input, expect, 268))         
    def test_65(self):
        input = """
            int a ;
            foo();
            float b;
            a != b ; 
            a = b +1 ;
            """
        expect = "Error on line 3 col 12: foo"
        self.assertTrue(TestParser.checkParser(input, expect, 269))     
    def test_66(self):
        input = """
            int a ;
            foo();
            float b;
            if(a != b)  
            a = b +1 ;
            else a = b - 1;
            """
        expect = "Error on line 3 col 12: foo"
        self.assertTrue(TestParser.checkParser(input, expect, 270))
    def test_67(self):
        input = """
            int a ;
            foo();
            float b;
            if(a != b)  
            break ;
            else continue;
            return;
            """
        expect = "Error on line 3 col 12: foo"
        self.assertTrue(TestParser.checkParser(input, expect, 271))  
    def test_68(self):
        input = """
            int a ;
            foo();
            float b;
            if(a != b)  
            a = b +1 ;
            else a = b - 1;
            a[100];
            100;
            b;
            return b;
            """
        expect = "Error on line 3 col 12: foo"
        self.assertTrue(TestParser.checkParser(input, expect, 272))  
    def test_69(self):
        input = """
            doo(1.2,3,4,5);
            foo();
            float b;
            a[100];
            100;
            b;
            return b;
            """
        expect = "Error on line 2 col 12: doo"
        self.assertTrue(TestParser.checkParser(input, expect, 273))       
    def test_70(self):
        input = """
           void tran(){
           int a ; 
           foo(1.,2.3,4);
           }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))          
    def test_71(self):
        input = """
            int a;
            return ; 
            """
        expect = "Error on line 3 col 12: return"
        self.assertTrue(TestParser.checkParser(input, expect, 275))  
    def test_72(self):
        input = """
        int main() {
        int a;
        if(a==10) {a + 1 = 11} else ;
        } 
            """
        expect = "Error on line 4 col 29: }"
        self.assertTrue(TestParser.checkParser(input, expect, 276))              
    def test_73(self):
        input = """
           int main() {
           int a;
           if(a==10) a + 1 = 11 ; else a + 1 = 12  ;
        }  
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))          
    def test_74(self):
        input = """int main(){
        foo(1.1);
        int a;
        doo(a);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))
    def test_75(self):
        input = """int main(){
        foo(1);
        int t(){int a;}
        int a;
        doo(a);
        }"""
        expect = "Error on line 3 col 13: ("
        self.assertTrue(TestParser.checkParser(input, expect, 279))
    def test_76(self):
        input = """int main(){
        int a;
        doo(a);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))
    def test_77(self):
        input = """int main(){
        int a;
        doo(a);
        float b;
        a = b/10;
        a = a +10;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))                           
    def test_78(self):
        input = """int main(){
        int a;
        a = b/10;
        a = a +10;
        putIntLn(a);
        return a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))        
    def test_79(self):
        input = """int main(){
        int a;
        doo(a);
        float b;
        string c ; 
        putString(c) ;
        putStringLn(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))          
    def test_80(self):
        input = """
        int a;
        doo(a);
        float b;
        a = b/10;
        a = a +10;
        """
        expect = "Error on line 3 col 8: doo"
        self.assertTrue(TestParser.checkParser(input, expect, 284))    
    def test_81(self):
        input = """void main(){
        int a,b;
        do{ 
        a = a*b;
        if(a > b) break;
        }
        while a < 10;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))         
    def test_82(self):
        input = """int main(){
        int a,b;
        do{ 
        a = a*b;
        if(a > b) break;
        }
        while a < 10;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))           
    def test_83(self):
        input = """
                int a,b;
                do{ 
                a = a*b;
                if(a > b) break;
                }
                while a < 10;
                }"""
        expect = "Error on line 3 col 16: do"
        self.assertTrue(TestParser.checkParser(input, expect, 287))    
    def test_90(self):
        input = """void main(){
        int a,b;
        a = b + 2;
        if(a>b) return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))          
    def test_89(self):
        input = """
        putBoolLn(true);
        putInt();
        putIntLn(5);"""
        expect = "Error on line 2 col 8: putBoolLn"
        self.assertTrue(TestParser.checkParser(input, expect, 289))
    def test_84(self):
        input = """void main(){
        int a,b;
        if(a>b) continue;
        return ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290)) 
    def test_85(self):
        input = """int foo(int a, int b){
        if(a > b) return a;
        return b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))                   
    def test_86(self):
        input = """int foo(int a, int b,float c){
        if(a > b) return a;
        else break;
        return b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))   
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))     
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))   
    def test_95(self):
        input = """
        int foo(int x,int a, int b, int c){
            return ;
        }
        int main(){
            return foo(3,4,2,1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))   
    def test_program_96(self):
        input = """
        int foo(int x,int a, int b, int c){
            x*a*b*c/a/b/c;
        }
        int main(){
            break ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))         
             