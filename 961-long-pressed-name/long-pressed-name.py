class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # If the length of name is greater than typed return False
        if len(name) > len(typed):
            return False
        # If name and typed have the same character, just increment the left and right pointers.
        left = right = 0
        while left < len(name):
            # If the right index is greater than length of typed, return False 
            if right >= len(typed):
                return False
            if name[left] == typed[right]:
                left += 1
                right += 1
            # If there is a difference, check if the current typed character is the same as the previous charactor of name
            else:
                if left != 0 and typed[right] == name[left - 1]:
                    right += 1
                else:
                    return False
        # If there are any remaining typed characters, check if they are the same as the last character of name 
        while right < len(typed):
            if name[left - 1] != typed[right]:
                return False
            right += 1
        return True
        
