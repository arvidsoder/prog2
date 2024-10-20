#include <iostream>
#include <chrono>
#include <cstdlib>
#include <functional>

using namespace std;

int64_t fib(int n){
    if (n <= 1) {
        return n;
    }
    return fib(n-1) + fib(n-2);
}

int64_t fib_mem(int n){
    int64_t mem[n+1];
    for (int i=0; i<=n; i++){
        mem[i] = -1;
    }
    function<int64_t(int)> _fib_mem = [&](int n) -> int64_t {
        if (n <= 1) return n;
        if (mem[n] != -1) return mem[n];
            
        mem[n] = _fib_mem(n-1) + _fib_mem(n-2);
        return mem[n];
    };
    return _fib_mem(n);
}



extern "C" {

int64_t fib_cpp_mem(int n){
    return fib_mem(n);
}

int64_t fib_cpp(int n) {
    return fib(n);
}

int fib_time_cpp(int n) {
    auto tp1 = chrono::high_resolution_clock::now();
    int64_t result = fib(n);
    auto tp2 = chrono::high_resolution_clock::now();

    chrono::duration<double, std::milli> duration = tp2 - tp1;
    return duration.count();
}
}
