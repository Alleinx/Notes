/**
 *  Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
 * 
 *  E.x. {2,4,1,3,5} has three inversions (2,1),(4,1),(4,3).
 *  Modify merge sort to get this algorithm with O(nlogn);
 */

#include <stdio.h>

#define SIZE 5

void merge_sort(int *A, int l, int r, int *);
void merge(int *A, int left, int mid, int right, int *);

int main(void) {
    int test_set[SIZE] = {2, 3, 8, 6, 1};
    int pair = 0;
    merge_sort(test_set, 0, SIZE - 1, &pair);

    for (int i = 0; i < SIZE; i++) {
        printf("%d\t", test_set[i]);
    }

    printf("\nPAIR: %d\n", pair);

    return 0;
}

void merge_sort(int *A, int l, int r, int *inversion_pair) {
    int mid;
    if (l >= r) {
        return;
    }   

    mid = (r - l) / 2 + l;
    
    merge_sort(A, l, mid, inversion_pair);
    merge_sort(A, mid + 1, r, inversion_pair);
    merge(A, l, mid, r, inversion_pair);
}

void merge(int *A, int left, int mid, int right, int *inversion_pair) {
    int i = left; /* start point */
    int j = mid + 1; /* start point */
    int arr_index = 0;
    int hold[right - left + 1];

    while (i <= mid && j <= right) {
        if (A[i] <= A[j]) {
            hold[arr_index] = A[i];
            i++;
        } else {
            hold[arr_index] = A[j];
            /* If A[j] < A[i], for the rest of A[i...mid]: A[i...mid] > A[j] and i < j*/
            *inversion_pair += mid - i + 1; 
            j++;
        }
        arr_index++;
    }

    while (i <= mid) {
        hold[arr_index] = A[i];
        i++;
        arr_index++;
    }

    while (j <= right) {
        hold[arr_index] = A[j];
        j++;
        arr_index++;
    }

    for (int t = 0; t < arr_index; t++) {
        A[left + t] = hold[t];
    }
}