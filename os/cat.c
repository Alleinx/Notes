#include <stdio.h>
#include <stdlib.h>

#define BUFSIZE 2048

void readFile(FILE *);

int main(int argc, char const *argv[]) {
    FILE *fp;

    if (argc == 1) {
        readFile(stdin);
    } else {
        while(--argc) {
            fp = fopen(*(++argv), "r+"); /* r+ for detecting if open a file or a directory */
            if (fp) {
                readFile(fp);
                fclose(fp);
            } else {
                fprintf(stderr, "Open failed: ");
                perror(*argv); 
            }
        
        }
    }

    return 0;
}

void readFile(FILE *fp) {
    char buf[BUFSIZE];

    while (fgets(buf, BUFSIZ, fp)) {
        fputs(buf, stdout);
    }
}
