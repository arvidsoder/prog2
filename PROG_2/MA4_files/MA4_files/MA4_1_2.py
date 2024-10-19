
"""
Solutions to module 4
Review date:
"""

student = "Arvid Söderström"
reviewer = ""

import math as m
import random as r
import concurrent.futures as futures
import functools

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

def hypersphere_exact(n, d):
    return m.pi**(d/2)/m.gamma(d/2 + 1)

def main():
    n = 1000000
    d = 11
    
    print(sphere_volume(n,d))
    print(hypersphere_exact(n,d))
    

if __name__ == '__main__':
	main()
