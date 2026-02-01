# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two cells sharing a common edge is 1.

# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

'''
Time complexity O(n * m)
Space complexity O(m * n)
'''


from collections import deque

class Solution:
    def updateMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])
        q = deque()
        dirs = ([0, 1], [1, 0], [0, -1], [-1, 0])
        seen = set()
        result = [[0] * m for _ in range(n)]

        for row in range(n):
            for col in range(m):
                if mat[row][col] == 0:
                    q.append((row, col, 0))
                    seen.add((row, col))

        while q:
            row, col, dist = q.popleft()
            
            for direction_row, direction_col in dirs:
                nrow, ncol = row + direction_row, col + direction_col
                if 0 <= nrow < n and 0 <= ncol < m and (nrow, ncol) not in seen:
                    seen.add((nrow, ncol))
                    q.append((nrow, ncol, dist + 1))
                    result[nrow][ncol] = dist + 1
        
        return result
    
a = Solution()
mat = [[0,0,0],[0,1,0],[0,0,0]]
result = a.updateMatrix(mat)
print(result)