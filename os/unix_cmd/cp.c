#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

#define BUFSIZE 2048
#define COPYMODE 0644

void err(char *, char *);

int main(int argc, char* argv[]) {
    int in_fd, out_fd, read_chars_len;
    char buf[BUFSIZE];

    if (argc != 3) {
        fprintf(stderr, "usage: %s source destination\n", *argv);
        return 1;
    }

    if ( (in_fd = open(argv[1], O_RDONLY)) == -1)
        err("Open source file failed ", argv[1]);
    
    if ( (out_fd = creat(argv[2], COPYMODE)) == -1)
        err("Write destination file failed ", argv[2]);

    while ( (read_chars_len = read(in_fd, buf, BUFSIZ))) {
        if (write(out_fd, buf, read_chars_len) != read_chars_len)
            err("Write error to ", argv[2]);
    }   

    if (read_chars_len == -1)
        err("Read error from ", argv[1]);

    if ( close(in_fd) == -1 || close(out_fd) == -1 ) 
        err("Error closing files ", "");

    return 0;
}

void err(char *s1, char *s2) {
    fprintf(stderr, "Error: %s", s1);
    perror(s2);
    exit(1);
}
