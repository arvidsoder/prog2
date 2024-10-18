""" bst.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""


from linked_list import LinkedList


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

    def __iter__(self):         # Dicussed in the text on generators
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

    def contains(self, k): #
        n = self.root
        def _contains(node, k):
            if node == None:
                return False
            if k == node.key:
                return True
            if k < node.key: 
                return _contains(node.left, k)
            if k > node.key:
                return _contains(node.right, k)
        return _contains(n, k)

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                 #            
        n = self.root
        def _height(node):
            if node == None:
                return 0
            else: 
                return 1 + max(_height(node.left),_height(node.right))
        return _height(n)
    
    def in_order_succ(self, root):
        root = root.right
        while (root != None) and (root.left != None):
            root = root.left
        return root

    def remove(self, key): #
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      #
        if r is None:
            return None
        elif k < r.key:
            r.left =  self._remove(r.left, k) # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k) # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:                                   # This is the tricky case.
                successor = self.in_order_succ(r)
                r.key = successor.key               # Put that key in this node
                r.right = self._remove(r.right, successor.key)  # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):                #            
        result = ""
        for i in self:
            result += str(i) + ", "
        return "<" + result[0:-2] + ">"

    def to_list(self):                      # o(n)    
        result = []
        for i in self:
            result.append(i)
        return result

    def to_LinkedList(self):                 # o(n^2)
        result = LinkedList()
        for i in self:
            result.insert(i)
        return result


def random_tree(n):                               # Useful
    pass


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print(t.to_list())

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")
    


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? yes because it can simply iterate through the BST and add 1
2. computing height? no because it needs to compare the height of each subtree, maybe if you know which level each node is at
3. contains? yes because it can search by iterating
4. insert? no
5. remove? no
"""
