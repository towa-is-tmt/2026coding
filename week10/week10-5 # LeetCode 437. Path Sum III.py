# week10-5.py 學習書 Binary Tree - DFS 第4題
# LeetCode 437. Path Sum III
# 題目：給定一棵二元樹，找出所有路徑的總和等於 targetSum 的數量

# 定義二元樹節點
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val        # 節點的值
#        self.left = left      # 左子節點
#        self.right = right    # 右子節點

from collections import Counter

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Counter 用來記錄「前綴和」出現的次數
        counter = Counter()
        counter[0] = 1  # 初始化：有一個總和為 0 的情況（代表從根開始）

        def helper(root, total):
            if root == None: 
                return 0  # 遞迴終止條件：空節點沒有路徑
            # 更新目前的總和
            total += root.val
            ans = counter[total - targetSum]
            counter[total] += 1  # 紀錄這個總和出現一次
            # 計算答案：如果存在某個前綴和 (total - targetSum)，
            # 代表從那個前綴到現在的路徑總和剛好等於 targetSum
            # 遞迴探索左右子樹
            ans += helper(root.left, total)
            ans += helper(root.right, total)
            # 回溯：離開這個節點時，把目前總和的計數減掉
            counter[total] -= 1

            return ans

        # 從根節點開始，初始總和為 0
        return helper(root, 0)
