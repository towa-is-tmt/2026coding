#1456. Maximum Number of Vowels in a Substring of Given Length
#母音 vowels: A E I O U  長度K的小字串最多幾個母音  
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') #把5個母音 變成set() 集合
        #以後用 if c in vowels: 就可以快速確認他是母音
        #以前 c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'
        count  = 0
        for i in range(k):
            if s[i] in vowels:  count+=1
        ans = count # 離開迴圈時 確認前K個字母 有count 個母音 先當答案
        N = len(s) #字串長度
        for i in range(k, N): #右邊每個字母逐一檢查
            if s[i] in vowels: count += 1 #右邊的頭 s[i] 又吃到一個母音
            if s[i-k] in vowels: count -= 1 #左邊的尾巴 s[i-1] 吐掉時 失去一個母音
            ans = max(ans, count )#更新答案最大值
        return ans
