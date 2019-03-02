/* This program using Monte carlo simulation to simulate gambling process, change BUYAMOUNT to see the win rate */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <stdbool.h>

#define BUYAMOUNT 25
#define TESTINGN 2000

int main(void) {
    int count = 0;
    bool one = false;
    bool two = false;
    bool three = false;
    int temp;
    time_t t;

    srand((unsigned) time(&t));


    for (int i = 0; i < TESTINGN; i++) {
        temp = 0;
        
        for (int j = 0; j < BUYAMOUNT; j++) {
            temp = rand() % 100;
            if (temp <= 55) {
                one = true;
            } else if (temp > 55 && temp <= 90) {
                two = true;
            } else {
                three = true;
            }
        }

        if (one && two && three) {
            count++;
        }
        
        one = two = three = 0;
    }
    
    printf("count: %d, winning rate: %f\n", count, (float)count/TESTINGN);
    return 0;
}
