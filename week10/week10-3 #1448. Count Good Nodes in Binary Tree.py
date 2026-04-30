#1448. Count Good Nodes in Binary Tree
#函是呼叫函式 解tree的問題
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def helper(root,biggest): #記得祖先最大的biggest
            if root==None: return 0 #提早結束
            ans = 0
            if root.val >= biggest:
                ans +=1
                biggest = root.val
            ans += helper(root.left, biggest)
            ans += helper(root.right, biggest)
            return ans
        return helper(root,root.val)
