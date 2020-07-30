# Time: O(N), Space: O(N)
class Solution:
    def decodeString(self, s: str) -> str:
        def form_chunk(stack):
            seq = extract_str(stack)
            rep = extract_num(stack)
            print(seq, rep)
            stack.append(seq * rep)
        
        def extract_str(stack):
            temp = ""
            while True:
                e = stack.pop()
                if (e == '[') or (e == None): break
                temp = e + temp
            return temp
        
        def extract_num(stack):
            temp = ""
            while True:
                if (not stack) or (not stack[-1].isnumeric()):
                    break
                else:
                    temp = stack.pop() + temp
            return int(temp)
        
        stack = collections.deque()
        for c in s:
            if c == ']':
                form_chunk(stack)
            else:
                stack.append(c)
        return "".join(stack)                