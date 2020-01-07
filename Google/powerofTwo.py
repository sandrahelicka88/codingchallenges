import unittest
'''Given an integer, write a function to determine if it is a power of two.'''

def powerTwo(x):
    i=1
    while i<x:
        i*=2
    return i == x

class Test(unittest.TestCase):
    def test_poweroftwo(self):
        output = powerTwo(1)
        self.assertTrue(output)
        output2 = powerTwo(1024)
        self.assertTrue(output2)
        output3 = powerTwo(218)
        self.assertFalse(output3)


       

if __name__ == '__main__':
    unittest.main()
    