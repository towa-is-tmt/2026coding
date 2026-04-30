# week10-6.py 學習計畫 Binary Tree - DFS 第5題
# LeetCode 1372. Longest ZigZag Path in a Binary Tree
# 找到中間 ZigZag 左右左右 or 右左右左 最長的哪一個

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 # 整個問題的答案（紀錄全域最長路徑）
        
        def helper(root):
            if root == None: 
                return 0, 0 # 如果節點為空，回傳左邊最長、右邊最長皆為 0
            
            # 遞迴呼叫：往左走與往右走
            # Lans1, Lans2 代表左邊小朋友回傳的（左最長, 右最長）
            Lans1, Lans2 = helper(root.left) 
            # Rans1, Rans2 代表右邊小朋友回傳的（左最長, 右最長）
            Rans1, Rans2 = helper(root.right)
            
            # 更新全域答案：
            # 當前節點往左走，必須接左子節點的「右路徑」 (Lans2 + 1)
            # 當前節點往右走，必須接右子節點的「左路徑」 (Rans1 + 1)
            self.ans = max(self.ans, Lans2 + 1, Rans1 + 1)
            
            # 回傳給上一層：
            # 當前節點的左路徑長度 = 左子節點的右路徑長度 + 1
            # 當前節點的右路徑長度 = 右子節點的左路徑長度 + 1
            return Lans2 + 1, Rans1 + 1
        
        helper(root)
        # 因為題目計算的是「邊」的數量，而 helper 回傳的是「節點」數量，
        # 所以最後答案要減 1。
        return self.ans - 1