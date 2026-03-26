#2352. Equal Row and Column Pairs
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter() #hash Map 可以知道影哪寫row出現幾次

        for row in grid: #每個row 逐一處理
            counter[tuple(row)] += 1
            #tuple() 可以把陣列[3,1,2,2], 變不會動(3,1,2,2)

        ans = 0 #有幾組?
        for col in zip(*grid): #矩陣transpose 再取出 col
            ans += counter[tuple(col)]
        return ans
