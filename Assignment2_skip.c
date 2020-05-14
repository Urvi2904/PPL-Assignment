#include<stdio.h>

void function(int a, int b, int c){
	char buffer1[5]; //8 bytes
	char buffer2[10]; //12 bytes
	int * ret_new;
	ret_new = buffer1 + 12; //8bytes of buffer1 + 4bytes of function rbp
	(*ret_new) += 10; //jump for new rip(main)
}

void main(){
	int x;
	x = 1;
	function(1, 2, 3);
	x = 2;
	printf("%d\n", x);
}

