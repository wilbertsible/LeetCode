# LeetCode # 66 Plus One

# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Example 3:

# Input: digits = [0]
# Output: [1]
 

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9


from typing import List

class Solution:
    def plusOne(self, digits:List[int])->List[int]:
        digits[len(digits) - 1] += 1
        for i in range(len(digits), 1, -1):
            print(digits[i - 1])
            if digits[i - 1] >= 10:
                mod = digits[i-1] % 10
                carry = (int)(digits[i-1] / 10)
                digits[i - 1] = mod
                digits[i - 2] = digits[i-2] + carry
        if(digits[0])>=10:
            print("goes here")
            mod = digits[0] % 10
            carry = (int)(digits[0] / 10)
            digits[0] = mod
            digits.insert(0, carry)
        return digits
s = Solution()
digits = [9,9,9]
print(s.plusOne(digits))