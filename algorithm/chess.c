#include <stdio.h>
struct 
{
    unsigned char a:4;
    unsigned char b:4;
}i;
/* 位域 */

int main (void) {

    for (i.a = 1; i.a <= 9; i.a++) {
        for (i.b = 1; i.b<= 9; i.b++) {
            if((i.b - i.a) % 3) {
                printf("A = %d,B = %d\n", i.a, i.b);
            }
        }
    }
    return 0;
}