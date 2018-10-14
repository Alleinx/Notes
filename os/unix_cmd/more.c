#include <stdio.h>
#include <stdlib.h>

#define PAGELEN 24
#define LINELEN 512

void readFile(FILE*);
int see_more(FILE*);

int main(int argc, char *argv[]) {
    FILE *fp;

    if (argc == 1) {
        readFile(stdin); /* deal with pipe */
    } else {
        while(--argc) {
            fp = fopen(*(++argv), "r");
            if(fp) {
                readFile(fp);
                fclose(fp);
            } else {
                printf("Open failed.\n");
                return 1;
            }
        }
    }

    return 0;
}

void readFile(FILE *fp) {
    int current_num_of_lines = 0;
    int extra_line_amount;
    char buf[LINELEN];

    /* Read user input from keyboard in order to
       deal with redirection bug */
    FILE *fp_keyboard = fopen("/dev/tty", "r");
    if (fp_keyboard == NULL) 
        exit(1);

    while (fgets(buf, LINELEN, fp)) {
        if (current_num_of_lines == PAGELEN) {
            extra_line_amount = see_more(fp_keyboard);

            printf("\033[1A"); /* cursor move up 1 line. */

            if (extra_line_amount == 0) {
                break; 
            }

            current_num_of_lines -= extra_line_amount;
        }
        
        if (fputs(buf, stdout) == EOF) {
            exit(1);
        }

        current_num_of_lines++;
    }
}

int see_more(FILE *path) {
    int c;
    while( (c = getc(path)) != EOF) {
        switch (c) {
            case 'q' :
                return 0;
            case ' ' :
                return PAGELEN;
            case '\n':
                return 1;
        }
        
    }

    return 0;
}
