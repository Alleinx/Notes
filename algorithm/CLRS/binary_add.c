/** This is a program calculating the sum of two binary number with logic operators
 *  >>>NOTE: version 1 only support positive numbers' addition.<<<
 * 
 * 
 * add_binary(A, B, n):
 * START
 *     hold[] = A.length + 1;
 *     carry = 0;
 *     for i = A.length to 1 do:
 *         hold[i+1] = add(A[i], B[i], carry);
 *     END
 *     hold[0] = carry
 *     return hold
 * END
 * 
 * add(A, B, Carry):
 * START
 *     result1 = A XOR B //A+B
 * 
 *     A   B   R1
 *     0   0   0
 *     0   1   1
 *     1   0   1
 *     1   1   0
 * 
 *     remainder_1 = A AND B //calculate the remainder of A+B;
 * 
 *     A   B   Rm
 *     0   0   0
 *     0   1   0
 *     1   0   0
 *     1   1   1
 * 
 *     result2 = result1 XOR Carry //(A+B+carry)
 * 
 *     R1  C   R2
 *     0   0   0
 *     0   1   1
 *     1   0   1
 *     1   1   0
 * 
 *     Carry = (result1 AND Carry) OR remainder_1 //update carry here;
 * 
 *     R1  C   Rm1   Updated_C
 *     0   0   0     0
 *     0   1   1     1
 *     1   0   0     0
 *     1   1   0     1
 *     Note: there are only 4 combination of R1, C and Rm1 not 8;
 *     return result2
 * END
 */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *add_binary(char *A, char *B, int size);
char add(char A, char B, int *carry);

int main(void) {
    int len = 0;
    printf("Note: Two binary numbers' length should be the same.\n");
    printf("Input binary numbers' length (Ex: 1001 = 4, 0100 = 4 ):");
    scanf("%d", &len);

    char *A = (char*) malloc(sizeof(char) * (len));
    char *B = (char*) malloc(sizeof(char) * (len));

    printf("Input first Binary number:");
    scanf("%s", A);

    printf("Input second Binary number:");
    scanf("%s", B);

    char *result = add_binary(A, B, len);
    printf("%s + %s = %s\n", A, B, result);

    free(A);
    free(B);
    free(result);
    return 0;
}

char *add_binary(char *A, char *B, int size) {
    char *result = (char*) malloc(sizeof(char) * (size+1));
    int carry = 0;
    for (int i = size - 1; i >= 0; i--) {
        result[i+1] = add(A[i], B[i], &carry);
    }

    result[0] = (carry == 0) ? '0' : '1';

    return result;
}

char add(char A, char B, int *carry) {
    int remain = ( (A & B) == '0' ? 0 : 1); 
    int result_1 = A ^ B; 
    int result_2 = result_1 ^ (*carry); 
    int remain2 = (result_1 & *carry) | remain;
    *carry = remain2;

    return result_2 == 0 ? '0' : '1';
}

