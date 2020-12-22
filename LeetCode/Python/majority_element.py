# Leetcode # 169 Majority Element


# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2


def majority_element(arr):
    dict = {}
    for item in arr:
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1
    for elem in dict:
        if dict[elem] >= len(arr) / 2:
            return elem

arr1 = [3,2,3]

arr2 = [2, 2, 1, 1, 1, 1, 2, 2]


print(majority_element(arr2))