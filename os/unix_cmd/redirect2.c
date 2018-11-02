/**
 * Algorithm : open-close-dup-close 
 */

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main(void) {
    int fd;
    char buf[100];

    fd = open("/etc/passwd", O_RDONLY); /* fd should be 3 */

    close(0); /* stdin is closed */

    if (dup(fd) == -1) {
        fprintf(stderr, "Error");
    } 
    
    /* now 0 is also point to /etc/passwd */
    close(fd); /* close fd = 3 */

    for (int i = 0; i < 3; i++) {
        fgets(buf, 100, stdin);
        printf("%s\n", buf);
    }

    return 0;
}