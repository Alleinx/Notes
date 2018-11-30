#include <stdio.h>
#include <pthread.h>
#include <stdbool.h>
#include <sys/types.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>

#define DEBUG 0

/* Job link list */

typedef struct job {
    void *(*running_function)(void *arg); /* function pointer */
    void *arg; /* arg for runing function */
    struct job *next; /* next job */
    int job_id; /* indicate current job id */
}CThread_job;

typedef struct {
    pthread_mutex_t queue_lock; /* lock */
    pthread_cond_t queue_ready; /* signal */
    CThread_job *queue_head; /* point to the begining of job list */
    bool is_closed; /* indicate whether the thread pool is destroyed */
    pthread_t *thread_id; /* store all thread id */
    int max_thread_num; /* How many threads are created in this thread pool */
    int cur_queue_size; /* how many job are  in the waiting queue */
}CThread_pool;

int pool_add_job (void *(*running_function) (void *arg), void *arg);
void *_thread_routine (void *arg);
void *myprocess(void *arg); /* test running function */

static CThread_pool *pool = NULL; 

void pool_init (int max_thread_num) {
    if (DEBUG) {
        printf("Creating thread pool....\n");
        printf("Thread pool size: %d\n", max_thread_num);
    }
    pool = (CThread_pool *)malloc(sizeof(CThread_pool));

    pthread_mutex_init(&(pool->queue_lock), NULL);
    pthread_cond_init(&(pool->queue_ready), NULL);

    pool->queue_head = NULL;
    pool->max_thread_num = max_thread_num; 

    pool->cur_queue_size = 0;

    pool->is_closed = false;
    pool->thread_id = (pthread_t *)malloc(sizeof(pthread_t) * max_thread_num);

    for (int i = 0; i < max_thread_num; i++) {
        pthread_create(&(pool->thread_id[i]), NULL, _thread_routine, NULL);
    }
} 

void *_thread_routine(void *arg) {
    if (DEBUG) {
        printf("Launching thread: %u\n", (unsigned)pthread_self()); 
    }
    
    while (true) {
        pthread_mutex_lock(&(pool->queue_lock)); /* lock here */

        /* If no work to do, then call wait */
        while (pool->cur_queue_size == 0 && !pool->is_closed) { 
            if (DEBUG) {
                printf("Thread: %u is waiting...\n", (unsigned)pthread_self());
            }
            pthread_cond_wait(&(pool->queue_ready), &(pool->queue_lock));
        }

        if (pool->is_closed) {
            pthread_mutex_unlock(&(pool->queue_lock));
            if (DEBUG) {
                printf("Thread %u closed...\n",(unsigned)pthread_self());
            }
            pthread_exit(0);
        }

        /* work here */
        if (DEBUG) {
            printf("Thread: %u starts working...\n", (unsigned)pthread_self());
        }
        assert(pool->cur_queue_size != 0);
        assert(pool->queue_head != NULL);
        pool->cur_queue_size--;

        CThread_job *job = pool->queue_head; /* get a job from waiting queue */
        pool->queue_head = job->next; /* modify pointer */

        pthread_mutex_unlock(&(pool->queue_lock)); /* unlock here */
        (*(job->running_function))(job->arg); /* run function */
        
        free(job); 
        job = NULL;

    }

    /* Never reach here */
    fprintf(stderr, "Error! System shutting down...\n");
    pthread_exit(NULL);
}

int pool_add_job (void *(*running_function) (void *arg), void *arg) {
    CThread_job *job = (CThread_job *)malloc(sizeof(CThread_job));

    job->running_function = running_function;
    job->arg = arg;
    job->next = NULL;
    job->job_id = *(int*)arg;

    pthread_mutex_lock(&(pool->queue_lock));
    CThread_job *member = pool->queue_head;

    if (member != NULL) {
        while (member->next != NULL) {
            member = member->next;
        }

        member->next = job; /* find the last place add job here */
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

    printf("Closing thread pool...\n");
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
    printf("Thread pool closed.\n");
    return 0;
}

/* Test here */
/*
int main(int argc, char* argv[]) {
    pool_init(NUMBER_OF_THREAD); // NUMBER_OF_THREAD threads in thread pool // 

    int *job = (int *)malloc(sizeof(int) * NUMBER_OF_JOB); // assign NUMBER_OF_JOB jobs here //

    for (int i = 0; i < NUMBER_OF_JOB; i++) {
        job[i] = i+1;
        pool_add_job(running_function, &job[i]);
    }

    
    sleep(5); // after 5 seconds all thread die //
    
    pool_destroy();
    free(job);

    return 0;
}
*/

