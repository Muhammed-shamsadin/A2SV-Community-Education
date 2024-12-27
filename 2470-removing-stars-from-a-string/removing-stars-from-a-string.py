class Solution:
    def removeStars(self, s: str) -> str:
        # initializing Stack
        stack = []
        
        for char in s:
            # if our stack is not empty
            if stack:
                if char == "*":
                    stack.pop()
                else:
                    stack.append(char)
            else:
                # if our stack is empty
                stack.append(char)
        
        # return the String  
        return ''.join(stack)