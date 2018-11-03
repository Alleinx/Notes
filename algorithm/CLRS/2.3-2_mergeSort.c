#include <stdio.h>

#define SIZE 12

void merge_sort(int *A, int l, int r);
void merge(int *A, int left, int mid, int right);

int main(void) {
    int test_set[SIZE] = {1,3,2,5,5,4,4,-3,1,7,6,0};

    merge_sort(test_set, 0, SIZE - 1);

    for (int i = 0; i < 12; i++) {
        printf("%d\t", test_set[i]);
    }

    printf("\n");

    return 0;
}

void merge_sort(int *A, int l, int r) {
    int mid;
    if (l >= r) {
        return;
    }   

    mid = (r - l) / 2 + l;
    
    merge_sort(A, l, mid);
    merge_sort(A, mid + 1, r);
    merge(A, l, mid, r);
}

void merge(int *A, int left, int mid, int right) {
    int i = left;
    int j = mid + 1;
    int arr_index = 0;
    int hold[right - left + 1];

    while (i <= mid && j <= right) {
        if (A[i] <= A[j]) {
            hold[arr_index] = A[i];
            i++;
        } else {
            hold[arr_index] = A[j];
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