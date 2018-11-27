#include <stdio.h>
#include <pthread.h>
#include <stdbool.h>
#include <sys/types.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>


typedef struct job {
    void *(*process)(void *arg);
    void *arg;
    struct job *next;
}CThread_job;

typedef struct {
    pthread_mutex_t queue_lock;
    pthread_cond_t queue_ready;

    CThread_job *queue_head;
    bool is_closed;
    pthread_t *thread_id;
    int max_thread_num;
    int cur_queue_size;
}CThread_pool;

int pool_add_job (void *(*process) (void *arg), void *arg);
void *thread_routine (void *arg);
void *myprocess(void *arg);

static CThread_pool *pool = NULL;

void pool_init (int max_thread_num) {
    pool = (CThread_pool *)malloc(sizeof(CThread_pool));

    pthread_mutex_init(&(pool->queue_lock), NULL);
    pthread_cond_init(&(pool->queue_ready), NULL);

    pool->queue_head = NULL;
    pool->max_thread_num = max_thread_num;
    pool->cur_queue_size = 0;

    pool->is_closed = false;
    pool->thread_id = (pthread_t *)malloc(sizeof(pthread_t) * max_thread_num);

    for (int i = 0; i < max_thread_num; i++) {
        pthread_create(&(pool->thread_id[i]), NULL, thread_routine, NULL);
    }
} 

int pool_add_job (void *(*process) (void *arg), void *arg) {
    CThread_job *job = (CThread_job *)malloc(sizeof(CThread_job));
    job->process = process;
    job->arg = arg;
    job->next = NULL;

    pthread_mutex_lock(&(pool->queue_lock));
    CThread_job *member = pool->queue_head;

    if (member != NULL) {
        while (member->next != NULL) {
            member = member->next;
        }
        member->next = job;
    } else {
        pool->queue_head = job;
    }

    assert(pool->queue_head != NULL);
    pool->cur_queue_size++;
    pthread_mutex_unlock(&(pool->queue_lock));
    pthread_cond_signal(&(pool->queue_ready));

    return 0;
}

int pool_destroy() {
    if (pool->is_closed) {
        return -1;
    }

    pool->is_closed = true;

    pthread_cond_broadcast(&(pool->queue_ready));

    for (int i = 0; i < pool->max_thread_num; i++) {
        pthread_join(pool->thread_id[i], NULL);
    }

    free(pool->thread_id);

    CThread_job *head = NULL;
    while (pool->queue_head != NULL) {
        head = pool->queue_head;
        pool->queue_head = pool->queue_head->next;
        free(head);
    }

    pthread_mutex_destroy(&(pool->queue_lock));
    pthread_cond_destroy(&(pool->queue_ready));

    free(pool);;
    pool=NULL;

    return 0;
}

void *thread_routine(void *arg) {
    printf("Starting thread %u\n", (unsigned)pthread_self()); /* Here */
    while (true) {
        pthread_mutex_lock(&(pool->queue_lock));
        while (pool->cur_queue_size == 0 && !pool->is_closed) {
            printf("thread %u is waiting\n", (unsigned)pthread_self());
            pthread_cond_wait(&(pool->queue_ready), &(pool->queue_lock));
        }

        if (pool->is_closed) {
            pthread_mutex_unlock(&(pool->queue_lock));
            printf("thread %u will exit\n",(unsigned)pthread_self());
            pthread_exit(0);
        }

        printf("thread %u is starting to work\n", (unsigned)pthread_self());
        assert(pool->cur_queue_size != 0);
        assert(pool->queue_head != NULL);

        pool->cur_queue_size--;
        CThread_job *job = pool->queue_head;
        pool->queue_head = job->next;
        pthread_mutex_unlock(&(pool->queue_lock));
        (*(job->process))(job->arg);
        free(job);
        job = NULL;

    }

    pthread_exit(NULL);
}

int main(int argc, char* argv[]) {
    pool_init(3); /* 3 thread in thread pool*/

    int *job = (int *)malloc(sizeof(int) * 10);
    for (int i = 0; i < 10; i++) {
        job[i] = i;
        pool_add_job(myprocess, &job[i]);
    }

    sleep(5);
    pool_destroy();
    free(job);

    return 0;
}

void *myprocess(void *arg) {
    printf("thread %u working on task %d\n", (unsigned)pthread_self(), *(int*)arg);
    sleep(1);

    return NULL;
}