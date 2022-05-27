grammar COMBAT;

start : expr | <EOF> ;

expr     : 'fight' player=PLAYER #timedFightExpr
	 | 'vs' player=PLAYER #additionalPlayerExpr
	 | 'begin' #startFightExpr
         ;

PLAYER: ('A' ..'Z' | 'a' .. 'z' | '0' .. '9')+;
WS : [ \r\n\t]+ -> skip;