#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define DEFAULT_PORT 5019


int main(int argc, char **argv){
	
	char szBuff[100];
	int msg_len;
	socklen_t addr_len;
	struct sockaddr_in local, client_addr;

	int sock, msg_sock;


	// Fill in the address structure
	local.sin_family		= AF_INET;
	local.sin_addr.s_addr	= INADDR_ANY;
	local.sin_port		= htons(DEFAULT_PORT);

	sock = socket(AF_INET,SOCK_STREAM, 0);	//TCp socket


	if (sock == -1) {
        perror("SOCKET");
		return -1;
	}

	if (bind(sock, (struct sockaddr *)&local, sizeof(local)) == -1) {
        perror("BIND");
		return -1;
	}

	if (listen(sock, 1) == -1){
        perror("Listen");
		return -1;
	}

	
	printf("Waiting for the connections ........\n");

	addr_len = sizeof(struct sockaddr_in);
	msg_sock = accept(sock, (struct sockaddr*)&client_addr, &addr_len); /* ???? */

	if (msg_sock == -1){
        perror("ACCEPT");
		return -1;
	}


	msg_len = recv(msg_sock, szBuff, sizeof(szBuff), 0);

	if (msg_len == -1){
		return -1;
	}

	if (msg_len == 0){
		printf("Client closed connection\n");
		close(msg_sock);
		return -1;
	}

	printf("Bytes Received: %d, message: %s from %s\n", msg_len, szBuff, inet_ntoa(client_addr.sin_addr));
	
	msg_len = send(msg_sock, szBuff, sizeof(szBuff), 0);
	if (msg_len == 0){
		printf("Client closed connection\n");
		close(msg_sock);
		return -1;
	}

	close(msg_sock);
}
		