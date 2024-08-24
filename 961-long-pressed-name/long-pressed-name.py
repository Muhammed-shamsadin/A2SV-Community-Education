class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_length = len(name)
        typed_length = len(typed)
        left = 0
        right = 0

        while left <= name_length and right < typed_length:
            if left < name_length and name[left] == typed[right]:
                left += 1
                right += 1
            elif name[left - 1] == typed[right] and left != 0:
                right += 1
            else:
                return False
        
        return left == name_length and right == typed_length