# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #  0 1 2 3 4 5 6 
        #  0 n-1, 1, n-2, 2, n-3, 3 ... 
        # first loop is counting
        # second loop goes to count // 2 and then starts reversing 
        # third loop i get everything in order  
        #  6 5 4  , count // 2. 
        #  0 6 1 5 2 4 3 

        def reverseLinkedList(node: Optional[ListNode]) -> ListNode:
            if not node:
                return None
            cur, prev = node, None

            while cur:
                nxt = cur.next 
                cur.next = prev 
                prev = cur
                cur = nxt 
            return prev 

        cur = head
        # count = 0 
        # while cur:
        #     count+= 1 
        #     cur = cur.next 
        # i = 0 
        # cur = head 
        # for _ in range(count // 2):
        #     cur = cur.next
        fast, slow = head, head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        turningPoint = slow.next
        slow.next = None
        rNode = reverseLinkedList(turningPoint)
        
        cur = head 
        orgNext = None

        while rNode: 
            orgNext = cur.next  
            cur.next = rNode 
            rNode = rNode.next 
            cur = cur.next 
            cur.next = orgNext 
            cur = cur.next
        



         


