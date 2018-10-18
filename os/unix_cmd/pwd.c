#include <stdio.h>
#include <sys/stat.h>
#include <dirent.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#define inode_number ino_t

inode_number get_inode_number(char *); /* return i-node number of a file */
void print_path_to(inode_number);
void find_file_name_for_inode_number(inode_number, char*, int);

int main(void) {
    print_path_to(get_inode_number("."));
    printf("\n");

    return 0;
}

void print_path_to(inode_number inode) {
    inode_number  next_inode;
    char name_container[BUFSIZ];

    if (get_inode_number("..") != inode) { // loop until root of UNIX file system.
        /* in Unix file system, the root node of whole file system has property . = .. */

        chdir(".."); /* go to parent dir */

        find_file_name_for_inode_number(inode, name_container, BUFSIZ);

        next_inode = get_inode_number(".");
        print_path_to(next_inode);

        printf("/%s", name_container);
    }
}

void find_file_name_for_inode_number(inode_number inode_to_find, char *namebuf, int buflen) {
    DIR *dir_ptr;
    struct dirent *dirent_ptr;
    
    dir_ptr = opendir(".");
    if (dir_ptr == NULL) {
        perror(".");
        exit(1);
    }

    while( (dirent_ptr = readdir(dir_ptr)) != NULL) {
        if (dirent_ptr -> d_ino == inode_to_find) {
            strncpy(namebuf, dirent_ptr->d_name, buflen);
            namebuf[buflen-1] = '\0';
            closedir(dir_ptr);
            return;
        }
    }

    fprintf(stderr, "Error looking for inum %llu\n", inode_to_find);
    exit(1);
}

inode_number get_inode_number(char* fname) {
    struct stat info;
    if ( stat(fname, &info) == -1) {
        fprintf(stderr, "Cannot stat");
        perror(fname);
        exit(1);
    }

    return info.st_ino;
}


