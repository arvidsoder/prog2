import math

def factorial(x:int) -> int:
    """this function is fucking awesome and based!!!!"""
    if x > 1:
        return x*factorial(x-1)
    else:
        return 1
c1 = 1/(1000*3)
n1 = 10**6
mergeT1 = c1*n1*math.log10(n1)
c2 = 1/(1000**2)
insertionT1 = c2*n1**2
print(mergeT1/60)
print(insertionT1/(3600*24))

n2 = 10**9
mergeT2 = c1*n2*math.log10(n2)
insertionT2 = c2*n2**2
print(mergeT2/(3600*24))
print(insertionT2/(3600*24*365))
print('--')
print((2**50 -1)/(3600*24*365))
n = 10**10

