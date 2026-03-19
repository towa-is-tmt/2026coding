#1732. Find the Highest Altitude
#找到最高的海拔高度
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain)
        ans = h = 0 #一開始高度為0
        for i in range(N): #逐個加起來
            h += gain[i] #現在增減的量 gain[i] 加進H
            ans = max(ans,h) #更新最高答案
        return ans