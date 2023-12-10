// classes.c

#include <stdio.h>

int climbing_ways(int n) 
{
    if (n<1) return 0;
    if (n==1 || n==2) return n;
    
    int a=1, b=1, temp=0;
    for(int i=3; i<=n; ++i) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return temp;
}

int main(int* argc, ) {
	printf("%d", climbing_ways(10));
}
