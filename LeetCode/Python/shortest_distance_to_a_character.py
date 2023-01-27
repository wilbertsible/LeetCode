# LeetCode February Coding Challenge 2021 #7: Shortest Distance to a Character
# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.

# Example 1:

# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
# Example 2:

# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]
 

# Constraints:

# 1 <= s.length <= 104
# s[i] and c are lowercase English letters.
# c occurs at least once in s.


from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        split = s.split(c)
        for i in range (len(split[0]), 0, -1):
            answer.append(i)
        answer.append(0)
        for i in range(1, len(split) - 1):
            if len(split[i]) % 2 == 1:
                for j in range(1, (int)(len(split[i])/2) + 2):
                    answer.append(j)
                for j in range((int)(len(split[i])/2), 0, -1):
                    answer.append(j)
                answer.append(0)
            elif split[i] == '':
                answer.append(0)
            else:
                for j in range(1, (int)(len(split[i])/2) + 1):
                    answer.append(j)
                for j in range((int)(len(split[i])/2), 0, -1):
                    answer.append(j)
                answer.append(0)
        for i in range(1, len(split[len(split) - 1]) + 1):
            answer.append(i)

        return answer

        


s = Solution()
string = "loveleetcode"
char = "e"

string2 = "aaaba"
char2 = "b"
print(s.shortestToChar(string, char))

