/* Maximum Contiguous Subarray Problem */
#include <stdio.h>

int cal_cross(int num[], int left, int right);
int max(int s1, int s2, int a);
int solve(int num[], int left, int right);

int main(void) {
    int num[5] = {1,-7,2,5,-7};
    int res = solve(num, 0, 4);
    printf("%d\n", res);
    return 0;
}

int solve(int num[], int left, int right) {
    if (left == right) {
        return num[left];
    }
    int mid = (right - left) / 2 + left; 
    int s1 = solve(num, left, mid);
    int s2 = solve(num, mid + 1, right);
    int a = cal_cross(num, left, right); 
    return max(s1,s2,a); 
}

int max(int s1, int s2, int a) {
    int temp = s1 > s2 ? s1 : s2;
    return temp > a ? temp : a;
}

int cal_cross(int num[], int left, int right) {
    int mid = (right - left) / 2 + left;
    int lmax = 0;
    int rmax = 0;
    int sum = 0;

    for(int i = mid; i >= left; i--) {
        sum += num[i];
        if (lmax <= sum) {
            lmax = sum;
        } else { 
            break;
        } 
    }

    for (int i = mid + 1, sum = 0; i <= right; i++) {
        sum += num[i];
        if (rmax <= sum) {
            rmax = sum;
        } else {
            break;
        }
    }

    return lmax + rmax;
}