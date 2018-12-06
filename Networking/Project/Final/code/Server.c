#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <stdbool.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include "lock.c"
#include "threadpool.c"

#define DEFAULT_PORT 5019
#define BUF_SIZE 100
#define MAX_LINE 1024
#define NUMBER_OF_THREAD 4
//structure of user
struct User{
	char name[20];
	char id[20];
	char password[100];
};
//structure of message
struct Account {
	char name[20];
	char telNum[20];
	char fox[20];
	char note[20];
	char author[100];
};

int GetTXTRow(char *fileName) {//find how many rows are there
	reader_lock();
	int c;
	FILE *fp;
	int lines = 1;
	fp = fopen(fileName, "rb");
	if (fp)
	{
		while ((c = fgetc(fp)) != EOF)
			if (c == '\n') lines++;
		fclose(fp);
	}
	reader_unlock();
	return lines;
}

int readuserData(char *fileName, int numOfRow, struct User *user) {
	char temp[MAX_LINE];
	char * pch;

	reader_lock();
	FILE *fpRead = fopen(fileName, "r");
	if (fpRead == NULL)
	{
		printf("\tFail to read data!\n");
		return 0;
	}
	
	for (int i = 0; i < numOfRow; i++)
	{
		fgets(temp, MAX_LINE, fpRead);
		pch = strtok(temp, "\t");
		strcpy(user[i].id, pch);

		pch = strtok(NULL, "\t");
		strcpy(user[i].name, pch);

		pch = strtok(NULL, "\t");
		strcpy(user[i].password, pch);

	}
	fclose(fpRead);
	reader_unlock();
	return 1;
}

int searchUser(int numOfRow, struct User *user, char* input) {//to judge whether the id is exist

	for (int i = 0; i < numOfRow; i++) {
		if (strcmp(input, user[i].id) == 0) {
			return 0;
		}
	}

	return 1;
}
int searchpassword(int numOfRow, struct User *user, char* input, char* password)//to search whether the password and id is match
{

	char next[2] = "\n";
	char password1[100]="";
	strcat(password1, password);
	strcat(password1, next);
	for (int i = 0; i < numOfRow; i++) {
		
		if (strcmp(input, user[i].id) == 0)
		{
			if (i != numOfRow - 1)
			{
				if (strcmp(password1, user[i].password) == 0)
				{
					return 1;
				}
			}
			else {
				if (strcmp(password, user[i].password) == 0)
				{
					return 1;
				}
			}
		}
	}

	return 0;
}
int readTXTData(char *fileName, int numOfRow, struct Account *data) {
	//read all user data and put into structure
	char temp[MAX_LINE];
	char * pch;
	writer_lock();//has a mutex lock because can't read and write at same time
	FILE *fpRead = fopen(fileName, "r");
	if (fpRead == NULL)
	{
		fprintf(stderr,"Fail to read data!\n");
		return 0;
	}

	// printf("--------------------------------\n");
	for (int i = 0; i < numOfRow; i++)
	{
		fgets(temp, MAX_LINE, fpRead);
		pch = strtok(temp, "\t");
		strcpy(data[i].name, pch);

		pch = strtok(NULL, "\t");
		strcpy(data[i].telNum, pch);

		pch = strtok(NULL, "\t");
		strcpy(data[i].fox, pch);

		pch = strtok(NULL, "\t");
		strcpy(data[i].note, pch);


		pch = strtok(NULL, "\t");
		strcpy(data[i].author, pch);
		// printf("--------------------------------\n");
	}

	fclose(fpRead);
	writer_unlock();
	return 1;
}

