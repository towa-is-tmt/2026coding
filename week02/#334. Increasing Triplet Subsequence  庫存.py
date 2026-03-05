#334. Increasing Triplet Subsequence
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        low = mid = inf
        for num in nums:
            if num < low: low = num 
            elif num > low and num < mid: mid = num
            elif num > mid: return True
        return False