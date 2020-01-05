import unittest

'''A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] != nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = ~'''

def findP(nums):
    left = 0
    right = len(nums)-1
    while left<right:
        middle = (left+right)//2
        if nums[middle]>nums[middle-1] and nums[middle]>nums[middle+1]:
            return middle
        
        if nums[middle]<nums[middle+1]:
            left = middle+1
        else:
            right = middle-1
    return left


class Test(unittest.TestCase):
    def test_peak(self):
        output = findP([1,2,3,1])
        self.assertEqual(output,2)
        output2 = findP([1,2,1,3,5,6,4])
        self.assertEqual(output2,5)


if __name__ == '__main__':
    unittest.main()
