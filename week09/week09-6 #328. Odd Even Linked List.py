#328. Odd Even Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# 定義單向鏈結串列的節點
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 建立一個空的陣列 a，準備用來存放 Linked List 的數值
        a = [] # 這題竟然可以用作弊法，先轉成陣列 a
        
        # 遍歷原始的 Linked List
        while head: # 逐一將 Linked List 的值，放入陣列 a
            a.append( head.val )
            head = head.next # 記得要換下一筆哦！
            
        # 取得陣列的大小
        N = len(a) # 陣列的大小
        
        # 建立一個虛擬頭節點 (Dummy Node)，用來建構新的結果串列
        # ans 是固定在開頭的指標，now 是用來往後串接的移動指標
        now = ans = ListNode() # 答案,有個 Node 右邊會塞真的 Nodes
        
        # 第一輪：處理「奇數位置」的節點 (索引 0, 2, 4...)
        # range(0, N, 2) 代表從 0 開始，每次跳 2 格
        for i in range(0, N, 2): # 偶數堆 (索引為偶數，即第 1, 3, 5 個節點)
            now.next = ListNode( a[i] ) # 逐一塞進去
            now = now.next # 串接下一個
            
        # 第二輪：處理「偶數位置」的節點 (索引 1, 3, 5...)
        # range(1, N, 2) 代表從 1 開始，每次跳 2 格
        for i in range(1, N, 2): # 奇數堆 (索引為奇數，即第 2, 4, 6 個節點)
            now.next = ListNode( a[i] ) # 逐一塞進去
            now = now.next # 串接下一個
            
        # 回傳 ans.next，因為第一個節點是空的 Dummy Node
        return ans.next