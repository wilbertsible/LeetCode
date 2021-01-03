# LeetCode # 226 Invert Binary Tree

# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:

# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp

# Used to check Tree
    def tree_preorder(self, root):
        preorder = []
        if root:
            preorder.append(root.val)
            preorder = preorder + self.tree_preorder(root.left)
            preorder = preorder + self.tree_preorder(root.right) 
        return preorder
    def tree_inorder(self, root):
        inorder = []
        if root:
            inorder = self.tree_inorder(root.left)
            inorder.append(root.val)
            inorder = inorder + self.tree_inorder(root.right)
        return inorder
    def tree_postorder(self, root):
        postorder = []
        if root:
            postorder = self.tree_postorder(root.left)
            postorder = postorder + self.tree_postorder(root.right)
            postorder.append(root.val)
        return postorder


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)


a = Solution()
print(a.tree_preorder(root))
print(a.tree_inorder(root))
print(a.tree_postorder(root))

a.invertTree(root)

print(a.tree_preorder(root))
print(a.tree_inorder(root))
print(a.tree_postorder(root))

