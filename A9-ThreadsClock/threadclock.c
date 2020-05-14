#include<stdio.h>
#include<pthread.h>
#include<time.h>
#include<unistd.h>

int secs, mins, hrs;


/*void delay(int number_of_seconds) {  

	int j = 0;
   	int milli_seconds = CLOCKS_PER_SEC * number_of_seconds; 
  
 	clock_t start_time = clock(); 
  
  	while (clock() < start_time + milli_seconds) 
         	j++; 

}*/
	

void *seconds() {

	while(1) {

		//delay(1)
		sleep(1);
		secs++;

	}

}


void *minutes() {
	while(1) {
		if(secs == 60){
			secs = 0;
			mins++;			
		}
	}
}


void *hour() {

	while(1) {

		if(mins == 60){

			mins = 0;			
			hrs++;

		}

	}

}


void *print() {

	while(1) {
	
		printf("\r%02d : %02d : %02d", hrs, mins, secs);

	}

}


int main() {
	pthread_t t1,t2,t3,t4;
	int a, b, c, d;
	
	printf("Enter starting hour: ");
	scanf("%d", &hrs);

	
	printf("Enter starting minute: ");
	scanf("%d", &mins);

	
	printf("Enter starting second: ");
	scanf("%d", &secs);	

	printf("\nClock\n\n");
		
	a = pthread_create(&t1, NULL, seconds, NULL);
	b = pthread_create(&t2, NULL, minutes, NULL);
	c = pthread_create(&t3, NULL, hour, NULL);
	d = pthread_create(&t4, NULL, print, NULL);
	
	pthread_join(t1, NULL);	
	pthread_join(t2, NULL);
	pthread_join(t3, NULL);
	pthread_join(t4, NULL);
		
	return 0;
}
