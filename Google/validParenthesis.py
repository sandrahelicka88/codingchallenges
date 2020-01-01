import unittest
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.'''

def isValid(s):
    if len(s)==0 or s == None:
        return True
    stack = []
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        elif ch == ')' and len(stack)!=0 and stack[-1]=='(':
            stack.pop()
        elif ch == ']' and len(stack)!=0 and stack[-1] == '[':
            stack.pop()
        elif ch == '}' and len(stack)!=0 and stack[-1] == '{':
            stack.pop()
        else:
            return False
    return len(stack)==0

a = ['','()', '({})', '()[]']
b = ['(','(]', '([}}']
class Test(unittest.TestCase):
    def test_validParenthesis(self):
        for string in a:
            self.assertTrue(isValid(string))
        for string in b:
            self.assertFalse(isValid(string))
        
if __name__ == '__main__':
    unittest.main()