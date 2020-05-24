//A program to demonstrate a stack oveflow causing a password bypass.
//password is "password"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SET_PASSWORD "password"

int check_authentication(char *password) {
	int auth_flag = 0;                          
	char password_buffer[16];                       
	strcpy(password_buffer, password);        //vulnerability. strcpy does not check string length.  
	if (strcmp(password_buffer, SET_PASSWORD) == 0)
		auth_flag = 1;
	return auth_flag;                           
}

int main(int argc, char *argv[]) {
	if(argc != 2) {                                  
		printf("Usage: ./a.out <password>");
		return -1;
	}
	if(check_authentication(argv[1]))              //if check_authentication is true grant access. will work for non-zero values.
		printf(" --- Access Granted. ---\n");
	else 
		printf(" XXX Access Denied. XXX\n");
	return 0;
}

