#include<stdio.h>
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        long int N;
        scanf("%ld",&N);
        long int n=N;
        int c=0,s;
        while(n>0)
        {
            int rem=0;
            rem=n%10;
            if(rem==0)
                s++;
            else if(N%rem==0)
                c++;
            n=n/10;
        }
        printf("%d\n",c);
    }
    return 0;
}

