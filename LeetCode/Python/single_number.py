# Leetcode # 136 Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

from typing import List

class Solution:
    def singleNumber(self, nums:List[int]) -> int:
        # if len(nums) < 2:
        #     return nums[0]
        # ptr1 = 0
        # ptr2 = 1
        # while ptr1 < len(nums):
        #     if nums[ptr1] == nums[ptr2]:
        #         temp = nums[ptr1 + 1]
        #         nums[ptr1 + 1] = nums[ptr2]
        #         nums[ptr2] = temp
        #         ptr1 += 2
        #         if ptr1 >= len(nums) - 1:
        #             return nums[ptr1]
        #         ptr2 = ptr1 + 1
        #     elif ptr2 == len(nums) - 1:
        #         return nums[ptr1]
        #     else:
        #         ptr2 += 1
        a = 0
        for i in nums:
            a ^= i
        return a
            

s = Solution()

nums =  [4,2,4,2,3]

print(s.singleNumber(nums))
            
        
