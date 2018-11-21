/**
 * Purpose: send messages to another terminal.
 * Method: open the other terminal for output then copy message from stdin to that terminal
 * 
 * Usage: write ttyname
 * use tty to get current terminal file.
 */

#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int fd;
    char buffer[BUFSIZ];

    char *name = ttyname(0);
    char *msg = "Message from ";
    int total_len = strlen(name) + strlen(msg);
    char *prompt_msg = (char *)malloc(total_len + 3);
    strcpy(prompt_msg, msg);
    strcat(prompt_msg, name);
    prompt_msg[total_len] = ':';
    prompt_msg[total_len + 1] = ' ';
    prompt_msg[total_len + 2] = '\0';

    if (argc != 2) {
        fprintf(stderr, "Usage: write ttyname\n");
        exit(1);
    }

    fd = open(argv[1], O_WRONLY); /* open for writing only */
    if (fd == -1) {
        perror(argv[1]);
        exit(1);
    }

    while (fgets(buffer, BUFSIZ, stdin) != NULL) {
        if (write (fd, prompt_msg, strlen(prompt_msg)) == -1) {
            break;
        }

        if (write(fd, buffer, strlen(buffer)) == -1) {
            break;
        }
    }

    close(fd);
    free(prompt_msg);

    return 0;
}