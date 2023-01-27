# Leetcode #100. Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val =  val
        self.left = left
        self.right = right

class Solution:
    # Preorder Traversal
    def isSameTree(self, p, q):
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p == None and q == None:
            return True
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right) 





s = Solution()
newTree1 = TreeNode(1)
newTree1.left = TreeNode(2)
newTree1.right = TreeNode(3)

newTree2 = TreeNode(1)
newTree2.left = TreeNode(2)
newTree2.right = TreeNode(3)

print(s.preorderCompare(newTree1,newTree2))


newTree3 = TreeNode(1)
newTree3.left = TreeNode(2)


newTree4 = TreeNode(1)
newTree4.right = TreeNode(2)

print(s.preorderCompare(newTree3,newTree4))

newTree5 = TreeNode(1)
newTree5.left = TreeNode(2)
newTree5.right = TreeNode(1)

newTree6 = TreeNode(1)
newTree6.left = TreeNode(1)
newTree6.right = TreeNode(2)

print(s.preorderCompare(newTree5,newTree6))s