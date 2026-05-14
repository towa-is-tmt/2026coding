class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set() #走過的不要再走
        ans = 0
        path = defaultdict(list) #path[now] 與那些城市相接
        for a, b in connections:
            path[a].append( (b, +1) )
            path[b].append( (a, -1) )

        def helper(now):
            ans = 0 #有幾條路 [方向不對]
            visited.add(now)
            for k, d in path[now]: #城市 now 可以到城市K 方向是d
                if k not in visited:
                    if d == +1: ans += 1 #要檢測方向 若方向出錯
                    ans += helper(k) #函式呼叫函示 裡面有幾條出錯
            return ans
        return helper(0) #從0出發