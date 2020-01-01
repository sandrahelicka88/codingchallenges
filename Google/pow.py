import unittest
'''Implement pow(x, n), which calculates x raised to the power n (xn).'''

def myPower(x,n):
    if n == 0:
        return 1
    elif n<0:
        return 1/myPower(x,-n)
    elif n%2:
        return x * myPower(x, n-1)
    else:
        return myPower(x*x, n//2)
        

print(myPower(3,3))


class Test(unittest.TestCase):
    def test_myPower(self):
        output = myPower(2.00000, 10)
        self.assertEqual(output, 1024.00000)
        output1 = myPower(2.10000, 3)
        self.assertEqual(round(output1,5), 9.26100)
        output2 = myPower(2.00000, -2)
        self.assertEqual(output2, 0.25000)
        output3 = myPower(34, 0)
        self.assertEqual(output3,1)

if __name__ == '__main__':
    unittest.main()