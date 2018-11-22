/* Solution to V1 or V2 could cause starvation. */
/* Here is a implementation of V2 reader-writer problem (reader starvation)*/

int read_count = 0;
int write_count = 0;
semaphore r_mutex = 1;
semaphore w_mutex = 1;
semaphore read_try = 1;
semaphore resource = 1;

/* reader start from here */
while (true) {
    wait(read_try);

    wait(r_mutex);
    read_count++;
    if (read_count == 1) {
        wait(resource);
    }
    signal(r_mutex);
    signal(read_try);

    /* read here */
    wait(r_mutex);
    read_count--;
    if (read_count == 0) {
        signal(resource);
    }
    signal(r_mutex);
}

/* writer start from here */
while (true) {
    wait(w_mutex);
    write_count++;
    if (write_count == 1) {
        wait(read_try);
    }
    signal(w_mutex);

    
    wait(resource);
    /* write here */
    signal(resource);

    wait(w_mutex);
    write_count--;
    if (write_count == 0) {
        signal(read_try);
    }

    signal(w_mutex);
}