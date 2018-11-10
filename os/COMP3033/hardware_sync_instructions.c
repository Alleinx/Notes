/* Test and set mechanism: */
bool test_and_set(bool *target) {
    bool rv = *target;
    *target = true;

    return rv;
}

do {
    while (test_and_set(&lock))
        ;

    /* critical section */
    lock = false;

    /* remainder section */
} while (true);


/* Compare and swap mechanism */
int compare_and_swap(int *value, int expected, int new_value) {
    int temp = *value;

    if (*value == expected) {
        *value = new_value;
    }

    return temp;
}

while (true) {
    waiting[i] = true;
    key = 1;

    while (waiting[i] && key == 1) {
        key = compare_and_swap(&lock, 0, 1);
    }

    waiting[i] = false;
    /* critical section */

    /* Following code provide bounded waiting. */
    j = (i + 1) % n;
    /* check if there have processes that want to enter critical section */
    while ( (j != i) && !waiting[j]) {
        j = (j + 1) % n;
    }

    if (j == i) {
        lock = 0;
        /* if no process want to enter critical section */
    } else {
        waiting[j] = false;
        /* give lock to the first process that want to enter the critical section */
    }

    /* remainder section */
}