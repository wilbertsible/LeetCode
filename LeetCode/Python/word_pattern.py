# Leetcode #$ 290. Word Pattern

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


class Solution:
    def wordPattern(self, pattern, s):
        wordArr = s.split(" ")
        if len(pattern) != len(wordArr):
            return False
        patternDict = {}
        for i in range(0, len(pattern)):
            if pattern[i] not in patternDict and wordArr[i] not in patternDict.values():
                patternDict[pattern[i]] = wordArr[i]
            elif pattern[i] not in patternDict and wordArr[i] in patternDict.values() or\
            patternDict[pattern[i]] != wordArr[i]:
                return False
        return True


solution = Solution()
pattern1 = "abba"
s1 = "dog cat cat dog"
print(solution.wordPattern(pattern1, s1))

pattern2 = "abba"
s2 = "dog cat cat fish"
print(solution.wordPattern(pattern2, s2))

pattern3 = "aaaa"
s3 = "dog cat cat dog"
print(solution.wordPattern(pattern3, s3))

pattern4 = "abc"
s4 = "dog cat dog"
print(solution.wordPattern(pattern4, s4))