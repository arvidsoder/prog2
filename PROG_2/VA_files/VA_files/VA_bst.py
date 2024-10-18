"""
Solutions to module VA bst

Student:
Mail:
"""
import random
import matplotlib.pyplot as plt
import math
import numpy as np
class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

    def height(self):                 #            
        n = self.root
        def _height(node):
            if node == None:
                return 0
            else: 
                return 1 + max(_height(node.left),_height(node.right))
        return _height(n)

    def ipl(self):    
        node = self.root
        level = 1
        def _ipl(node, level):
            if node == None:
                return 0
            else:
                return level + _ipl(node.left, level + 1) + _ipl(node.right, level + 1)
        return _ipl(node,level)

def random_tree(n):                               # Useful
    tree = BST()
    for _ in range(n):
        number = random.random()
        tree.insert(number)
    return tree
        


def main():
    nlst=[]
    heigt= []
    ipllist = []
    loglist = []
    for i in range(1,10):
        n = 1000*2**i
        t = random_tree(n)
        nlst.append(n)
        heigt.append(t.height())
        ipllist.append(t.ipl()/n)
        loglist.append(np.log2(n))
        print(f'N: {n}')
        print(f'Height {t.height()}')
        print(f'IPL/n {t.ipl()/n}')
        print(f'1.39*log2(n) =  {1.39*np.log2(n)}')
    nplst = np.array(nlst)
    npheigt = np.array(heigt)

#nlst,heigt,nlst, np.log10(np.array(nlst))/(np.log10(1.39)), 
    plt.plot(nlst,np.array(ipllist),nlst ,1.39*np.array(loglist))
    plt.plot(nlst, heigt, nlst, 2.5*np.log2(nplst))
    plt.legend(['ipl/n','theory 1.39*log2(n)','height', 'theory 2.5*log2(n)'])
    plt.show()
    


if __name__ == "__main__":
    main()


"""

Results for ipl of random trees
===============================
How well does that agree with the theory?
It agrees well.
What can you guess about the
height?
In a balanced tree, for every height increase there will be an additional 2^h nodes, h = height
The height is then = O(log2(n))
"""
