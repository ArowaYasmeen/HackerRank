int main()
{
    int N;
    int i,p=0,n=0,z=0;
    scanf("%d",&N);
    int a[N];
    for(i=0; i<N; i++)
    {
        scanf("%d",&a[i]);
        if(a[i]<0)
            n++;
        if(a[i]>0)
            p++;
        if(a[i]==0)
            z++;
    }
    printf("%lf\n%lf\n%lf\n",(double)p/N,(double)n/N,(double)z/N);
    return 0;
}
