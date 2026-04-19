# week08-6.py 學習計畫 Binary Search 最難的第4題
# LeetCode 875. Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 準備一個函式 helper(k) 看答案對不對
        def helper(k): # 1小時吃 k 個香蕉, 能成功 h 小時吃完嗎?
            total = 0 # 你猜 k，它會用多少時間
            for pile in piles: # 很多堆香蕉, 逐一檢查
                total += pile // k # 要吃掉這堆香蕉 pile 要花多少時間
                if pile % k > 0: total += 1 # 有餘數, 再多 1 小時
            return total <= h # 符合條件 (在 h 小時內吃完)
        
        # 使用 bisect_left 在 [1, max(piles)] 範圍內找第一個符合 helper 的速度
        # range(1, max(piles)) 的範圍是 1 到 max(piles)-1
        # 所以最後結果需要依照 bisect 的特性處理
        return bisect_left(range(1, max(piles)), True, key=helper) + 1