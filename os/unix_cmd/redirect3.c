/**
 * After calling fork(), child process derives fds from its parent process.
 * Before child process calling exec(), performing redirect.
 * 
 * This program show how to redirect output for another program.
 * idea: fork -> inside the child process: redirect -> exec();
 */

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>

int main(void) {
    int pid;
    int fd;

    if ( (pid = fork()) == -1) {
        perror("fork");
        return 1;
    }

    if (pid == 0) {
        /* Child here */
        close(1); /* close stdout */
        fd = creat("redirect.txt", 0644); /* open; now fd = 1(stdout) */
        execlp("who", "who", NULL);

        /* Execute if an error occured */
        perror("execlp");
        return 1;
    } else {
        wait(NULL);
        printf("Finish\n");
    }

    return 0;
}