#include<stdio.h>
int main()
{
	printf("Enter your age-->");
	int age;
	scanf("%d",age);
	if (age<=10)
	{
		printf("you pay 100 rupees");
	}
	else if(25>age>10)
	{
		printf("you pay 200 rupees");
	}
	else if(50>age>25)
	{
		printf("you pay 300 rupees");
	}
	else{
		printf("you are not able to ride ");
	}
	return 0;
}
