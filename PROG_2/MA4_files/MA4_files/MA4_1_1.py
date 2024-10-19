
"""
Solutions to module 4
Review date:
"""

student = "Arvid Söderström"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math
import concurrent.futures as futures
import time

def approximate_pi(n):
    points_inside_x = []
    points_inside_y = []
    points_outside_x = []
    points_outside_y = []
    n_inside_circle = 0
    for i in range(n):
        point_x = r.uniform(-1,1)
        point_y = r.uniform(-1,1)
        if (point_x**2 + point_y**2) <= 1:
            n_inside_circle += 1
            points_inside_x.append(point_x)
            points_inside_y.append(point_y)
        else:
            points_outside_x.append(point_x)
            points_outside_y.append(point_y)

    pi_approx = 4*(n_inside_circle/n)
    approximate_pi.in_x = points_inside_x
    approximate_pi.in_y = points_inside_y
    approximate_pi.out_x = points_outside_x
    approximate_pi.out_y = points_outside_y
    return pi_approx

def main():
    dots = [1000, 10000, 100000]
    
    for n in dots:
        pi = approximate_pi(n)
        plt.plot(approximate_pi.in_x, approximate_pi.in_y, 'o', color = 'r')
        plt.plot(approximate_pi.out_x, approximate_pi.out_y, 'o', color = 'b')
        plt.show()
    print(f'PI: {math.pi}')
    
    '''
    timer1 = time.perf_counter()
    with futures.ProcessPoolExecutor() as ex:
        p = [1000, 10000, 100000]
        results = ex.map(approximate_pi, p)
    for r in results:
        print(r)
    timer2 = time.perf_counter()
    print(f'Time: {round(timer2 - timer1,3)}')
    '''
if __name__ == '__main__':
	main()
