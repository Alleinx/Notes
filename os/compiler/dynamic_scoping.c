/* This program demonstrate how dynamic scope works */
/* Dynamic scope: A use of a name x refers to the declaration of x in the most recently called procedure with such a declaration */
/* Declaration: Tells about the types of things. E.x: int i */
/* Definitions: Tells about the value of things. E.x: i = 3;*/

#include <stdio.h>

#define a (x+1)

int x = 2;

void b(void) {
    int x = 1;
    printf("%d\n", a);
}

void c(void) {
    printf("%d\n", a);
}

int main(void) {
    b();
    c();
    
    return 0;
}
