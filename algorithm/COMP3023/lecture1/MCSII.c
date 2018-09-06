/* dp[n] = max(0, dp[n-1]) + num[n] */

#include <stdio.h>

int MCS(int num[], int len);

int main(void) {
    int num[5] = {3,-2,7,-8,-10};
    int res = MCS(num, 5);
    printf("%d\n", res);
    return 0;
}

int MCS(int num[], int len) {
    int holder = num[0];

    for (int i = 1; i < len; i++) {
        if (num[i-1] > 0) {
            num[i] += num[i-1];
        }
        if (num[i] > holder) {
            holder = num[i];
        }
    }

    return holder;
}