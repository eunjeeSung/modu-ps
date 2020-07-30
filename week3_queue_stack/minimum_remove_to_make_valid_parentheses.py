# Time: O(N), Space: O(N)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:        
        idx_to_remove = []
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if len(stack) == 0:
                    idx_to_remove.append(i)
                else:
                    stack.pop()
            elif s[i] == '(':
                stack.append(i)
        idx_to_remove += stack
        ans = ""
        for i, c in enumerate(s):
            if i not in idx_to_remove:
                ans = ans + c
        return ans