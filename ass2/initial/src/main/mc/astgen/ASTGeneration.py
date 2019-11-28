
#Trần Mạnh Hưng 
#1711646

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import * 

class ASTGeneration(MCVisitor):
    #PROGRAM
    def visitProgram(self,ctx:MCParser.ProgramContext):
        decl = (int)(len(ctx.fun_decl())+len(ctx.vardecl()))
        lst = []
        for i in range(decl):
            if(isinstance(ctx.getChild(i),MCParser.Fun_declContext)):
                lst.append(self.visit(ctx.getChild(i)))
            if(isinstance(ctx.getChild(i),MCParser.VardeclContext)):
                lst+=self.visit(ctx.getChild(i))
        return Program(lst)    
    

    #VARDECL
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        lst = []
        for x in ctx.var():
            if (x.INTLIT()):
                lst.append(VarDecl((x.ID().getText()),ArrayType(x.INTLIT().getText(),self.visit(ctx.pritype()))))
            else:
                lst.append(VarDecl((x.ID().getText()),self.visit(ctx.pritype())))
        return lst
    

    #PRITYPE    
    def visitPritype(self,ctx:MCParser.PritypeContext):
        if (ctx.BOOLEAN()):
            return BoolType()
        if (ctx.FLOAT()):
            return FloatType()
        if (ctx.INTTYPE()):
            return IntType()
        if (ctx.STRING()):
            return StringType()
    


    #FUNCDECL        
    def visitFun_decl(self,ctx:MCParser.Fun_declContext):
        Id_ = Id(ctx.ID().getText())
        paraList = self.visit(ctx.paraList())
        type_ = self.visit(ctx.type_())
        block_state = self.visit(ctx.block_state())
        return FuncDecl(Id_,paraList,type_, block_state)
    

    

    #PARALIST    
    def visitParaList(self,ctx:MCParser.ParaListContext):
        lst = []
        for x in ctx.para():
            if (x.getChildCount() == 4):
                Id_ = x.ID().getText()
                ArrayPointer = ArrayPointerType(self.visit(x.pritype()))
                lst.append(VarDecl(Id_,ArrayPointer))
            else:
                Id_ = x.ID().getText()
                pritype = self.visit(x.pritype())
                lst.append(VarDecl(x.ID().getText(),pritype))
        return lst            
    



    #TYPE_    
    def visitType_(self,ctx:MCParser.Type_Context):
        if (ctx.VOID()):
            return VoidType()
        if (ctx.pritype()):
            return self.visit(ctx.pritype())
        if (ctx.array_pointer()):
            return self.visit(ctx.array_pointer())
    



    #ARRAY_POTNTER        
    def visitArray_pointer(self,ctx:MCParser.Array_pointerContext):
        ArrayPointer = ArrayPointerType(self.visit(ctx.pritype()))
        if(ctx.ID()):
        	Id_ = self.visit(ctx.ID())
        	return VarDecl(Id_,ArrayPointer)
        else:
        	return ArrayPointer	



    #BLOCK_STATE        
    def visitBlock_state(self,ctx:MCParser.Block_stateContext):
        return Block(self.visit(ctx.var_stmtList()))
    




    #VAR_STMTLIST    
    def visitVar_stmtList(self,ctx:MCParser.Var_stmtListContext):
        countVarStmt = (int)(len(ctx.vardecl())+len(ctx.statement()))
        lst = []
        for i in range(countVarStmt):
            if(isinstance(ctx.getChild(i),MCParser.StatementContext)):
                lst.append(self.visit(ctx.getChild(i)))
            if(isinstance(ctx.getChild(i),MCParser.VardeclContext)):
                lst+=self.visit(ctx.getChild(i))
        return lst
    


    #STATEMENT    
    def visitStatement(self,ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)
    


    #IFSTATEMENT    
    def visitIf_state(self,ctx:MCParser.If_stateContext):
        exp = self.visit(ctx.exp())
        stmt0 = self.visit(ctx.statement(0))
        if(ctx.ELSE()):
            stmt1 = self.visit(ctx.statement(1))
            return If(exp,stmt0,stmt1)
        else:
            return If(exp,stmt0)    
    

    #FORSTATEMENT
    def visitFor_state(self,ctx:MCParser.For_stateContext):
        exp1 = self.visit(ctx.exp(0))
        exp2 = self.visit(ctx.exp(1))
        exp3 = self.visit(ctx.exp(2))
        stmt = self.visit(ctx.statement())
        return For(exp1,exp2,exp3,stmt)
    

    #DO_WHILE_STATEMENT
    def visitDo_while_state(self,ctx:MCParser.Do_while_stateContext):
        exp = self.visit(ctx.exp())
        statementList = self.visit(ctx.statementList())
        return Dowhile(statementList,exp)
    

    #STATEMENTLIST
    def visitStatementList(self,ctx:MCParser.StatementListContext):
        countStmt = (int)(len(ctx.statement()))
        lst = []
        for i in range(countStmt):
            if(isinstance(ctx.getChild(i),MCParser.StatementContext)):
                lst.append(self.visit(ctx.getChild(i)))
        return lst        
    

    
    #EXP_STATEMENT
    def visitExp_statement(self,ctx:MCParser.Exp_statementContext):
        return self.visit(ctx.exp())   
    

    
    #RETURN
    def visitReturn_statement(self,ctx:MCParser.Return_statementContext):
        if(ctx.exp()):
            return Return(self.visit(ctx.exp()))
        else:
            return Return()
    


    #BREAK
    def visitBreak_state(self,ctx:MCParser.Break_stateContext):
        return  Break()
    


    #CONTINUE
    def visitContinue_state(self,ctx:MCParser.Continue_stateContext):
        return Continue()          
    

    #EXP
    def visitExp(self, ctx:MCParser.ExpContext):
        
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp1())
        else:
            exp1 = self.visit(ctx.exp1())
            exp0 = self.visit(ctx.exp())
            Assign = ctx.getChild(1).getText()   
            return BinaryOp(Assign,exp1,exp0)
    

    def visitExp1(self, ctx:MCParser.Exp1Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp2())
        else:
            or_ = ctx.getChild(1).getText()
            exp1 = self.visit(ctx.exp1())
            exp2 = self.visit(ctx.exp2())
            return BinaryOp(or_,exp1,exp2)
    

    def visitExp2(self, ctx:MCParser.Exp2Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp3())
        else:
            and_ = ctx.getChild(1).getText()
            exp2 = self.visit(ctx.exp2())
            exp3 = self.visit(ctx.exp3())
            return BinaryOp(and_,exp2,exp3)
    

    def visitExp3(self, ctx:MCParser.Exp3Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp4(0))
        else:
            op = ctx.getChild(1).getText()
            exp4 = self.visit(ctx.exp4(0))
            exp4_ = self.visit(ctx.exp4(1))
            return BinaryOp(op,exp4,exp4_)
    

    def visitExp4(self, ctx:MCParser.Exp4Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp5(0))
        else:
            op = ctx.getChild(1).getText()
            exp5 = self.visit(ctx.exp5(0))
            exp5_ = self.visit(ctx.exp5(1))  
            return BinaryOp(op,exp5,exp5_)
    

    def visitExp5(self, ctx:MCParser.Exp5Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp6())
        else:
            op = ctx.getChild(1).getText()
            exp5 = self.visit(ctx.exp5()) 
            exp6 = self.visit(ctx.exp6())
            return BinaryOp(op,exp5,exp6)
    

    def visitExp6(self, ctx:MCParser.Exp6Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp7())
        else:
            op = ctx.getChild(1).getText()
            exp6 = self.visit(ctx.exp6())
            exp7 = self.visit(ctx.exp7()) 
            return BinaryOp(op,exp6,exp7)
    

    def visitExp7(self,ctx:MCParser.Exp7Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp8())
        else:
            op = ctx.getChild(0).getText()
            exp7 = self.visit(ctx.exp7())    
            return UnaryOp(op,exp7)
    

    def visitExp8(self, ctx:MCParser.Exp8Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.operands())
        else:
            operands = self.visit(ctx.operands())
            exp = self.visit(ctx.exp())
            return ArrayCell(operands,exp)
    #END_EXP



    #OPERANDS
    def visitOperands(self,ctx:MCParser.OperandsContext):
        if (ctx.INTLIT()):
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif (ctx.STRINGLIT()):
            return StringLiteral(ctx.STRINGLIT().getText())
        elif (ctx.bool_lit()):
            return self.visit(ctx.bool_lit())      
        elif (ctx.ID()):
            return Id(ctx.ID().getText())
        elif (ctx.FLOATLIT()):
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif (ctx.func_call()):
            return self.visit(ctx.func_call()) 
        else:
            return self.visit(ctx.exp())
    
    

    #BOOLLIT        
    def visitBool_lit(self,ctx:MCParser.Bool_litContext):
        val = True if ctx.TRUE() else False
        return BooleanLiteral(val)        
    
    

    #FUNCALL
    def visitFunc_call(self,ctx:MCParser.Func_callContext):
        return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.listexp())) 
    
    

    #LISTEXP
    def visitListexp(self,ctx:MCParser.ListexpContext):
        expCount = (int)(len(ctx.exp())+len(ctx.CM()))
        lst = []
        for i in range(expCount):
            if(isinstance(ctx.getChild(i),MCParser.ExpContext)):
                lst.append(self.visit(ctx.getChild(i)))    
        return lst                                   


                       










