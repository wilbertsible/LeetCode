# Leetcode # 144. Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def preorderTraversal(self, root):
        if root == None:
            return []
        preorderArr = [root.val]
        currNode = None
        prevHistory = [root]
        if root.left != None:
            currNode = root.left
            preorderArr.append(currNode.val)
            currNode.val = 101
        elif root.right != None:
            currNode = root.right
            preorderArr.append(currNode.val)
            currNode.val = 101
        else: 
            return preorderArr
        while currNode != root or (currNode.left != None and currNode.left.val != 101) or (currNode.right != None and currNode.right.val != 101):
            if currNode.left != None and currNode.left.val < 101:
                prevHistory.append(currNode)
                currNode = currNode.left
                preorderArr.append(currNode.val)
                currNode.val = 101
            elif currNode.right != None and currNode.right.val < 101:
                prevHistory.append(currNode)
                currNode = currNode.right
                preorderArr.append(currNode.val)
                currNode.val = 101
            else:
                currNode = prevHistory.pop()
        return preorderArr

s = Solution()
tree0 = TreeNode(1)
tree0.left = TreeNode(2)
tree0.left.left = TreeNode(4)
tree0.left.right = TreeNode(5)
tree0.right = TreeNode(3)
tree0.right.left = TreeNode(6)
tree0.right.right = TreeNode(7)

print(s.preorderTraversal(tree0))


tree1 = TreeNode(1)
tree1.right = TreeNode(2)
tree1.right.left = TreeNode(3)

print(s.preorderTraversal(tree1))

tree2 = None
print(s.preorderTraversal(tree2))

tree3 = TreeNode(1)
print(s.preorderTraversal(tree3))
