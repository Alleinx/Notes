#include <stdio.h>

#define COUNT 10
#define BUFFERSIZE 2048

void display(FILE *fp);
void read_from_stdin(FILE *fp);

int main(int argc, char* argv[]) {
    FILE *file_ptr;
    int count_input_file = argc - 1;

    if (argc == 1) {
        read_from_stdin(stdin);
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
                return 1;
            }
        }
    }

    return 0;
}

void display(FILE *fp) {
    char buf[BUFFERSIZE];
    int count_line = COUNT;

    fseek(fp, -1, SEEK_END); /* Move fp to the last character of the file. */
    while (1) {
        /* count lines */
        if (fgetc(fp) == '\n') {
            --count_line; 
            if (count_line == 0) {
                break;
            }
        }

        /** Notes: since fgetc move fp to (p_previous + 1), 
         * so we need to move fp -2 from current position. */

        /** fseek return -1 value if exceed the begining of the file.
         *  If so, we need to move fp to the begining of the file.
         * 
         *  If we don't move fp to SEEK_SET, it will remain unchanged when 
         *  exceed the ***begining of the file*** (if exceed end of the file, fseek will return 0). 
         *  Notes: not at the position of SEEK_SET but SEEK_CUR
         * (if exceed end of the file, fp will point to SEEK_END?).
         */

        if (fseek(fp, -2, SEEK_CUR) != 0) {
            fseek(fp, 0, SEEK_SET);
            break;
        }
    }

    while(fgets(buf, BUFFERSIZE, fp)) {
        fputs(buf, stdout);
    }

}

void read_from_stdin(FILE *fp) {
    char buf[BUFFERSIZE];

    while (fgets(buf, BUFFERSIZE, fp)) {
        // fputs(buf, stdout); ???
    }
}