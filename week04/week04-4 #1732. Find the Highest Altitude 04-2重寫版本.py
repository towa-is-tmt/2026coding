#week04-4.py (04-2的重寫版本)
#1732. Find the Highest Altitude
#找到最高的海拔高度
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0 #一開始高度為0
        for gg in gain: #py進階for 迴圈寫法 依序取出 gg
            H += gg
            ans = max(ans, H)
        return ans
