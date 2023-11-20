# Generated from StateMachine.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .StateMachineParser import StateMachineParser
else:
    from StateMachineParser import StateMachineParser

# This class defines a complete generic visitor for a parse tree produced by StateMachineParser.

class StateMachineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StateMachineParser#statemachine.
    def visitStatemachine(self, ctx:StateMachineParser.StatemachineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#composite_state.
    def visitComposite_state(self, ctx:StateMachineParser.Composite_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#simple_state.
    def visitSimple_state(self, ctx:StateMachineParser.Simple_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#state_rule.
    def visitState_rule(self, ctx:StateMachineParser.State_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#initial_state.
    def visitInitial_state(self, ctx:StateMachineParser.Initial_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#transition.
    def visitTransition(self, ctx:StateMachineParser.TransitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#separated_assignment.
    def visitSeparated_assignment(self, ctx:StateMachineParser.Separated_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#file_.
    def visitFile_(self, ctx:StateMachineParser.File_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#assignment.
    def visitAssignment(self, ctx:StateMachineParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#expression.
    def visitExpression(self, ctx:StateMachineParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#atom.
    def visitAtom(self, ctx:StateMachineParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#number.
    def visitNumber(self, ctx:StateMachineParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StateMachineParser#variable.
    def visitVariable(self, ctx:StateMachineParser.VariableContext):
        return self.visitChildren(ctx)



del StateMachineParser