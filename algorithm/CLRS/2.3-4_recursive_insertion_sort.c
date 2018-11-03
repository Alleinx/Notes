#include <stdio.h>

void insertion_sort(int *, int);

int main(void) {
    int test_set[] = {0,7,1,4,-2,4,10,5,9};

    insertion_sort(test_set, 8);

    for (int i = 0; i < 9; i++) {
        printf("%d\t", test_set[i]);
    }
    printf("\n");

    return 0;
}

void insertion_sort(int *A, int n) {
    int key;
    if (n == 0) {
        return;
    }

    insertion_sort(A, n-1);
    key = A[n];

    while (n >= 0) {
        n--;
        if (key < A[n]) {
            A[n+1] = A[n];
        } else {
            break;
        }
    }

    A[n+1] = key;
}