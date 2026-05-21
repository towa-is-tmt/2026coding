#994. Rotting Oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0]) #長 寬
        visited = set()
        queue = deque()
        fresh = 0
        #queue.append( (i,j,0)) 把爛掉橘子放入queue
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2: 
                    visited.add( (i,j) )
                    queue.append( (i,j,0) )
                if grid[i][j] == 1: fresh +=1 #多1個新鮮橘子
        if fresh == 0: return 0
        ans = -1 #甚麼時候全部爛掉 不知道 一開始 -1 沒有爛掉
        while queue:
            i,j,t = queue.popleft()
            ans = t #更新爛掉的時間
            for ii,jj in (i+1,j),(i-1,j), (i,j+1), (i,j-1):
                if ii < 0 or jj < 0 or ii >= M or jj >= N: continue
                if (ii,jj) in visited: continue
                if grid[ii][jj] == 1: #這格式還沒爛掉的橘子 可以感染他
                    fresh -= 1
                    visited.add( (ii,jj) )
                    queue.append( (ii,jj,t+1) ) #將在 t+1 時爛掉
        if fresh>0: return -1 #只要還有任何一顆霉爛掉 還是新鮮的 就沒有輸
        return ans

        