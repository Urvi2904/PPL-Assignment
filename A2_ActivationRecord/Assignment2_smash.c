#include<stdio.h>
#include<string.h>

int main(int argc, char *argv[]){
	if(argc != 2){
		printf("Usage : ./a.out <string>\n");
		return -1;
	} 
	char buffer[20];
	strcpy(buffer, argv[1]);
	printf("%s\n", buffer);
	return 0;
}


