#include <stdio.h>
#include <dirent.h>
#include <sys/types.h>

void ls(char []);

int main(int argc, char* argv[]) {
    if (argc == 1) {
        ls(".");
    } else {
        while (--argc) {
            ls(* ++argv);
        }
    }

    return 0;
}

void ls(char dirname[]) {
    DIR * dir_ptr;
    struct dirent * dirent_ptr;

    if ( !(dir_ptr = opendir(dirname)) ) {
        fprintf(stderr, "ls : cannot open %s\n", dirname);
    } else {
        while ( (dirent_ptr = readdir(dir_ptr)) ) {
            printf("%s\n", dirent_ptr->d_name);
        }

        closedir(dir_ptr);
    }
}