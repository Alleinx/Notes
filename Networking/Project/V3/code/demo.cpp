#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 1024

struct Account{
	char name[20];
	char telNum[20];
	char fox[20];
	char note[20];
};

int GetTXTRow(char *fileName){
	int c;
	FILE *fp;
	int lines=1;
	fp=fopen(fileName, "rb");
	if(fp)
	{
		while((c=fgetc(fp)) != EOF)
			if(c=='\n') lines++;
		fclose(fp);
	}
	return lines;
}

int readTXTData(char *fileName,int numOfRow, Account *data){
	char temp[MAX_LINE];
	char * pch;
	FILE *fpRead=fopen(fileName,"r");
	if(fpRead==NULL)
	{
		printf("Fail to read data!");
		return 0;
	}
	printf("--------------------------------\n");
	for(int i=0;i<numOfRow;i++)
	{
		fgets(temp,MAX_LINE,fpRead);
		pch = strtok(temp,"\t");
		printf("Name:%s\n",pch);
		strcpy(data[i].name, pch);

		pch = strtok(NULL,"\t");
		printf("Tel:%s\n",pch);
		strcpy(data[i].telNum, pch);

		pch = strtok(NULL,"\t");
		printf("Fox:%s\n",pch);
		strcpy(data[i].fox, pch);

		pch = strtok(NULL,"\t");
		printf("Note:%s\n",pch);
		strcpy(data[i].note, pch);
		printf("--------------------------------\n");
	}
	fclose(fpRead);
	return 1;
}

int searchData(int numOfRow,Account *data){
	char input[20]=" ";
	int resultNum=0;
	while(strcmp(input, "exit") != 0){
		printf("Search(enter exit to exit):");
		scanf("%s",input); 
		getchar();
		printf("--------------------------------\n");
		if(strcmp(input, "exit") == 0)
			break;
		for(int i=0;i<numOfRow;i++){
			if(strcmp(input, data[i].name) == 0){
				printf("result %d:\n",resultNum+1);
				printf("Tele:%s\nFox:%s\nNote:%s\n",data[i].telNum,data[i].fox,data[i].note);
				printf("--------------------------------\n");
				resultNum++;
				continue;
			}
			if(strcmp(input, data[i].telNum) == 0){
				printf("result %d:\n",resultNum+1);
				printf("Name:%s\nFox:%s\nNote:%s\n",data[i].name,data[i].fox,data[i].note);
				printf("--------------------------------\n");
				resultNum++;
				continue;
			}
			if(strcmp(input, data[i].fox) == 0){
				printf("result %d:\n",resultNum+1);
				printf("Name:%s\nFox:%s\nNote:%s\n",data[i].name,data[i].telNum,data[i].note);
				printf("--------------------------------\n");
				resultNum++;
				continue;
			}
		}
		printf("%d data suit for your keyword!\n",resultNum);
		printf("--------------------------------\n");
		resultNum=0;
	}
	return 1;
}


int addData(char *fileName){
	FILE *fp;
	char temp[20]="";
	if ((fp=fopen(fileName,"a"))==NULL){
		printf("Open Failed.\n");
		return 0;
	}
	printf("--------------------------------\n");
	getchar();
	fprintf(fp,"\n");
	printf("Enter name:");
	scanf("%[^\n]", temp);
	getchar();
	fprintf(fp,"%s\t",temp);

	printf("\nEnter telephone number:");
	scanf("%[^\n]", temp);
	getchar();
	fprintf(fp,"%s\t",temp);

	printf("\nEnter fox number:");
	scanf("%[^\n]", temp);
	getchar();
	fprintf(fp,"%s\t",temp);

	printf("\nEnter note:");
	scanf("%[^\n]", temp);
	getchar();
	fprintf(fp,"%s",temp);

	printf("Finish! Your request is send to Sever.\n");
	printf("--------------------------------\n");

	fclose(fp);
	return 1;
}

