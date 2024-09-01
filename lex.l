%{
#include <stdio.h>
#include <string.h>
int cnt = 0, i = 0, j = 0;
char st[20][10];
int c = 0, m = 0;
int lookup(char st[10][10], char *id, int n);
%}

digit [0-9]*
id [A-Z][a-zA-Z0-9]*
datatype inum|dnum|dub|tf|str|cstr
unsigned_integer {digit}*
signed_integer -{digit}*
unsigned_float {digit}*\.{digit}*[eE][+-]?{digit}*
keyword agar|keliye|iterate|jabtak|return|pass|warna
arop [+\-\*\/\%]
p print

%%

"\n" { c = 0; }
"@" { c = 1; }
"/@" { m = 1; }
"@/" { m = 0; }
{datatype} { if (!c && !m) fprintf(yyout, "\n%s is Datatype", yytext); }
{keyword} { if (!c && !m) fprintf(yyout, "\n%s is Keyword", yytext); }
{unsigned_integer} { if (!c && !m) fprintf(yyout, "\n%s is Unsigned Integer", yytext); }
{signed_integer} { if (!c && !m) fprintf(yyout, "\n%s is Signed Integer", yytext); }
{unsigned_float} { if (!c && !m) fprintf(yyout, "\n%s is Unsigned Float", yytext); }
{id} { if (c == 0 && m == 0) { if (!lookup(st, yytext, i)) { strcpy(st[i++], yytext); fprintf(yyout, "\n%s is Identifier", yytext); cnt++; } } }
{arop} { if (!c && !m) fprintf(yyout, "\n%s is Arithmetic Operator", yytext); }
{p} { if (!c && !m) fprintf(yyout, "\n%s is Function", yytext); }
. { if (!c && !m) fprintf(yyout, "\n%s is Delimiter", yytext); }

%%

int main(int argc, char **argv)
{
    yyin = fopen(argv[1], "r");
    yyout = fopen(argv[2], "w");
    yylex();
    printf("No. of identifiers are : %d\n", cnt);
    printf("The contents of the symbol table are:\n");
    for (j = 0; j < i; j++)
        printf("%s\n", st[j]);
    return 0;
}

int yywrap()
{
    return 1;
}

int lookup(char st[10][10], char *id, int n)
{
    for (j = 0; j < n; j++)
        if (!strcmp(st[j], id))
            return 1;
    return 0;
}