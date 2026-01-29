# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# naive solution
class Solution:
    def twoSum(self, nums, target: int):
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return [-1, -1]

# O(nlogn)
class Solution:
    def twoSum(self, nums, target: int):
        left = 0
        right = len(nums) - 1
        
        sorted_nums = sorted(nums)
        result = []

        while left < right:
            total = sorted_nums[left] + sorted_nums[right]
            if total == target:
                result = [sorted_nums[left], sorted_nums[right]]
                break
            elif total < target:
                left += 1
            else:
                right -= 1

        output = [-1, -1]

        for i in range(len(nums)):
            first_idx = 0
            second_idx = 1
            if nums[i] == result[first_idx] and output[first_idx] == -1:
                output[first_idx] = i
            elif nums[i] == result[second_idx] and output[second_idx] == -1:
                output[second_idx] = i
        
        return output

# O(n)
class Solution:
    def twoSum(self, nums, target: int):
        num_map = {}
        
        for i in range(len(nums)):
            sub = target - nums[i]

            if sub in num_map:
                return [num_map[sub], i]
            
            num_map[nums[i]] = i

        return [-1, -1]


nums = [3,3]
target = 6
a = Solution()
result = a.twoSum(nums, target)
print(result)