# Generated from StateMachine.g4 by ANTLR 4.10.1
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
        4,1,31,155,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,1,0,4,0,34,8,0,11,0,12,0,35,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,4,1,52,8,1,11,1,12,1,
        53,3,1,56,8,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,64,8,2,10,2,12,2,67,9,
        2,1,2,1,2,1,3,1,3,3,3,73,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,88,8,5,1,5,1,5,1,5,5,5,93,8,5,10,5,12,5,96,9,
        5,1,5,3,5,99,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,5,8,111,
        8,8,10,8,12,8,114,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,128,8,10,1,10,3,10,131,8,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,5,10,142,8,10,10,10,12,10,145,9,10,1,11,1,
        11,3,11,149,8,11,1,12,1,12,1,13,1,13,1,13,0,1,20,14,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,0,4,2,0,12,12,14,14,2,0,15,19,29,29,1,0,
        25,26,1,0,27,28,156,0,28,1,0,0,0,2,40,1,0,0,0,4,59,1,0,0,0,6,72,
        1,0,0,0,8,74,1,0,0,0,10,79,1,0,0,0,12,102,1,0,0,0,14,106,1,0,0,0,
        16,112,1,0,0,0,18,117,1,0,0,0,20,130,1,0,0,0,22,148,1,0,0,0,24,150,
        1,0,0,0,26,152,1,0,0,0,28,29,5,7,0,0,29,30,5,14,0,0,30,31,5,1,0,
        0,31,33,3,8,4,0,32,34,3,6,3,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,
        1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,5,2,0,0,38,39,5,0,0,1,
        39,1,1,0,0,0,40,41,5,9,0,0,41,42,5,14,0,0,42,46,5,1,0,0,43,45,3,
        10,5,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,
        55,1,0,0,0,48,46,1,0,0,0,49,51,3,8,4,0,50,52,3,6,3,0,51,50,1,0,0,
        0,52,53,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,49,
        1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,5,2,0,0,58,3,1,0,0,0,59,
        60,5,8,0,0,60,61,5,14,0,0,61,65,5,1,0,0,62,64,3,10,5,0,63,62,1,0,
        0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,
        1,0,0,0,68,69,5,2,0,0,69,5,1,0,0,0,70,73,3,4,2,0,71,73,3,2,1,0,72,
        70,1,0,0,0,72,71,1,0,0,0,73,7,1,0,0,0,74,75,5,11,0,0,75,76,5,10,
        0,0,76,77,5,14,0,0,77,78,5,3,0,0,78,9,1,0,0,0,79,80,5,10,0,0,80,
        81,7,0,0,0,81,82,5,4,0,0,82,87,5,13,0,0,83,84,5,5,0,0,84,85,3,12,
        6,0,85,86,5,6,0,0,86,88,1,0,0,0,87,83,1,0,0,0,87,88,1,0,0,0,88,98,
        1,0,0,0,89,90,5,28,0,0,90,94,5,1,0,0,91,93,3,14,7,0,92,91,1,0,0,
        0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,
        1,0,0,0,97,99,5,2,0,0,98,89,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,
        100,101,5,3,0,0,101,11,1,0,0,0,102,103,3,26,13,0,103,104,7,1,0,0,
        104,105,3,20,10,0,105,13,1,0,0,0,106,107,3,18,9,0,107,108,5,3,0,
        0,108,15,1,0,0,0,109,111,3,18,9,0,110,109,1,0,0,0,111,114,1,0,0,
        0,112,110,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,112,1,0,0,
        0,115,116,5,0,0,1,116,17,1,0,0,0,117,118,3,26,13,0,118,119,5,29,
        0,0,119,120,3,20,10,0,120,19,1,0,0,0,121,122,6,10,-1,0,122,123,5,
        23,0,0,123,124,3,20,10,0,124,125,5,24,0,0,125,131,1,0,0,0,126,128,
        7,2,0,0,127,126,1,0,0,0,127,128,1,0,0,0,128,129,1,0,0,0,129,131,
        3,22,11,0,130,121,1,0,0,0,130,127,1,0,0,0,131,143,1,0,0,0,132,133,
        10,5,0,0,133,134,5,31,0,0,134,142,3,20,10,6,135,136,10,4,0,0,136,
        137,7,3,0,0,137,142,3,20,10,5,138,139,10,3,0,0,139,140,7,2,0,0,140,
        142,3,20,10,4,141,132,1,0,0,0,141,135,1,0,0,0,141,138,1,0,0,0,142,
        145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,21,1,0,0,0,145,143,
        1,0,0,0,146,149,3,24,12,0,147,149,3,26,13,0,148,146,1,0,0,0,148,
        147,1,0,0,0,149,23,1,0,0,0,150,151,5,22,0,0,151,25,1,0,0,0,152,153,
        5,21,0,0,153,27,1,0,0,0,15,35,46,53,55,65,72,87,94,98,112,127,130,
        141,143,148
    ]

