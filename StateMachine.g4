grammar StateMachine;

import simple_arithmetic;

/* Lexer rules */
fragment LOWERCASE: [a-z];
fragment UPPERCASE: [A-Z];

STATEMACHINE: 'StateMachine';
STATE: 'state';
COMPOSITE_STATE: 'composite state';
TRANSITION_SYMBOL: '->';
INITIAL: 'INITIAL';
FINAL: 'FINAL';

TEXT: '\'' (UPPERCASE | LOWERCASE)+ '\'';
NAME: UPPERCASE (LOWERCASE | UPPERCASE)*;

NOT_EQ: '!=';
INF: '<';
INF_EQ: '<=';
SUP: '>';
SUP_EQ: '>=';

WS: [ \t\r\n] -> skip;

/* Parser rules */

statemachine:
	STATEMACHINE NAME '{' initial_state states += state_rule+ '}' EOF;

composite_state:
	COMPOSITE_STATE NAME '{' transitions += transition* (
		initial_state states += state_rule+
	)? '}';

simple_state: STATE NAME '{' transitions += transition* '}';

state_rule: (simple_state | composite_state);

initial_state: INITIAL TRANSITION_SYMBOL target = NAME ';';

transition:
	TRANSITION_SYMBOL target = (NAME | FINAL) ':' input = TEXT 
	('[' guard ']')? 
	('/' '{' assignments += separated_assignment* '}')? ';';

guard: variable (EQ | NOT_EQ | INF | INF_EQ | SUP | SUP_EQ) expression;

separated_assignment: assignment ';';