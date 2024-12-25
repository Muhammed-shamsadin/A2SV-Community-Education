class Solution:
    def validateStackSequences(self, pushed, popped):
        length = len(pushed)
        stack = []
        pointer = 0

        for i in range(length):
            if stack:
                # check if the stack[-1] == pushed[pointer]
                while stack and stack[-1] == popped[pointer]:
                    stack.pop()
                    pointer += 1

            stack.append(pushed[i])

        while stack and  stack[-1] == popped[pointer]:
            stack.pop()
            pointer += 1
            
                

        if stack:
            return False
        else:
            return True