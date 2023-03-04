#include<stdio.h>
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        int N,K,c=0;
        scanf("%d%d",&N,&K);
        while(N--)
        {
            int s;
            scanf("%d",&s);
            if(s<=0) c++;
        }
        if(c>=K) printf("NO\n");
        else printf("YES\n");
    }
    return 0;
}