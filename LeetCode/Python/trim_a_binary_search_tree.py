# LeetCode February Coding Challenge 2021 #2: Trim a Binary Search Tree

# Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

# Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

# Example 1:

# Input: root = [1,0,2], low = 1, high = 2
# Output: [1,null,2]
# Example 2:


# Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# Output: [3,2,null,1]
# Example 3:

# Input: root = [1], low = 1, high = 2
# Output: [1]
# Example 4:

# Input: root = [1,null,2], low = 1, high = 3
# Output: [1,null,2]
# Example 5:

# Input: root = [1,null,2], low = 2, high = 4
# Output: [2]
 

# Constraints:

# The number of nodes in the tree in the range [1, 104].
# 0 <= Node.val <= 104
# The value of each node in the tree is unique.
# root is guaranteed to be a valid binary search tree.
# 0 <= low <= high <= 104


class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high:int)-> TreeNode:
        
        for i in range(self.lowest_tree_value(root), low):
            print(i)
            print("here")
            root = self.deleteNode(root, i)
            print(self.tree_inorder(root))
        for i in range(high + 1, self.highest_tree_value(root) + 1):
            print(i)
            root = self.deleteNode(root, i)
            print(self.tree_inorder(root))
        return root


    def minValueNode(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current
    
    def deleteNode(self, root: TreeNode, target: int)-> None:
        if root is None:
            return root
        if target < root.val:
            root.left = self.deleteNode(root.left, target)
        elif(target > root.val):
            root.right = self.deleteNode(root.right, target)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root
    
    def lowest_tree_value(self, root):
        curr = root
        while(curr.left != None):
            curr = curr.left
        return curr.val
    def highest_tree_value(self, root):
        curr = root
        while(curr.right != None):
            curr = curr.right
        return curr.val

    # For checking purposes
    def tree_inorder(self, root):
        inorder = []
        if root:
            inorder = self.tree_inorder(root.left)
            inorder.append(root.val)
            inorder = inorder + self.tree_inorder(root.right)
        return inorder

s = Solution()
root = TreeNode(3)
root.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.right = TreeNode(4)

# root = TreeNode(1)
# root.right = TreeNode(2)


print(s.tree_inorder(s.trimBST(root, 1, 3)))