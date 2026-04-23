#206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head: #只要含有資料 就塞到陣列a 後面
            a.append(head.val) #就塞到陣列的後面
            head = head.next #換下一筆
        now = ans = ListNode() #答案將串到裡面

        #下面用到過來的迴圈 把陣列的值 逐一串到ans 的後面 
        N = len(a) #陣列的長度 要倒過來的迴圈
        for i in range(N-1, -1, -1):
            now.next = ListNode(a[i])
            now = now.next
        return ans.next