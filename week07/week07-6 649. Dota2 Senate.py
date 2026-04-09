#649. Dota2 Senate
# week07-6.py 學習計畫 Queue 第 2 題
# LeetCode 649. Dota2 Senate 模擬兩個陣營互相消滅的過程
from collections import deque  # 引入 deque（雙端佇列）模組
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))  # 將字串轉成列表再放入 deque，模擬排隊
        banR, banD = 0, 0  # 記錄被消滅的次數（Radiant、Dire）
        R, D = senate.count('R'), senate.count('D')  # 計算目前各陣營人數

        while queue:  # 只要還有人在隊列中就繼續
            now = queue.popleft()  # 取出最前面的人（要行動的人）

            if now == 'R':  # Radiant 陣營
                if banR > 0:  # 若之前被消滅過（有待消滅的名額）
                    banR -= 1  # 用掉一個消滅名額
                    R -= 1  # Radiant 人數減一
                    # continue  # 放棄行動權
                else:  # 沒被消滅，保有行動權
                    banD += 1  # 增加消滅 Dire 的名額
                    queue.append(now)  # 自己回到隊尾等待下一輪
            else:  # Dire 陣營
                if banD > 0:  # 若之前被消滅過
                    banD -= 1
                    D -= 1
                    # continue
                else:  # 沒被消滅，保有行動權
                    banR += 1  # 增加消滅 Radiant 的名額
                    queue.append(now)  # 自己回到隊尾等待下一輪

            # 若某一方人數歸零，代表另一方勝利
            if R == 0:
                return "Dire"  # Radiant 全滅，Dire 勝利
            if D == 0:
                return "Radiant"  # Dire 全滅，Radiant 勝利
