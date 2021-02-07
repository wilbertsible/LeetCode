# LeetCode February Coding Challenge 2021 #4: Longest Harmonious Subsequence
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:

# Input: nums = [1,2,3,4]
# Output: 2
# Example 3:

# Input: nums = [1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109

from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        fmap = {}
        for i in range(len(nums)):
            if nums[i] in fmap:
                fmap[nums[i]] += 1
            else:
                fmap[nums[i]] = 1
        highestCount = 0
        count = 0
        for i in fmap:
            if(i + 1) in fmap:
                count = fmap[i] + fmap[i+1]
            if count > highestCount:
                highestCount = count
        return highestCount
                    

s = Solution()

nums = [1,3,2,2,5,2,3,7]
print(s.findLHS(nums))