#2390. Removing Stars From a String
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                stack.pop() #遇到星號 吐掉一個字母
            else:
                stack.append(c) #把不是星號的字母塞進去
        return ''.join(stack) #把陣列 join成字串