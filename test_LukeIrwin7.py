import unittest
from LukeIrwin7_1 import *

class TestLab7(unittest.TestCase):

    def test_one(self):
        '''
        Method to test the one function and to make sure it raises the correct errors
        '''
        self.assertEqual(one(1), 1)
        self.assertEqual(one(2), 3)
        self.assertEqual(one(3), 6)
        self.assertEqual(one(4), 10)

        with self.assertRaises(TypeError):
            one('2')
            one('s')
            one(True)
            one(2.1)
            one(None)
            one()

    def test_two(self):
        '''
        Method to test the two function and to make sure it raises the correct errors
        '''
        self.assertEqual(two(2, 1), 2)
        self.assertEqual(two(2, 2), 4)
        self.assertEqual(two(2, 3), 8)
        self.assertEqual(two(3, 4), 81)

        with self.assertRaises(TypeError):
            two('s', 2)
            two(2, 's')
            two(2.1, 2)
            two(2, 2.1)
            two(2, True)
            two(True, 2)
            two(2, None)
            two(None, 2)
            two(2)
            two()


    def test_three(self):
        '''
        Method to test the three function and to make sure it raises the correct errors
        '''
        self.assertEqual(three(5), '5 4 3 2 1')
        self.assertEqual(three(10), '10 9 8 7 6 5 4 3 2 1')

        with self.assertRaises(TypeError):
            three('2')
            three('s')
            three(True)
            three(2.1)
            three(None)
            three()

if __name__ == '__main__':
    unittest.main()