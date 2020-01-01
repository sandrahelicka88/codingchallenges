import unittest
'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]'''


def generateParenth(n):
    ans = []
    def helper(s,left, right):
        if len(s) == 2 *n:
            ans.append(s)
            return ans
        if left<n:
            helper(s+'(', left+1, right)
        if right<left:
            helper(s+')', left, right+1)
    helper('',0, 0)
    return ans

class Test(unittest.TestCase):
    def test_parenthesisPermutation(self):
        output = generateParenth(0)
        self.assertEqual(output, [''])
        output1 = generateParenth(1)
        self.assertEqual(output1, ['()'])
        output2 = generateParenth(3)
        self.assertEqual(output2, ['((()))', '(()())', '(())()', '()(())', '()()()'])


if __name__ == '__main__':
    unittest.main()


