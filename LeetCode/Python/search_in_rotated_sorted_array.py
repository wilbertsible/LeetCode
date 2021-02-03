# LeetCode # 33 Search in Rotated Sorted Array

# You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# If target is found in the array return its index, otherwise, return -1.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(target >=  nums[0]):
            i = 0
            while i < len(nums) and target >= nums[i]:
                if target == nums[i]:
                    return i
                i += 1
            return -1
        else:
            i = len(nums) - 1
            print(nums[i])
            while i >= 0 and target <= nums[i]:
                print(nums[i])
                if target == nums[i]:
                    return i
                i -= 1
            return -1

s = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
nums2 = [1]

target = 2

print(s.search(nums2, target))