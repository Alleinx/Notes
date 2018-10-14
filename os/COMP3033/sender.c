#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <unistd.h>

int main(void) {
    const int SIZE = 4096;
    const char *name = "OS";
    const char *msg_0 = "Hello";
    const char *msg_1 = " world!";
    int fd;
    char *ptr;

    fd = shm_open(name, O_CREAT | O_RDWR, 0666);
    ftruncate(fd, SIZE);    

    ptr = (char*) mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    sprintf(ptr, "%s", msg_0);
    ptr += strlen(msg_0);
    sprintf(ptr, "%s", msg_1);
    ptr += strlen(msg_1);

    return 0;
}
