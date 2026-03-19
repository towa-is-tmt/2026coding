#week04-4b.py (week04-3.py重寫版本)
#3866. First Unique Even Element
#找到陣列中 只出現過一次的偶數 第一次出現的位置
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = [0] * 200
        for nn in nums: #把陣列的值逐一取出
            H[nn] += 1 #統計數量
        for nn in nums: #再來一次 逐一取出來
            if nn % 2 == 0 and H[nn] == 1: #偶數 and 落單
                return nn
        return -1