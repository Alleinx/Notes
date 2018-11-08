/* Longest Common Substring with dynamic programming */

int longest_common_sub_string(char *X, char *Y, int len_x, int len_y) {
    int container[len_x + 1][len_y + 1];
    int result = 0;

    for (int i = 0; i <= len_x; i++) {
        for (int j = 0; j <= len_y; j++) {
            if (i == 0 || j == 0) {
                container[i][j] = 0;

            } else if (X[i-1] == Y[j-1]) {
                container[i][j] = container[i-1][j-1] + 1;
                result = (result > container[i][j]) ? result : container[i][j];

            } else {
                container[i][j] = 0;
            }
        }
    }

    return result;
}