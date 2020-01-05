import unittest
'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(3)
node1 = TreeNode(1)
node4 = TreeNode(4)
node2 = TreeNode(2)
root.left = node1
root.right = node4
node1.right = node2

root2 = TreeNode(5)
nodeleft = TreeNode(3)
nodeRight = TreeNode(6)
root2.left = nodeleft
root2.right = nodeRight
leftLeft = TreeNode(2)
rightRight = TreeNode(4)
nodeleft.left = leftLeft
nodeleft.right = rightRight
nodeleft1 = TreeNode(1)
leftLeft.left = nodeleft1

def findkthSmallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k-=1
        if k == 0:
            return root.data
        root = root.right

class Test(unittest. TestCase):
    def test_kthsmall(self):
        output = findkthSmallest(root,2)
        self.assertEqual(output,2)
        output2 = findkthSmallest(root,1)
        self.assertEqual(output2,1)
        output3 = findkthSmallest(root2,3)
        self.assertEqual(output3,3)
        output4 = findkthSmallest(root2,1)
        self.assertEqual(output4,1)

if __name__ == '__main__':
    unittest.main()