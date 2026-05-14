#399. Evaluate Division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        path = defaultdict(list)
        for (a,b),v in zip(equations,values): #用拉鍊壓鎖起來
            path[a].append( (b,v) ) #正的走
            path[b].append( (a,1/v) ) #倒著走
        def helper(now, target, v0):
            if now not in path or target not in path: return -1
            if now == target: return v0
            visited.add(now)
            ans = -1
            for node, v in path[now]:
                if node not in visited: #沒走過 就可以走走看
                    ans = max(ans,helper(node,target, v0*v))
            return ans
        ans = []
        for a,b in queries:
            visited = set()
            ans.append(helper(a,b, 1) )
        return ans