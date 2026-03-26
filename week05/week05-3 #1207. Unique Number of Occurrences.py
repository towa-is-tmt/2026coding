#1207. Unique Number of Occurrences
#每種數字出現的次數 必須都不一樣
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr) #統計數字出現的次數
        s = set() #用來看出現的次數是否獨一無二
        for c in counter:
            if counter[c] in s: #如果有出現過 就失敗
                return False
            s.add( counter[c]) #現在這個出現的次數放進s裡
        return True
        