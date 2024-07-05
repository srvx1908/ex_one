#include<stdio.h>
int main()
{
	printf("****....WELCOME....****");
	int age;
	printf("\nEnter your age :");
	scanf("%d",&age);
	if(age>=18){
		printf("\nyou are able to vote..");
		
	}
	else{
		printf("you are not able to vote..");
	}
}
