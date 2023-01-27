# Leetcode #70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step



class Solution:
    def climbStairs(self, n):    
        memo = {}
        self.climbRecursion(n,memo)
        return memo[n]
       
    def climbRecursion(self, n, memo):
        if(n in memo):
            return memo[n]
        count = 0
        if n == 0:
            return 1
        if n < 0:
            return 0
        else:
            memo[n] = self.climbRecursion(n-2, memo) + self.climbRecursion(n-1, memo)
            return memo[n]

s = Solution()
print("climbStairs: 2")
print(s.climbStairs(2))
print("climbStairs: 3")
print(s.climbStairs(3))
print("climbStairs: 4")
print(s.climbStairs(4))
print("climbStairs: 5")
print(s.climbStairs(5))
print("climbStairs: 6")
print(s.climbStairs(6))
print("climbStairs: 7")
print(s.climbStairs(7))
    