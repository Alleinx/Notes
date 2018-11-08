/* Compiler and processor may executes in random order, which causes problems */
/* Q1 : consider what's the expected output */
/* Q2 : what if flag = true finished before x = 100 ,then print x executes.*/
/* Q3 : what if print x finished before while() ? */

code(1) {
    while (!flag);
    print x;
}

code(2) {
    x = 100;
    flag = true;
}

<----------------------------------------------------------------->
/* Here are memory barrier mechanism provied by OS */

while (!flag)
    memory_barrier();
    /* Memory barrier here guarantee the value of flag is loaded before the value of x */
print x;

x = 100;
memory_barrier();
/* memory barrier here guarantee the value of x is assigned before flag */
flag = true;

/** 
 * consider Peterson's solution for synchronization,
 * we need to put a memory barrier between 
 * flag = true and turn = j to guarantee the algorithm generate expected solution.
 */


