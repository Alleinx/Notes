/* DiningPhilosophers problem with dead-lock free but not stravation-free */
/* Monitor : could only get 0 or 2 forks at the same time */
monitor Dining_Philosophers {
    enum{THINKING, HUNGRY, EATING}state[5];
    condition self[5]; /* store processes' status */

    void pickUp(int i) {
        state[i] = HUNGRY;
        test(i); /* test if could eat */
        
        if (state[i] != EATING) {
            self[i].wait();
        }
    }

    void putDown(int i) {
        state[i] = THINKING;
        test((i + 4) % 5); /* inform its neighbor */
        test((i + 1) % 5);
    }

    void test(int i) {
        if ( (state[(i + 4) % 5] != EATING) && (state[(i + 1) % 5] != EATING) && state[i] == HUNGRY) {
            state[i] = EATING;
            self[i].signal();
        }
    }

    init() {
        for (int i = 0; i < 5; i++) {
            state[i] = THINKING;
        }
    }
}