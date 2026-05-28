#746. Min Cost Climbing Stairs
from functools import * #比賽時 要自己教這行 才能用@cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache#函試呼叫函示 把大問題變成小問題
        def helper(i): #現在踩在第i格 之後要多少錢
            if i >= len(cost): return 0 
            return cost[i] + min( helper(i+1), helper(i+2)) 
        return min( helper(0), helper(1))