import unittest
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
def dfs(grid,i,j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j] == '0':
        return 0
    grid[i][j]='0'
    dfs(grid,i+1,j)
    dfs(grid, i-1,j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)
    return 1

def numOfIslands(grid):
    islands = 0
    if len(grid) == 0 or grid == None:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                islands+= dfs(grid, i, j)
    return islands

grid1 = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0'],
    ]
grid2 = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1'],
    ]

class Test(unittest.TestCase):
    def test_islands(self):
        output1 = numOfIslands(grid1)
        self.assertEqual(output1,1)
        output2 = numOfIslands(grid2)
        self.assertEqual(output2,3)

if __name__ == '__main__':
    unittest.main()


print(numOfIslands(grid2))