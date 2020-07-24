"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Time: O(N), Space: O(N)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ans_head = prev = Node(-1, None, None)
        original = head
        nodes = {}
        while original:
            if original.random is None:
                rand = None
            elif original.random in nodes:
                rand = nodes[original.random]
            else:
                rand = Node(original.random.val, None, None)
                nodes[original.random] = rand
            
            if original in nodes:
                prev.next = nodes[original]
                prev.next.random = rand
            else:
                prev.next = Node(original.val, None, rand)
                nodes[original] = prev.next
                
            prev, original = prev.next, original.next
            
        return ans_head.next