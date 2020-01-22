import unittest

'''Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.'''

def asingCook(g,s):
    g.sort()
    s.sort()
    a_pointer = 0
    b_pointer = 0
    while a_pointer<len(g) and b_pointer<len(s):
        if g[a_pointer]<=s[b_pointer]:
            a_pointer+=1
            b_pointer+=1
        else:
            b_pointer+=1
    return a_pointer


class Test(unittest.TestCase):
    def test_asignCook(self):
        output = asingCook([1,2,3],[1,1])
        self.assertEqual(output,1)
        output2 = asingCook([1,2],[1,2,3])
        self.assertEqual(output2,2)


if __name__ =='__main__':
    unittest.main()