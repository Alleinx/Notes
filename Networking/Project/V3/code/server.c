#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <stdbool.h>
#include "threadpool.c"

extern CThread_pool* pool;

#define NUMBER_OF_THREAD 5
#define DEFAULT_PORT 5019

void *runner(void *param);
char *search(char *str);
int add(char *str);

int main(int argc, char *argv[]) {
	pthread_t tid;
	char szBuff[100];
	int msg_len;
	socklen_t addr_len;
	struct sockaddr_in local, client_addr;
	int sock, msg_sock;
	int hold[10];
	int count = 0;
	bool find = false;

	local.sin_family = AF_INET;
	local.sin_addr.s_addr = INADDR_ANY;
	local.sin_port = htons(DEFAULT_PORT);
	sock = socket(AF_INET,SOCK_STREAM, 0);	
	pool_init(NUMBER_OF_THREAD); // NUMBER_OF_THREAD threads in thread pool // 

	if (sock == -1) {
		perror("SOCKET");
		return -1;
	}
	if (bind(sock, (struct sockaddr *)&local, sizeof(local)) == -1) {
		perror("BIND");
		return -1;
	}

	if (listen(sock, 1) == -1) {
		perror("Listen");
		return 1;
	}

	
	
	while (true) {
		printf("Server: Waiting for the connections ........\n");
		addr_len = sizeof(struct sockaddr_in);

		/* if no new connection is created, server thread sleep here */
		msg_sock = accept(sock, (struct sockaddr*)&client_addr, &addr_len); 
		
		if (msg_sock == -1){
			perror("ACCEPT");
			return -1;
		}

		printf("Server: detected an new connection, distribute work...\n");
		pool_add_job(runner, &msg_sock);
	}

	pool_destroy();
	return 0;
}
		
void *runner(void *param) {
	int msg_sock = *(int*)param;
	char szBuff[100];
	while (true) {
		
    	int msg_len = recv(msg_sock, szBuff, sizeof(szBuff), 0);

		/* if an error occured about recv */
		if (msg_len == -1) {
			return 0;
		}

		/* if client closd connection */
		if (msg_len == 0) {
			printf("Thread %u: Client closed connection.\n",(unsigned)pthread_self());
			close(msg_sock);
			return 0;
		}
		/* Running here */

		printf("Thread %u: Receive a user input, socket number : %d...\n",(unsigned)pthread_self() ,msg_sock);

		char *result = search(szBuff);

		msg_len = send(msg_sock, result != NULL ? result : "NOT FOUND", sizeof(szBuff), 0);

		printf("Thread %u: Send succeed...\n", (unsigned)pthread_self());
	}

	close(msg_sock);
    return 0; 
}

char *search(char *str) {
	char temp[100];
	FILE *fd = fopen("data.txt", "r");

	if (fd == NULL) {
		perror("data.txt");
		exit(1);
	}

	while (fscanf(fd, "%s\n", temp) != -1) {
		if (strcmp(temp, str) == 0) {
			return str;
		}
	}

	fclose(fd);
	return NULL;
} 

int add(char *str) {
	FILE *fd = fopen("data.txt", "a");
	if (fd == NULL) {
		perror("data.txt");
		exit(1);
	}

	int len = fwrite(str, strlen(str), 1, fd);
	if (len != strlen(str)) {
		perror("Write");
		exit(1);
	}
	fclose(fd);
	return 0;
}