int searchData(int numOfRow, struct Account *data, char* input, char* result) {

	int resultNum = 0;

	for (int i = 0; i < numOfRow; i++) {
		if (strcmp(input, data[i].name) == 0) {//if find, put it to a string

			char  *zhang = data[i].telNum, *er = data[i].fox, *xiong = data[i].note, *name = data[i].name;
			char space[2] = "\t";
			char next[2] = "\n";

			strcat(result, name);
			strcat(result, space);
			strcat(result, zhang);
			strcat(result, space);
			strcat(result, er);
			strcat(result, space);
			strcat(result, xiong);
			strcat(result, next);
			resultNum++;
			continue;
		}

		if (strcmp(input, data[i].telNum) == 0) {
			char  *zhang = data[i].telNum, *er = data[i].fox, *xiong = data[i].note;
			if (resultNum == 0)
			{
				strcpy(result, zhang);
			}
			else {
				strcat(result, er);
			}
			strcat(result, er);
			strcat(result, xiong);
			strcat(result, (char*)'\n');
			resultNum++;
			continue;
		}

		if (strcmp(input, data[i].fox) == 0) {
			char  *zhang = data[i].telNum, *er = data[i].fox, *xiong = data[i].note;
			if (resultNum == 0)
			{
				strcpy(result, zhang);
			}
			else {
				strcat(result, er);
			}
			strcat(result, er);
			strcat(result, xiong);
			strcat(result, (char*)'\n');
			resultNum++;
			continue;
		}
	}

	printf("--------------------------------\n");
	printf("%d data suit for your keyword!\n", resultNum);
	printf("--------------------------------\n");
	return resultNum;
}


int modifyData(int numOfRow, struct Account *data, char* input, char* result, int* selected, int* which, char* currentuser) {

	int resultNum = 0;

	for (int i = 0; i < numOfRow; i++) {
		if (strcmp(input, data[i].name) == 0 && strcmp(currentuser, data[i].author) == 0) {

			char  *zhang = data[i].telNum, *er = data[i].fox, *xiong = data[i].note, *name = data[i].name;
			char space[2] = "\t";
			char next[2] = "\n";

			strcat(result, name);
			strcat(result, space);
			strcat(result, zhang);
			strcat(result, space);
			strcat(result, er);
			strcat(result, space);
			strcat(result, xiong);
			strcat(result, next);
			selected[resultNum] = i;//to indicate whitch message satisfy the search
			which[resultNum] = 1;//if equal 1, means you want to modify name
			resultNum++;
			continue;
		}
		if (strcmp(input, data[i].telNum) == 0 && strcmp(currentuser, data[i].author) == 0) {
			char  *zhang = data[i].telNum, *er = data[i].fox, *xiong = data[i].note, *name = data[i].name;
			char space[2] = "\t";
			char next[2] = "\n";

			strcat(result, name);
			strcat(result, space);
			strcat(result, zhang);
			strcat(result, space);
			strcat(result, er);
			strcat(result, space);
			strcat(result, xiong);
			strcat(result, next);
			selected[resultNum] = i;
			which[resultNum] = 2;
			resultNum++;
			continue;
		}
		if (strcmp(input, data[i].fox) == 0 && strcmp(currentuser, data[i].author) == 0) {
			char  *zhang = data[i].telNum, *er = data[i].fox, *xiong = data[i].note, *name = data[i].name;
			char space[2] = "\t";
			char next[2] = "\n";

			strcat(result, name);
			strcat(result, space);
			strcat(result, zhang);
			strcat(result, space);
			strcat(result, er);
			strcat(result, space);
			strcat(result, xiong);
			strcat(result, next);
			selected[resultNum] = i;
			which[resultNum] = 3;
			resultNum++;
			continue;
		}
		if (strcmp(input, data[i].note) == 0 && strcmp(currentuser, data[i].author) == 0) {
			char  *zhang = data[i].telNum, *er = data[i].fox, *xiong = data[i].note, *name = data[i].name;
			char space[2] = "\t";
			char next[2] = "\n";

			strcat(result, name);
			strcat(result, space);
			strcat(result, zhang);
			strcat(result, space);
			strcat(result, er);
			strcat(result, space);
			strcat(result, xiong);
			strcat(result, next);
			selected[resultNum] = i;
			which[resultNum] = 4;
			resultNum++;
			continue;
		}
	}
	printf("--------------------------------\n");
	printf("%d data suit for your keyword!\n", resultNum);
	printf("--------------------------------\n");
	return resultNum;
}

