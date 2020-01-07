import unittest

'''Given a binary tree, return all root-to-leaf paths.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def dfs(root, path, paths):
    path+=str(root.data)
    if root.left == None and root.right == None:
        paths.append(path)
    if root.left:
        dfs(root.left, path+'->', paths)
    if root.right:
        dfs(root.right, path+'->', paths)


def binaryTreePaths(root):
    paths = []
    if root == None:
        return paths
    dfs(root, '', paths)
    return paths



root = Node(5)
nodeL = Node(7)
nodeR = Node(10)
root.left = nodeL
root.right = nodeR
leftleft = Node(13)
nodeL.left = leftleft
rightright = Node(18)
nodeR.left = rightright


class Test(unittest.TestCase):
    def testPaths(self):
        output = binaryTreePaths(root)
        self.assertEqual(output, ['5->7->13', '5->10->18'])


if __name__ == '__main__':
    unittest.main()