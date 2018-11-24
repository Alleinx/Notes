/* auto-append mode ->atomic write operation, incase of race condition */
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main(void) {
    int s;
    int fd;
    char *msg;
    s = fcntl(fd, F_GETFL); /* fcntl() provide control for file descriptors */
    s |= O_APPEND; /* With O_APPEND, lseek and write will be binded together and become a atomic operation */

    int result = fcntl(fd, F_SETFL, s); /* set the file descriptor flags to arg */
    if (result == -1) {
        perror("Setting Append");
    } else {
        write(fd, &msg, sizeof(msg));
    }

    return 0;
}