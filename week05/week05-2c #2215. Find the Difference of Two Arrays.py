#2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1, num2 = set(nums1), set(nums2)  
        return [list(num1 - num2), list(num2 - num1)]#1裡有的數字減掉2裡有的數字 1裡有的數字減掉2裡有的數字 再轉回list
        #第三版本