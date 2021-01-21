# LeetCode # 58 Length of Last Word

# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Example 2:

# Input: s = " "
# Output: 0
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.

from typing import List

class Solution:
    def lengthOfLastWord(self, s:str)-> int:
        tokenizer = s.split(' ')
        for i in range(len(tokenizer), 0, -1):
            print(tokenizer[i-1])
            if tokenizer[i-1] != '':
                return len(tokenizer[i-1])
        return 0

s = Solution()

words ="Hello World"

print(s.lengthOfLastWord(words))