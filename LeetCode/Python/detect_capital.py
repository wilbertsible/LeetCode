# Leetcode #520. Detect Capital

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

class Solution:
    def detectCapitalUse(self, word):
        if len(word) < 2:
            return True
        elif len(word) < 3 and not word[0].isupper() and word[1].isupper():
            return False
        isUpperArr = []
        for i in range(0,len(word)):
            isUpperArr.append(word[i].isupper())
        if isUpperArr[0] == True  and isUpperArr[1] == True:
            for i in range(2, len(isUpperArr)):
                if isUpperArr[i] == False:
                    return False
        elif isUpperArr[0] == True  and isUpperArr[1] == False:
            for i in range(2, len(isUpperArr)):
                if isUpperArr[i] == True:
                    return False
        elif isUpperArr[0] == False:
            for i in range(1, len(isUpperArr)):
                if isUpperArr[i] != False:
                    return False
        return True






s = Solution()
word1 = "USA"
print(s.detectCapitalUse(word1))
word2 = "FlaG"
print(s.detectCapitalUse(word2))
word3 = "mL"
print(s.detectCapitalUse(word3))