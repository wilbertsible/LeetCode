# LeetCode February Coding Challenge 2021 #10: Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution:
    def isAnagram(self, s:str, t:str) ->bool:
        letters = {}
        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        for i in t:
            if i not in letters:
                return False
            elif i in letters:
                letters[i] -=1
        for i in letters:
            if letters[i] != 0:
                return False
        return True
s = Solution()
s1 = "anagram"
s2= "agaram"

print(s.isAnagram(s1, s2))
