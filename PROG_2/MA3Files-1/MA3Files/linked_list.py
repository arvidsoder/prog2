""" linked_list.py

Student:
Mail:
Reviewed by: Divya Shridar
Date reviewed:
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):          #   
        if self.first == None:
            return 0
        f = self.first
        result = 1
        while f.succ:
            result +=1
            f = f.succ
        return result
    
    def mean(self):               
        pass

    def remove_last(self):       # 
        if self.first == None:
            raise ValueError("empty list xD troolololoololo")
        elif self.first.succ == None:
            last_value = self.first.data
            self.first = None
            return last_value
        f = self.first
        while f.succ.succ:
            f = f.succ
        last_value = f.succ.data
        f.succ = None
        return last_value

    def remove(self, x):         #
        if self.first == None: return False
        if x == self.first.data:
            self.first = self.first.succ
            return True
        f = self.first
        while f.succ:
            if x == f.succ.data:
                f.succ = f.succ.succ
                return True
            f = f.succ
        return False
    
    def to_list(self):
        if self.first == None:
                return []
        f = self.first
        def _to_list(node):
            if node.succ != None:
                return [node.data] + _to_list(node.succ)
            else:
                return [node.data]
        return _to_list(f)

    def remove_all(self, x):      #
        if self.first == None:
            return 0
        f = self.first
        def _remove_all(node, x):
            if (node == self.first) and (x == node.data):
                self.first = node.succ
                if self.first == None: return 0
                else: return 1 + _remove_all(node.succ, x)

            if node.succ == None:
                return 0
            if x == node.succ.data:
                node.succ = node.succ.succ
                return 1 + _remove_all(node, x)
            else:
                return _remove_all(node.succ, x)
        return _remove_all(f, x)

    def __str__(self):            #
        result = ""
        for i in self:
            result += str(i) + ", "
        return "(" + result[0:-2] + ")"

    def copy(self):               #
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 
        o(n^2) ??
    '''

    def copy2(self):               # Should be more efficient
        result = LinkedList()
        result.first = self.first
        f = self.first
        if f == None or f.succ == None: return result
        f = f.succ
        while f.succ:
            result.Node(f.data, f.succ)
            f = f.succ
        return result
    ''' Complexity for this implementation:
        o(n)
    '''

def main():
    lst = LinkedList()
    for x in [6,6]:
        lst.insert(x)
    lst.print()
    print(lst.remove_all(6))
    print(lst)
    link2 = lst.copy2()
    lst.remove_all(1)
    print(link2)
    print(lst)
    # Test code:

if __name__ == '__main__':
    main()
