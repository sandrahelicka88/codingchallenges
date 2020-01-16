import unittest
'''Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def node_toList(node):
    list_form = []
    if node ==None:
        return []
    while node:
        list_form.append(node.val)
        node = node.next
    return list_form

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

class Test(unittest.TestCase):
    def test_deleteNode(self):
        output = deleteNode(n3)
        self.assertEqual(node_toList(n1),[1,2,4,5])
        output2 = deleteNode(n1)
        self.assertEqual(node_toList(n1),[2,4,5])

if __name__ == '__main__':
    unittest.main()