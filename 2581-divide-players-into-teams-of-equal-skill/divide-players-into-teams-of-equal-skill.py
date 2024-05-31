class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        result = skill[0] * skill[-1]
        check_skill = skill[0] + skill[-1]

        left, right = 1, len(skill) - 2

        while left < right:
            cs = skill[left] + skill[right]
            if check_skill != cs:
                return -1
            
            result += skill[left] * skill[right]

            left += 1
            right -= 1

        return result