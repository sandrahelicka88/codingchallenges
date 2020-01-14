import unittest
'''You are given 2D grid MxN initialized with three possible values:
-1 -wall or an obstcle,
0 -gate,
INF means an empty room.
Fill each empty room with a distance to its nearest gate. If its impossible to reach the gate, it should be filled with INF.'''


def dfs(i,j,count, matrix):
    if i <0 or i>=len(matrix) or j<0 or j>=len(matrix[i]) or matrix[i][j]<count:
        return
    matrix[i][j] = count
    dfs(i+1,j,count+1, matrix)
    dfs(i-1,j,count+1, matrix)
    dfs(i,j+1, count+1, matrix)
    dfs(i,j-1, count+1, matrix)



def wallsGates(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                dfs(i,j,0,matrix)
    return matrix

print(wallsGates([['INF',-1,0,'INF'],
                ['INF', 'INF', 'INF',-1],
                ['INF', -1,'INF', -1],
                [0, -1, 'INF', 'INF']]
            ))

    
class Test(unittest.TestCase):
    def test_wallsGates(self):
        output = wallsGates([['INF',-1,0,'INF'],
                ['INF', 'INF', 'INF',-1],
                ['INF', -1,'INF', -1],
                [0, -1, 'INF', 'INF']])
        self.assertEqual(output, [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]])

if __name__ == '__main__':
    unittest.main()