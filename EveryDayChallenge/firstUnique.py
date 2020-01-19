import unittest
'''Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.'''
def uniqueChar(string):
    lookUp = {}
    for ch in string:
        if ch in lookUp:
            lookUp[ch]+=1
        else:
            lookUp[ch]=1
    
    for index, char in enumerate(string):
        if lookUp[char]==1:
            return index
    return -1


class Test(unittest.TestCase):
    def test_uniqueChar(self):
        output = uniqueChar('leetcode')
        self.assertEqual(output,0)
        output2 = uniqueChar('loveleetcode')
        self.assertEqual(output2,2)
        output3 = uniqueChar('babajagajaga')
        self.assertEqual(output3,-1)

if __name__ == "__main__":
    unittest.main()