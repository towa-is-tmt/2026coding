from functools import * #比賽時 要自己教這行 才能用@cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        a = [0] * (N+1)
        a[0] = cost[0]
        a[1] = cost[1]
        for i in range(2,N+1):
            a[i] = min(a[i-1], a[i-2])
            if i < N: a[i] += cost[i]
        return a[N]