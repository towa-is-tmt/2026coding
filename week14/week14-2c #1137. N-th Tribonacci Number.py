class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0,1,1]
        if n<3: return a[n]
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3) 