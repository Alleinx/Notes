#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <pthread.h>

#define DEFAULT_PORT 5019
#define MAX_THREAD 26

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

	local.sin_family = AF_INET;
	local.sin_addr.s_addr = INADDR_ANY;
	local.sin_port = htons(DEFAULT_PORT);
	sock = socket(AF_INET,SOCK_STREAM, 0);	

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
	
	while(1) {
		printf("Waiting for the connections ........\n");

		addr_len = sizeof(struct sockaddr_in);
		msg_sock = accept(sock, (struct sockaddr*)&client_addr, &addr_len); /* check man here for invalid Parameter */
		printf("Accept a request\n");

		if (msg_sock == -1){
			perror("ACCEPT");
			return -1;
		}
		/* add thread here */
		pthread_t t;
		pthread_attr_t attr_detached;
		pthread_attr_init(&attr_detached);
		pthread_attr_setdetachstate(&attr_detached, PTHREAD_CREATE_DETACHED);
		pthread_create(&t, &attr_detached, runner, &msg_sock);
	}
	close(msg_sock);
	return 0;
}
		
void *runner(void *param) {
	int msg_sock = *(int*)param;
	char szBuff[100];

    int msg_len = recv(msg_sock, szBuff, sizeof(szBuff), 0);

	char *result = search(szBuff);
	
	if (msg_len == -1) {
		return 0;
	}

	if (msg_len == 0) {
		printf("Client closed connection\n");
		close(msg_sock);
		return 0;
	}

	printf("User input: %s,Result: %s \n", szBuff, result != NULL ? result : "Nothing");
		
	msg_len = send(msg_sock, result != NULL ? result : "NOT FOUND", sizeof(szBuff), 0);

	if (msg_len == 0) {
		printf("Client closed connection\n");
		close(msg_sock);
		return 0;
	}

	close(msg_sock);
    return 0; // Thread dies.
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
