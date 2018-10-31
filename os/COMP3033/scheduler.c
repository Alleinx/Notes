#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct{
    int process_index; /* indicates process index (start from 1) */
    int burst_time; /* store process burst time (unchanged) */
    int period; /* store process period (unchanged) */
    int next_ddl; /* store next ddl time */
    int remaining_time; /* How long this process could run */
    int cpu_burst_amount; /* how many times cpu bursts */
    int running_time; /* total running time */
    int idle_time; /* total time waiting for next period arrivial */
}process, *process_ptr;

int gcd(int a, int b);
int lcm(int a[], int num);

void scheduler(process_ptr, int);
int select_next_process(process_ptr, int,  int);
bool could_run(process_ptr);

void missed_ddl(process_ptr, int, int, int *);
void normal_run(process_ptr, int*, int, process_ptr, int);
void preempted(process_ptr, process_ptr, int, int, int);
void finish(process_ptr, int, int*);
void update(process_ptr, int,int);

void cal_total_waiting_time(process_ptr, int *, int, int);
int total_cpu_bursts(process_ptr, int);

int main(void) {
    char prompt_msg_number_of_process[] = "Enter the number of processes to schedule: ";
    char prompt_msg_burst_time[] = "Enter the burst time of process ";
    char prompt_msg_period_time[] = "Enter the period of process ";
    int number_of_process = 0;
    int temp;
    process_ptr process_container;

    /* init_schedular */
    printf("%s",prompt_msg_number_of_process);
    scanf("%d", &number_of_process);

    process_container = (process_ptr) malloc(sizeof(process) * number_of_process);

    for (int i = 0; i < number_of_process; i++) {
        printf("%s%d: ", prompt_msg_burst_time, i + 1);
        scanf("%d", &temp);
        process_container[i].process_index = i+1; /* process_index starts from 1 */
        process_container[i].burst_time = temp; 
        process_container[i].remaining_time = temp;

        printf("%s%d: ", prompt_msg_period_time, i + 1);
        scanf("%d", &temp);
        process_container[i].period = temp;
        process_container[i].next_ddl = temp;
        process_container[i].idle_time = 0;
        process_container[i].running_time = 0;
        process_container[i].cpu_burst_amount = 0;
    }

    scheduler(process_container, number_of_process);
   
    free(process_container);
    return 0;
}

void scheduler(process_ptr ptr, int number_of_process) {
    int cur_time = 0; /* system current time */
    int maxTime;
    int process_period_arr[number_of_process]; /* for calculating maxTime */

    int next_process_index; /* for judging if preempted occured. */
    int last_process_index;

    int waiting_time = 0; /* Total waiting time */
    int total_bursts = 0;

    /* calculate maxTime */
    for (int i = 0; i < number_of_process; i++) {
        process each = ptr[i];
        process_period_arr[i] = each.period;
    }
    maxTime = lcm(process_period_arr, number_of_process);

    /* init next_process_index and last_process_index*/
    next_process_index = select_next_process(ptr, number_of_process, maxTime);
    last_process_index = next_process_index;

    while (cur_time < maxTime) {
        /**
         * Select next process to run
         * if (could run) -> run
         * else -> wait
         * */

        next_process_index = select_next_process(ptr, number_of_process, maxTime);

        if (next_process_index == -1) {
            /* wait here */
            cur_time += 1;

            for (int i = 0; i < number_of_process; i++) {
                ptr[i].idle_time++;
            }
        } else {
            /* run here */
            missed_ddl(&ptr[next_process_index], cur_time, maxTime, &waiting_time);
            preempted(&ptr[last_process_index], &ptr[next_process_index],cur_time,last_process_index,next_process_index);
            normal_run(&ptr[next_process_index], &cur_time, last_process_index, ptr, number_of_process);
            finish(&ptr[next_process_index], cur_time, &waiting_time);
        }

        /* update process status here */
        update(ptr, cur_time, number_of_process);
        /* store last_running_process_index; */
        last_process_index = next_process_index;
    }

    total_bursts = total_cpu_bursts(ptr, number_of_process);
    cal_total_waiting_time(ptr, &waiting_time, maxTime, number_of_process);
    printf("%d: MaxTime reached\n", maxTime);
    printf("Sum of all waiting time: %d\n", waiting_time);
    printf("Number of CPU bursts: %d\n",total_bursts);
    printf("Average Waiting Time: %.6f\n", (float)waiting_time / total_bursts);
}

/**
 * select_next_process
 * DESCRIPTION : This function find the next process to run. If there exist process that could run, 
 * return it's process_index.Otherwise, return -1 to indicate waiting is required.
 * 
 * RETURN : 
 *      > process_index : if find a process could run.
 *      > -1            : need to wait.
 */

