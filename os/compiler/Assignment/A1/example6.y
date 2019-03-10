%{
#include <stdio.h>
#include <string.h>
#define YYSTYPE char *

void yyerror(const char *str) {
    fprintf(stderr, "Error: %s\n", str);
}

int yywrap() {
    return 1;
}

main() {
    yyparse();
}

%}

%token FILETOK ZONETOK QUOTE FILENAME OBRACE EBRACE WORD SEMICOLON

%%
commands: /* empty */
        | commands command SEMICOLON
        ;

command:
        zone_set
        ;

zone_set:
        ZONETOK quotedname zonecontent
        {
            printf("Complete zone for '%s' found\n", $2);
        }
        ;

quotedname:
        QUOTE FILENAME QUOTE
        {
            $$=$2;
        }
        ;

zonecontent:
        OBRACE zonestatements EBRACE
        ;
        /* Note: this grammar chokes on filenames without either a '.' or '/' in them */

zonestatements: /* empty */
        |
        zonestatements zonestatement SEMICOLON
        ;

zonestatement:
        statements
        |
        FILETOK quotedname
        {
            printf("A zonefile name '%s' was encountered\n", $2);
        }
        ;

statements: /* empty */
        | statements statement
        ;

block:
        OBRACE zonestatements EBRACE SEMICOLON
        ;

statement: WORD | block | quotedname
%%