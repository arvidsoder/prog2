"""
Solutions to module VA 1
Student: 
Mail:
"""
import sys


def exchange(a, coins):
    mem = {}

    def _exchange(a, coins:tuple) -> int : 
        """ Count possible way to exchange a with the coins in coins. Use memoization"""
        arg = (a, coins)
        if arg in mem:
            return mem[arg]
        if a == 0:
            return 1
        if (len(coins) == 0) or (a < 0): 
            return 0
        
        mem[arg] = _exchange(a, coins[1:]) + _exchange(a-coins[0], coins)
        return mem[arg]
    
    return _exchange(a, coins)

def zippa(l1: list, l2: list) -> list: 
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    if len(l1) == 0:
        return l2[:]
    if len(l2) == 0:
        return l1[:]
    return [l1[0], l2[0]] + zippa(l1[1:], l2[1:])




def main():
    sys.setrecursionlimit(1000000)
    l1 = [1, 3, 5, 7, 9]
    l2 = [2, 4, 6, 2]
    print('\nCode that demonstates my implementations\n')
    print(zippa(l1,l2))
    print(min([2,5]))

if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 1

What time did it take to calculate large sums such as 1000 and 2000? 

What happens if you try to calculate e.g. 10000?
  
"""
