class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == '/':
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(char))
        
        return stack[-1]
