# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_arr = []

        numb = n

        while numb > 0:
            result = numb % 2
            binary_arr.append(result)
            numb = numb // 2
        
        return sum(binary_arr)
    

n = 128
a = Solution()
print(a.hammingWeight(n))
