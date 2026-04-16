#2300. Successful Pairs of Spells and Potions
# week08-4.py 學習計畫 Binary Search
# LeetCode 2300. Successful Pairs of Spells and Potions
# 想知某種 spells[i] 魔法，配幾種藥水可以成功?

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort() # 藥水「小到大」排好，才能用二分搜尋
        P = len(potions) # 有 P 種藥水
        ans = []
        
        for spell in spells: # 每每一種魔法，都試一次
            # 目標是：spell * potion >= success
            # 移項後：potion >= success / spell
            # 使用 bisect_left 找出第一個「大於等於」這個數值的藥水位置
            now = P - bisect_left(potions, success / spell)
            ans.append(now) #全部藥水P瓶 - 會失敗的藥水??
            
        return ans