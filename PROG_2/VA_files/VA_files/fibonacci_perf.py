import ctypes
import ctypes.util
import os
import matplotlib.pyplot as plt
import time
import sys
sys.setrecursionlimit(100000)

if os.name == "nt":
    os.add_dll_directory(os.path.abspath("./fibonacci.dll"))
    dll_path = os.path.abspath("./fibonacci.dll")
    
else:
    os.add_dll_directory(os.path.abspath("./fibonacci.so"))
    dll_path = os.path.abspath("./fibonacci.so")
dll_path = os.path.abspath("./fibonacci.dll")
lib_cpp = ctypes.CDLL(dll_path)  # Windows


# Set the return and argument types for the fib function
lib_cpp.fib_cpp.argtypes = [ctypes.c_int]
lib_cpp.fib_cpp.restype = ctypes.c_int64

lib_cpp.fib_cpp_mem.argtypes = [ctypes.c_int]
lib_cpp.fib_cpp_mem.restype = ctypes.c_int64
# Set the return and argument types for the fib_time function
lib_cpp.fib_time_cpp.argtypes = [ctypes.c_int]
lib_cpp.fib_time_cpp.restype = ctypes.c_double

def fib_py(n:int) -> int:
    if (n <= 1):
        return n
    return fib_py(n-1) + fib_py(n-2)

def fib_py_mem(n:int) -> int:
    memory = {0:0, 1:1}
    def _fib(n):
        if n < 0:
            return 0
        if n not in memory:
            memory[n] = _fib(n-1) + _fib(n-2)
        return memory[n]
    return _fib(n)

def timed_func(func, n:int):
    t1 = time.perf_counter()
    value = func(n)
    t2 = time.perf_counter()
    return (t2-t1, value)

def main():
    n_lst = list(range(10,41,2))
    t_fib_py_lst = []
    t_fib_cpp_lst = []
    
    for n in n_lst:
        t_fib_py_lst.append(timed_func(fib_py, n)[0])
        t_fib_cpp_lst.append(timed_func(lib_cpp.fib_cpp, n)[0])
    
    
    n2_lst = list(range(10,1000,2))
    t_fib_py_mem_lst = []
    t_fib_cpp_mem_lst = []
    for n2 in n2_lst:
        t_fib_py_mem_lst.append(timed_func(fib_py_mem, n2)[0])
        t_fib_cpp_mem_lst.append(timed_func(lib_cpp.fib_cpp_mem, n2)[0])

    plt.plot(n_lst, t_fib_py_lst)
    plt.plot(n_lst, t_fib_cpp_lst)
    plt.legend(['python', 'c++'])
    plt.title('Comparison in computation time: fibonacci')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.show()
    plt.plot(n2_lst, t_fib_py_mem_lst)
    plt.plot(n2_lst, t_fib_cpp_mem_lst)
    plt.legend(['python', 'c++'])
    plt.title('Comparison in computation time: fibonacci using memoization')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.show()



if __name__ == '__main__':
    main()