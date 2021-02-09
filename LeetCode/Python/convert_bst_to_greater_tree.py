# LeetCode February Coding Challenge 2021 #7: Convert BST to Greater Tree
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

 

# Example 1:


# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# Example 2:

# Input: root = [0,null,1]
# Output: [1,null,1]
# Example 3:

# Input: root = [1,0,2]
# Output: [3,3,2]
# Example 4:

# Input: root = [3,2,4,1]
# Output: [7,9,4,10]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -104 <= Node.val <= 104
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.


from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        inorder = self.tree_reverse_inorder(root)
        sum = 0
        for i in range(0, len(inorder)):
            sum = sum + inorder[i]
            inorder[i]  = sum
        self.tree_inorder_change(root, inorder)
        return root
    # Obtains the reverse inorder tree traversal
    def tree_reverse_inorder(self, root):
        inorder = []
        if root:
            inorder = self.tree_reverse_inorder(root.right)
            inorder.append(root.val)
            inorder = inorder + self.tree_reverse_inorder(root.left)
        return inorder
    # Inorder Traversal of the Tree and Channge the value of the TreeNode
    def tree_inorder_change(self, root, traversal):
        if root:
            self.tree_inorder_change(root.left,traversal)
            root.val = traversal.pop()
            self.tree_inorder_change(root.right, traversal)
    # Use to check the result
    def tree_inorder(self, root):
        inorder = []
        if root:
            inorder = self.tree_inorder(root.left)
            inorder.append(root.val)
            inorder = inorder + self.tree_inorder(root.right)
        return inorder

s = Solution()
root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

s.convertBST(root)
print(s.tree_inorder(root))

