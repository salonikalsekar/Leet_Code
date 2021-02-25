# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        stack = []

        stack.append((root, False))

        while stack:

            curr, visited = stack.pop()
            if curr:
                if visited:
                    result.append(curr.val)
                else:
                    stack.append((curr.right, False))
                    stack.append((curr, True))
                    stack.append((curr.left, False))

        return result