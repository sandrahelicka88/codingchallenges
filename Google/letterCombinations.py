import unittest

'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]'''

def letterCombinations(digits):
    result = []
    if len(digits)==0 or digits == None:
        return result
    mapping = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    combo(digits, mapping, result, '', 0)
    return result

def combo(digits, mapping, result, current, index):
    if index == len(digits):
        result.append(current)
        return
    letters = mapping[int(digits[index])]
    for i in range(len(letters)):
        combo(digits, mapping, result, current+letters[i], index+1)


class Test(unittest.TestCase):
    def test_letterCombin(self):
        output1 = letterCombinations('23')
        self.assertEqual(output1, ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        output2 = letterCombinations('')
        self.assertEqual(output2, [])
        output3 = letterCombinations('78')
        self.assertEqual(output3, ['pt', 'pu', 'pv', 'qt', 'qu', 'qv', 'rt', 'ru', 'rv', 'st', 'su', 'sv'])


    


if __name__ == '__main__':
    unittest.main()