int select_next_process(process_ptr ptr, int number_of_process, int maxTime) {
    /** Next ddl could exceed maxTime, so we times a number here to prevent this happening
     *  Otherwise, this function will get run solution.
     */
    int earliest_ddl = maxTime * 10; 

    int next_process_index = -1; 

    for (int i = 0; i < number_of_process; i++) {
        if (ptr[i].next_ddl < earliest_ddl && could_run(&ptr[i])) {
            earliest_ddl = ptr[i].next_ddl;
            next_process_index = ptr[i].process_index - 1;
        }
    }

    return next_process_index;
}

/**
 * could_run
 * DESCRIPTION : This function check if the given process could run.
 */

bool could_run(process_ptr process) {
    return process->remaining_time > 0;
}

/**
 * normal_run
 * DESCRIPTION : This function run the given process. Besides, it also update other processes's idle_time;
 */

void normal_run(process_ptr process, int* cur_time, int last_run, process_ptr container, int number_of_process) {
    /* print msg here */
    if (*cur_time == 0 || last_run != process->process_index - 1) {
        printf("%d: process %d starts\n", *cur_time, process->process_index);
    }

    /* update running process's status */
    process->remaining_time -= 1;
    process->running_time++;

    /* update other processes' idle_time */
    for (int i = 0; i < number_of_process; i++) {
        if (i != process->process_index - 1) {
            /* update other processes' idle_time  */
            if (container[i].remaining_time <= 0) {
                container[i].idle_time++;
                /** if the process_i is already finished, then process_i.idle_time++, which
                 *  means it's waiting for the next process to arrive.
                 */
            }
        }
    }

    *cur_time += 1; /* update system current time */
}

/**
 * missed_ddl
 * DESCRIPTION : This function check if the process missed the ddl;
 * 
 * > when we meet the ddl, check if the remaining time > 0;
 * If so, the given process exceeds its ddl.
 */

void missed_ddl(process_ptr process, int cur_time, int max_time, int *wait_time) {
    if (process->remaining_time - 1 > 0 && cur_time + 1 < max_time && cur_time + 1 == process -> next_ddl) {
        /** 
         * remaing_time -1 and cur_time + 1 here because we put this function before normal_run.
         */

        printf("%d: process %d missed deadline (%d ms left)\n", cur_time + 1, process->process_index, process->remaining_time - 1);
    }
}

/**
 * preempted
 * DESCRIPTION : This function check if there is a preemption occured;
 * 
 * > If last running process != current running process 
 * and last process could still run ,then, there is a preemption.
 */
void preempted(process_ptr last_process, process_ptr next_process, int cur_time, int last_run, int next_run) {
    /* If last operation is wait, just return */
    if (last_run == -1) {
        return;
    }

    if (last_run != next_run && last_process->remaining_time > 0) {
        printf("%d: process %d preempted!\n", cur_time, last_process->process_index); 
    }
}

/**
 * finish
 * DESCRIPTION : This function terminate a process;
 */
void finish(process_ptr process, int cur_time, int *wait_time) {
    if (process->remaining_time == 0) {
        printf("%d: process %d ends\n", cur_time, process->process_index);
    }
}

/**
 * update
 * DESCRIPTION : This function update process status;
 * 
 * > Check all the processes and update their status if current time = process_i.next_ddl;
 */
void update(process_ptr process, int cur_time, int number_of_process) {
    for (int i = 0; i < number_of_process; i++) {
        if (cur_time == process[i].next_ddl) {
            process[i].next_ddl += process[i].period;

            /* remaining_time += burst_time here because the given process may exceed it's ddl */
            process[i].remaining_time += process[i].burst_time;

            process->cpu_burst_amount++;
        }
    }
}

/**
 * cal_total_waiting_time
 * DESCRIPTION : This function calculate total waiting time;
 * 
 * Total waiting time = (maxTime * number_of_process) - each process's running time and idle time;
 */

void cal_total_waiting_time(process_ptr ptr, int *waiting_time, int max_time, int number_of_process) {
    *waiting_time = number_of_process * max_time;
    int temp;
    for (int i = 0; i < number_of_process; i++) {
        temp = (ptr[i].running_time + ptr[i].idle_time);
        *waiting_time -= temp;
    }
}

/**
 * total_cpu_bursts
 * DESCRIPTION : This function calculate total cpu bursts amount;
 */

int total_cpu_bursts(process_ptr ptr, int number_of_process) {
    int sum = 0;
    for (int i = 0; i < number_of_process; i++) {
        sum += ptr[i].cpu_burst_amount;
    }

    return sum;
}

int lcm(int a[], int num) {
    int result = 1;
    for (int i = 0; i < num; i++) {
        result *= a[i] / gcd(result, a[i]);
    }

    return result;
}

int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}