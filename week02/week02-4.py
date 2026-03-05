#11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i,j = 0, len(height) -1 #左邊i，右邊j
        while i < j: # 只要左右還沒撞一起
            area = (j-i) * min(height[i],height[j]) #算出現在的面積
            ans = max(ans, area) #更新答案
            if height[i] < height[j]: i += 1 #小的i往右
            else: j -= 1 #小的j往左

        return ans