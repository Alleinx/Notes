#include <stdio.h>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <time.h>
#include <string.h>
#include <pwd.h>
#include <grp.h>

/* BUG: ls /tmp */

void ls(char []);
void do_stat(char *);
void show_file_info(char *, struct stat*);
void mode_to_letters(int, char []);
char *uid_to_name(uid_t);
char *gid_to_name(gid_t);

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
            do_stat(dirent_ptr->d_name);
        }

        closedir(dir_ptr);
    }
}

void do_stat(char *file_name) {
    struct stat info;
    if ( stat(file_name, &info) == -1) {
        perror(file_name);
    } else {
        show_file_info(file_name, &info);
    }
}

void show_file_info(char *file_name, struct stat *info_p) {
    char modestr[11]; /* restore mode information */

    mode_to_letters(info_p -> st_mode, modestr);
    printf("%s", modestr); /* mode information */
    printf("%2d ", (int) info_p -> st_nlink); /* number of hard links to the file */
    printf("%-4s ", uid_to_name(info_p -> st_uid)); /* user id */
    printf("%-4s ", gid_to_name(info_p -> st_gid)); /* group id */
    printf("%4ld ", (long)info_p -> st_size); /* file size */
    printf("%4s", 4 + ctime(&(info_p -> st_mtime))); /* last modify time */
    printf("%s\n", file_name); /* file name */
}

void mode_to_letters(int mode, char str[]) {
    strcpy(str, "----------");
    if (S_ISDIR(mode)) str[0] = 'd';
    if (S_ISCHR(mode)) str[0] = 'c';
    if (S_ISBLK(mode)) str[0] = 'b';

    if (mode & S_IRUSR) str[1] = 'r';
    if (mode & S_IWUSR) str[2] = 'w';
    if (mode & S_IXUSR) str[3] = 'x';

    if (mode & S_IRGRP) str[4] = 'r';
    if (mode & S_IWGRP) str[5] = 'w';
    if (mode & S_IXGRP) str[6] = 'x';

    if (mode & S_IROTH) str[7] = 'r';
    if (mode & S_IWOTH) str[8] = 'w';
    if (mode & S_IXOTH) str[9] = 'x';
}

char *uid_to_name(uid_t uid) {
    struct passwd *pw_ptr;
    static char numstr[10];

    if ( !(pw_ptr = getpwuid(uid)) ) {
        sprintf(numstr, "%d", uid);
        return numstr;
    } 
    
    return pw_ptr -> pw_name;
}

char *gid_to_name(gid_t gid) {
    struct group *grp_ptr;
    static char numstr[10];
    
    if ( !(grp_ptr = getgrgid(gid)) ) {
        sprintf(numstr, "%d", gid);
        return numstr;
    }

    return grp_ptr -> gr_name;
}