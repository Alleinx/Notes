/**
 *  Semaphore values may be negative,
 *  whereas semaphore values are never negative 
 *  under the classical definition of semaphores with busy waiting.
 * 
 *  The list of waiting processes can be easily implemented by 
 *  a link field in each process control block.
 * 
 *  Each semaphore contains an intever value and a pointer to a list of PCBs.
 * 
 */



typedef struct {
    int value;
    struct process *list;
}semaphore;

void wait(semaphore *S) {
    S->value--;

    if (S->value < 0) {
        add_process_to_waiting_list(this);
        sleep(this);
    }
}

void signal(semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        P = remove_process_from_waiting_list();
        wakeup(P);
    }
}