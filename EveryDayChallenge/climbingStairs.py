import unittest

'''You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.'''

def climbStairs(n):
    a = 1
    b = 1
    for i in range(2,n+1):
        sum = a+b
        a = b
        b = sum
    return b

class Test(unittest.TestCase):
    def test_stairs(self):
        output = climbStairs(3)
        self.assertEqual(output,3)
        output2 = climbStairs(12)
        self.assertEqual(output2,233)


if __name__ == '__main__':
    unittest.main()