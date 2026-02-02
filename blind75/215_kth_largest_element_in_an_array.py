# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import heapq

'''
Time complexity: O(N)
Space complexity: O(N)
'''

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        max_heap = []
        for n in nums:
            heapq.heappush(max_heap, -n)

        largest = -1
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
        
        return largest

nums = [3,2,3,1,2,4,5,5,6]
k = 4


'''
Min heap
'''

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

a = Solution()
result = a.findKthLargest(nums, k)
print(result)