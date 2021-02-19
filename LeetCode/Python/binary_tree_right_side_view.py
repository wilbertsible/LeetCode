# LeetCode February Coding Challenge 2021 #6: Binary Tree Right Side View
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        answer = []
        arr1 = []
        arr2 = []
        arr1.append(root)
        answer.append(root.val)
        while len(arr1) > 0:
            while len(arr1) > 0:
                curr = arr1.pop()
                if curr.left != None:
                    arr2.append(curr.left)
                if curr.right != None:
                    arr2.append(curr.right)
            if len(arr2) > 0:
                answer.append(arr2[len(arr2)-1].val)
            while len(arr2) > 0:
                arr1.append(arr2.pop())
        return answer



s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)

print(s.rightSideView(root))

