class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def helper(i):
            if i==0: return 0
            if i==1: return 1
            if i==2: return 1
            return helper(i-1) + helper(i-2) + helper(i-3)
        return helper(n)