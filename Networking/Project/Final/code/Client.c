#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <stdbool.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <ctype.h>
#include <netdb.h>

#define DEFAULT_PORT	5019


int main(int argc, char **argv) {

	char szBuff[100];
	char szBuff1[5];
	int msg_len = 0, msg_len1 = 0, msg_len3 = 0;
	//int addr_len;
	struct sockaddr_in server_addr;
	struct hostent *hp;
	int connect_sock;
	char operation[10] = "";
	char result[1000];
	char *server_name = (char*)"localhost";
	unsigned short	port = DEFAULT_PORT;
	unsigned int	addr;

	if (argc != 3) {
		printf("echoscln [server name] [port number]\n");
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

	memset(&server_addr, 0, sizeof(server_addr));
	memcpy(&(server_addr.sin_addr), hp->h_addr, hp->h_length);
	server_addr.sin_family = hp->h_addrtype;
	server_addr.sin_port = htons(port);

	connect_sock = socket(AF_INET, SOCK_STREAM, 0);	//TCp socket

	if (connect_sock == -1) {
		fprintf(stderr, "socket() failed with error \n");
		return -1;
	}

	if (connect(connect_sock, (struct sockaddr *)&server_addr, sizeof(server_addr))== -1) {
		fprintf(stderr, "connect() failed with error \n");
		return -1;
	}

	if (hp == NULL) {
		fprintf(stderr, "Cannot resolve address: \n");
		return -1;
	}

		//copy the resolved information into the sockaddr_in structure

	printf("\t\t%-20s %-45s \n", "current user is : ", "tourist");
	printf("\t=======================================================\n");
	printf("\t||\t%-45s||\n","Welcome! Here is the operation you can do:");
	printf("\t||\t%-45s||\n", "Exit: exit");
	printf("\t||\t%-45s||\n", "1:Search data");
	printf("\t||\t%-45s||\n", "2:Add data");
	printf("\t||\t%-45s||\n", "3:Modify data");
	printf("\t||\t%-45s||\n", "4:register");
	printf("\t||\t%-45s||\n", "5:log in");
	printf("\t=======================================================\n");
	printf("%-s","Choose Operation( Enter the number ):");
	scanf("%s", operation);//input index 

	char currentuser[100] = "tourist";//if not log in,current user is tourist
	while (strcmp(operation, "exit") != 0)
	{
		char input[100];
		char modify[100];
		char index[10];

		if (strcmp(operation, "1") == 0) {
			printf("\nInput the attribute you want to search\n");
			printf("( Enter a Name or a Phone Number or a Fox Number )\n>>");
			scanf("%s", input);
		}

		if (strcmp(operation, "2") == 0) {
			char name[20];
			char telNum[20];
			char fox[20];
			char note[20];
			printf("\nEnter name:");
			scanf("%s", name);

			printf("\nenter telNum:");
			scanf("%s", telNum);

			printf("\nemter fox:");
			scanf("%s", fox);

			printf("\nenter note:");
			scanf("%s", note);

			char space[2] = "\t";
			char next[2] = "\n";
			strcat(input, next);
			strcat(input, name);
			strcat(input, space);
			strcat(input, telNum);
			strcat(input, space);
			strcat(input, fox);
			strcat(input, space);
			strcat(input, note);
			strcat(input, space);
			strcat(input, currentuser);
		}

		if (strcmp(operation, "3") == 0) {
			printf("\nWhich item you want to modify?\n");
			printf("You can enter a Name, a Phone Number, a Fox Number or a Note.\n");
			printf("You can only modify the data which is added by you:\n>>");
			scanf("%s", input);
		}
		if (strcmp(operation, "4") == 0) {
			printf("Which id you want?\n>>");
			scanf("%s", input);
		}

		if (strcmp(operation, "5") == 0) {
			printf("what is your user id?\n>>");
			scanf("%s", input);
		}

		if (strcmp(operation, "1") == 0)
		{
			msg_len = send(connect_sock, operation, sizeof(operation), 0);//send operation to server
			msg_len = recv(connect_sock, szBuff, sizeof(szBuff), 0);
			msg_len1 = send(connect_sock, input, sizeof(input), 0);//send a string that you want to search
			msg_len = recv(connect_sock, result, sizeof(result), 0);

			if (strcmp(operation, "") == 0)
			{
				printf("no result!\n");
			}
			else {
				printf("\n>>>Result<<<\n%s\n\n", result);
			}
		}
		if (strcmp(operation, "2") == 0)//if you not log in,the author of the article you add is "tourist"
		{
			msg_len = send(connect_sock, operation, sizeof(operation), 0);
			msg_len = recv(connect_sock, szBuff, sizeof(szBuff), 0);
			msg_len1 = send(connect_sock, input, sizeof(input), 0);
			printf("\nAdd Succeed...\n\n");
		}

		if (strcmp(operation, "3") == 0)//you can only modify article you have add(the author is you)
		{
			msg_len = send(connect_sock, operation, sizeof(operation), 0);
			msg_len = recv(connect_sock, szBuff, sizeof(szBuff), 0);
			msg_len1 = send(connect_sock, input, sizeof(input), 0);
			msg_len = recv(connect_sock, szBuff, sizeof(szBuff), 0);
			msg_len1 = send(connect_sock, currentuser, sizeof(currentuser), 0);
			msg_len1 = recv(connect_sock, result, sizeof(result), 0);

			if (strcmp(result, "") == 0)
			{
				printf("no result\n");
			}
			else {
				printf("\nWe got: \n%s\nWhich result you want to modify?\n(input index start from 1)\n>>", result);
				//if have multiple result, select one using index (0,1,2...)
				scanf("%s", index);
				msg_len1 = send(connect_sock, index, sizeof(index), 0);
				msg_len = recv(connect_sock, szBuff, sizeof(szBuff), 0);
				printf("you want to modify %s to what?\n>>", input);//the sever will automatically know you want to search name or tele or note and directly modify it
				scanf("%s", modify);
				msg_len1 = send(connect_sock, modify, sizeof(modify), 0);
				printf("Request Sended...\n\n");
			}
		}
		if (strcmp(operation, "4") == 0)
		{
			char answer[2];
			char userinfo[200];
			char username[100];
			char password[100];
			msg_len = send(connect_sock, operation, sizeof(operation), 0);

			msg_len = recv(connect_sock, szBuff, sizeof(szBuff), 0);

			msg_len1 = send(connect_sock, input, sizeof(input), 0);//send id to sever

			msg_len = recv(connect_sock, answer, sizeof(answer), 0);//receive answer of whether this id is available, no same id in database


			if (strcmp(answer, "f") == 0) {
				printf("\n\tid hass already exist\n\t");
			} else if (strcmp(answer, "t") == 0) {
				printf("Which username you want?\n>>");
				scanf("%s", username);
				printf("Which password you want?\n>>");
				scanf("%s", password);
				char space[2] = "\t";
				char next[2] = "\n";
				strcat(userinfo, next);
				strcat(userinfo, input);
				strcat(userinfo, space);
				strcat(userinfo, username);
				strcat(userinfo, space);
				strcat(userinfo, password);
				msg_len = send(connect_sock, userinfo, sizeof(userinfo), 0);
				printf("Request send...\n\n");
			}
		}

		if (strcmp(operation, "5") == 0)
		{
			char password[100] = "";
			char answer[2] = "";
			printf("what is your password?\n>>");
			scanf("%s", password);
			msg_len = send(connect_sock, operation, sizeof(operation), 0);
			msg_len = recv(connect_sock, szBuff, sizeof(szBuff), 0);
			msg_len1 = send(connect_sock, input, sizeof(input), 0);//send id to server
			msg_len1 = recv(connect_sock, szBuff, sizeof(result), 0);
			msg_len = send(connect_sock, password, sizeof(password), 0);//send password to sever
			msg_len3 = recv(connect_sock, answer, sizeof(answer), 0);//receive result that whether log in successful
			
			if (strcmp(answer, "f") == 0) {
				printf("Error log in!\n");
			} else if (strcmp(answer, "t") == 0) {
				memcpy(currentuser, input, 100);//if success, update user name
			}
		}

		if (msg_len == -1) {
			fprintf(stderr, "send() failed with error \n");
			close(connect_sock);
			return -1;
		}

		if (msg_len == 0) {
			printf("server closed connection\n");
			close(connect_sock);
			return -1;
		}

		if (msg_len1 == -1) {
			fprintf(stderr, "send() failed with error \n");
			close(connect_sock);
			return -1;
		}

		if (msg_len1 == 0) {
			printf("server closed connection\n");
			close(connect_sock);
			return -1;
		}

		printf("\t\t%-20s %-45s \n", "current user is : ", currentuser);
		printf("\t=======================================================\n");
		printf("\t||\t%-45s||\n","Welcome! Here is the operation you can do:");
		printf("\t||\t%-45s||\n", "exit: Exit");
		printf("\t||\t%-45s||\n", "1:Search data");
		printf("\t||\t%-45s||\n", "2:Add data");
		printf("\t||\t%-45s||\n", "3:Modify data");
		printf("\t||\t%-45s||\n", "4:register");
		printf("\t||\t%-45s||\n", "5:log in");
		printf("\t=======================================================\n");
		printf("Choose Operation( Enter the number ):");
		scanf("%s", operation);//input index 
		memset(result, '\0', sizeof(result));
	}

	close(connect_sock);
	return 0;
}


