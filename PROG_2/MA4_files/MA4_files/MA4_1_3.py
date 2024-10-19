
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
import functools
import concurrent.futures as futures
import time as t

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    ns = 0
    for _ in range(n):
        points = [r.uniform(-1,1) for _ in range(d)]
        if functools.reduce(lambda x, y : x+y, map(lambda x: x**2 ,points)) <= 1 :
            ns += 1
    vol = (ns*2**d)/n
    return vol

def hypersphere_exact(n,d):
    return m.pi**(d/2)/m.gamma(d/2 + 1)

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    #using multiprocessor to perform 10 iterations of volume function
    with futures.ProcessPoolExecutor() as ex:
        futur = [ex.submit(sphere_volume, n, d) for _ in range(np)]
        results = map(lambda x: x.result(), futur)
    result = sum(results)/np
    return result


# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    with futures.ProcessPoolExecutor() as ex:
        futur = [ex.submit(sphere_volume, round(n/np), d) for _ in range(np)]
        results = map(lambda x: x.result(), futur)
    result = sum(results)/np
    return result

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    time1 = t.perf_counter()
    for y in range (10):
        sphere_volume(n,d)
    time2 = t.perf_counter()
    print(f'part 1 series: {time2 - time1}')

    time1parallell = t.perf_counter()
    sphere_volume_parallel1(100000,11,10)
    time2parallell = t.perf_counter()
    print(f'part 1 parallell: {time2parallell - time1parallell}')

if __name__ == '__main__':
	main()