int modifyData(int numOfRow,Account *data,char *fileName){
	int resultNum=0;
	int *suitIndex = (int *)malloc(numOfRow * sizeof(int));
	char input[20]="";
	int operation=-1;
	int choose=-1;
	printf("Enter the keyword to search the data you want to modify:");
	scanf("%s",input);
	getchar();
	for(int i=0;i<numOfRow;i++){
		if(strcmp(input, data[i].name) == 0){
			printf("result %d:\n",resultNum);
			printf("Tele:%s\nFox:%s\nNote:%s\n",data[i].telNum,data[i].fox,data[i].note);
			suitIndex[resultNum]=i;
			resultNum++;
			continue;
		}
		if(strcmp(input, data[i].telNum) == 0){
			printf("result %d:\n",resultNum);
			printf("Name:%s\nFox:%s\nNote:%s\n",data[i].name,data[i].fox,data[i].note);
			suitIndex[resultNum]=i;
			resultNum++;
			continue;
		}
		if(strcmp(input, data[i].fox) == 0){
			printf("result %d:\n",resultNum);
			printf("Name:%s\nFox:%s\nNote:%s\n",data[i].name,data[i].telNum,data[i].note);
			suitIndex[resultNum]=i;
			resultNum++;
			continue;
		}
	}

	if(resultNum==0){
		printf("Sorry cannot find data suit keyword!\n");
		return 1;
	}

	if(resultNum==1){
		while(operation!=0){
			printf("Which one do you want to modify:\n");
			printf("0:exit\n1:name\n2:telephone number\n3:fox number\n4:note\n");
			scanf("%d",&operation);
			getchar();
			if(operation==0)
				break;
			if(operation==1){
				printf("Former name:%s\n",data[suitIndex[0]].name);
				printf("New name:");
				scanf("%s",data[suitIndex[0]].name);
				getchar();
			}
			if(operation==2){
				printf("Former telephone number:%s\n",data[suitIndex[0]].telNum);
				printf("New telephone number:");
				scanf("%s",data[suitIndex[0]].telNum);
				getchar();
			}
			if(operation==3){
				printf("Former fox number:%s\n",data[suitIndex[0]].fox);
				printf("New fox number:");
				scanf("%s",data[suitIndex[0]].fox);
				getchar();
			}
			if(operation==4){
				printf("Former note:%s\n",data[suitIndex[0]].note);
				printf("New note:");
				scanf("%[^\n]",data[suitIndex[0]].note);
				getchar();
			}
		}
	}

	if(resultNum>1){
		printf("There are %d result suit for your keyword.\n",resultNum);
		for(int i=0;i<resultNum;i++){
			printf("%d:\nName:%s\nTele:%s\nFox:%s\nNote:%s\n",i,data[suitIndex[i]].name,data[suitIndex[i]].telNum,data[suitIndex[i]].fox,data[suitIndex[i]].note);
		}
		printf("Which one do you choose?\n");
		scanf("%d",&choose);
		getchar();

		while(operation!=0){
			printf("Which one do you want to modify:\n");
			printf("0:exit\n1:name\n2:telephone number\n3:fox number\n4:note\n");
			scanf("%d",&operation);
			getchar();
			if(operation==0)
				break;
			if(operation==1){
				printf("Former name:%s\n",data[suitIndex[choose]].name);
				printf("New name:");
				scanf("%s",data[suitIndex[choose]].name);
				getchar();
			}
			if(operation==2){
				printf("Former telephone number:%s\n",data[suitIndex[choose]].telNum);
				printf("New telephone number:");
				scanf("%s",data[suitIndex[choose]].telNum);
				getchar();
			}
			if(operation==3){
				printf("Former fox number:%s\n",data[suitIndex[choose]].fox);
				printf("New fox number:");
				scanf("%s",data[suitIndex[choose]].fox);
				getchar();
			}
			if(operation==4){
				printf("Former note:%s\n",data[suitIndex[choose]].note);
				printf("New note:");
				scanf("%[^\n]",data[suitIndex[0]].note);
				getchar();
			}
		}
	}

	FILE *fp;
	fp=fopen(fileName, "w");
	fclose(fp);

	fp=fopen(fileName,"a");
	for(int i=0;i<numOfRow;i++){
		fprintf(fp,"%s\t",data[i].name);
		fprintf(fp,"%s\t",data[i].telNum);
		fprintf(fp,"%s\t",data[i].fox);
		fprintf(fp,"%s",data[i].note);
	}
	fclose(fp);
	return 0;
}


int main()
{
	int operation=-1;
	int numOfRow=0;
	while(operation!=0){	
		printf("--------------------------------\n");
		printf("Loading Data ...\n");
		numOfRow=GetTXTRow("data.txt");
		Account *data = (Account *)malloc(numOfRow * sizeof(Account));
		readTXTData("data.txt",numOfRow,data);
		printf("Finish loading!\n");
		printf("--------------------------------\n");

		printf("--------------------------------\n");
		printf("Welcome!Here is the operation you can do:\n");
		printf("0:exit\n1:search data\n2:add data\n3:modify data\n");
		printf("--------------------------------\n");
		printf("Choose Operation:");
		scanf("%d",&operation);
		if(operation==1)
			searchData(numOfRow,data);
		if(operation==2)
			addData("data.txt");
		if(operation==3)
			modifyData(numOfRow,data,"data.txt");
	}
	getchar();

	return 1;
}
