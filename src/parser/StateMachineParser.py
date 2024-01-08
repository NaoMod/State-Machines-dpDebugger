# Generated from ../../StateMachine.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,142,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,0,4,0,32,8,0,11,0,12,0,33,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        5,1,43,8,1,10,1,12,1,46,9,1,1,1,1,1,4,1,50,8,1,11,1,12,1,51,3,1,
        54,8,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,2,1,
        2,1,3,1,3,3,3,71,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        5,5,84,8,5,10,5,12,5,87,9,5,3,5,89,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        7,5,7,98,8,7,10,7,12,7,101,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,
        9,1,9,1,9,1,9,3,9,115,8,9,1,9,3,9,118,8,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,5,9,129,8,9,10,9,12,9,132,9,9,1,10,1,10,3,10,136,8,
        10,1,11,1,11,1,12,1,12,1,12,0,1,18,13,0,2,4,6,8,10,12,14,16,18,20,
        22,24,0,3,2,0,11,11,13,13,1,0,19,20,1,0,21,22,143,0,26,1,0,0,0,2,
        38,1,0,0,0,4,57,1,0,0,0,6,70,1,0,0,0,8,72,1,0,0,0,10,77,1,0,0,0,
        12,93,1,0,0,0,14,99,1,0,0,0,16,104,1,0,0,0,18,117,1,0,0,0,20,135,
        1,0,0,0,22,137,1,0,0,0,24,139,1,0,0,0,26,27,5,6,0,0,27,28,5,13,0,
        0,28,29,5,1,0,0,29,31,3,8,4,0,30,32,3,6,3,0,31,30,1,0,0,0,32,33,
        1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,35,1,0,0,0,35,36,5,2,0,0,
        36,37,5,0,0,1,37,1,1,0,0,0,38,39,5,8,0,0,39,40,5,13,0,0,40,44,5,
        1,0,0,41,43,3,10,5,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,
        45,1,0,0,0,45,53,1,0,0,0,46,44,1,0,0,0,47,49,3,8,4,0,48,50,3,6,3,
        0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,54,
        1,0,0,0,53,47,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,2,0,0,
        56,3,1,0,0,0,57,58,5,7,0,0,58,59,5,13,0,0,59,63,5,1,0,0,60,62,3,
        10,5,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,
        66,1,0,0,0,65,63,1,0,0,0,66,67,5,2,0,0,67,5,1,0,0,0,68,71,3,4,2,
        0,69,71,3,2,1,0,70,68,1,0,0,0,70,69,1,0,0,0,71,7,1,0,0,0,72,73,5,
        10,0,0,73,74,5,9,0,0,74,75,5,13,0,0,75,76,5,3,0,0,76,9,1,0,0,0,77,
        78,5,9,0,0,78,79,7,0,0,0,79,80,5,4,0,0,80,88,5,12,0,0,81,85,5,22,
        0,0,82,84,3,12,6,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,
        86,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,88,81,1,0,0,0,88,89,1,0,0,
        0,89,90,1,0,0,0,90,91,5,5,0,0,91,92,5,3,0,0,92,11,1,0,0,0,93,94,
        3,16,8,0,94,95,5,3,0,0,95,13,1,0,0,0,96,98,3,16,8,0,97,96,1,0,0,
        0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,
        99,1,0,0,0,102,103,5,0,0,1,103,15,1,0,0,0,104,105,3,24,12,0,105,
        106,5,23,0,0,106,107,3,18,9,0,107,17,1,0,0,0,108,109,6,9,-1,0,109,
        110,5,17,0,0,110,111,3,18,9,0,111,112,5,18,0,0,112,118,1,0,0,0,113,
        115,7,1,0,0,114,113,1,0,0,0,114,115,1,0,0,0,115,116,1,0,0,0,116,
        118,3,20,10,0,117,108,1,0,0,0,117,114,1,0,0,0,118,130,1,0,0,0,119,
        120,10,5,0,0,120,121,5,25,0,0,121,129,3,18,9,6,122,123,10,4,0,0,
        123,124,7,2,0,0,124,129,3,18,9,5,125,126,10,3,0,0,126,127,7,1,0,
        0,127,129,3,18,9,4,128,119,1,0,0,0,128,122,1,0,0,0,128,125,1,0,0,
        0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,19,1,0,0,0,
        132,130,1,0,0,0,133,136,3,22,11,0,134,136,3,24,12,0,135,133,1,0,
        0,0,135,134,1,0,0,0,136,21,1,0,0,0,137,138,5,16,0,0,138,23,1,0,0,
        0,139,140,5,15,0,0,140,25,1,0,0,0,14,33,44,51,53,63,70,85,88,99,
        114,117,128,130,135
    ]

