#Needs to fix

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p:TreeNode, q:TreeNode)->bool:
        isEqualPreorder = self.isArrayEqual(self.tree_preorder(p), self.tree_preorder(q))
        isEqualInorder = self.isArrayEqual(self.tree_inorder(p), self.tree_inorder(q))
        isEqualPostorder = self.isArrayEqual(self.tree_postorder(p), self.tree_postorder(q))
        if(isEqualPreorder and isEqualInorder and isEqualPostorder):
            return True
        else:
            return False
    def isArrayEqual(self, arr1, arr2)-> bool:
        if len(arr1) != len(arr2):
            return False
        for i in range(0, len(arr1)):
            if(arr1[i] != arr2[i]):
                return False
        return True
    
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

s = Solution()

p = TreeNode(1)
p.left = TreeNode()
p.right = TreeNode(2)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)


print(s.isSameTree(p, q))