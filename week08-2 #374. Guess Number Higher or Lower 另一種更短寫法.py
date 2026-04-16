# week08-1.py 學習計畫 Binary Search 第1題
# 題目提供 guess() API 你可以呼叫它，找出 1...n 裡面的「答案」

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number (猜太大)
#          1 if num is lower than the picked number (猜太小)
#          otherwise return 0 (猜中了)
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        #另一種寫法
        return bisect_left(range(n+1), 0, key = lambda x:-guess(x) )