# LeetCode February Coding Challenge 2021 #15: Letter Case Permutation
# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. You can return the output in any order.

 

# Example 1:

# Input: S = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: S = "3z4"
# Output: ["3z4","3Z4"]
# Example 3:

# Input: S = "12345"
# Output: ["12345"]
# Example 4:

# Input: S = "0"
# Output: ["0"]
 

# Constraints:

# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.


from typing import List;
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        count = 0
        permutation = []
        for i in S:
            if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
                count += 1
        permutation_binary = []
        for i in range(0,2**count):
            string_binary = str(bin(i))[2:count + 2]
            for j in range(0, count - len(string_binary)):
                string_binary = "0" + string_binary
            permutation_binary.append(string_binary)
        letter_count = 0
        word = ""
        for i in range(0, len(permutation_binary)):
            word = ""
            letter_count = 0
            for j in S:
                if (j >= 'A' and j <= 'Z') or (j >= 'a' and j <= 'z'):
                    if permutation_binary[i][letter_count] == "0":
                        word +=j.lower()
                    elif permutation_binary[i][letter_count] == "1":
                        word += j.upper()
                    letter_count += 1
                else:
                    word += j
            permutation.append(word)
        return permutation


s = Solution()

string = "a1b2cd"


print(s.letterCasePermutation(string))