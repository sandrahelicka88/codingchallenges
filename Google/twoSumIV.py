import unittest
'''Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.'''

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def helper(root,seen,k):
    if root == None:
        return
    if k-root.val in seen:
        return True
    seen.append(root.val)
    if helper(root.left, seen,k) or helper(root.right,seen,k):
        return True
    return False


def twoSum(root, k):
    return helper(root, [], k)


root = Node(5)
left = Node(3)
right = Node(6)
root.left = left
root.right = right
leftLeft = Node(2)
leftRight = Node(4)
rightRight = Node(7)
left.left = leftLeft
left.right = leftRight
right.right = rightRight

class Test(unittest.TestCase):
    def test_twoSum(self):
        output = twoSum(root,9)
        self.assertTrue(output)
        output2 = twoSum(root,3)
        self.assertFalse(output2)


if __name__ == '__main__':
    unittest.main()