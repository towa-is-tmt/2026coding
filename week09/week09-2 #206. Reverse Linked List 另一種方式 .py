
lass Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head  # 沒辦法移動則直接回傳
        
        ans = ans1 = head # 「第奇數個」放在前面
        ans20 = ans2 = head.next # 「第偶數個」放在後面
        head = head.next.next
        
        while head != None:
            ans1.next, head = head, head.next
            ans1 = ans1.next
            
            if head != None:
                ans2.next, head = head, head.next
                ans2 = ans2.next
                
        ans1.next = ans20
        ans2.next = None
        return ans