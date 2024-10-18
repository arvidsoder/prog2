# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_count(self):
        ''' Reasonable tests
        1. search empty lists
        2. count first, last and interior elements
        3. search for a list
        4. check that sublists on several levels are searched
        5. search non existing elements
        6. check that the list searched is not destroyed
        '''
        self.assertEqual(count(2, []), 0)
        self.assertEqual(count(1, [1, 2, 1]), 2)
        self.assertEqual(count(7, [1, 2, [4, 7], 4, [4], 7]), 2)
        self.assertEqual(count(7, [2, 7, [1, 7, [1, 7], 2], 2]), 3)
        self.assertEqual(count(7, [[[7]]]), 1)
        self.assertEqual(count(7, [[2,2], 1, 3]), 0)
        self.assertEqual(count([2,2], [[2,2], 1, 3]), 1)
        test_list = [2, 1 , 2, 7, 1, [2, 1, 2 , 7], 0, 5]
        test_list2 = test_list
        testN = count(1, test_list)
        self.assertEqual(test_list, test_list2)
        print('\nTests count')
        print('*** Should be implemented!***')


if __name__ == "__main__":
    unittest.main()