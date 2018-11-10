/**
 * Time complexity: O(n)
 * 
 * Evaluate value of 2x^3 - 6x^2 + 2x - 1 for x = 3
 * Input: poly[] = {2, -6, 2, -1}, x = 3
 * Output: 5
 * 
 * Evaluate value of 2x^3 + 3x + 1 for x = 2
 * Input: poly[] = {2, 0, 3, 1}, x = 2
 * Output: 23
 */

int polynomial(int *poly, int x, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum = poly[i] + x * sum;
    }

    return sum;
}