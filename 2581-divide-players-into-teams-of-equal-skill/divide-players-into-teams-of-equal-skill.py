class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skill into a non-decreasing order.
        skill.sort()
        
        # Step 2: initialize 2 pointers (left) and (right) at first index and last index respectively
        length = len(skill)
        left, right = 0, length - 1

        # Step 3: "check" to check whether there is a way to divide the players into teams or not.
        check = skill[left] + skill[right]

        # Step 4: Variable called chemistry where we calculate the sum of all teams chemistry.
        chemistry = 0


        while left < right:
            if skill[left] + skill[right] == check:
                chemistry += (skill[left] * skill[right])
            else:
                return -1
                break
                
            left += 1
            right -= 1

        return chemistry

