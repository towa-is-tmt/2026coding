#DFS深度優先搜尋 tree最喜歡用函式呼叫函式
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0 #沒有東西 深度是0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+ 1
