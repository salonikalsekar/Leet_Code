# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            id = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[id])

            root.left = self.buildTree(preorder, inorder[:id])
            root.right = self.buildTree(preorder, inorder[id + 1:])

            return root
