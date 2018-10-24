#include <stdio.h>
#include <signal.h>
#include <sys/time.h>
#include <unistd.h>
#include <stdlib.h>

void countdown(int);
int set_ticker(int);

int main(void) {

    signal(SIGALRM, countdown); /* countdonw will be invoked when receive signal from kernel*/

    /**
     *  1000 = real time timer; 
     *  < 1000 = accelerated real time timer;
     *  > 1000 = slower real time timer.
     */

    if (set_ticker(1000) == -1) { 
        perror("set_ticker");
    } else {
        while (1) {
            pause();
        }
    }

    return 0;
}

void countdown(int signum) {
    static int num = 10;
    printf("%d...", num--);

    /**
     *  use fflush to display information every time receive signal
     *  if not, messages will be printed out when the clock stops.
     */
    fflush(stdout);  

    if (num < 0) {
        printf("DONE!\n");
        exit(0);
    }
}


int set_ticker(int n_msec) {
    struct itimerval new_timeset;
    long n_sec, n_usec;

    n_sec = n_msec / 1000; // 1 sec = 1000 milliseconds;
    n_usec = (n_msec % 1000) * 1000L; // 1 microsecond = 10^3 milliseconds;

    new_timeset.it_interval.tv_sec = n_sec;
    new_timeset.it_interval.tv_usec = n_usec;

    new_timeset.it_value.tv_sec = n_sec;
    new_timeset.it_value.tv_usec = n_usec;

    return setitimer(ITIMER_REAL, &new_timeset, NULL);
}