int modifyDatatofile(int numOfRow, struct Account *data, char *fileName)//put data to file
{
	writer_lock();
	FILE *fp;
	fp = fopen(fileName, "w");
	fclose(fp);

	fp = fopen(fileName, "a");
	for (int i = 0; i < numOfRow; i++) {
		/*if (i != 0)
		{
			fprintf(fp, "\n");
		}*/
		fprintf(fp, "%s\t", data[i].name);
		fprintf(fp, "%s\t", data[i].telNum);
		fprintf(fp, "%s\t", data[i].fox);
		fprintf(fp, "%s\t", data[i].note);
		fprintf(fp, "%s", data[i].author);
	}

	fclose(fp);
	writer_unlock();
	return 0;
}
int addData(char *fileName, char* toadd) {
	FILE *fp;
	writer_lock();
	if ((fp = fopen(fileName, "a")) == NULL) {
		printf("Open Failed.\n");
		return 0;
	}

	fprintf(fp, "%s", toadd);
	printf("--------------------------------\n");
	printf("Finish! Your request is sended to Sever.\n");
	printf("--------------------------------\n");
	fclose(fp);
	writer_unlock();
	return 1;
}


void* handle_accept(void* param)
{
	int socket_feed = *(int*)param;
	char buffer[BUF_SIZE];
	char buffer1[BUF_SIZE];

	while (true) {
		memset(buffer, 0, BUF_SIZE);  //reset buffer
		memset(buffer1, 0, BUF_SIZE);
		
		int strLen = recv(socket_feed, buffer, BUF_SIZE, 0);  //receive message from client(receive user operation)
		
		if (strLen == -1) {
			fprintf(stderr, "recv() failed with error \n");
			close(socket_feed);
			return 0;
		}

		if (strLen == 0) {
			fprintf(stderr, "Client closed connection\n");
			close(socket_feed);
			return 0;
		}

		send(socket_feed, buffer, sizeof(buffer), 0);

		int strLen1 = recv(socket_feed, buffer1, BUF_SIZE, 0); //receive message from client(receive user input)

		if (strLen1 == -1) {
			fprintf(stderr, "recv() failed with error\n");
			close(socket_feed);
			return 0;
		}

		if (strLen1 == 0) {
			fprintf(stderr, "Client closed connection\n");
			close(socket_feed);
			return 0;
		}

		int numOfRow = GetTXTRow("data.txt");//get the row number of message
		struct Account *data = (struct Account *)malloc(numOfRow * sizeof(struct Account));//create structrue to save message
		readTXTData("data.txt", numOfRow, data);//read data to structrue
		printf("Finish loading!\n");

		if (strcmp(buffer, "1") == 0) {
			char result[1000];
			memset(result, '\0', sizeof(result));
			int num = searchData(numOfRow, data, buffer1, result);
			send(socket_feed, num != 0 ? result : "No given data.", sizeof(result), 0);//send result back to client	
		}
		if (strcmp(buffer, "2") == 0) {
			char result[1000] = "";
			addData("data.txt", buffer1);
		}
		if (strcmp(buffer, "3") == 0) {
			char currentuser[100] = "";
			send(socket_feed, buffer, sizeof(buffer), 0);
			strLen1 = recv(socket_feed, currentuser, sizeof(currentuser), 0);
			printf("%s\n", currentuser);
			int *suitIndex = (int *)malloc(numOfRow * sizeof(int));//create arry to record whih info satisfy search
			int *whichtodelete = (int *)malloc(numOfRow * sizeof(int));//create array to record which item you want to modify
			//1 means name, 2 means telephone number...
			char result[1000] = "";
			char modify[100] = "";
			int number = modifyData(numOfRow, data, buffer1, result, suitIndex, whichtodelete, currentuser);
			// printf("%s", result);
			send(socket_feed, result, sizeof(result), 0);
			if (strcmp(result, "") != 0) {
				char index[10] = { 0 };
				strLen = recv(socket_feed, index, 10, 0);//receive index of record you want to modify
				send(socket_feed, index, sizeof(index), 0);
				strLen = recv(socket_feed, modify, sizeof(modify), 0);//receive value you want to modify to
				int num = atoi(index);//transform string to int
				num--;
				// printf("%d", num);
				if (whichtodelete[num] == 1)//if 1, modify name
				{
					strcpy(data[suitIndex[num]].name, modify);
				}
				else if (whichtodelete[num] == 2)
				{
					strcpy(data[suitIndex[num]].telNum, modify);
				}
				else if (whichtodelete[num] == 3)
				{
					strcpy(data[suitIndex[num]].fox, modify);
				}
				else if (whichtodelete[num] == 4)
				{
					strcpy(data[suitIndex[num]].note, modify);
				}

				modifyDatatofile(numOfRow, data, "data.txt");
			}

		}

		if (strcmp(buffer, "4") == 0)
		{
			int userRow = GetTXTRow((char*)"user.txt");//get number of user
			struct User *user = (struct User *)malloc(userRow * sizeof(struct User));//create user structrue
			readuserData("user.txt", userRow, user);//read user info to structure
			int answer = searchUser(userRow, user, buffer1);

			if (answer == 0) {
				send(socket_feed, "f", sizeof("f"), 0);
			} else {
				send(socket_feed, "t", sizeof("t"), 0);
				char getit[300] = "";
				recv(socket_feed, getit, sizeof(getit), 0);//receive user name and password
				addData("user.txt", getit);//add to user database
			}
		}
		if (strcmp(buffer, "5") == 0) {

			int userRow = GetTXTRow((char*)"user.txt");
			struct User *user = (struct User *)malloc(userRow * sizeof(struct User));
			readuserData("user.txt", userRow, user);
			char password[100] = "";
			send(socket_feed, password, sizeof(password), 0);//receive password
			recv(socket_feed, password, sizeof(password), 0);
			
			int answer = searchpassword(userRow, user, buffer1, password);//check whether id and password match
			if (answer == 0)
			{
				send(socket_feed, "f", sizeof("f"), 0);
			}
			else {//told server that it log in successfully
				send(socket_feed, "t", sizeof("t"), 0);
			}
		}

	}

	close(socket_feed);
	return 0;
}

