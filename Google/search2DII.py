import unittest

'''Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.'''


def searchMatrix(matrix, target):
    if len(matrix) == 0 or matrix == None:
        return False
    row = 0
    col = len(matrix[0])-1
    while row <len(matrix) and col>=0:
        if matrix[row][col] == target:
            return True
        if matrix[row][col]>target:
            col-=1
        else:
            row+=1
    return False

matrixA = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
class Test(unittest.TestCase):
    def test_searchMatrix(self):
        output = searchMatrix(matrixA, 25)
        self.assertFalse(output)
        output2 = searchMatrix(matrixA, 14)
        self.assertTrue(output2)

if __name__ == '__main__':
    unittest.main()