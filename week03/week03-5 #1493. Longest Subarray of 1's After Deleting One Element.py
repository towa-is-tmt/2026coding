#1493. Longest Subarray of 1's After Deleting One Element
#陣列裡 一定要刪掉1個 問剩下陣列裡 最長的1有幾個?
# sliding window 伸縮自如的蛇蛇 肚子裡 可以容忍最多1個0
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        zero = 0 #蛇的體內 有幾個[有毒的0]
        tail = 0 #蛇的尾巴 一開始停在0的地方 拉肚子時 會右縮
        ans = 0 #蛇最後得長度
        for head in range(N): #蛇的頭 逐一往右吃
            if nums[head] == 0: zero += 1 #如果吃到[有毒的0] zero 加1
            while zero > 1: #[有毒的0] 太多了
                if nums[tail] == 0: zero -=1 #如果拉肚子 拉出[有毒的0] zero減1
                tail += 1 #尾巴吐之後 右縮
            ans = max(ans, head- tail + 1) #更新最大長度
        return ans - 1 #要刪掉1個