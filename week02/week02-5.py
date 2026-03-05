#1679. Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort() #小到大排好
        left = 0 #左手
        right = len(nums) -1 #右手
        while left < right: #當左手小於右手 沒撞在一起
            sumNum = nums[left] + nums[right] #左手右手加起來
            if sumNum == k: #如果加起來剛好等於k
                ans += 1 #答案加一
                left += 1 #左手前進一格
                right -= 1 #右手退一格
            elif sumNum < k: #如果k大於加總
                left += 1 #那左手前進一格
            else: #否則(#如果k小於加總)
                right -= 1 #右手退一格
        return ans