int main(void) {
	int msg_len;
	struct sockaddr_in local, client_addr;
	socklen_t addr_len;
	int sock, msg_sock;

	local.sin_family = AF_INET;
	local.sin_addr.s_addr = INADDR_ANY;
	local.sin_port = htons(DEFAULT_PORT);

	sock = socket(AF_INET, SOCK_STREAM, 0);	//TCp socket


	if (sock == -1) {
		fprintf(stderr, "socket() failed with error\n");
		return -1;
	}


	if (bind(sock, (struct sockaddr *)&local, sizeof(local)) == -1) {
		fprintf(stderr, "bind() failed with error \n");
		return -1;
	}

	if (listen(sock, 20) == -1) {
		fprintf(stderr, "listen() failed with error \n");
		return -1;
	}

	lock_init();
	pool_init(NUMBER_OF_THREAD);

	printf("Waiting for the connections ........\n");
	while (true)
	{
		addr_len = sizeof(client_addr);
		msg_sock = accept(sock, (struct sockaddr*)&client_addr, &addr_len);
		if (msg_sock == -1) {
			fprintf(stderr, "accept() failed with error\n");
			return -1;
		}

		printf("accepted connection from %s, port %d\n",
			inet_ntoa(client_addr.sin_addr),
			htons(client_addr.sin_port));

		pool_add_job(handle_accept, &msg_sock);
	}

	close(msg_sock);
	pool_destroy();
	lock_destroy();
	return 0;
}