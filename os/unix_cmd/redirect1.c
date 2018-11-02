/**
 * Algorithm :close-then-open 
 * First close(0) -> close stdin
 * then fd = open(file) -> now file is stdin, with fd = 0;
 * 
 * lowest-avaliable-fd:
 * fd : index of array that store a sequence of opening file. 
 * Unix use 0,1,2 to represent stdin,stdout,stderr.
 * Every time opening a file, Unix will assign lowest available value to fd.
 */

#include <stdio.h>  
#include <unistd.h>
#include <fcntl.h>

int main(void) {
    int fd;
    char buf[100];

    for (int i = 0; i < 3; i++) {
        fgets(buf, 100, stdin);
        printf("%s", buf);
    }

    close(0); /* close stdin */
    
    fd = open("/etc/passwd", O_RDONLY); /* fd = 0 now */
    if (fd != 0) {
        fprintf(stderr, "Couldn't open data as fd 0\n");
        return 1;
    }

    for (int i = 0; i < 3; i++) {
        fgets(buf, 100, stdin); /* now stdin is "/etc/passwd" */
        printf("%s", buf);
    }

    return 0;
}