import unittest
'''Given an integer n, return the number of trailing zeroes in n!.'''

def trailingZeroes(n):
        count = 0
        while n != 0:
            tmp = n//5
            n = tmp
            count += tmp
            
        return count

class Test(unittest.TestCase):
    def test_trailingZeroes(self):
        output = trailingZeroes(3)
        self.assertEqual(output,0)
        output = trailingZeroes(5)
        self.assertEqual(output,1)


if __name__ == '__main__':
    unittest.main()
