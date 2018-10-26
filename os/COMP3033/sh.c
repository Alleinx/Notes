#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

/* inside unistd.h */
/* #define STDIN_FILENO 0 */
/* #define STDOUT_FILENO 1 */
/* #define STDERR_FILENO 2 */


#define SIZE 1024

void printPromptMessage(char *);
void printErrorMessage(char *);
void readUserInputTo(char *);


int main(void) {
    char buf[SIZE];
    int status;
    pid_t pid;
    char prompt[] = "Type a command: ";
    char forkFailed[] = "Fork Failed\n";
    char execFailed[] = "Child: exec failed\n";

    while(1) {
        printPromptMessage(prompt);
        readUserInputTo(buf);
        
        if (strcmp(buf, "exit") == 0) {
            break;
        }

        pid = fork();
        if (pid < 0) {
        /* Error */
            printErrorMessage(forkFailed);
            return 1;
        } else if (pid == 0) {
        /* Child process */
            execlp(buf, buf, NULL);
        /* Executed when exec failed */
            printErrorMessage(execFailed);
            return 1;
        } else {
        /* Parent process*/
            wait(&status);
        }
    }

    return 0;
}

void printPromptMessage(char *str) {
    write(STDOUT_FILENO, str, strlen(str));
}

void printErrorMessage(char *str) {
    write(STDERR_FILENO, str, strlen(str));
}

void readUserInputTo(char *buf) {
    read(STDIN_FILENO, buf, SIZE); /* Read user input */

    for (int i = 0; i < SIZE; i++) {
        if (buf[i] == '\n' || buf[i] == '\r') {
            buf[i] = '\0';
            break;
        }
    }
}
