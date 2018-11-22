/* Solution to V1 or V2 could cause starvation. */
/* Here is a implementation of V2 reader-writer problem (reader starvation)*/

int read_count = 0;
int write_count = 0;
semaphore r_mutex = 1; /* provide mutual exclusion for r_count */
semaphore w_mutex = 1; /* provide mutual exclusion for w_count */
semaphore read_try = 1;
semaphore resource = 1;

/* reader start from here */
while (true) {
    wait(read_try); /* try to enter critical section */

    wait(r_mutex); /* try to report yourself as a reader */
    read_count++;
    if (read_count == 1) {
        wait(resource); /* if first reader, lock the resource */
    }

    signal(r_mutex);
    signal(read_try);

    /* read here */

    wait(r_mutex); 
    read_count--;
    if (read_count == 0) {
        signal(resource); /* if last reader, unlock the resource */
    }

    signal(r_mutex);
}

/* writer start from here */
while (true) {
    wait(w_mutex);

    write_count++;
    if (write_count == 1) {
        wait(read_try); /* if first writer, lock all readers */
    }

    signal(w_mutex); 

    wait(resource); 

    /* write here */

    signal(resource);

    wait(w_mutex);
    write_count--;
    if (write_count == 0) {
        signal(read_try); /* if last writer, unlock all readers */
    }

    signal(w_mutex);
}