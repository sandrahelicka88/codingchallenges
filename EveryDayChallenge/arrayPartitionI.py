import unittest
'''Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.'''

def arrayPairSum(nums):
    nums.sort()
    result = 0
    for i in range(len(nums)):
        if i%2 ==0:
            result+=nums[i]
    return result

class Test(unittest.TestCase):
    def test_arrayPairSum(self):
        output = arrayPairSum([1,4,3,2])
        self.assertEqual(output,4)
        output2 = arrayPairSum([4,3,8,9])
        self.assertEqual(output2,11)
        output3 = arrayPairSum([2,3])
        self.assertEqual(output3,2)

if __name__ =='__main__':
    unittest.main()