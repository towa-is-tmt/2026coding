#283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        N = len(nums)
        for i in range(N):
            if nums[i] != 0: #遇到不是0的樹 要搬到左邊
                nums[k] = nums[i] #左邊nums[k] 右邊nums[i]
                k += 1 #換下一個位子
        for i in range(k,N): #剩下的格子 從k 開始 N 結束
            nums[i] = 0 #全部補0