import unittest
'''Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.'''

def isHappy(n):
    path = set()
    while n not in path and n!=1:
        path.add(n)
        nextSum = 0
        while n:
            nextSum+=(n%10)**2
            n = n//10
        n = nextSum
    return n==1

class Test(unittest.TestCase):
    def test_happyNumber(self):
        self.assertTrue(isHappy(19))

if __name__ == '__main__':
    unittest.main()

