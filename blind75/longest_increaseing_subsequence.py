# Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

from bisect import bisect_left

# The idea is find the smallest possible tail of an increasing subsequence of length k + 1 => find the left most branch in BST
# time complexity in this case is O(n log n)
# space complexity is O(n)

class Solution:
    def lengthOfLIS(self, nums) -> int:
        sub = []

        for num in nums:
            # Returns the leftmost insertion point for the element. If the element exists, the insertion point will be before the existing entries.
            left_pos = bisect_left(sub, num)

            # when inserted to BST if the num was largest then it will be append to the end of the sub arr (top of BST)
            # in that case, we append the number to the sub
            if left_pos == len(sub):
                sub.append(num)
            else:
                # otherwise just replace the number to the position
                sub[left_pos] = num

        return len(sub)
    
nums = [10,9,2,5,3,7,101,18]
a = Solution()
result = a.lengthOfLIS(nums)
print(result)