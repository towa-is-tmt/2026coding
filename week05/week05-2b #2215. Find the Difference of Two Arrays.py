#2215. Find the Difference of Two Arrays
#加速版本 快很多
#程式跑很慢的版本
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1,num2 = set(nums1), set(nums2) #第二版本加的
        ans1 = [] #放[nums1 但不在 num2] 的數
        for num in nums1: #逐一取出
            if num not in nums2: #沒在裡面
                ans1.append(num) #放入答案

        ans2 = [] #放[nums2 但不在 num1] 的數
        for num in nums2:
            if num not in nums1:
                ans2.append(num)
        return [list(set(ans1)), list(set(ans2))] #把方括號list 變set 再變回list 重複就不見了