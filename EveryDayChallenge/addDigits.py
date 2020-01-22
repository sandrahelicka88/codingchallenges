import unittest

'''Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.'''

def addDigit(num):
    while num>=10:
        if num ==0:
            return 0
        elif num%9==0:
            return 9
        else:
            num = num%9
    return num


class Test(unittest.TestCase):
    def test_addDigits(self):
        output = addDigit(9)
        self.assertEqual(output,9)
        output2 =addDigit(38)
        self.assertEqual(output2,2)
        output3 = addDigit(123)
        self.assertEqual(output3,6)



if __name__ == '__main__':
    unittest.main()