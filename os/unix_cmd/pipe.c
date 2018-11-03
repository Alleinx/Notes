/**
 * pipe(int[2])
 * pipe[1] = write side
 * pipe[0] = read side
 * 
 * This program demonstrates how to create and use a pipe between 2 process
 * argv[1] -> write side
 * argv[2] -> read side. 
 * 
 * create pipe -> fork (Now child process has same pipe with its parents)
 * -> Parent process: close(pipe[1]), dup(pipe[0], 0), close(pipe[0]) //change stdin with pipe[0]
 * -> child process: close(pipe[0]), dup(pipe[1], 1), close(pipe[1]) //change stdout with pipe[1]
 */

#include <stdio.h>
#include <unistd.h>


int main(int argc, char* argv[]) {
    int pid;
    int i_pipe[2];

    if (argc != 3) {
        fprintf(stderr, "usage: pipe cmd1 cmd2\n");
        return -1;
    }

    /* create pipe here */
    if (pipe(i_pipe) == -1) {
        perror("Can't get pipe");
        return 1;
    }

    if ( (pid = fork()) == -1) {
        perror("fork failed.");
        return 1;
    }

    /* Now child and parent has same pipe */

    if (pid > 0) {
        close(i_pipe[1]); /* parent process read from pipe */

        /* Change stdin here */
        if (dup2(i_pipe[0], 0) == -1) {
            fprintf(stderr, "Error: Modify stdin of %s\n", argv[2]);
            return 1;
        }

        close(i_pipe[0]); /* now stdin of parent process is i_pipe[0] */
        execlp(argv[2], argv[2], NULL);

        /* execute when error occurs */
        fprintf(stderr, "Error: command not found: %s\n", argv[2]);
        return 1;
    } else {
        close(i_pipe[0]); /* child process read from pipe */

        if (dup2(i_pipe[1], 1) == -1) {
            fprintf(stderr, "Error: Modify stdout of %s\n", argv[1]);
            return 1;
        }

        close(i_pipe[1]); /* now stdout of child process is i_pipe[0] */
        execlp(argv[1], argv[1], NULL);

        /* execute when error occurs */
        fprintf(stderr, "Error: command not found: %s\n", argv[1]);
        return 1;
    }

    return 0;
}   