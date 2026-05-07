#199. Binary Tree Right Side View
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []  # 用來存放右側視角能看到的節點值

        def helper(root, level):
            if not root:  # 如果節點是空的，直接返回
                return
            # 如果目前層數還沒有被記錄過，就把這個節點加入答案
            # 因為我們是先走右邊，所以第一個遇到的就是右側視角能看到的
            if level == len(ans):
                ans.append(root.val)
            # 先遞迴右子樹，再遞迴左子樹
            helper(root.right, level + 1)
            helper(root.left, level + 1)

        # 從根節點開始，層數設為 0
        helper(root, 0)
        return ans