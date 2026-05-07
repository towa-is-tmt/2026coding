#236. Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        a = [] #負責放答案
        def helper(root):
            count = 0 # 下面有幾個p or q 的node
            if root == None: return 0 #沒東西
            if root==p or root==q: count +=1 #找到1個 
            count += helper(root.left)
            count += helper(root.right)
            if count == 2: #收集2個了
                a.append(root)
            return count #現在收集到幾個
        helper(root) #記得 發動 函示呼叫函示
        return a[0] #最前面 第1次出現的答案