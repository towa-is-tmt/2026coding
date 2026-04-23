#206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: #(終止條件 最簡單的狀況)
            return head
        head2 = head.next
        ans = self.reverseList(head.next) #函式呼叫函式
        head2.next, head.next = head, None
        return ans