class StateMachineParser ( Parser ):

    grammarFileName = "StateMachine.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "'['", "']'", "'StateMachine'", 
                     "'state'", "'composite state'", "'->'", "'INITIAL'", 
                     "'FINAL'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "'.'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STATEMACHINE", "STATE", 
                      "COMPOSITE_STATE", "TRANSITION_SYMBOL", "INITIAL", 
                      "FINAL", "TEXT", "NAME", "WS", "VARIABLE", "NUMBER", 
                      "LPAREN", "RPAREN", "PLUS", "MINUS", "TIMES", "DIV", 
                      "EQ", "POINT", "POW" ]

    RULE_statemachine = 0
    RULE_composite_state = 1
    RULE_simple_state = 2
    RULE_state_rule = 3
    RULE_initial_state = 4
    RULE_transition = 5
    RULE_separated_assignment = 6
    RULE_file_ = 7
    RULE_assignment = 8
    RULE_expression = 9
    RULE_atom = 10
    RULE_number = 11
    RULE_variable = 12

    ruleNames =  [ "statemachine", "composite_state", "simple_state", "state_rule", 
                   "initial_state", "transition", "separated_assignment", 
                   "file_", "assignment", "expression", "atom", "number", 
                   "variable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    STATEMACHINE=6
    STATE=7
    COMPOSITE_STATE=8
    TRANSITION_SYMBOL=9
    INITIAL=10
    FINAL=11
    TEXT=12
    NAME=13
    WS=14
    VARIABLE=15
    NUMBER=16
    LPAREN=17
    RPAREN=18
    PLUS=19
    MINUS=20
    TIMES=21
    DIV=22
    EQ=23
    POINT=24
    POW=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StatemachineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._state_rule = None # State_ruleContext
            self.states = list() # of State_ruleContexts

        def STATEMACHINE(self):
            return self.getToken(StateMachineParser.STATEMACHINE, 0)

        def NAME(self):
            return self.getToken(StateMachineParser.NAME, 0)

        def initial_state(self):
            return self.getTypedRuleContext(StateMachineParser.Initial_stateContext,0)


        def EOF(self):
            return self.getToken(StateMachineParser.EOF, 0)

        def state_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StateMachineParser.State_ruleContext)
            else:
                return self.getTypedRuleContext(StateMachineParser.State_ruleContext,i)


        def getRuleIndex(self):
            return StateMachineParser.RULE_statemachine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatemachine" ):
                return visitor.visitStatemachine(self)
            else:
                return visitor.visitChildren(self)




    def statemachine(self):

        localctx = StateMachineParser.StatemachineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_statemachine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(StateMachineParser.STATEMACHINE)
            self.state = 27
            self.match(StateMachineParser.NAME)
            self.state = 28
            self.match(StateMachineParser.T__0)
            self.state = 29
            self.initial_state()
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                localctx._state_rule = self.state_rule()
                localctx.states.append(localctx._state_rule)
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==StateMachineParser.STATE or _la==StateMachineParser.COMPOSITE_STATE):
                    break

            self.state = 35
            self.match(StateMachineParser.T__1)
            self.state = 36
            self.match(StateMachineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._transition = None # TransitionContext
            self.transitions = list() # of TransitionContexts
            self._state_rule = None # State_ruleContext
            self.states = list() # of State_ruleContexts

        def COMPOSITE_STATE(self):
            return self.getToken(StateMachineParser.COMPOSITE_STATE, 0)

        def NAME(self):
            return self.getToken(StateMachineParser.NAME, 0)

        def initial_state(self):
            return self.getTypedRuleContext(StateMachineParser.Initial_stateContext,0)


        def transition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StateMachineParser.TransitionContext)
            else:
                return self.getTypedRuleContext(StateMachineParser.TransitionContext,i)


        def state_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StateMachineParser.State_ruleContext)
            else:
                return self.getTypedRuleContext(StateMachineParser.State_ruleContext,i)


        def getRuleIndex(self):
            return StateMachineParser.RULE_composite_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_state" ):
                return visitor.visitComposite_state(self)
            else:
                return visitor.visitChildren(self)




    def composite_state(self):

        localctx = StateMachineParser.Composite_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_composite_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(StateMachineParser.COMPOSITE_STATE)
            self.state = 39
            self.match(StateMachineParser.NAME)
            self.state = 40
            self.match(StateMachineParser.T__0)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateMachineParser.TRANSITION_SYMBOL:
                self.state = 41
                localctx._transition = self.transition()
                localctx.transitions.append(localctx._transition)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==StateMachineParser.INITIAL:
                self.state = 47
                self.initial_state()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 48
                    localctx._state_rule = self.state_rule()
                    localctx.states.append(localctx._state_rule)
                    self.state = 51 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==StateMachineParser.STATE or _la==StateMachineParser.COMPOSITE_STATE):
                        break



            self.state = 55
            self.match(StateMachineParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._transition = None # TransitionContext
            self.transitions = list() # of TransitionContexts

        def STATE(self):
            return self.getToken(StateMachineParser.STATE, 0)

        def NAME(self):
            return self.getToken(StateMachineParser.NAME, 0)

        def transition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StateMachineParser.TransitionContext)
            else:
                return self.getTypedRuleContext(StateMachineParser.TransitionContext,i)


        def getRuleIndex(self):
            return StateMachineParser.RULE_simple_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_state" ):
                return visitor.visitSimple_state(self)
            else:
                return visitor.visitChildren(self)




    def simple_state(self):

        localctx = StateMachineParser.Simple_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simple_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(StateMachineParser.STATE)
            self.state = 58
            self.match(StateMachineParser.NAME)
            self.state = 59
            self.match(StateMachineParser.T__0)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateMachineParser.TRANSITION_SYMBOL:
                self.state = 60
                localctx._transition = self.transition()
                localctx.transitions.append(localctx._transition)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(StateMachineParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class State_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_state(self):
            return self.getTypedRuleContext(StateMachineParser.Simple_stateContext,0)


        def composite_state(self):
            return self.getTypedRuleContext(StateMachineParser.Composite_stateContext,0)


        def getRuleIndex(self):
            return StateMachineParser.RULE_state_rule

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitState_rule" ):
                return visitor.visitState_rule(self)
            else:
                return visitor.visitChildren(self)




    def state_rule(self):

        localctx = StateMachineParser.State_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_state_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [StateMachineParser.STATE]:
                self.state = 68
                self.simple_state()
                pass
            elif token in [StateMachineParser.COMPOSITE_STATE]:
                self.state = 69
                self.composite_state()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initial_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.target = None # Token

        def INITIAL(self):
            return self.getToken(StateMachineParser.INITIAL, 0)

        def TRANSITION_SYMBOL(self):
            return self.getToken(StateMachineParser.TRANSITION_SYMBOL, 0)

        def NAME(self):
            return self.getToken(StateMachineParser.NAME, 0)

        def getRuleIndex(self):
            return StateMachineParser.RULE_initial_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitial_state" ):
                return visitor.visitInitial_state(self)
            else:
                return visitor.visitChildren(self)




    def initial_state(self):

        localctx = StateMachineParser.Initial_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_initial_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(StateMachineParser.INITIAL)
            self.state = 73
            self.match(StateMachineParser.TRANSITION_SYMBOL)
            self.state = 74
            localctx.target = self.match(StateMachineParser.NAME)
            self.state = 75
            self.match(StateMachineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.target = None # Token
            self.input_ = None # Token
            self._separated_assignment = None # Separated_assignmentContext
            self.assignments = list() # of Separated_assignmentContexts

        def TRANSITION_SYMBOL(self):
            return self.getToken(StateMachineParser.TRANSITION_SYMBOL, 0)

        def TEXT(self):
            return self.getToken(StateMachineParser.TEXT, 0)

        def NAME(self):
            return self.getToken(StateMachineParser.NAME, 0)

        def FINAL(self):
            return self.getToken(StateMachineParser.FINAL, 0)

        def DIV(self):
            return self.getToken(StateMachineParser.DIV, 0)

        def separated_assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StateMachineParser.Separated_assignmentContext)
            else:
                return self.getTypedRuleContext(StateMachineParser.Separated_assignmentContext,i)


        def getRuleIndex(self):
            return StateMachineParser.RULE_transition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransition" ):
                return visitor.visitTransition(self)
            else:
                return visitor.visitChildren(self)




    def transition(self):

        localctx = StateMachineParser.TransitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_transition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(StateMachineParser.TRANSITION_SYMBOL)
            self.state = 78
            localctx.target = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==StateMachineParser.FINAL or _la==StateMachineParser.NAME):
                localctx.target = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 79
            self.match(StateMachineParser.T__3)
            self.state = 80
            localctx.input_ = self.match(StateMachineParser.TEXT)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==StateMachineParser.DIV:
                self.state = 81
                self.match(StateMachineParser.DIV)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==StateMachineParser.VARIABLE:
                    self.state = 82
                    localctx._separated_assignment = self.separated_assignment()
                    localctx.assignments.append(localctx._separated_assignment)
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 90
            self.match(StateMachineParser.T__4)
            self.state = 91
            self.match(StateMachineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Separated_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(StateMachineParser.AssignmentContext,0)


        def getRuleIndex(self):
            return StateMachineParser.RULE_separated_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeparated_assignment" ):
                return visitor.visitSeparated_assignment(self)
            else:
                return visitor.visitChildren(self)




    def separated_assignment(self):

        localctx = StateMachineParser.Separated_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_separated_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.assignment()
            self.state = 94
            self.match(StateMachineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class File_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(StateMachineParser.EOF, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StateMachineParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(StateMachineParser.AssignmentContext,i)


        def getRuleIndex(self):
            return StateMachineParser.RULE_file_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_" ):
                return visitor.visitFile_(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = StateMachineParser.File_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_file_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateMachineParser.VARIABLE:
                self.state = 96
                self.assignment()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.match(StateMachineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(StateMachineParser.VariableContext,0)


        def EQ(self):
            return self.getToken(StateMachineParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(StateMachineParser.ExpressionContext,0)


        def getRuleIndex(self):
            return StateMachineParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = StateMachineParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.variable()
            self.state = 105
            self.match(StateMachineParser.EQ)
            self.state = 106
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(StateMachineParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StateMachineParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(StateMachineParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(StateMachineParser.RPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(StateMachineParser.AtomContext,0)


        def PLUS(self):
            return self.getToken(StateMachineParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(StateMachineParser.MINUS, 0)

        def POW(self):
            return self.getToken(StateMachineParser.POW, 0)

        def TIMES(self):
            return self.getToken(StateMachineParser.TIMES, 0)

        def DIV(self):
            return self.getToken(StateMachineParser.DIV, 0)

        def getRuleIndex(self):
            return StateMachineParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = StateMachineParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [StateMachineParser.LPAREN]:
                self.state = 109
                self.match(StateMachineParser.LPAREN)
                self.state = 110
                self.expression(0)
                self.state = 111
                self.match(StateMachineParser.RPAREN)
                pass
            elif token in [StateMachineParser.VARIABLE, StateMachineParser.NUMBER, StateMachineParser.PLUS, StateMachineParser.MINUS]:
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==StateMachineParser.PLUS or _la==StateMachineParser.MINUS:
                    self.state = 113
                    _la = self._input.LA(1)
                    if not(_la==StateMachineParser.PLUS or _la==StateMachineParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 116
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 128
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = StateMachineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 119
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 120
                        self.match(StateMachineParser.POW)
                        self.state = 121
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = StateMachineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 123
                        _la = self._input.LA(1)
                        if not(_la==StateMachineParser.TIMES or _la==StateMachineParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 124
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = StateMachineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 125
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 126
                        _la = self._input.LA(1)
                        if not(_la==StateMachineParser.PLUS or _la==StateMachineParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expression(4)
                        pass

             
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(StateMachineParser.NumberContext,0)


        def variable(self):
            return self.getTypedRuleContext(StateMachineParser.VariableContext,0)


        def getRuleIndex(self):
            return StateMachineParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = StateMachineParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atom)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [StateMachineParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.number()
                pass
            elif token in [StateMachineParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(StateMachineParser.NUMBER, 0)

        def getRuleIndex(self):
            return StateMachineParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = StateMachineParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(StateMachineParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(StateMachineParser.VARIABLE, 0)

        def getRuleIndex(self):
            return StateMachineParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = StateMachineParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(StateMachineParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




