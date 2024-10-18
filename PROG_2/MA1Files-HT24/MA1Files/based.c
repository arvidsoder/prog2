#include <stdlib.h>
#include <stdio.h>

int main() {
int fibo = fib(5);
printf("%.*d", 10, fibo);
}
int fib(int n){
    if (n == 0){
        return 0;
    }
    else if (n == 1){
        return 1;
    }
    else{
        return fib(n-1) + fib(n-2);
    }
}

