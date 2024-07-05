#include<stdio.h>
int main ()
{
	int pass;
	printf("press 1 if you pass in science and math\n # press 2 if you pass only in science \n #press 3 if you pass only in math");
	printf("\nplease select one option from 1,2 and 3-->");
	scanf("%d",&pass);
	if(pass==1){
		printf("cngrates....you win 45 rupees..");
	}
	else if(pass==2){
		printf("congrates....you win 15 rupees");
	}
	else{
		printf("congrates....you win 15 rupees ");
		
	}
	return 0;
	
	
}
