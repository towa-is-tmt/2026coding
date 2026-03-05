#392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t) # 字串的長度
        if N1 == 0: return False #如果左邊字串是0 那就不用比 直接return Ｆalse
        i = 0 # 要記得，i從0開始
        for k in range(N2): # 右邊一個個去試
            if s[i] == t[k]: # 找到1個「左右」符合的了
                i += 1 # 左邊的 i 往右升一級

        if i==N1: # 左邊的 i 有走到左邊的結束，太好了
            return True # 成功
        return False # 失敗