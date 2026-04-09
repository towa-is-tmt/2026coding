# week07-5.py 學習計畫 Queue 第 1 題
# 933. Number of Recent Calls 想知道 3000 毫秒範圍內有幾個 ping
from collections import deque  # 引入 deque（雙端佇列）模組

class RecentCounter:

    def __init__(self):  # 物件的建構子（constructor），只在建立物件時呼叫一次
        # 使用 Queue 的資料結構，但在 Python 中可用 collections.deque
        # deque 是 Double Ended Queue 的縮寫，可從兩端加入或移除元素
        self.queue = deque()  # 宣告一個 deque 物件，存放所有 ping 的時間點

    def ping(self, t: int) -> int:
        self.queue.append(t)  # 將目前的時間 t 加入右端（最新的 ping）
        # 當最左邊（最舊的 ping）超出 3000 毫秒範圍，就移除它
        while self.queue[0] < t - 3000:
            self.queue.popleft()  # 從左邊移除最舊的 ping
        # 回傳目前 queue 中的元素數量，也就是 3000 毫秒內的 ping 次數
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)