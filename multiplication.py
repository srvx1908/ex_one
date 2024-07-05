#include<stdio.h>
int main()
{
	int i;
	printf("enter your number:");
	scanf("%d",&i);
    int a=i;
    do{
        printf("%d",a);
        a=a+i;
        
    }while(a<=i*10);
    return 0;
}
