#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define N 26   // Total number of threads (in addition to main thread).
#define M 10  // Number of loop iterations per thread.

int flag[N];
int sum = 0;  // Data shared by all the threads.

void get_lock(int);
void release_lock(int);
bool door_is_closed();
bool wait_for_closing_door();
bool wait_finish(int);
bool inform_all_door_is_closed(int);
bool another_thread_want_to_enter();

// The function executed by each thread.
void *runner(void *param) {
    int i = *(int *)param; // This thread’s ID number.
    int m;

    for(m = 0; m < M; m++) {

        get_lock(i); /* get lock here */

        // The Critical Section starts right below.
        int s = sum;
        // Even threads increase s, odd threads decrease s.
        if(i % 2 == 0) {
            s++;
        } else {
            s--;
        }

        // Sleep a small random amount of time.  Do not remove this code.
        struct timespec delay;
        delay.tv_sec = 0;
        delay.tv_nsec = 100000000ULL * rand() / RAND_MAX;
        nanosleep(&delay, NULL);
        sum = s;
        // The Critical Section ends right above.

        release_lock(i); /* release lock here */

        printf("%c", 'A' + i); // Print this thread’s ID number as a letter.
        fflush(stdout);
    }

    return 0; // Thread dies.
}

int main(void) {
    pthread_t tid[N]; // Thread ID numbers.
    int param[N];     // One parameter for each thread.
    int i;

    // Create N threads.  Each thread executes the runner function with
    // i as argument.
    for(i = 0; i < N; i++) {
        param[i] = i;
        flag[i] = 0; /* init all thread status here */
        pthread_create(&tid[i], NULL, runner, &param[i]);
    }

    // Wait for N threads to finish.
    for(i = 0; i < N; i++) {
        pthread_join(tid[i], NULL);
    }

    printf("\nResult is %d\n", sum);
    return 0; 
}

void get_lock(int self) {
    flag[self] = 1; /* Want to enter waiting room */
    while (door_is_closed()) ; /* wait door to be open */

    flag[self] = 3;
    if (another_thread_want_to_enter()) {
        flag[self] = 2;
        while (wait_for_closing_door()) ;
    }

    flag[self] = 4;
    while (wait_finish(self)); /* wait thread with smaller tid to finish first */
}

void release_lock(int self) {
    while (inform_all_door_is_closed(self)) ;

    flag[self] = 0; /* exit waiting room */
}

bool door_is_closed() {
    for (int i = 0; i < N; i++) {
        if (flag[i] == 3 || flag[i] == 4) {
            return true;
        }
    }

    return false;
}

bool another_thread_want_to_enter() {
    for (int i = 0; i < N; i++) {
        if (flag[i] == 1) {
            return true;
        }
    }

    return false;
}

bool wait_for_closing_door() {
    for (int i = 0; i < N; i++) {
        if (flag[i] == 4) {
            return false;
        }
    }

    return true;
}

bool wait_finish(int j) {
    for (int i = 0; i <= j - 1; i++) {
        if (flag[i] != 0 && flag[i] != 1) {
            return true;
        }
    }

    return false;
}

bool inform_all_door_is_closed(int j) {
    j += 1;
    for(; j < N; j++) {
        if (flag[j] == 3 || flag[j] == 2) {
            return true;
        }
    }

    return false;
}

