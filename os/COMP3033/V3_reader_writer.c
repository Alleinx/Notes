/**
 * V3: No thread shall be allowed to starve;
 * The operation of obtaining a lock on the shared data will always
 * terminate in a bounded amount of time.
 * 
 */

int read_count = 0;
Semaphore resource = 1; /* controls (read & write) access to the resource */
Semaphore read = 1; 
Semaphore service_queue = 1; /* FAIRNESS : preserves ordering of requests (signaling must be FIFO) */

void writer() {
    wait(service_queue); /* try to enter the service queue (FIFO) */
    wait(resource); /* wait for resource, get when other writers and readers all finish their job*/
    signal(service_queue);

    /* write here */
    signal(resource);
}

void reader() {
    wait(service_queue);

    wait(read); /* mutual exclusion for modify read_count */
    if (read_count == 0) {
        wait(resource);
    }
    read_count++;
    signal(read);

    signal(service_queue);

    /* read here */

    wait(read);
    read_count--;
    if (read_count == 0) {
        signal(resource); /* unlock resource after all readers finish reading */
    }
    signal(read);
}