"""
Solutions to module 1
Student: Arvid Söderström
Mail: arvid.s@live.se
Reviewed by: Mattias Levin
Reviewed date: 2024-09-12
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def multiply(m: int, n: int) -> int:  
    if n == 0:
        return 0
    else:
        return m + multiply(m, n-1)


def harmonic(n: int) -> float:              
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)
    


def get_binary(x: int) -> str:         
    if x == 0: 
        return "0"
    elif x == 1:
        return "1"
    elif x < 0:
        return "-" + get_binary(-x)
    
    else:
        return get_binary(x//2) + f"{x%2}" 

def reverse_string(s: str) -> str:        
    if s == "":
        return ""
    else: 
        return s[-1] + reverse_string(s[0:-1])

def largest(a: iter):                     
    if len(a) == 1: 
        return a[0]
    elif a[0] >= a[-1]:
        return largest(a[:-1])
    elif a[0] < a[-1]:
        return largest(a[1:])

def count(x, s: list) -> int: 
    if s == []:
        return 0
    if s[0] == x: 
        return 1 + count(x, s[1:])
    elif isinstance(s[0],list):
        return count(x, s[0]) + count(x, s[1:])
    else: 
        return count(x, s[1:])



def bricklek(f: str, t: str, h: str, n: int) -> str:
    if n==1: return [f"{f}->{t}"]
    elif n > 1: return bricklek(f, h, t, n-1) + [f'{f}->{t}'] + bricklek(h, t, f, n-1)
    else: return []


def fib(n: int) -> int:                      
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fib_time_est(n):
    PHI = 1.618033988749895
    time1 = time.perf_counter()
    fib(36)
    time2 = time.perf_counter()
    calctime = time2 - time1
    return calctime*PHI**(n-36)

def fib2(n):
    memory = {0:0, 1:1}
    def fib_mem2(n):
        if n not in memory:
            memory[n] = fib_mem2(n-1) + fib_mem2(n-2)
        return memory[n]
    return fib_mem2(n)


def main():
    print('\nCode that demonstates my implementations\n')

    print('\n\nCode for analysing fib and fib_mem\n')
    PHI = 1.618033988749895
    #### exponetional test
    t0 = time.perf_counter()
    fib(32)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    fib(31)
    t3 = time.perf_counter()
    calctime1 = t1 -t0
    calctime2 = t3 -t2

    print(f'phi {calctime1/calctime2}') #checks if the relation is 1.6^n
    #### fib time estimation
    print(f'{fib_time_est(50)/(60*60)} hours to comput fib 50')
    print(f'{fib_time_est(100)/(60*60*24*365)} years to compute fib 100')
    #### fib with memory
    memtime1 = time.perf_counter()
    fib2(100)
    memtime2 = time.perf_counter()
    print(f'fib2 100 time {(memtime2-memtime1)/1000} ms')
    print(f'fib2 100: {fib2(100)}')
    ####
    print('\nBye!')

if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
  2**50 -1 seconds
  36 000 000 years
  
  
  Exercise 9: Time for Fibonacci:
  a) see main()

  b)
  fib n=50 : 2.6 hours
  fib n=100 : 8 000 000 years
  

  
  
  Exercise 10: Time for fib_mem:
  
  
  
  
  
  Exercise 11: Comparison sorting methods:
  theta = c n log n 
  c 1000 log10 1000 = 1s
  c = 1/(1000*3)
  merge n=10^6 : 33 minutes
  insertion n=10^6 : 12 days
  
  merge n=10^9 : 35 days
  insertion n=10^9 : 32000 years
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
  c = 0.1
  0.1 n log n = n
  log n = 10
  answer:
  For n > 10**10, A is faster than B
"""
