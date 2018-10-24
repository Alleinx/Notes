/**
 * Q1 : Does the handler stay in effect after a signal arrives
 * Q2 : What if a signalX arrives while handling signalX ?
 * Q3 : What if signalX arrives while handling signalY ?
 * Q4 : What happens to read() when a signal arrives?
 * purpose : Test implementation on this computer.
 * 
 * Test case:
 * 1.^C ^C ^C ^C //program exit?
 * 2.^\ ^C ^\ ^C 
 * 3. hello ^c return
 * 4.hello return ^c
 * 5. ^\ ^\ hello ^c
 */

#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

void interrupt_handler(int);
void quit_handler(int);

#define INPUTLEN 100

int main(int argc, char *argv[]) {
    int nchars;
    char input[INPUTLEN];

    signal(SIGINT, interrupt_handler);
    signal(SIGQUIT, quit_handler);

    do {
        printf("\nType a message\n");
        nchars = read(0, input, (INPUTLEN - 1));
        if (nchars == -1) {
            perror("Read input error.");
        } else {
            input[nchars] = '\0';
            printf("You typed: %s\n", input);
        }
    } while ( strncmp(input, "quit", 4) != 0);

    return 0;
}

void interrupt_handler(int s) {
    printf("Received signal %d.. waiting\n", s);
    sleep(2);
    printf("Leaving interrupt handler.\n");
}

void quit_handler(int s) {
    printf("Received signal %d.. waiting\n", s);
    sleep(3);
    printf("Leaving quit handler.\n");
}
