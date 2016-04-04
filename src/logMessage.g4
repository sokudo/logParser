grammar logMessage;


messages
    : (message NL?)*
    ;

message
    : WS* timeStamp PS reqId PS proc PS thread PS
      logger PS logLevel PS userId PS
      timeExpense WS source WS query
    ;

timeStamp
    : TimeStamp
    ;

reqId
    : Uuid
    ;

proc
    : DecimalNumber
    ;

thread
    : DecimalNumber
    ;

logger
    : (~ '|')*
    ;

userId
    : DecimalNumber
    ;

timeExpense
    : '(' FixedPointNumber ')'
    ;

source
    : '/*' WS? assignment (('_' | WS) assignment)*
    ;

// Query contains '*/' followed by the SQL query.
query
    : UncomQuery
    ;

// Value here is surrounded by '<' and '>'.
assignment
    : Name '=' AngledValue
    ;

logLevel
    : 'CRITICAL'
    | 'INFO'
    | 'WARNING'
    | 'DEBUG'
    | 'VERBOSE'
    ;


// Lexer rules.

UncomQuery
    : '*/' WS (~ ';')* ';'
    ;

AngledValue
    : '<' (~ [> ])*? '>'
    ;

PS
    : '|'
    ;

DecimalNumber
    : Digit+
    ;

TimeStamp
    : Year '-' Month '-' Day ' ' Hour ':' Minute ':' Sec ',' Milli
    ;


FixedPointNumber
    : Digit+ '.' Digit+
    ;

Uuid
    : Hex4 Hex4 '-' Hex4 '-' Hex4 '-' Hex4 '-' Hex4 Hex4 Hex4
    ;

WS
    : ' '+
    ;

NL
    : '\r'? '\n'
    ;

Name
    : Letter (Letter | '_' | Digit )*
    ;

fragment Hex4
    : Hex Hex Hex Hex
    ;

fragment Year
    : Digit Digit Digit Digit
    ;

fragment Month
    : '0' Digit
    | '1' [012]
    ;

fragment Day
    : '0' [1-9]
    | [12] Digit
    | '3' [01]
    ;

fragment Hour
    : [01] Digit
    | '2' [0-3]
    ;

fragment Minute
    : [0-5] Digit
    ;

fragment Sec
    : [0-5] Digit
    ;

fragment Milli
    : Digit Digit Digit
    ;

fragment Digit
    : [0-9]
    ;

fragment Hex
    : [0-9A-Fa-f]
    ;

fragment Letter
    : [a-zA-Z]
    ;

ErrorChar
    : .
    ;
