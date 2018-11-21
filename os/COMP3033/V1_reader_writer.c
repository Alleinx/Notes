/* V1: reader-writer problem : no reader should wait for other reader to finish.*/
/* V2: reader-writer problem : once a writer is ready, the writer perform its write as soon as possible */
/* Solution to V1 or V2 could cause starvation. */
/* Here is a implementation of V1 reader-writer problem (writer starvation)*/



/* shared by reader and writer */
semaphore rw_mutex = 1; /* mutual exclusion for writers, first or last reader that enters or exit the critical section.*/
semaphore mutex = 1; /* mutual exclusion for update the value of read_count */
int read_count = 0; /* count currently how many processes are currently reading the object */

/* writer start from here */
while (true) {
    wait(rw_mutex);

    /* perform writing here */

    signal(rw_mutex);
}

/* reader start from here */
while (true) {
    /* Try read */
    wait(mutex);

    read_count++;
    if (read_count == 1) {
        wait(rw_mutex); 
        /**
         *  starvation for writer here 
         *  If a reader get rw_mutex, then writer must wait until all all reader finish their work.
         * */
    }

    signal(mutex);

    /* read here */

    wait(mutex);
    read_count--;
    if (read_count == 0) {
        signal(rw_mutex);
    }

    signal(mutex);
}