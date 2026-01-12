# Given a sorted array of integers nums, determine if there exists a pair of numbers that sum to a given target.
# Example:
# Input: nums = [1,3,4,6,8,10,13], target = 13
# Output: True (3 + 10 = 13)
# Input: nums = [1,3,4,6,8,10,13], target = 6
# Output: False

def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return True
        
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return False


nums = [1, 3, 4, 6, 8, 10, 13]
target = 6
result = two_sum(nums, target)
print(result)