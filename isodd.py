import unittest


def IsOdd(n):
    return bool(n & 1)

print (IsOdd(12))

class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(IsOdd(1))

    def testTwo(self):
        self.assertFalse(IsOdd(2))

def main(): 
    unittest.main()

if __name__ == '__main__':
    main()               








