#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


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
            if( (fp = fopen(*(++argv), "r")) != NULL) {
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
    char buf[LINELEN];
    int num_of_lines = 0;
    int reply;
    FILE *fp_keyboard = fopen("/dev/tty", "r");
    /* Read from keyboard */
    if (fp_keyboard == NULL)
        exit(1);

    while (fgets(buf, LINELEN, fp)) {
        if (num_of_lines == PAGELEN) {
            reply = see_more(fp_keyboard);
            
            if (reply == 0) {
                break; 
            }

            num_of_lines -= reply;
        }
        if (fputs(buf, stdout) == EOF) {
            exit(1);
        }

        num_of_lines++;
    }
}


int see_more(FILE *path) {
    int c;
    while( (c = getc(path)) != EOF) {
        switch (c) {
            case 'q' :
                return 0;
                break;
            case ' ' :
                return PAGELEN;
                break;
            case '\n':
                return 1;
                break;
        }
        
    }

    return 0;
}
