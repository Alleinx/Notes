#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <netdb.h>
#include <arpa/inet.h>

#define DEFAULT_PORT 5019


int main(int argc, char *argv[]) {
	
	char szBuff[100];
	int msg_len;
	struct sockaddr_in server_addr;
	struct hostent *hp;
	int connect_sock;


	char			*server_name = "localhost";
	unsigned short	port = DEFAULT_PORT;
	unsigned int	addr;

	if (argc != 3) {
		fprintf(stderr, "Usage: client [server name] [port number]\n");
		return -1;
	} else {
		server_name = argv[1];
		port = atoi(argv[2]);
	}

	if (isalpha(server_name[0])) {
		hp = gethostbyname(server_name);
	} else {
		addr = inet_addr(server_name);
		hp = gethostbyaddr((char*)&addr, 4, AF_INET);
	}

	if (hp == NULL) {
        perror("Cannot resolve address");
		return -1;
	}

	//copy the resolved information into the sockaddr_in structure
	memset(&server_addr, 0, sizeof(server_addr));
	memcpy(&(server_addr.sin_addr), hp->h_addr, hp->h_length);
	server_addr.sin_family = hp->h_addrtype;
	server_addr.sin_port = htons(port);
	
	while (1) {
		connect_sock = socket(AF_INET,SOCK_STREAM, 0);	
		if (connect_sock == -1) {
			perror("socket() failed with error");
			return -1;
		}

		printf("Client connecting to: %s\n", hp->h_name);


	
		if ( connect(connect_sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
			perror("connect() failed with error");
			return -1;
		}

		printf("input character string:\n");
		scanf("%s",szBuff); /* If necessary, change to gets() here. */
	
		msg_len = send(connect_sock, szBuff, sizeof(szBuff), 0); /* send here */
	
		if (msg_len == -1) {
			perror("send() failed");
			return -1;
		}

		if (msg_len == 0) {
			printf("server closed connection\n");
			close(connect_sock);
			return -1;
		}

		msg_len = recv(connect_sock, szBuff, sizeof(szBuff), 0); /* receive here */
	
		if (msg_len == -1) {
			perror("send() failed with error");
			close(connect_sock);
			return -1;
		}

		if (msg_len == 0) {
			printf("server closed connection\n");
			close(connect_sock);
			return -1;
		}

		printf("Echo from the server %s.\n", szBuff);
		close(connect_sock);
	}
	
    return 0;
}