class StateMachineParser ( Parser ):

    grammarFileName = "StateMachine.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "':'", "'['", "']'", 
                     "'StateMachine'", "'state'", "'composite state'", "'->'", 
                     "'INITIAL'", "'FINAL'", "<INVALID>", "<INVALID>", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "'.'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STATEMACHINE", 
                      "STATE", "COMPOSITE_STATE", "TRANSITION_SYMBOL", "INITIAL", 
                      "FINAL", "TEXT", "NAME", "NOT_EQ", "INF", "INF_EQ", 
                      "SUP", "SUP_EQ", "WS", "VARIABLE", "NUMBER", "LPAREN", 
                      "RPAREN", "PLUS", "MINUS", "TIMES", "DIV", "EQ", "POINT", 
                      "POW" ]

    RULE_statemachine = 0
    RULE_composite_state = 1
    RULE_simple_state = 2
    RULE_state_rule = 3
    RULE_initial_state = 4
    RULE_transition = 5
    RULE_guard = 6
    RULE_separated_assignment = 7
    RULE_file_ = 8
    RULE_assignment = 9
    RULE_expression = 10
    RULE_atom = 11
    RULE_number = 12
    RULE_variable = 13

    ruleNames =  [ "statemachine", "composite_state", "simple_state", "state_rule", 
                   "initial_state", "transition", "guard", "separated_assignment", 
                   "file_", "assignment", "expression", "atom", "number", 
                   "variable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    STATEMACHINE=7
    STATE=8
    COMPOSITE_STATE=9
    TRANSITION_SYMBOL=10
    INITIAL=11
    FINAL=12
    TEXT=13
    NAME=14
    NOT_EQ=15
    INF=16
    INF_EQ=17
    SUP=18
    SUP_EQ=19
    WS=20
    VARIABLE=21
    NUMBER=22
    LPAREN=23
    RPAREN=24
    PLUS=25
    MINUS=26
    TIMES=27
    DIV=28
    EQ=29
    POINT=30
    POW=31

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
            self.state = 28
            self.match(StateMachineParser.STATEMACHINE)
            self.state = 29
            self.match(StateMachineParser.NAME)
            self.state = 30
            self.match(StateMachineParser.T__0)
            self.state = 31
            self.initial_state()
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                localctx._state_rule = self.state_rule()
                localctx.states.append(localctx._state_rule)
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==StateMachineParser.STATE or _la==StateMachineParser.COMPOSITE_STATE):
                    break

            self.state = 37
            self.match(StateMachineParser.T__1)
            self.state = 38
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
            self.state = 40
            self.match(StateMachineParser.COMPOSITE_STATE)
            self.state = 41
            self.match(StateMachineParser.NAME)
            self.state = 42
            self.match(StateMachineParser.T__0)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateMachineParser.TRANSITION_SYMBOL:
                self.state = 43
                localctx._transition = self.transition()
                localctx.transitions.append(localctx._transition)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==StateMachineParser.INITIAL:
                self.state = 49
                self.initial_state()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 50
                    localctx._state_rule = self.state_rule()
                    localctx.states.append(localctx._state_rule)
                    self.state = 53 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==StateMachineParser.STATE or _la==StateMachineParser.COMPOSITE_STATE):
                        break



            self.state = 57
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
            self.state = 59
            self.match(StateMachineParser.STATE)
            self.state = 60
            self.match(StateMachineParser.NAME)
            self.state = 61
            self.match(StateMachineParser.T__0)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateMachineParser.TRANSITION_SYMBOL:
                self.state = 62
                localctx._transition = self.transition()
                localctx.transitions.append(localctx._transition)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
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
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [StateMachineParser.STATE]:
                self.state = 70
                self.simple_state()
                pass
            elif token in [StateMachineParser.COMPOSITE_STATE]:
                self.state = 71
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
            self.state = 74
            self.match(StateMachineParser.INITIAL)
            self.state = 75
            self.match(StateMachineParser.TRANSITION_SYMBOL)
            self.state = 76
            localctx.target = self.match(StateMachineParser.NAME)
            self.state = 77
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

        def guard(self):
            return self.getTypedRuleContext(StateMachineParser.GuardContext,0)


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
            self.state = 79
            self.match(StateMachineParser.TRANSITION_SYMBOL)
            self.state = 80
            localctx.target = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==StateMachineParser.FINAL or _la==StateMachineParser.NAME):
                localctx.target = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 81
            self.match(StateMachineParser.T__3)
            self.state = 82
            localctx.input_ = self.match(StateMachineParser.TEXT)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==StateMachineParser.T__4:
                self.state = 83
                self.match(StateMachineParser.T__4)
                self.state = 84
                self.guard()
                self.state = 85
                self.match(StateMachineParser.T__5)


            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==StateMachineParser.DIV:
                self.state = 89
                self.match(StateMachineParser.DIV)
                self.state = 90
                self.match(StateMachineParser.T__0)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==StateMachineParser.VARIABLE:
                    self.state = 91
                    localctx._separated_assignment = self.separated_assignment()
                    localctx.assignments.append(localctx._separated_assignment)
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 97
                self.match(StateMachineParser.T__1)


            self.state = 100
            self.match(StateMachineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GuardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(StateMachineParser.VariableContext,0)


        def expression(self):
            return self.getTypedRuleContext(StateMachineParser.ExpressionContext,0)


        def EQ(self):
            return self.getToken(StateMachineParser.EQ, 0)

        def NOT_EQ(self):
            return self.getToken(StateMachineParser.NOT_EQ, 0)

        def INF(self):
            return self.getToken(StateMachineParser.INF, 0)

        def INF_EQ(self):
            return self.getToken(StateMachineParser.INF_EQ, 0)

        def SUP(self):
            return self.getToken(StateMachineParser.SUP, 0)

        def SUP_EQ(self):
            return self.getToken(StateMachineParser.SUP_EQ, 0)

        def getRuleIndex(self):
            return StateMachineParser.RULE_guard

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGuard" ):
                return visitor.visitGuard(self)
            else:
                return visitor.visitChildren(self)




    def guard(self):

        localctx = StateMachineParser.GuardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_guard)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.variable()
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << StateMachineParser.NOT_EQ) | (1 << StateMachineParser.INF) | (1 << StateMachineParser.INF_EQ) | (1 << StateMachineParser.SUP) | (1 << StateMachineParser.SUP_EQ) | (1 << StateMachineParser.EQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 104
            self.expression(0)
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
        self.enterRule(localctx, 14, self.RULE_separated_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.assignment()
            self.state = 107
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
        self.enterRule(localctx, 16, self.RULE_file_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateMachineParser.VARIABLE:
                self.state = 109
                self.assignment()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
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
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.variable()
            self.state = 118
            self.match(StateMachineParser.EQ)
            self.state = 119
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [StateMachineParser.LPAREN]:
                self.state = 122
                self.match(StateMachineParser.LPAREN)
                self.state = 123
                self.expression(0)
                self.state = 124
                self.match(StateMachineParser.RPAREN)
                pass
            elif token in [StateMachineParser.VARIABLE, StateMachineParser.NUMBER, StateMachineParser.PLUS, StateMachineParser.MINUS]:
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==StateMachineParser.PLUS or _la==StateMachineParser.MINUS:
                    self.state = 126
                    _la = self._input.LA(1)
                    if not(_la==StateMachineParser.PLUS or _la==StateMachineParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 129
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 141
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = StateMachineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 132
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 133
                        self.match(StateMachineParser.POW)
                        self.state = 134
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = StateMachineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 135
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 136
                        _la = self._input.LA(1)
                        if not(_la==StateMachineParser.TIMES or _la==StateMachineParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 137
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = StateMachineParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 138
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 139
                        _la = self._input.LA(1)
                        if not(_la==StateMachineParser.PLUS or _la==StateMachineParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 140
                        self.expression(4)
                        pass

             
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_atom)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [StateMachineParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.number()
                pass
            elif token in [StateMachineParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
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
        self.enterRule(localctx, 24, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
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
        self.enterRule(localctx, 26, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
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
        self._predicates[10] = self.expression_sempred
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
         




