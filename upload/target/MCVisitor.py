# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardecl.
    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#pritype.
    def visitPritype(self, ctx:MCParser.PritypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#fun_decl.
    def visitFun_decl(self, ctx:MCParser.Fun_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#type_.
    def visitType_(self, ctx:MCParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paraList.
    def visitParaList(self, ctx:MCParser.ParaListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para.
    def visitPara(self, ctx:MCParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array.
    def visitArray(self, ctx:MCParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_pointer.
    def visitArray_pointer(self, ctx:MCParser.Array_pointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operands.
    def visitOperands(self, ctx:MCParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#bool_lit.
    def visitBool_lit(self, ctx:MCParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#index_op.
    def visitIndex_op(self, ctx:MCParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listexp.
    def visitListexp(self, ctx:MCParser.ListexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_state.
    def visitIf_state(self, ctx:MCParser.If_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_while_state.
    def visitDo_while_state(self, ctx:MCParser.Do_while_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statementList.
    def visitStatementList(self, ctx:MCParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_state.
    def visitFor_state(self, ctx:MCParser.For_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_state.
    def visitBreak_state(self, ctx:MCParser.Break_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_state.
    def visitContinue_state(self, ctx:MCParser.Continue_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_statement.
    def visitReturn_statement(self, ctx:MCParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_statement.
    def visitExp_statement(self, ctx:MCParser.Exp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_state.
    def visitBlock_state(self, ctx:MCParser.Block_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_stmtList.
    def visitVar_stmtList(self, ctx:MCParser.Var_stmtListContext):
        return self.visitChildren(ctx)



del MCParser