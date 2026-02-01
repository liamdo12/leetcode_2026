# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.


# Input: grid = [[0,1],[1,0]]
# Output: 2

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1

'''
Let N be the number of cells in the grid.

Time complexity: O(N)
Space complexity: O(N)
'''


from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:

        n = len(grid)
        m = len(grid[0])

        start_row = 0
        start_col = 0

        end_row = n - 1
        end_col = m - 1

        if grid[start_row][start_col] == 1 or grid[end_row][end_col] == 1:
            return -1

        visited = set()
        q = deque([(start_row, start_col, 1)])

        visited.add((start_row, start_col))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        while q:
            row, col, step = q.popleft()
            if (row, col) == (end_row, end_col):
                return step
            
            for dr, dc in directions:
                next_r, next_c = row + dr, col + dc

                if 0 <= next_r < n and 0 <= next_c < m and grid[next_r][next_c] != 1 and (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    q.append((next_r, next_c, step + 1))

        return -1


grid = [[0,0,0],[1,1,0],[1,1,0]]
a = Solution()
result = a.shortestPathBinaryMatrix(grid)
print(result)
