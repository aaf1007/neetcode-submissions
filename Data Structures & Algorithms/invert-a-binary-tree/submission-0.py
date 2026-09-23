# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        ans = TreeNode()

        def dfs(root, ans):
            if root == None:
                return  
            
            ans.val = root.val

            if root.left:
                ans.right = TreeNode()
                dfs(root.left, ans.right)

            if root.right:
                ans.left = TreeNode()
                dfs(root.right, ans.left)

            return

        dfs(root,ans)
        return ans