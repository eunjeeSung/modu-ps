# Time: O(m+n), Space: O(m) or O(n)
# intersection은 노드의 intersection이지 value의 교차가 아니었음
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = {}
        currA, currB = headA, headB
        
        while currA:
            nodes[currA] = None
            currA = currA.next
        
        while currB:
            if currB in nodes:
                return currB
            currB = currB.next
            
        return None