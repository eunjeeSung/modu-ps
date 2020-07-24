# Time: O(N) / Space: O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ans = ListNode()
        carry = False
        while (l1 is not None) or (l2 is not None):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            val = val1 + val2 + 1 if carry else val1 + val2
            carry = False
            if val >= 10:
                val = val - 10
                carry = True
                
            ans.next = ListNode(val, None)
            ans = ans.next
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if carry is True:
            ans.next = ListNode(1, None)
            
        return head.next