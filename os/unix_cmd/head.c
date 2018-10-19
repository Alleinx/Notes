#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define COUNT 10
#define BUFFERSIZE 2048

void display(FILE *);

int main(int argc, char* argv[]) {
    FILE *file_ptr;
    int count_input_file = argc - 1;

    if (argc == 1) {
        display(stdin);
    } else {
        while (--argc) {
            file_ptr = fopen(*(++argv), "r+");
            if (file_ptr) {
                if (count_input_file > 1) {
                    printf("\n==> %s <==\n", *argv);
                }
                display(file_ptr);
                fclose(file_ptr);
            } else {
                perror(*argv);
                exit(1);
            }
        }
    }

    return 0;
}

void display(FILE *fp) {
    char buf[BUFFERSIZE];
    int count_line = COUNT;
    int str_len;

    while (fgets(buf, BUFFERSIZE, fp)) {
        str_len = strlen(buf);
        
        for (int i = 0; i < str_len; i++) {
            if (buf[i] == '\n') {
                count_line--;
                if (count_line == 0) {
                    buf[i + 1] = '\0';
                    break;
                }
            } 
        } 

        fputs(buf, stdout);

        if (count_line == 0) {
            /** if already print COUNT line, stop
             *  Note: use return here, not exit(); otherwise, can't read more than 1 file */
            return;
        }
    }
}
