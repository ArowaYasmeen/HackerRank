#include<stdio.h>
#include<math.h>
int reverse(int x)
{
    int reverse=0;
    while(x!=0)
    {
        reverse=reverse*10;
        reverse=reverse+x%10;
        x=x/10;
    }
    return reverse;
}
int main()
{
    int i,j,k,c=0;
    scanf("%d%d%d",&i,&j,&k);
    int a;
    for(a=i;a<=j;a++)
    {
        int opp;
        opp=reverse(a);
        if((int)fabs(a-opp)%k==0) c++;
    }
    printf("%d\n",c);
    return 0;
}
