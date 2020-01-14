import unittest
'''There are a row of n houses, each house can be painted with one of the three colors:red,blue or green. The cost of painting each house of certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house is representing by a nx3 cost matrix. For example costs [0][0] is the cost of painting house 0 with color red, costs[1][2] is the cost of painting house 1 with the color green, and so on... Find the minimum cost to paint all houses.'''

def minCost(matrix):
    if len(matrix) == 0 or matrix == None:
        return 0
    
    for i in range(1, len(matrix)):
        matrix[i][0] += min(matrix[i-1][1], matrix[i-1][2])
        matrix[i][1] += min(matrix[i-1][0], matrix[i-1][2])
        matrix[i][2] += min(matrix[i-1][0], matrix[i-1][1])
    
    return min(min(matrix[i][0], matrix[i][1]), matrix[i][2])


print(minCost([[17,2,17],[16,16,5],[14,3,9]]))

    
class Test(unittest.TestCase):
    def test_minCost(self):
        output = minCost([[17,2,17],[16,16,5],[14,3,9]])
        self.assertEqual(output,10)


if __name__ == '__main__':
    unittest.main()