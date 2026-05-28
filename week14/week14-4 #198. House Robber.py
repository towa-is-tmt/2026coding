#198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:    
        @cache
        def helper(i): #如果搶第一間房 可以搶多少間
            if i >= len(nums): return 0 #整條街搶玩了 沒得搶了
            return nums[i] + max(helper(i+2), helper(i+3))
        return max(helper(0), helper(1))