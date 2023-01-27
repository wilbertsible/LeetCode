# Leetcode # 926. Flip String to Monotone Increasing

# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

# Return the minimum number of flips to make s monotone increasing.

 

# Example 1:

# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
# Example 2:

# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
# Example 3:

# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.


class Solution:
    def minFlipsMonoIncr(self, s):
        total = 0
        for i in range(0,len(s)):
            if s[i] == '1':
                total = total + 1
        total_left = 0
        total_right = total
        len_right  = len(s)
        curr_max_flip = 1000000
        for i in range(0, len(s)):
            if total_right == 0 and len_right >= total_left:
                curr_flip = total_left
            else:
                curr_flip = total_left + (len_right - total_right)
            if curr_flip < curr_max_flip:
                curr_max_flip = curr_flip
            if s[i] == '1':
                total_right = total_right - 1
                total_left = total_left + 1
            len_right = len_right  - 1
        return curr_max_flip
            

                










s = Solution()
s0 = "00110"
print(s.minFlipsMonoIncr(s0))
s1 = "010110"
print(s.minFlipsMonoIncr(s1))
s2 = "00011000"
print(s.minFlipsMonoIncr(s2))
s3 = "10011111110010111011"
print(s.minFlipsMonoIncr(s3))
s4 = "00000010010000001000"
print(s.minFlipsMonoIncr(s4))