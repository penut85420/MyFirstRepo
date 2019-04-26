from myObject import myObject
import unittest

class myObject_test(unittest.TestCase):

    def test_add(self):
        self.assertEqual(myObject(3, 5).add(), 8)

    def test_sub(self):
        self.assertEqual(myObject(3, 5).sub(), -2)

    def test_mul(self):
        self.assertEqual(myObject(3, 5).mul(), 15)

    def test_div(self):
        self.assertEqual(myObject(3, 5).div(), 0)

if __name__ == '__main__':
    unittest.main()