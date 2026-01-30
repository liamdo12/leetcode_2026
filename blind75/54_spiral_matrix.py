# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix):
        n = len(matrix)
        result = []

        rows = len(matrix)
        cols = len(matrix[0])
        up = left = 0
        right = cols - 1
        down = rows - 1

        while len(result) < rows * cols:
            # move from left to right
            for i in range(up, right + 1):
                result.append(matrix[up][i])
            
            # move from top right to bottom right
            for i in range(up + 1, down + 1):
                result.append(matrix[i][right])

            if up != down:
                # move from bottom right to bottom left
                for i in range(right - 1, left, -1):
                    result.append(matrix[down][i])

            if left != right:
                # move from bottom left to top left
                for i in range(down, up, -1):
                    result.append(matrix[i][left])

            up += 1
            left += 1
            right -= 1
            down -= 1

        return result
    


a = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result = a.spiralOrder(matrix)
print(result)









'''
0, 0
0, 1
0, 2
0, 3
1, 3
2, 3
2, 2
2, 1
2, 0
1, 0
1, 1
1, 2


0, 0
0, 1
0, 2
0, 3
1, 3
2, 3
2, 2
2, 1
2, 0
1, 0
1, 1
1, 2



total rows = n
total col = n - 1

'''