
"""
 * @author nhphung
"""

#Trần Mạnh Hưng 
#1711646



from AST import * 
from Visitor import BaseVisitor
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return 'MType([' + ','.join(str(x) for x in self.partype) + '],' + str(self.rettype) + ')'

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return 'Symbol(' + str(self.name) + ',' + str(self.mtype) + ')'


class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putInt",MType([IntType()],VoidType())),
    Symbol("putIntLn",MType([IntType()],VoidType())),
    Symbol("getFloat",MType([],FloatType())),
    Symbol("putFloat",MType([FloatType()],VoidType())),
    Symbol("putFloatLn",MType([FloatType()],VoidType())),
    Symbol("putBool",MType([BoolType()],VoidType())),
    Symbol("putBoolLn",MType([BoolType()],VoidType())),
    Symbol("putString",MType([StringType()],VoidType())),
    ]
    callFunc = []

    
    def __init__(self,ast):
        
        self.ast = ast

    
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)
    #DEFINE Hàm 
    def type_check_Operant(self,LHS,RHS):
        if type(LHS) is IntType and type(RHS) is IntType:
            return IntType()
        elif type(LHS) in [FloatType,IntType] and type(RHS) in [FloatType,IntType]:
            return FloatType()
        elif type(LHS) is BoolType and type(RHS) is BoolType:
            return BoolType()
        return None 

    def type_check(self,LHS,RHS,type_check = True):
            if type(LHS) is FloatType and type(RHS) in [IntType,FloatType]:
                return FloatType()
            elif type(LHS) is type(RHS):
                return type(LHS)
            if(type_check == False):
                if type(LHS) is type(RHS):
                    if (type(LHS.eleType)==type(RHS.eleType)):
                        return type(LHS) 
                elif type(LHS) in [ArrayType,ArrayPointerType] and type(RHS) is ArrayType:
                    if (type(LHS.eleType)==type(RHS.eleType)):
                        return RHS   
            return None

    def raiseRedeclred(self,kind,name,list_decl,func_list):
        x = self.lookup(name,list_decl,func_list)
        if x is not None:
            raise Redeclared(kind,name)
        return False
    def raiseUnreach(self,name,listFunc):
        res = self.lookup(name,listFunc,lambda x:x)
        if res is None:
            raise UnreachableFunction(name)
        return False
    
    def raiseUndeclred(self,ast,c,kind):
        res = self.lookup(ast.method.name,c,lambda x: x.name)
        if res is None:
            raise Undeclared(kind,ast.method.name)
        elif type(res.mtype) is not MType:
            raise TypeMismatchInExpression(ast)
        return res.mtype.rettype   
    
    def returnInStatement(self,x):
        if type(x) is If:
            return 1
        elif type(x) is Return:
            return 1
        elif type(x) is Block:
            return 1
        elif type(x) is For:
            return 1
        elif type(x) is Dowhile:
            return 1
        elif type(x) is Continue:
            return 1
        elif type(x) is Break:
            return 1
        return None
   
    def checkNotLeft(self,ast,LHS):
        if not instance(ast.left,LHS):
            raise 
    #DEFINE DỮ LIỆU
    def visitProgram(self,ast, c):
        # print(ast.decl)
        list_global = c.copy()
        i = 0
        for x in ast.decl:
            if type(x) is FuncDecl:
                self.raiseRedeclred(Function(),x.name.name,list_global,lambda x: x.name)
                param_list = x.param
                list_global.append(Symbol(x.name.name, MType([i.varType for i in param_list], x.returnType)))
            if type(x) is VarDecl:
                self.raiseRedeclred(Variable(),x.variable,list_global,lambda x: x.name)
                list_global.append(Symbol(x.variable,x.varType))
        list_funcCall = list_global
        main = self.lookup("main",list_global,lambda x: x.name)
        if main and type(main.mtype) is MType:
            i = i + 1
        if i == 0:
            raise NoEntryPoint()
        for x in ast.decl:
            
            if type(x) is FuncDecl:
                [self.visit(x,(list_global))]            
        for x in ast.decl:
            if type(x) is FuncDecl:
                if x.name.name == "main":
                    continue
                else:
                    self.raiseUnreach(x.name.name,self.callFunc)
        return None
        
      
   
    def visitFuncDecl(self,ast,c):
        list_local = []
        inLoop = False
        stmts = []
        for var_decl in ast.param:
            self.raiseRedeclred(Parameter(),var_decl.variable,list_local,lambda x: x.name)
            list_local.append(Symbol(var_decl.variable,var_decl.varType))
        for x in ast.body.member:
            if type(x) is VarDecl:
                self.raiseRedeclred(Variable(),x.variable,list_local,lambda x: x.name)
                list_local.append(Symbol(x.variable,x.varType))
            resultType = self.returnInStatement(x)       
            if resultType is not None:
                temp = [self.visit(x,((c+list_local)[::-1],ast.returnType,False))]
                stmts.extend(temp)
            else:
                temp = [self.visit(x,(c+list_local)[::-1])]    
                stmts.append(temp)
        checkReturn = False
        for x in stmts:
            if x is True:
                checkReturn = True
        if (type(ast.returnType) is not VoidType):
            if checkReturn is False:
                raise FunctionNotReturn(ast.name.name)        
        return None    
    
    
    def visitCallExpr(self, ast, c):
        self.raiseUndeclred(ast,c,Function())
        self.callFunc.append(ast.method.name)
        at = [self.visit(x,c) for x in ast.param]
        res = self.lookup(ast.method.name,c, lambda x : x.name)
        if len(ast.param) != len(res.mtype.partype):
            raise TypeMismatchInExpression(ast)
        else:
            for x in list(zip(res.mtype.partype,at)):
                if self.type_check(x[0],x[1],False) is None:
                    raise TypeMismatchInExpression(ast)
        for x in ast.param:
            [self.visit(x,c)]
        x = self.visitId(ast.method,c)
        return x.rettype
    
    # Phần Typemissmatch cho Statement
    
    def visitIf(self,ast,c):
        decl,retType,inLoop = c
        expr = self.visit(ast.expr,decl)
        if type(expr) is not BoolType:
            raise TypeMismatchInStatement(ast)
        if type(ast.thenStmt) is Block:
            [self.visit(ast.thenStmt,c)]   
        else:    
            resultType = self.returnInStatement(ast.thenStmt)       
            if resultType is not None:
                [self.visit(ast.thenStmt,c)]   
            else:   
                [self.visit(ast.thenStmt,decl)]          
        if ast.elseStmt is not None:
            if type(ast.elseStmt) is Block:
                [self.visit(ast.elseStmt,c)]
            else:
                resultType = self.returnInStatement(ast.elseStmt)       
                if resultType is not None:
                    [self.visit(ast.elseStmt,c)]   
                else:    
                    [self.visit(ast.elseStmt,decl)]   
        
    def visitFor(self,ast,c):
        decl,retType,inLoop = c
        expr1 = self.visit(ast.expr1,decl)
        expr2 = self.visit(ast.expr2,decl)
        expr3 = self.visit(ast.expr3,decl)
        if type(expr1) is not IntType or type(expr3) is not IntType or type(expr2) is not BoolType:
            raise TypeMismatchInStatement(ast)      
        [self.visit(ast.loop,(decl,retType,True))]
        
        
    def visitDowhile(self,ast,c):
        decl,retType,inLoop = c
        exp = self.visit(ast.exp,decl)
        if type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        lensl = len(ast.sl)
        for y in range(lensl):
            resultType = self.returnInStatement(ast.sl[y])       
            if resultType is not None:
                [self.visit(ast.sl[y],(decl,retType,True))]
            else:   
                [self.visit(ast.sl[y],decl)]   
            
        
    
    def visitReturn(self,ast,c):
        decl,k,inLoop = c
        
        if type(k) is VoidType:
            if ast.expr != None:
                raise TypeMismatchInStatement(ast)
        elif type(k) is ArrayPointerType or type(k) is ArrayType:
            x = self.visit(ast.expr,decl)
            if  self.type_check(k,x,False) is None:
                raise TypeMismatchInStatement(ast)
        else:    
            x = self.visit(ast.expr,decl)
            if  self.type_check(k,x,True) is None:
                raise TypeMismatchInStatement(ast)
        return True
   
   
    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left,c)
        right = self.visit(ast.right,c)
        result = self.type_check_Operant(left,right)
        if ast.op in ['<','<=','>','>=','==','!=']:
            if ast.op in ['==','!=']:
                    if type(left) is not type(right) or type(left) is FloatType or type(right) is FloatType:
                        raise TypeMismatchInExpression(ast)
            if result is not None:
                if type(left) is BoolType or type(right) is BoolType:
                    raise TypeMismatchInExpression(ast)
                return BoolType()
            raise TypeMismatchInExpression(ast)    
        elif ast.op in ['+','-','*','/','%']:
            if ast.op in ['%']:
                if type(left) is not type(right):
                    raise TypeMismatchInExpression(ast)
            if result is not None:
                if type(left) is BoolType or type(right) is BoolType:
                    raise TypeMismatchInExpression(ast)
                else:   
                    return result
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['=']:
            if not isinstance(ast.left, LHS):
                raise NotLeftValue(ast.left)
            if result is not None:
                if type(left) is BoolType or type(right) is BoolType:
                    raise TypeMismatchInExpression(ast)
                
                
                else:
                    return result
        elif ast.op in ['&&','||']:
            if result is not None:
                if type(left) is BoolType and type(right) is BoolType:
                    return BoolType()
            else: 
                raise TypeMismatchInExpression(ast)
        raise TypeMismatchInExpression(ast)         
    
    
    def visitUnaryOp(self,ast,c):
        expr = self.visit(ast.body,c)
        if ast.op == '-':
            if type(expr) in [IntType, FloatType]:
                return  expr
        elif ast.op == '!':
            if type(expr) is BoolType:
                return BoolType
        raise TypeMismatchInExpression(ast)
    
    def visitArrayCell(self,ast,c):
        x = self.visit(ast.arr,c)
        y = self.visit(ast.idx,c)
        if type(x) not in [ArrayType,ArrayPointerType]:
            raise TypeMismatchInExpression(ast)
        if type(y) is not IntType:
            raise TypeMismatchInExpression(ast)
        return x.eleType     
    
    def visitId(self,ast,c):
        res_var = self.lookup(ast.name,c,lambda x:x.name)
        if res_var is None: 
            raise Undeclared(Identifier(),ast.name)
        return res_var.mtype
    
    
    def visitVarDecl(self,ast,c):
        pass
    
    
    def visitBlock(self,ast,c):
        list_local_envi =  []
        decl,retType,inLoop = c
        for x in ast.member:
            if type(x) is VarDecl:
                self.raiseRedeclred(Variable(),x.variable,list_local_envi,lambda x: x.name)
                list_local_envi.append(Symbol(x.variable,x.varType))
            if type(x) is Id or type(x) is BinaryOp or type(x) is CallExpr:
                [self.visit(x,list_local_envi + decl)]
            else:
                [self.visit(x,(list_local_envi + decl,retType,inLoop))]
        return None        
    
    
    def visitContinue(self,ast,c):
        decl,retType,inLoop = c
        if inLoop is False:
            raise ContinueNotInLoop()
        return None
    def visitBreak(self,ast,c):
        decl,retType,inLoop = c
        if inLoop is False:
            raise BreakNotInLoop()
        return None    
    
    
    #Visit các kiểu
    def visitArrayType(self,ast,c):
        return ArrayType()
    def visitArrayPointerType(self,ast,c):
        return ArrayPointerType()
    def visitIntLiteral(self,ast, c): 
        return IntType()
    def visitBooleanLiteral(self,ast,c):
        return BoolType()
    def visitFloatLiteral(self, ast,c):
        return FloatType()
    def visitStringLiteral(self, ast,c):
        return StringType()        
    