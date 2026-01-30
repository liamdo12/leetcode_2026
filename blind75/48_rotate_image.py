# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


'''
this is naive solution 

3x3
arr[0][0] = arr[0][2]
arr[0][1] = arr[1][2]
arr[0][2] = arr[2][2]

arr[1][0] = arr[0][1]
arr[1][1] = arr[1][1]
arr[1][2] = arr[2][1]

arr[2][0] = arr[0][0]
arr[2][1] = arr[1][0]
arr[2][2] = arr[2][0]

=> arr[row][col] = arr[col][n--]

'''


class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        arr = [[None] * n for _ in range(n)]

        total_col = n - 1
        start = 0

        while total_col >= 0:
            for i in range(n):
                arr[i][total_col] = matrix[start][i]
            
            start += 1
            total_col -= 1

        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[i][j]


matrix = [[1,2,3],[4,5,6],[7,8,9]]

# a = Solution()
# a.rotate(matrix)
# print(matrix)


'''
the idea is to control how many rows (i) we process when rotating the matrix in place
each iteration rotates 4 cells at once: top => right => bottom => left => top
so we only need to process half of the matrix, not all cells

for n is even (n = 4)
n = 4 => n // 2 = 2 => n % 2 = 0 
=> n // 2 + n % 2 = 2
=> for i in range(2) => we only need the top half

for n is odd (n = 5)
n = 5 => n // 2 = 2 => n % 2 = 1
=> n // 2 + n % 2 = 3
=> for i in range(3) => we include the rows (i = 2) because it in the middle rows and still need rotation


for j in range(n // 2) => the number of columns we need to process

clockwise rotation

top pos: (i, j)
right pos: (j, n - 1 - i)
bottom pos: (n - 1 - i, n - 1 - j)
left : (n - 1 - j, i)



top => right => bottom => left

.  .  T  .  .
.  .  .  .  .
.  L  .  R  .
.  .  B  .  .
.  .  .  .  .

'''

class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)

        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i] # bottom left
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1] # bottom right
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i] # top right
                matrix[j][n - 1 - i] = matrix[i][j] 
                matrix[i][j] = tmp # top left

matrix = [[1,2,3],[4,5,6],[7,8,9]]
            
a = Solution()
a.rotate(matrix)



