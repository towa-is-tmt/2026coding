# week16-4.py 學習計畫 Intervals 第2題
# LeetCode 452. Minimum Number of Arrows to Burst Balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 氣球依「右邊界」排序
        points.sort(key = lambda x:x[1]) 
        
        ans = 0
        previous_end = -inf
        
        for start, end in points: # 逐一取出氣球
            # 氣球有矩陣哦！只好再多射1箭
            if previous_end < start: 
                ans += 1 # 要為現在的 [start, end] 的氣球，射1箭
                previous_end = end
                
        return ans