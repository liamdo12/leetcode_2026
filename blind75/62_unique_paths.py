# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.


# solution 1: 
# To such cell one could move
# either from the cell on the left (m, n - 1), or from the cell above
# (m - 1, n). That means that the total number of paths to move into (m, n) cell
# is uniquePaths(m - 1, n) + uniquePaths(m, n - 1).
# this is naive solution

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
    

# solution 2
# DP solution
# the idea is Initiate 2D array d[m][n] = number of paths. To start, put number of paths
# equal to 1 for the first row and the first column.
# For the simplicity, one could initiate the whole 2D array by ones.

# Iterate over all "inner" cells: d[col][row] = d[col - 1][row] + d[col][row - 1]
# time complexity: O(m x n)
# space complexity: O(m x n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                dp[col][row] = dp[col - 1][row] + dp[col][row - 1]

        # this is the final block
        return dp[m - 1][n - 1]
    

    