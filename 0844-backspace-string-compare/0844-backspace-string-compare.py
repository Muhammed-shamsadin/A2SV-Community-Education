class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for char in s:
            if char == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(char)
                
        
        for char in t:
            if char == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(char)
        
        # check 
        if len(s_stack) == len(t_stack):
            left = 0
            for right in range(len(s_stack)):
                if s_stack[left] != t_stack[right]:
                    return False
                left += 1
        else:
            return False
        
        return True