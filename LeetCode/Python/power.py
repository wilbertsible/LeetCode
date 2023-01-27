# Leetcode #50. Pow(x, n)

# Companies
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

# Constraints:

# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# -104 <= xn <= 104

class Solution:
    def myPow(self,x, n):
        if n < 0:
            return 1 / self.powTemp(x,-1*n)
        elif n == 0:
            return 1
        else: 
            return self.powTemp(x,n)
    
    def powTemp(self, x, n):
        if n < 1:
            return 1
        elif n % 2 == 0:
            return self.powTemp(x*x, n/2)
        else:
            return x * self.powTemp(x, n-1)

        
s = Solution()
x1 = 2.00000
n1 = 10
print(s.myPow(x1,n1))

x2 = 2.10000
n2 = 3
print(s.myPow(x2,n2))

x3 = 2.00000
n3 = -2
print(s.myPow(x3,n3))