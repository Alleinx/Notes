#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define WHITE 0
#define GRAY  1
#define FILE_LENGTH 128 /* limit of input file_name's length */

typedef struct {
    int color;
    int *adjacent_vertex_list; /* adjacency list of vertex */
    int next_adjacent_index; /* indicate the next element in the adjacency list */
    int vertex_index;
}vertex, *vertex_ptr;

int convert_to_int(char);
void reset_status(vertex_ptr, int);
void free_memory(vertex_ptr, int);
int get_from_adjacent_list(vertex*, int);

void perform_DFS(vertex_ptr, int);
void DFS_visit(vertex*, int, vertex_ptr);
void perform_BFS(vertex_ptr, int);
void BFS_visit(vertex*, int, vertex_ptr);
void perform_topological_sorting(vertex_ptr, int);
void topological_visit(vertex *, int, vertex_ptr, int*, int *);

int main(void) {
    char file_name[FILE_LENGTH];
    int read_char;
    int number_of_vertex = 0;
    vertex_ptr graph;
    FILE *fp;

    while (true) {
        /* read user input here */
        printf("Input the name of the graph file: ");
        if (scanf("%s", file_name) == EOF) {
            return 0;
        }

        /* open file here */
        fp = fopen(file_name, "r");
        if (fp == NULL) {
            perror(file_name);
            continue;
        }

        /* init here */
        number_of_vertex = convert_to_int(getc(fp));
        graph = (vertex_ptr) malloc(sizeof(vertex) * number_of_vertex);
        for (int i = 0; i < number_of_vertex; i++) {
            graph[i].vertex_index = i;
            graph[i].adjacent_vertex_list = (int *) malloc(sizeof(int) *number_of_vertex);
        }
        
        /* read data into graph*/
        for (int i = 0; i < number_of_vertex; i++) {
            for (int counter = 0; counter < number_of_vertex;) {
                read_char = getc(fp);
                if (read_char == '0' || read_char == '1') {
                    graph[i].adjacent_vertex_list[counter] = convert_to_int(read_char);
                    counter++;
                }
            }
        }

        
        perform_DFS(graph, number_of_vertex);
        perform_BFS(graph, number_of_vertex);
        perform_topological_sorting(graph, number_of_vertex);

        free_memory(graph, number_of_vertex);
        fclose(fp);
    }
    return 0;
}

/**
 * convert_to_int
 * Description: This function convert given char type input to int.
 * E.x.
 * '1' -> 1
 * '0' -> 0
 */
int convert_to_int(char c) {

    if (c > '9' || c < '0') {
        fprintf(stderr, "Error: invalid number of vertex\n");
        exit(1);
    }

    return c - '0';
}

void free_memory(vertex_ptr ptr, int number_of_vertex) {
    for (int i = 0; i < number_of_vertex; i++) {
        free(ptr[i].adjacent_vertex_list);
    }

    free(ptr);
}

void reset_status(vertex_ptr ptr, int number_of_vertex) {
    for (int i = 0; i < number_of_vertex; i++) {
        ptr[i].color = WHITE;
        ptr[i].next_adjacent_index = 0;
    }
}

void perform_DFS(vertex_ptr graph, int number_of_vertex) {
    reset_status(graph, number_of_vertex);

    printf("Perform DFS:\n");

    for (int i = 0; i < number_of_vertex; i++) {
        if (graph[i].color == WHITE) {
            DFS_visit(&graph[i], number_of_vertex, graph);
        }
    }
    printf("\n");
}

void DFS_visit(vertex* vertex, int number_of_vertex, vertex_ptr adjacent_list) {
    vertex->color = GRAY;
    int next_vertex;
    printf("%d\t", vertex->vertex_index);

    while ( (next_vertex = get_from_adjacent_list(vertex, number_of_vertex)) != -1) {
        if (adjacent_list[next_vertex].color == WHITE) {
            DFS_visit(&adjacent_list[next_vertex], number_of_vertex, adjacent_list); 
        } 
    }
}

/**
 * get_from_adjacent_list
 * Description: This function finds the next element from the adjacency list of given vertex.
 * 
 * RETURN VALUE:
 * -1 : if No adjacent vertex is found.
 * index of the first adjacent vertex of the given vertex : otherwise.
 */

int get_from_adjacent_list(vertex* vertex, int number_of_vertex) {
    int result = -1;

    while (vertex->next_adjacent_index < number_of_vertex) {
        if (vertex->adjacent_vertex_list[vertex->next_adjacent_index] == 0) {
            vertex->next_adjacent_index++;
        } else {
            result = vertex->next_adjacent_index;
            vertex->next_adjacent_index++;
            break;
        }
    }

    return result;
}

void perform_BFS(vertex_ptr graph, int number_of_vertex) {
    reset_status(graph, number_of_vertex);

    printf("Perform BFS:\n");
    for (int i = 0; i < number_of_vertex; i++) {
        if (graph[i].color == WHITE) {
            BFS_visit(&graph[i], number_of_vertex, graph);
        }
    }
    
    printf("\n");
}

void BFS_visit(vertex* vertex, int number_of_vertex, vertex_ptr adjacent_list) {
    int v;
    int queue[number_of_vertex]; /* loop queue of size number_of_vertex */
    int in = 0;
    int out = 0;
    int next_vertex = 0;
    vertex->color = GRAY;

    /* enqueue here */
    queue[in] = vertex->vertex_index;
    in = (in + 1) % number_of_vertex;

    while (in != out) {
        /* dequeue an element here */
        v = queue[out];
        printf("%d\t", v);
        out = (out + 1) % number_of_vertex;
        
        /* add all unvisited adjacent elements of vertex v into the queue */

        for (int i = 0; i < number_of_vertex; i++) {
            if (adjacent_list[v].adjacent_vertex_list[i] == 1) {
                if (adjacent_list[i].color == WHITE) {
                    queue[in] = i;
                    in = (in + 1) % number_of_vertex;
                    adjacent_list[i].color = GRAY;
                }
            }
        }
    }
}

void perform_topological_sorting(vertex_ptr graph, int number_of_vertex) {
    int stack[number_of_vertex];
    int in = 0;
    int out;

    reset_status(graph, number_of_vertex);

    printf("Perform topological sorting\n");

    for (int i = 0; i < number_of_vertex; i++) {
        if (graph[i].color == WHITE) {
            topological_visit(&graph[i], number_of_vertex, graph, stack, &in);
        }
    }

    /* pop all the elements in the stack */
    out = in;
    while (out > 0) {
        out--;
        printf("%d\t", stack[out]);
    }
    printf("\n");
}

void topological_visit(vertex* vertex, int number_of_vertex, vertex_ptr adjacent_list, int *stack, int *in) {
    vertex->color = GRAY;
    int next_vertex;
    
    while ( (next_vertex = get_from_adjacent_list(vertex, number_of_vertex)) != -1) {
        if (adjacent_list[next_vertex].color == WHITE) {
            topological_visit(&adjacent_list[next_vertex], number_of_vertex, adjacent_list, stack, in); 
        } 
    }
    
    /* push into stack */
    stack[*in] = vertex->vertex_index;
    *in = *in + 1;
}