class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Approach: we only have those characters in the string => '(', ')', '{', '}', '[' and ']'
        '''
        stack = []

        for char in s:
            if stack:
                # Check if the top of the stack matches the closing bracket
                if (stack[-1] == '(' and char == ')') or (stack[-1] == '{' and char == '}') or (stack[-1] == '[' and char == ']'):
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        if stack:
            return False
        return True
