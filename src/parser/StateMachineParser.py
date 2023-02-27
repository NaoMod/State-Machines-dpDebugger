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
        4,1,15,73,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,0,1,1,1,1,1,1,1,
        1,5,1,29,8,1,10,1,12,1,32,9,1,1,1,1,1,4,1,36,8,1,11,1,12,1,37,3,
        1,40,8,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,2,
        1,2,1,3,1,3,3,3,57,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,1,2,0,12,12,14,14,72,0,12,
        1,0,0,0,2,24,1,0,0,0,4,43,1,0,0,0,6,56,1,0,0,0,8,58,1,0,0,0,10,63,
        1,0,0,0,12,13,5,7,0,0,13,14,5,14,0,0,14,15,5,1,0,0,15,17,3,8,4,0,
        16,18,3,6,3,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,
        0,0,0,20,21,1,0,0,0,21,22,5,2,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,
        25,5,9,0,0,25,26,5,14,0,0,26,30,5,1,0,0,27,29,3,10,5,0,28,27,1,0,
        0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,39,1,0,0,0,32,30,
        1,0,0,0,33,35,3,8,4,0,34,36,3,6,3,0,35,34,1,0,0,0,36,37,1,0,0,0,
        37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,33,1,0,0,0,39,40,1,
        0,0,0,40,41,1,0,0,0,41,42,5,2,0,0,42,3,1,0,0,0,43,44,5,8,0,0,44,
        45,5,14,0,0,45,49,5,1,0,0,46,48,3,10,5,0,47,46,1,0,0,0,48,51,1,0,
        0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,
        5,2,0,0,53,5,1,0,0,0,54,57,3,4,2,0,55,57,3,2,1,0,56,54,1,0,0,0,56,
        55,1,0,0,0,57,7,1,0,0,0,58,59,5,11,0,0,59,60,5,10,0,0,60,61,5,14,
        0,0,61,62,5,3,0,0,62,9,1,0,0,0,63,64,5,10,0,0,64,65,7,0,0,0,65,66,
        5,4,0,0,66,67,5,13,0,0,67,68,5,5,0,0,68,69,5,13,0,0,69,70,5,6,0,
        0,70,71,5,3,0,0,71,11,1,0,0,0,6,19,30,37,39,49,56
    ]

class StateMachineParser ( Parser ):

    grammarFileName = "StateMachine.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "'['", "'/'", "']'", 
                     "'StateMachine'", "'state'", "'composite state'", "'->'", 
                     "'INITIAL'", "'FINAL'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STATEMACHINE", 
                      "STATE", "COMPOSITE_STATE", "TRANSITION_SYMBOL", "INITIAL", 
                      "FINAL", "TEXT", "NAME", "WS" ]

    RULE_statemachine = 0
    RULE_composite_state = 1
    RULE_simple_state = 2
    RULE_state_rule = 3
    RULE_initial_state = 4
    RULE_transition = 5

    ruleNames =  [ "statemachine", "composite_state", "simple_state", "state_rule", 
                   "initial_state", "transition" ]

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
    WS=15

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
            self.state = 12
            self.match(StateMachineParser.STATEMACHINE)
            self.state = 13
            self.match(StateMachineParser.NAME)
            self.state = 14
            self.match(StateMachineParser.T__0)
            self.state = 15
            self.initial_state()
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                localctx._state_rule = self.state_rule()
                localctx.states.append(localctx._state_rule)
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==StateMachineParser.STATE or _la==StateMachineParser.COMPOSITE_STATE):
                    break

            self.state = 21
            self.match(StateMachineParser.T__1)
            self.state = 22
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
            self.state = 24
            self.match(StateMachineParser.COMPOSITE_STATE)
            self.state = 25
            self.match(StateMachineParser.NAME)
            self.state = 26
            self.match(StateMachineParser.T__0)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateMachineParser.TRANSITION_SYMBOL:
                self.state = 27
                localctx._transition = self.transition()
                localctx.transitions.append(localctx._transition)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==StateMachineParser.INITIAL:
                self.state = 33
                self.initial_state()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 34
                    localctx._state_rule = self.state_rule()
                    localctx.states.append(localctx._state_rule)
                    self.state = 37 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==StateMachineParser.STATE or _la==StateMachineParser.COMPOSITE_STATE):
                        break



            self.state = 41
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
            self.state = 43
            self.match(StateMachineParser.STATE)
            self.state = 44
            self.match(StateMachineParser.NAME)
            self.state = 45
            self.match(StateMachineParser.T__0)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateMachineParser.TRANSITION_SYMBOL:
                self.state = 46
                localctx._transition = self.transition()
                localctx.transitions.append(localctx._transition)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
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
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [StateMachineParser.STATE]:
                self.state = 54
                self.simple_state()
                pass
            elif token in [StateMachineParser.COMPOSITE_STATE]:
                self.state = 55
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
            self.state = 58
            self.match(StateMachineParser.INITIAL)
            self.state = 59
            self.match(StateMachineParser.TRANSITION_SYMBOL)
            self.state = 60
            localctx.target = self.match(StateMachineParser.NAME)
            self.state = 61
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
            self.output = None # Token

        def TRANSITION_SYMBOL(self):
            return self.getToken(StateMachineParser.TRANSITION_SYMBOL, 0)

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(StateMachineParser.TEXT)
            else:
                return self.getToken(StateMachineParser.TEXT, i)

        def NAME(self):
            return self.getToken(StateMachineParser.NAME, 0)

        def FINAL(self):
            return self.getToken(StateMachineParser.FINAL, 0)

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
            self.state = 63
            self.match(StateMachineParser.TRANSITION_SYMBOL)
            self.state = 64
            localctx.target = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==StateMachineParser.FINAL or _la==StateMachineParser.NAME):
                localctx.target = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 65
            self.match(StateMachineParser.T__3)
            self.state = 66
            localctx.input_ = self.match(StateMachineParser.TEXT)
            self.state = 67
            self.match(StateMachineParser.T__4)
            self.state = 68
            localctx.output = self.match(StateMachineParser.TEXT)
            self.state = 69
            self.match(StateMachineParser.T__5)
            self.state = 70
            self.match(StateMachineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





