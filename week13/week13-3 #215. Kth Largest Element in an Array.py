#215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 先排序法的寫法
        # nums.sort(reverse=True) # 先排序 O(NlogN)
        # return nums[k-1] # 第k大的數，是0...k-1

        # 要用 Heap 寫法, 可以找到小的數
        # heapify(nums) # 變成 heap 資料結構
        # while nums:
        #     print(heappop(nums))

        # 後段保留固定長度
        heapify(nums)  # 變成 heap 資料結構 O(logN)
        for i in range(len(nums) - k):
            heappop(nums)  # 出掉不同的 N-k 個數
        return heappop(nums)  # 對下的數, 就是最大的第k大的。
