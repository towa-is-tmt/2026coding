#872. Leaf-Similar Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = []
        def helper(root):
            if root.left == None and root.right == None: #葉子
                a.append(root.val) #把質加到a
            if root.left: helper(root.left) #如果左邊有
            if root.right: helper(root.right) #如果右邊有
        helper(root1)
        a,b = [], a #因為a塞好資料 要再開一個新的[] 並把舊的a 送給b
        helper(root2)
        return a == b