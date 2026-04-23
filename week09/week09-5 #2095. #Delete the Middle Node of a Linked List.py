#2095. Delete the Middle Node of a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return [] #很討厭的狀況: 只有一個 避不掉
        
        prev = fast = slow = head #fast兔子 slow烏龜一開始都在最前面
        while fast != None and fast.next != None:
            fast = fast.next.next #兔子跳兩格
            prev = slow #烏龜在走之前先記前一格位置
            slow = slow.next #烏龜走一格
        #print(slow.val) #當兔子到終點時 烏龜在中間
        prev.next = slow.next
        return head