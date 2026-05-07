# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findRightest(root): #找到最右邊的那個人
            if root.right: #右邊還有
                return findRightest(root.right) #繼續往右走
            return root #沒有右邊 那就自己上
        
        if root==None: return root
        if root.val == key: 
            if root.left:
                now = findRightest(root.left) #找到繼承者NOW
                root.val = now.val #把繼承的質塞進來
                root.left = self.deleteNode(root.left, now.val) #再把左邊小樹裡面舊的Node殺掉
            else:
                return root.right
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
        