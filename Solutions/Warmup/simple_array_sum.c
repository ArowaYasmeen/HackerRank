#include<stdio.h>
int main()
{
    int N,i;
    scanf("%d",&N);
    int array[N];
    for(i=0;i<N;i++)
    {
        scanf("%d",&array[i]);
    }
    int sum=0;
    for(i=0;i<N;i++)
    {
        sum=sum+array[i];
    }
    printf("%d",sum);
    return 0;
}