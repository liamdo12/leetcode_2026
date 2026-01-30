# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.


'''
Recursion
time complexity = O(M x N)
space complexity = O(M x N)
'''
from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # add this for caching for DP memoization
        @lru_cache(maxsize=None)
        def lcs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            elif text1[i] == text2[j]:
                return 1 + lcs(i + 1, j + 1)
            else:
                return max(lcs(i + 1, j), lcs(i, j + 1))

        return lcs(0, 0)



text1 = "ezupkr"
text2 = "ubmrapg"

a = Solution()
result = a.longestCommonSubsequence(text1, text2)

print(result)
