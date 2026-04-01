# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode()
        carry = 0
        while l1 and l2:
            total = carry + l1.val + l2.val 
            carry = 1 if total >= 10 else 0 
            digit = total % 10
            node.next = ListNode(digit)
            l1 = l1.next
            l2 = l2.next
            node = node.next

        continuedList = l1 if l1 else l2
        while continuedList:
            total = carry + continuedList.val
            carry = 1 if total >= 10 else 0 
            digit = total % 10
            print(carry, digit)
            node.next = ListNode(digit)
            continuedList = continuedList.next
            node = node.next
        if carry: 
            node.next = ListNode(carry)
        return head.next
                 
