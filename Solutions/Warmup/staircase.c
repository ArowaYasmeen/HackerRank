int main()
{
    int n,i;
    scanf("%d",&n);
    int row,space,hash;
    for(row=1; row<=n; row++)
    {
        for(space=n-row; space>0; space--)
        {
            printf(" ");
        }
        for(hash=1; hash<=row; hash++)
        {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
