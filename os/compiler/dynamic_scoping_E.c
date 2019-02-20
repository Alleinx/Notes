#include <stdio.h>

#define a (x+1)

int x = 2;

void b(void) {
    x = a;
    printf("%d\n", x);
}

void c(void) {
    int x = 1;
    printf("%d\n", a);
}

int main(void) {
    b();
    c();

    return 0;
}
