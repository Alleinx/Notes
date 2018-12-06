#include <stdio.h>
#include <pthread.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct {
	pthread_mutex_t resource;
	pthread_mutex_t rmutex;
	int read_count;
    bool is_destoried;
}Lock;

static Lock * lock = NULL;

void lock_init() {
    printf("Initializing lock....\n");
    lock = (Lock *)malloc(sizeof(Lock));

    pthread_mutex_init(&(lock->resource), NULL);
    pthread_mutex_init(&(lock->rmutex), NULL);
    lock->read_count = 0;
    lock->is_destoried = false;
}

int lock_destroy() {
    if (lock->is_destoried) {
        return -1;
    }

    printf("Destroy lock...\n");
    lock->is_destoried = true;

    pthread_mutex_destroy(&(lock->resource));
    pthread_mutex_destroy(&(lock->rmutex));
    free(lock);
    lock = NULL;
    printf("Lock destroyed...\n");

    return 0;
}

int reader_lock() {
    pthread_mutex_lock(&(lock->rmutex));
    lock->read_count++;

    if (lock->read_count == 1) {
        pthread_mutex_lock(&(lock->resource));
    }

    pthread_mutex_unlock(&(lock->rmutex));

    return 0;
}

int reader_unlock() {
    pthread_mutex_lock(&(lock->rmutex));
    lock->read_count--;

    if (lock->read_count == 0) {
        pthread_mutex_unlock(&(lock->resource));
    }

    pthread_mutex_unlock(&(lock->rmutex));

    return 0;
}

int writer_lock() {
    pthread_mutex_lock(&(lock->resource));

    return 0;
}

int writer_unlock() {
    pthread_mutex_unlock(&(lock->resource));

    return 0;
}

