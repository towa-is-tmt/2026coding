#3866. First Unique Even Element
#找到陣列中 只出現過一次的偶數 第一次出現的位置
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        N = len(nums)
        ans = -1
        H = [0] * 200 #很多格 H[??] 對應??出現過幾次
        for i in range(N): 
            H[ nums[i] ] += 1 #把出現的數字 塞進H[??]裡面
        for i in range(N):
            if nums[i] % 2 == 0 and H [ nums[i] ] == 1: #偶數 只出現一次
                return nums[i] #找到答案了

        return ans